# prompt_registry.py
import os, yaml
from functools import lru_cache
from typing import Optional, Dict

class PromptNotFound(Exception): ...

class PromptRegistry:
    def __init__(self, backend):
        self.backend = backend

    def get(self, key: str, version: Optional[str] = None) -> str:
        """
        key = 'summarizer' or 'joke_writer'
        version = 'v2' or None for latest
        """
        return self.backend.get(key, version)

    def render(self, key: str, variables: Dict, version: Optional[str] = None) -> str:
        tmpl = self.get(key, version)
        return tmpl.format(**variables)

# ---------- FileSystem backend (Dev) ----------
class FSBackend:
    def __init__(self, root: str = "prompts"):
        self.root = root

    @lru_cache(maxsize=256)
    def get(self, key: str, version: Optional[str]) -> str:
        dirpath = os.path.join(self.root, key)
        if not os.path.isdir(dirpath):
            raise PromptNotFound(f"Prompt group '{key}' not found")

        if version:
            path = os.path.join(dirpath, f"{version}.txt")
            if not os.path.exists(path):
                raise PromptNotFound(f"{key}:{version} not found")
            return _read(path)

        # latest = highest vN.txt
        versions = sorted(
            [f for f in os.listdir(dirpath) if f.startswith("v") and f.endswith(".txt")],
            key=lambda f: int(f[1:-4])  # 'v12.txt' -> 12
        )
        if not versions:
            raise PromptNotFound(f"No versions for '{key}'")
        return _read(os.path.join(dirpath, versions[-1]))

def _read(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# ---------- (Optional) DB backend (Prod) ----------
# Minimal interface—swap in your actual DB/ORM calls.
class DBBackend:
    """
    Table schema idea:
      prompts(key TEXT, version TEXT, template TEXT, is_active BOOL, created_at TIMESTAMP)
    'latest' logic can be is_active=TRUE or max(created_at) per key
    """
    def __init__(self, conn):
        self.conn = conn

    @lru_cache(maxsize=512)
    def get(self, key: str, version: Optional[str]) -> str:
        cur = self.conn.cursor()
        if version:
            cur.execute(
                "SELECT template FROM prompts WHERE key=%s AND version=%s LIMIT 1",
                (key, version),
            )
        else:
            cur.execute(
                "SELECT template FROM prompts WHERE key=%s AND is_active=TRUE "
                "ORDER BY created_at DESC LIMIT 1",
                (key,),
            )
        row = cur.fetchone()
        if not row:
            raise PromptNotFound(f"{key}:{version or 'latest'} not found")
        return row[0]
