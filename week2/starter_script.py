# starter_ai_logic.py — fill in the parts marked TODO

import openai
import janus_swi as janus
import os
from dotenv import load_dotenv

load_dotenv()  # loads your API key from .env file

client = openai.OpenAI()

# The knowledge base (facts + rules)
knowledge_base = """
human(socrates).
human(plato).
mortal(X) :- human(X).
"""

# TODO: Change this question to something you're curious about!
question = "Is Socrates mortal?"

# Ask ChatGPT to translate the question into a Prolog query
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content":
            "You are a logic translator. Given a question and a Prolog "
            "knowledge base, output ONLY the Prolog query (no explanation). "
            "Example: mortal(socrates)."},
        {"role": "user", "content":
            f"Knowledge base:\n{knowledge_base}\n\n"
            f"Question: {question}\n\n"
            f"Write the Prolog query:"}
    ]
)

query = response.choices[0].message.content.strip()
print(f"🤖 AI translated your question to: {query}")

# Run the query in Prolog
janus.consult("kb", knowledge_base)
result = janus.query_once(query.rstrip('.'))
print(f"✅ Prolog says: {result}")