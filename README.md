# Prompt Engineer Python Project

This project demonstrates in-context learning and prompt engineering techniques in Python. 

## Getting Started
1. Ensure you have Python 3.7+ and https://ollama.com/windows installed.
2. Create a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ollama pull llama3
   ollama serve
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the main demo:
   ```powershell
   python main.py
   ```

## The purpose of every file under Lab folder

### Classification
- `classify.py`: True/false classification prompt.
- `few_shot.py`: Few-shot emotion classification.
- `one_shot.py`: One-shot learning for email writing and concept simplification.

### Chain of thought
- `chain_of_thought.py`: Chain-of-thought reasoning for math, decision-making, and process explanation.
- `self_consistency.py`: Self-consistency reasoning for reliable answers.

### Langchain expression language (LCEL)
- `lcel_summarize.py`: Summarize content in one sentence.
- `lcel_summarize_test.py`: Test file for summarization.
- `lcel_text_classfication.py`: LCEL-based text classification.
- `lcel_qa_test.py`: LCEL-based question answering.
- `lcel_code_generation.py`: SQL query generation from natural language.
- `lcel_custom_format.py`: Product review analysis for sentiment, features, and summary.
- `chain_factory.py`: Factory for creating LangChain chains from prompt templates.
- `langchain_expression_language.py`: LCEL workflow composition and reliability.

### Miscellaneous
- `wind.py`: Simple wind response prompt.


