from web3 import Web3

from utils import logger
from config import node

def balance_check(private_key, acc_info):
    w3 = Web3(Web3.HTTPProvider(node))
    if w3.is_connected():
        account = w3.eth.account.from_key(private_key)
        adres = account.address
        balance = w3.eth.get_balance(adres)
        balance_eth = w3.from_wei(balance, 'ether')
        logger.success(f'Баланс - {balance_eth} ETH, acc.{acc_info}')
        return balance_eth, adres
    else:
        logger.error(f'Не удалось подключиться к сети.')
            

        