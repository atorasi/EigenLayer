from web3 import Web3, HTTPProvider
from random import randint

from utils import logger, abi_read, failed_accs_w
from config import node

def approve_trans(private_key, acc_info, token_adress, abi_file, token_name):
    w3 = Web3(HTTPProvider(node))
    
    logger.info(f'Аппруваю {token_name} - acc.{acc_info}')
    acc = w3.eth.account.from_key(private_key)
    adres = acc.address
    
    bal_contract = w3.eth.contract(address=Web3.to_checksum_address(token_adress), abi=abi_read(abi_file))
    balance_fp = bal_contract.functions.balanceOf(adres).call()
    balance_at = w3.from_wei(balance_fp, 'ether')
    balance_to_deposit = float(balance_at) * randint(50000, 70000) / 100000
    logger.info(f'Баланс {token_name} - {balance_at}, acc.{acc_info}')
    
    contract_instance = w3.eth.contract(address=token_adress, abi=abi_read(abi_file))
    tx = contract_instance.functions.approve('0x779d1b5315df083e3F9E94cB495983500bA8E907', balance_fp).build_transaction({
        "gasPrice": w3.eth.gas_price,
        "from": adres,
        "nonce": w3.eth.get_transaction_count(adres),
        "value": 0,
    })
    
    sign = acc.sign_transaction(tx)
    hash = w3.eth.send_raw_transaction(sign.rawTransaction)
    reciept = w3.eth.wait_for_transaction_receipt(hash)
    
    logger.info(f"Transaction: https://goerli.etherscan.io/tx/{w3.to_hex(hash)}")        
    return w3.to_wei(balance_to_deposit, 'ether')
    
    
        