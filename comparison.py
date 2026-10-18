
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()


def compare_documents(text_a, text_b):
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError(
            "Gemini API key missing. Check your .env file."
        )

    if len(text_a) > 20000 or len(text_b) > 20000:
        raise ValueError(
            "PDF is too long. Please use shorter documents."
        )

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are an AI Document Comparison Assistant.

Compare Document A and Document B carefully.

RULES:
- Use only information from the documents.
- Never invent facts.
- Keep facts from A and B separate.
- If information is missing, say:
  "Not found in the provided text".
- Explain meaningful differences clearly.
- Mention supporting text when possible.

Give the output with these headings:

## Summary A
## Summary B
## Similarities
## Differences
## Key Details Comparison
## Overall Conclusion
## Limitations

DOCUMENT A:
{text_a}

DOCUMENT B:
{text_b}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    if not response.text:
        raise ValueError("AI returned an empty response.")

    return response.text

