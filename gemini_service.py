from gemini_client import client


def generate_text(prompt):
    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text
