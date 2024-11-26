import requests

def call_gemini_api(text, api_key):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent"
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
    api_key = 'gemini_api_key_here' 
    text = "Just say hello if this message is received"
    response = call_gemini_api(text, api_key)
    print("Response from Gemini API:", response)
