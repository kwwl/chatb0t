from dotenv import load_dotenv
import os
from groq import Groq

load_dotenv()
groq_key = os.environ["GROQ_KEY"].strip()

client = Groq(api_key=groq_key)

# ------------------------------------------------
# Petite mémoire interne (simple liste)
# ------------------------------------------------
chat_history = []  # each element: {"role":"user/assistant", "content":"..."}


def ask_gpt(prompt):
    # Ajouter la requête utilisateur à la mémoire
    chat_history.append({"role": "user", "content": prompt})

    # Garder seulement les 5 derniers messages
    short_history = chat_history[-5:]

    # Construire le message complet
    messages = [
        {"role": "system", "content": "Soit le meilleur des assistant"}
    ] + short_history

    completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=messages,
        temperature=1,
        max_completion_tokens=8192,
        top_p=1,
        reasoning_effort="medium",
        stream=True,
    )

    list_of_chunks = []
    full_response = ""

    for chunk in completion:
        if chunk.choices[0].delta.content:
            list_of_chunks.append(chunk.choices[0].delta.content)

    full_response = "".join(list_of_chunks)

    # Ajouter la réponse à la mémoire
    chat_history.append({"role": "assistant", "content": full_response})

    return full_response


if __name__ == "__main__":
    response = ask_gpt("Tu préfères python ou javascript ?")
    print(response)
