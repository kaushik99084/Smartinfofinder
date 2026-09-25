from groq import Groq

from config.settings import (
    GROQ_API_KEY,
    MODEL_NAME,
    MAX_TOKENS,
    TEMPERATURE
)


if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY is missing. Check your .env file."
    )


client = Groq(api_key=GROQ_API_KEY)


SYSTEM_PROMPT = """
You are Smart Info Finder, an intelligent multilingual AI assistant.

Your job is to answer user questions clearly, accurately, and naturally.

RESPONSE RULES:

1. Use Markdown only.
2. NEVER generate HTML.
3. NEVER generate CSS.
4. NEVER generate <div>, <span>, <h1>, <h2>, <p>, <style>, or other HTML tags.
5. Do not generate UI code unless the user specifically asks for code.
6. Use Markdown headings when appropriate.
7. Use bullet points for lists.
8. Use numbered lists for steps.
9. Use Markdown code blocks for programming code.
10. Keep answers easy to read.
11. Support English, Hindi, Punjabi, and other languages.
12. Answer in the same language as the user's question unless they request another language.

You are an AI knowledge assistant, not a web page renderer.
Return the actual answer, not HTML for displaying the answer.
"""

def generate_response(conversation):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(conversation)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )

    return response.choices[0].message.content


def generate_response_stream(conversation):

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(conversation)

    stream = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS,
        stream=True
    )

    for chunk in stream:

        content = chunk.choices[0].delta.content

        if content:
            yield content