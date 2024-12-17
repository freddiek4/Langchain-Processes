import requests
import json

def load_config():
    with open('config.json') as f:
        return json.load(f)

def call_gemini_api(text):
    config = load_config()
    url = config['api_url']
    api_key = config['api_key']
    
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [{
            "parts": [{
                "text": text
            }]
        }]
    }
    response = requests.post(f"{url}?key={api_key}", headers=headers, json=data)
    if response.ok:
        return response.json() 
    else:
        print("Failed to fetch data:", response.json())
        return None
    
if __name__ == "__main__":
    text = "say hello if this message is received"
    response = call_gemini_api(text)
    print("Response from Gemini API:", response)