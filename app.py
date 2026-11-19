
from flask import Flask
import gradio as gr
from starlette.middleware.wsgi import WSGIMiddleware
import uvicorn

# Flask application
app = Flask(__name__)

@app.route("/")
def home():
    return '<h1>Welcome to Flask</h1><a href="/gradio">Open Gradio</a>'

# Gradio application
def greet(name):
    return "Hello " + name

demo = gr.Interface(fn=greet, inputs="text", outputs="text")

# Combine Flask and Gradio
from fastapi import FastAPI

main_app = FastAPI()
main_app.mount("/", WSGIMiddleware(app))
main_app = gr.mount_gradio_app(main_app, demo, path="/gradio")

# Run both on port 5000
if __name__ == "__main__":
    uvicorn.run(main_app, host="0.0.0.0", port=5000)
