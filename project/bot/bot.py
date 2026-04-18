import os
import google.genai as genai
gemini_model=genai.Client(api_key=os.environ.get('chatbot'))
# goodmorning how can I help you?
def simple_bot(question):
  prompt=f""" The student has asked the {question}, give a structured and brief reply."""
  try:
      response = gemini_model.models.generate_content(
      model="gemini-2.5-flash",contents=prompt)
      reply= response.text

  except Exception as e:
      print("Gemini error:", e)
      reply="Chatbot temporarily unavailable."
  return reply
def chatbot():
  text=simple_bot(question)
  while text not in ['Quit','Bye','Goodbye','Exit']:
    return simple_bot(question)
