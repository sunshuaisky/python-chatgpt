from flask import Flask
from openai import OpenAI
app = Flask(__name__)

@app.route('/')
def hello_world():
  client = OpenAI(
      api_key = "sk-mlPdUvYgfqTmBEt5QHSSWmB58161aXcuYBzqNPpufojCkJTF",
      base_url = "https://api.agicto.cn/v1"
  )
  chat_completion = client.chat.completions.create(
      messages=[
          {
              "role": "user",
              "content": "会发生第三次世界大战吗？",
          }
      ],
      model="gpt-4",
  )
  print(chat_completion.choices[0].message.content)
  return chat_completion.choices[0].message.content

if __name__ == '__main__':
  app.run()

if __name__ == '__main__':
    app.run()