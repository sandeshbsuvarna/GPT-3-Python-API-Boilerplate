from flask import Flask, redirect, url_for, render_template, request
import openai, requests, json
openai.api_key = "YOUR_KEY_HERE"

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",textarea = "") 

@app.route('/ajax', methods = ['POST'])
def ajax_request():
    r=json.loads(str(openai.Completion.create(
    engine="davinci",
    prompt= request.form['subject'],
    max_tokens=50,
    temperature=0.5,
    top_p= 1,
    n=1,
    stream=False,
    )))
    print(r)
    text = request.form['subject'] + r["choices"][0]["text"]
    return render_template("home.html",textarea = text) 

if __name__ == "__main__":
    app.run()