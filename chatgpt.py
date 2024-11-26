import requests

def call_chatgpt(prompt, api_key):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {"Authorization": f"Bearer {api_key}","Content-Type": "application/json"}
    data = {"model": "gpt-3.5-turbo","messages": [{"role": "user", "content": prompt}]}
    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    if response.ok: 
        return response_json['choices'][0]['message']['content']
    else: 
        return response_json.get('error', 'Failed to get response from API')

if __name__ == "__main__":
    api_key = 'open_ai_key_here'
    prompt = 'GPT: return success message if prompt is received'
    response = call_chatgpt(prompt, api_key)
    print("Response from GPT-3.5:", response)
