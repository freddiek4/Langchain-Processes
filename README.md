# Project Setup Guide

## Prerequisites
1. Install required dependencies:  
```bash
pip install -r requirements.txt  
```

## API Configuration

### Gemini Setup
1. Configure Gemini API:
   - Add your Gemini API key to `gemini_api.py`
   - Run:
```bash
python gemini_api.py     
```

### LangChain Setup
1. Install LangChain dependencies
2. Configure LangSmith environment:   
```bash
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
export LANGCHAIN_API_KEY="your_langchain_api_key"
export LANGCHAIN_PROJECT="langchain_processes"   
```

## Usage Example
```python
from my_custom_module import ChatGemini

api_key = 'your_gemini_api_key'
llm = ChatGemini(api_key)
response = llm.invoke("Respond with Gemini Activated if this message is received")
print("Response from Gemini:", response)
```