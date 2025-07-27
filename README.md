---
title: Rule-Based Chatbot
emoji: 💬
colorFrom: gray
colorTo: blue
sdk: streamlit
sdk_version: 1.25.0
app_file: app/chatbot_app.py
pinned: false
---
# 💬 Rule-Based Chatbot

A simple chatbot that answers basic user queries using pre-defined rules. No machine learning involved — just Python logic.

## 🧠 Features
- Responds to greetings, help, pricing, return policy, and hours
- Uses keyword-matching logic
- Streamlit UI for easy interaction

## 🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app/chatbot_app.py
# 💬 Rule-Based Chatbot

Ask questions like "hi", "help", or "what's your name?" and the bot will respond using simple rules.
