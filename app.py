from flask import Flask, request, jsonify, render_template
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/translate', methods=['POST'])
def translate_text():
    data = request.get_json()
    text = data.get("text")
    target = data.get("target")

    if not text or not target:
        return jsonify({"error": "Missing text or target language"}), 400

    try:
        translated = GoogleTranslator(source='auto', target=target).translate(text)
        return jsonify({"translatedText": translated})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
