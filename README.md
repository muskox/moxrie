moxrie
======

REST service for words in word games. Define your own rules for your game.


Description
===========

A word record is a JSON hash like so:

<pre>
{"string": "a",
 "meaning": "The article in English.",
 "use": "I drive a car to work.",
 "legal": true,
 "reference": ['http://www.merriam-webster.com/dictionary/a',]
}
</pre>

```GET /words/<word>```
Returns the matching word record

```POST /words/<word>```
Creates a new word record.


Requirements
============

- Python
- virtualenv


Installation
============

<pre>
$ virtualenv venv
$ . venv/bin/activate
$ venv/bin/pip install flask
$ ./moxrie.py
# New Window
$ python load_data.py
$ curl localhost:5000/words/a
</pre>

TODO
====

- Make /rules - First rule, no proper nouns
- Load up 2 letter words via script

Voting
======

This is a possible feature. Voting 2nd API. People submit via API, other vote. If you say legal = true, meaning and use required. Reference is optional. If legal is false, nothing is required.

