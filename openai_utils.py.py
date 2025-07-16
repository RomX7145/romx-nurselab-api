import openai

def ask_medical_question(question: str, context: str) -> str:
    prompt = f"Context: {context}\n\nQuestion: {question}\n\nAnswer:"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful and knowledgeable medical assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.5
    )
    
    return response.choices[0].message["content"].strip()
