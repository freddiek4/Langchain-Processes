import os
os.environ['LANGCHAIN_TRACING_V2'] = 'true'
os.environ['LANGCHAIN_ENDPOINT'] = 'https://api.smith.langchain.com'
os.environ['LANGCHAIN_API_KEY'] = 'api_key_here'
os.environ['LANGCHAIN_PROJECT'] = 'langchain_processes'
print("Environment configured for LangChain.")
