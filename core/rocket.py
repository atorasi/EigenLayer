from web3 import HTTPProvider, Web3

from utils import abi_read, logger, failed_accs_w
from config import node


def bridge_geth(private_key, deposit_value, acc_info):
    w3 = Web3(HTTPProvider(node))
    
    acc = w3.eth.account.from_key(private_key)
    adres = acc.address

    logger.info(f'Бриджу {deposit_value} в Rocket Pool, acc.{acc_info}')
    
    contract_instance = w3.eth.contract(address='0xa9A6A14A3643690D0286574976F45abBDAD8f505', abi=abi_read('abies\\rocketpool.json'))
    
    gas_price = w3.eth.gas_price
    nonce = w3.eth.get_transaction_count(adres)
    wei_amount = w3.to_wei(deposit_value, 'ether')
    

    tr = contract_instance.functions.deposit().build_transaction({
        "gasPrice": gas_price,
        "from": adres,
        "nonce": nonce,
        "value": wei_amount,
    })
    
    sign = acc.sign_transaction(tr)
    tx = w3.eth.send_raw_transaction(sign.rawTransaction)
    reciept = w3.eth.wait_for_transaction_receipt(tx)

    logger.info(f"Transaction: https://goerli.etherscan.io/tx/{w3.to_hex(tx)}")    
    return(w3.to_hex(tx))
    
    
        