import requests
import hashlib
import sys


def hash_password(string):
    password = string.encode('utf-8')
    hashed_password = hashlib.sha1(password)
    query_password = f'{hashed_password.hexdigest()}'
    return query_password.upper()


def req_api(query):
    url = f'https://api.pwnedpasswords.com/range/{query[:5]}'
    resp = requests.get(url)
    if resp.status_code != 200:
        raise RuntimeError(f'Error {resp.status_code}')
    return resp


def check_api(password):
    key = hash_password(password)
    response = req_api(key[:5])
    tail = key[5:]
    hashes = (line.split(':') for line in response.text.splitlines())
    for item in hashes:
        if tail == item[0]:
            return f'This password was leaked {item[1]} times! Might be wise to change it!'
    return 'Your password was NOT leaked!'


def main(args):
    for password in args:
        print(check_api(password))


main(sys.argv[1:])
