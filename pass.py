#! /usr/bin/python3
import json, sys, getpass, os
from Crypto.Hash import SHA256
from Crypto.Hash import SHA512


def loadPasswds():
    pass_path = os.environ['PASS_PY_PATH']
    return json.load(open(pass_path + "pass.json", "r", encoding="utf-8"))

def addMasterpass(mp,services):
    hash = SHA512.new(mp.encode('utf-8'))
    services['masterpass'] = hash.hexdigest()
    return services

def checkMasterpass():
    mp = getpass.getpass('Masterpassword:')
    hash = SHA512.new(mp.encode('utf-8'))
    if hash.hexdigest() == services['masterpass']:
        return mp
    else:
        return False

def getPass(service,services):
    hash = SHA256.new()
    mp = checkMasterpass()
    if mp != False:
        hash.update(mp.encode('utf-8') + services[service]['salt'].encode('utf-8'))
        return hash.hexdigest()
    else:
        return False

def save(passServices):
    jsonStr = str(json.dumps(passServices))
    open('pass.json',"w").write(jsonStr)

def check_if_valid():
	current_dir = os.environ['PWD']
	os.system("cd $PASS_PY_PATH && git pull https://github.com/csdummi/CommandlinePasswordManager.git")
	os.system("cd " + current_dir)

if __name__ == '__main__':
    check_if_valid()
    args = sys.argv
    services = loadPasswds()

    if sys.argv[1] == 'get': # Get Password to service

        passwd = getPass(sys.argv[2],services) # Ask for Password without displaying it in the console
        if passwd != False: # paswd is either False or the password for service
            split_at = services[sys.argv[2]]['split_at']
            passwd = passwd[:split_at]
            middle_index = int(len(passwd) / 2)
            passwd = passwd[:middle_index].upper() + passwd[middle_index-1:]
            print(passwd)

        else: # Display error message
            print("Masterpassword wrong!")

    elif sys.argv[1] == 'set': # Set new Masterpassword
        services = addMasterpass(getpass.getpass("New Masterpassword:"), services)
        save(services)
    else: # Invalid parameters : Display usage
        usage = """
        Usage:\n
        \tget <service>:\t Get Password for Service after entering Masterpassword\n
        \tset:\tSet Masterpassword
        """
        print(usage)
