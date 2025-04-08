from flask import Flask, render_template, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Base URL for the LM Studio API
BASE_URL = "http://100.93.200.7:1234/v1"
model_name = "deepseek-r1-distill-qwen-7b"  # Default model

def list_models():
    """Fetch the list of currently loaded models."""
    url = f"{BASE_URL}/models"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Failed to fetch models: {response.status_code} - {response.text}"}

def chat_completion(messages):
    """Generate a chat completion."""
    url = f"{BASE_URL}/chat/completions"
    payload = {"model": model_name, "messages": messages}
    response = requests.post(url, json=payload)
    return response.json() if response.status_code == 200 else {"error": response.text}

def text_completion(prompt, max_tokens):
    """Generate a text completion."""
    url = f"{BASE_URL}/completions"
    payload = {"model": model_name, "prompt": prompt}
    if max_tokens > 0:
        payload["max_tokens"] = max_tokens
    response = requests.post(url, json=payload)
    return response.json() if response.status_code == 200 else {"error": response.text}

def generate_embeddings(input_texts):
    """Generate text embeddings."""
    url = f"{BASE_URL}/embeddings"
    payload = {"model": model_name, "input": input_texts}
    response = requests.post(url, json=payload)
    return response.json() if response.status_code == 200 else {"error": response.text}

@app.route("/")
def index():
    """Render the main menu."""
    return render_template("index.html", model_name=model_name)

@app.route("/list_models", methods=["GET"])
def list_models_route():
    """API route to list models."""
    models = list_models()
    return jsonify(models)

@app.route("/chat/completions", methods=["POST"])
def chat_completion_route():
    """API route for chat completion."""
    global model_name
    user_message = request.form.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    messages = [{"role": "user", "content": user_message}]
    try:
        response = chat_completion(messages)
        return jsonify(response)  # Return the LLM's response as JSON
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/text_completion", methods=["POST"])
def text_completion_route():
    """API route for text completion."""
    prompt = request.form.get("prompt")
    max_tokens = int(request.form.get("max_tokens", 50))
    response = text_completion(prompt, max_tokens)
    return jsonify(response)

@app.route("/generate_embeddings", methods=["POST"])
def generate_embeddings_route():
    """API route for generating embeddings."""
    input_texts = request.form.get("input_texts").split(",")
    response = generate_embeddings(input_texts)
    return jsonify(response)

@app.route("/change_model", methods=["POST"])
def change_model_route():
    """API route to change the model."""
    global model_name
    new_model = request.form.get("model_name")
    model_name = new_model
    return jsonify({"message": f"Model changed to {model_name}"})

if __name__ == "__main__":
    app.run(debug=True)