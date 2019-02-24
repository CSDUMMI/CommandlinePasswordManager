#! /bin/python3
"""

    A Password-Manager on the Commandline
    Copyright (C) 2019 Joris Gutjahr <joris.gutjahr@gmail.com>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import json, sys, getpass
from Crypto.Hash import SHA256
from Crypto.Hash import SHA512

def loadPass():
    return json.load(open("pass.json","r",encoding="utf-8"))

def passForService(service,passServices):
    hash = SHA256.new()
    mp = checkMasterPassword()
    if type(mp) == type("string"):
        hash.update(mp.encode('utf-8') + passServices[service].encode('utf-8'))
        return "Password for " + service + "\n" + str(hash.hexdigest())
    else:
        return "Masterpassword wrong!"

def checkMasterPassword():
    masterpass = getpass.getpass("Masterpassword:")
    sha512 = SHA512.new(masterpass.encode('utf-8'))
    masterpassHash = str(sha512.hexdigest())
    if masterpassHash == passServices['masterpass']:
        return masterpass
    else:
        return False


def addMasterPass(passServices):
    sha512 = SHA512.new(getpass.getpass("New Masterpassword:").encode('utf-8'))
    passServices['masterpass'] = str(sha512.hexdigest())
    return passServices

def addNewService(item,hashSeed,passServices):
    passServices[item] = hashSeed

def savePass(passServices):
    open("pass.json","w").write(json.dumps(passServices))

if __name__ == '__main__':
    cmd = sys.argv[1]

    if cmd == 'get':
        service = sys.argv[2]
        # output password to service
        passServices = loadPass()
        print(passForService(service,passServices))
    elif cmd == 'add':
        item = sys.argv[2]
        passServices = loadPass()
        if item == 'masterpass':
            passServices = addMasterPass(passServices)
        else:
            hashSeed = sys.argv[3]
            passServices = addNewService(item,hashSeed,passServices)
        savePass(passServices)
    else:
        print ("Usage: add or get Password")
