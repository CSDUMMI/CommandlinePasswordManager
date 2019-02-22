#! /bin/python3
import json, sys, getpass
from Crypto.Hash import SHA256

def passForService(service):
    passServices = json.load(open("pass.json","r", encoding="utf-8"))
    hash = SHA256.new()
    hash.update(passServices[service].encode('utf-8'))
    hash.update(str(hash.hexdigest())
                .encode('utf-8')
                + getpass.getpass("Masterpassword:")
                .encode('utf-8'))
    return hash.hexdigest()

if __name__ == '__main__':
    service = sys.argv[1]
    print(passForService(service))
