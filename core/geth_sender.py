from web3 import Web3, HTTPProvider
from config import node
from utils import logger, failed_accs_w

def send_geth_to_steth(private_key, value, acc_info):
    steth_address = '0x1643E812aE58766192Cf7D2Cf9567dF2C37e9B7F'
    w3 = Web3(HTTPProvider(node))

    acc = w3.eth.account.from_key(private_key)
    logger.info(f'Обмениваю {value}gETH на stETH, acc.{acc_info}')
    
    
    tr = {
        'from': acc.address,
        'to': steth_address,
        'gasPrice': w3.eth.gas_price,
        'nonce': w3.eth.get_transaction_count(acc.address),
        'value': w3.to_wei(value, 'ether'),
        'gas': 400000,
        'chainId': 5,
    }
    
    sign = acc.sign_transaction(tr)
    hash = w3.eth.send_raw_transaction(sign.rawTransaction)
    reciept = w3.eth.wait_for_transaction_receipt(hash)
    
    logger.info(f"Transaction: https://goerli.etherscan.io/tx/{w3.to_hex(hash)}")
    
    return(w3.to_hex(hash))
    

