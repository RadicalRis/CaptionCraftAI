from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
from google import genai
import os
import json
import re

load_dotenv()

app = Flask(__name__)
CORS(app)

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Missing GEMINI_API_KEY. Check your .env file.")

client = genai.Client(api_key=api_key)


@app.route("/")
def home():
    return send_from_directory(".", "index.html")


@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    business = data.get("businessType", "")
    platform = data.get("platform", "")
    topic = data.get("topic", "")
    tone = data.get("tone", "")
    audience = data.get("audience", "")

    prompt = f"""
Create marketing content for a small business.

Business Type: {business}
Platform: {platform}
Topic: {topic}
Tone: {tone}
Target Audience: {audience}

Return ONLY valid JSON in this exact format:
{{
  "caption1": "string",
  "caption2": "string",
  "hashtags": "string",
  "cta": "string",
  "idea": "string"
}}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    ai_text = response.text.strip()

    # Remove markdown code block if Gemini adds it
    ai_text = re.sub(r"^```json", "", ai_text).strip()
    ai_text = re.sub(r"^```", "", ai_text).strip()
    ai_text = re.sub(r"```$", "", ai_text).strip()

    try:
        parsed = json.loads(ai_text)
    except json.JSONDecodeError:
        return jsonify({
            "caption1": ai_text,
            "caption2": "",
            "hashtags": "",
            "cta": "",
            "idea": ""
        })

    return jsonify(parsed)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050, use_reloader=False)