from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    translate = translator.english_to_french(text_to_translate)
    return translate

@app.route("/frenchToEnglish")
def frenchToEnglish():
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    translate = translator.french_to_english(text_to_translate)
    return translate

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    
    return render_template('index.html')


    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
