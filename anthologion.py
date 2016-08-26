#!/usr/bin/python
from flask import Flask
import pypandoc as pandoc
from horologion.generate_hour import generate_service
app = Flask(__name__)

@app.route("/services")
def midnight_service():
    markdown = generate_service("oc", "eastern", "en-us", "hmbm", "midnight")
    return pandoc.convert_text(markdown, 'html5', format='md', extra_args=['-s'])

@app.route("/")
def homepage():
    with open("index.html") as blat:
        index = blat.read()
    return index

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("80"), debug=False)
