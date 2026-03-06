import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_ai(notes, question):

    prompt = f"""
    You are an Islamic Dars assistant.

    Notes:
    {notes}

    Question:
    {question}

    Answer only using the notes.
    """

    chat = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant",
    )

    return chat.choices[0].message.content