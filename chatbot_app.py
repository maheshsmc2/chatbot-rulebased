
import streamlit as st

# Simple rule-based responses
def get_bot_response(user_input):
    user_input = user_input.lower()

    if any(greet in user_input for greet in ["hi", "hello", "hey"]):
        return "👋 Hello! How can I help you today?"
    elif "bye" in user_input or "see you" in user_input:
        return "👋 Goodbye! Have a great day!"
    elif "your name" in user_input:
        return "🤖 I'm a simple rule-based chatbot."
    elif "help" in user_input or "support" in user_input:
        return "🛠 You can ask about pricing, returns, or store hours."
    elif "price" in user_input:
        return "💰 You can find pricing details on our website."
    elif "return" in user_input:
        return "🔁 You can return any item within 30 days."
    elif "hours" in user_input or "open" in user_input:
        return "🕘 We're open from 9 AM to 6 PM, Monday to Saturday."
    else:
        return "❓ Sorry, I didn’t understand that. Please try again."

# Streamlit UI
st.title("💬 Rule-Based Chatbot")
st.write("Ask something and I'll try to help you!")

user_input = st.text_input("You:")
if user_input:
    response = get_bot_response(user_input)
    st.markdown(f"**Bot:** {response}")
