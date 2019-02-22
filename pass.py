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
