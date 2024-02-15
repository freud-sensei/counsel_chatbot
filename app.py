import gradio as gr
from transformers import pipeline

def counsel_chat(message, history):
  pipeline_model = pipeline("text-generation", model="freud-sensei/counsel_chatbot")
  sentence = f"질문: {message} 답변:"
  answer = pipeline_model(sentence)
  return answer[0]["generated_text"][len(sentence):]

chatbot2 = gr.ChatInterface(counsel_chat)
chatbot2.launch()
