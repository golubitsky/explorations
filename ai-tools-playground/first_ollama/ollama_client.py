import requests
import json


def ask_ollama(prompt, model="llama3.1:8b"):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt},
        stream=True,
    )

    output = ""
    for line in response.iter_lines():
        if line:
            try:
                output += json.loads(line.decode("utf-8"))["response"]
            except Exception:
                continue
    return output.strip()
