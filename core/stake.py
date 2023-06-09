from web3 import Web3, HTTPProvider
from random import randint

from utils import logger, abi_read, failed_accs_w
from config import node

def stake_tokens(key, name, value, token, contr):

    w3 = Web3(HTTPProvider(node))
    acc = w3.eth.account.from_key(key)

    contract_instance = w3.eth.contract(address='0x779d1b5315df083e3F9E94cB495983500bA8E907', abi=abi_read('abies\eigen_layer.json'))
    
    tx = contract_instance.functions.depositIntoStrategy(contr, token, value).build_transaction({
        'from': acc.address,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(acc.address),
        'value': 0
    })
    
    sign = acc.sign_transaction(tx)
    hash = w3.eth.send_raw_transaction(sign.rawTransaction)
    reciept = w3.eth.wait_for_transaction_receipt(hash)
    
    logger.info(f"Transaction: https://goerli.etherscan.io/tx/{w3.to_hex(hash)}")
    
    return(w3.to_hex(hash))
    
        
        
