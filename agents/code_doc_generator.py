import requests
import json

def generate_docs(code, api_key, model="gpt-3.5-turbo"):
    return _call_openai_api(f"Generate documentation for this code:\n\n{code}", api_key, model, "You are a documentation generator. Create clear and professional documentation for the provided code with topics and subtopics.")

def _call_openai_api(prompt, api_key, model, system_message):
    # ... (Your API call logic here) ...
    # (Same API call logic as in code_generator.py)
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]
    data = {
        "model": model,
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 1024,
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        response_json = response.json()
        if "choices" in response_json and len(response_json["choices"]) > 0:
            return response_json["choices"][0]["message"]["content"]
        else:
            return "Could not generate a response."
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except KeyError as e:
        print(f"Error: Missing key: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON: {e}")
        return None