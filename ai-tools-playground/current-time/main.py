import ollama
from datetime import datetime

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

SYSTEM_PROMPT = """
You are an AI that can use tools. You have access to the following tool:

  get_current_time – returns the current time as a string.

To use this tool, respond with exactly:
  TOOL_CALL:get_current_time

Do not explain the tool call or add anything else—just return the line above if needed.

If you receive a response in the following format:
  TOOL_RESPONSE:get_current_time <string>

You should treat it as the result of a tool invocation and format a helpful final response for the user based on that.
"""

def main():
    client = ollama.Client()

    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ("exit", "quit"):
            break

        # Step 1: Ask the model
        response = client.chat(
            model='llama3',
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ]
        )['message']['content']

        print("\nAI:", response)

        # Step 2: Handle tool call if present
        if response.strip() == "TOOL_CALL:get_current_time":
            result = get_current_time()
            tool_response = f"TOOL_RESPONSE:get_current_time {result}"

            final = client.chat(
                model='llama3',
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": user_input},
                    {"role": "assistant", "content": response},
                    {"role": "user", "content": tool_response},
                ]
            )['message']['content']

            print("\nAI (final):", final)

if __name__ == "__main__":
    main()