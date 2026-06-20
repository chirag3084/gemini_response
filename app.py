from flask import Flask, request, jsonify
from gemini_service import generate_text

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "<h1>Welcome Back</h1>"


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        prompt = data["prompt"]
        response = generate_text(prompt)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
