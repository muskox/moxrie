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
</pre>
