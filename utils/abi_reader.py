import json

def abi_read(file):
    abi = json.loads(open(file).read())
    return abi