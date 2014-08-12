#!/usr/bin/python

import subprocess
import sys

server_name = "localhost:5000"


def main():
    # Create user
    cmd = '''curl -i -H "Content-Type: application/json" -X POST -d '{"use":"I drive a car to work.","meaning":"The article in English.","references":["http://www.merriam-webster.com/dictionary/a"]}' http://%s/words/a''' % server_name
    curl_cmd = subprocess.call(cmd,shell=True)

if __name__ == "__main__":
    main()
