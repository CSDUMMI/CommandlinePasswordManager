#! /usr/bin/python3
import json, sys, getpass, os, pyperclip
from Crypto.Hash import SHA256
from Crypto.Hash import SHA512
from CLI.CLI import CLI

class Pass(CLI):
    """
Usage:
pass get <service>                   Get Password to service
pass set                             Set Masterpassword
pass add <name> <split_at> <salt>    Add new service
pass list                            List services
    """
    def __init__(self):
        super().__init__(os.environ['PASS_PY_PATH'] + '/pass.json','get','set','add','list')
        current = os.environ['PWD']
        os.system('cd $PASS_PY_PATH && git status && git pull && cd ' + current)
        
    def check(self):
        mp = getpass.getpass('Masterpassword:')
        hash = SHA512.new(mp.encode('utf-8'))

        if hash.hexdigest() == self.state['masterpass']:
            return mp
        else:
            return False

    def get(self,args):
        service = args[0]
        hash = SHA256.new()
        mp = self.check()
        if mp != False:
            hash.update(mp.encode('utf-8') + self.state[service]['salt'].encode('utf-8'))
            passwd = hash.hexdigest()
            passwd = passwd[:int(len(passwd)/2)].upper() + passwd[int(len(passwd)/2):]
            try:
                pyperclip.copy(passwd)
            except:
                print(passwd)
        else:
            print('Masterpassword wrong')

    def set(self,args):
        hash = SHA512.new(getpass.getpass('New Masterpassword:').encode('utf-8'))
        self.state['masterpass'] = hash.hexdigest()

    def add(self,args):
        name = args[0]
        split_at = args[1]
        salt = args[2]
        self.state[name] = {'salt':salt,'split_at':int(split_at)}

    def list(self,args):
        for service in self.state.keys():
            if service != 'masterpass':
                print(service)


if __name__ == '__main__':
    pass_cli = Pass()
    pass_cli.run()
