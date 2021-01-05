import re
import json

from difflib import SequenceMatcher
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/simmy', methods=['POST'])
def simmy():
    comps = request.json
    text_dict = cleaner(comps)
    return jsonify(text_dict)

def cleaner(text_dict):
    """Remove non-alphanumeric data and update dict."""
    for key in text_dict:
        words = text_dict[key]
        compressed_letters = re.sub(' ', '', words)
        text_dict.update({key: compressed_letters})
    return matcher(text_dict)

def matcher(text_dict):
    """Use difflib.SequenceMatcher(standard library) for comparison."""
    a = text_dict['text1']
    b = text_dict['text2']
    return round(SequenceMatcher(None, a, b).ratio(), 2)
