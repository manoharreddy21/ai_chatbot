# 🤖 AI Chatbot Project Workflow
📌 <Project_Overview>
Generative AI Chatbot built using Streamlit + Groq API
Real-time conversational AI web application
Secure API-based LLM integration
🚀 <Workflow>
1️⃣ <Application_Launch>
streamlit run app.py
Starts Streamlit UI
Opens chatbot in browser
2️⃣ <Environment_Setup>
Loads .env file
Retrieves GROQ_API_KEY
Secure API connection established with Groq
3️⃣ <Session_Initialization>
Uses st.session_state.messages
Stores conversation history
Defines system prompt:
Professional tone
Structured responses
AI assistant behavior
4️⃣ <User_Input_Handling>
User sends message via chat input
Stored as:
{"role": "user", "content": "message"}
5️⃣ <LLM_API_Request>
Sends full chat history to model
Model used: llama-3.1-8b-instant
Includes:
User input
Chat history
System instructions
6️⃣ <AI_Response_Generation>
LLM processes input
Generates contextual response
Returns:
{"role": "assistant", "content": "response"}
7️⃣ <UI_Rendering>
Streamlit displays:
User message
AI response
Real-time chat experience
8️⃣ <Memory_Management>
Stores all messages in session state
Maintains conversation context
Enables continuous chat flow
9️⃣ <Reset_Chat>
Clears session memory
Restarts fresh conversation
🧠 <Architecture_Flow>
User Input
   ↓
Streamlit UI
   ↓
Session Memory
   ↓
Groq LLM API
   ↓
AI Response
   ↓
Streamlit Output
🔥 <Key_Features>
💬 Real-time AI chat interface
🧠 Context-aware memory system
⚡ Fast LLM inference
🔐 Secure API handling (.env)
🔄 Reset chat functionality
🧑‍💼 Professional system prompt
🎯 <Use_Cases>
AI Personal Assistant
Customer Support Bot
Learning Assistant
GenAI Portfolio Project
