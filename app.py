

from flask import Flask
import gradio as gr
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import uvicorn

# Flask application
app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>My Flask Application</h2>
    <a href="/page1"><button>Page 1</button></a>
    <a href="/gradio/"><button>Gradio</button></a>
    """

@app.route("/page1")
def page1():
    return "<h2>Welcome to Page 1</h2><a href='/'>Home</a>"

# Gradio application
def greet(name):
    return "Hello " + name

demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="My Gradio Application"
)

# FastAPI application
api = FastAPI()

# IMPORTANT: Mount Gradio FIRST
api = gr.mount_gradio_app(api, demo, path="/gradio")

# Mount Flask LAST
api.mount("/", WSGIMiddleware(app))

if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=5000)
