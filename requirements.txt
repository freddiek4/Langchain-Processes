1. need to have requests installed:
- pip install -r requirements.txt

gemini model activation:
- python gemini_api.py
- add api key here (stored)

langchain dependencies:
- add langchain api key
- pip install -U langchain langchain-openai
- configure environment to connect to LangSmith:
  - project name: langchain_processes
    LANGCHAIN_TRACING_V2=true
    LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
    LANGCHAIN_API_KEY="api_key_here"
    LANGCHAIN_PROJECT="langchain_processes"

    from my_custom_module import ChatGemini  
    api_key = 'gemini_api_key_here'  
    llm = ChatGemini(api_key)
    response = llm.invoke("Respond with Gemini Activated if this message is received")
    print("Response from Gemini:", response)
