chat_history = []


def add_to_history(question, answer):
    chat_history.append({
        "question": question,
        "answer": answer
    })


def get_chat_history():

    history = ""

    for chat in chat_history[-3:]:
        history += f"User: {chat['question']}\n"
        history += f"Assistant: {chat['answer']}\n\n"

    return history