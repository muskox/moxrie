#!venv/bin/python
from flask import Flask, jsonify, request, abort, make_response

app = Flask(__name__)

words = []

@app.route('/')
def index():
    return "Hello, Moxrie"

@app.route('/words/<word>', methods=['GET'])
def get_word(word):
    the_word = filter(lambda w: w['string'] == word, words)
    if len(the_word) == 0:
        abort(404)
    return jsonify( the_word[0] )


@app.route('/words/<word>', methods=['POST'])
def post_word(word):
    if not request.json or not word:
        abort(400) 
    json_obj = request.json

    if not word_json_valid(json_obj):
        abort(400)

    word_already_exits = False
    for w in words:
        if w['string'] == word:
            word_already_exits = True
    if word_already_exits:
        abort(400) 

    the_word = {
        'string': word,
        'meaning': request.json['meaning'],
        'use': request.json['use'],
        'legal': False,
        'references': request.json['references']
    }
    words.append(the_word)
    return jsonify( the_word ), 201

def word_json_valid(json_request):
    if not 'meaning' in json_request:
        return False
    if not 'use' in json_request:
        return False
    if not 'references' in json_request:
        return False
    return True



if __name__ == '__main__':
    app.run(debug = True)
