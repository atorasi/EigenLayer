from random import randint

from config import *
from core import balance_check, bridge_geth, send_geth_to_steth, approve_trans, stake_tokens
from utils import logger, wanna_sleep_activ, wanna_sleep_accs, success_accs_w, failed_accs_w


if __name__ == '__main__':
    print(text1)
    
    with open('private_keys.txt') as file:
        pkeys = [row.strip() for row in file]
        
    logger.info(f'Загружено {len(pkeys)} аккаунтов')

    for acc_number, key in enumerate(pkeys, start=1):
        try:
            logger.info(f'Начинаю выполнять аккаунт {key[:3]}...{key[-3:]} - |№{acc_number}|')
            acc_info = f'{key[:3]}...{key[-3:]}'
            
            balance, adres = balance_check(key, acc_info)
            
            reason = 'RocketPool'
            value_to_rpool = float(balance) * randint(percent_from_rp * 1000, percent_from_rp * 1000) / 100000 if balance >= 0.1 else randint(1200, 2000) / 100000
            balance = float(balance) - value_to_rpool
            hash_rpool = bridge_geth(key, value_to_rpool, acc_info)
            logger.success(f'Задепозитил в RocketPool - acc.{acc_info}, сплю {wanna_sleep_activ()} |№{acc_number}|')
            
            reason = 'gETH sender'
            value_to_steth = float(balance) * randint(percent_from_st * 1000, percent_to_st * 1000) / 100000
            balance = float(balance) - value_to_steth
            hash_steth = send_geth_to_steth(key, value_to_steth, acc_info)
            logger.success(f'Отправил gETH - acc.{acc_info}, сплю {wanna_sleep_activ()} |№{acc_number}|')  
            
            reason = 'approve rETH'
            balance_reth = approve_trans(key, acc_info, reth_adres, 'abies\\reth_goerli.json', 'rETH')
            logger.success(f'Апрувнул rETH - acc.{acc_info}, сплю {wanna_sleep_activ()} |№{acc_number}|')
            
            reason = 'stake rETH'
            stake_reth = stake_tokens(key, acc_info, balance_reth, reth_adres, reth_stake)
            logger.success(f'Застейкал rETH- acc.{acc_info}, сплю {wanna_sleep_activ()} |№{acc_number}|')

            reason = 'approve stETH'
            balance_steth = approve_trans(key, acc_info, steth_adres, 'abies\\steth_goerli.json', 'stETH')
            logger.success(f'Апрувнул stETH - acc.{acc_info}, сплю {wanna_sleep_activ()} |№{acc_number}|')
            
            reason = 'stake stETH'
            stake_steth = stake_tokens(key, acc_info, balance_steth, steth_adres, steth_stake)
            logger.success(f'Застейкал stETH- acc.{acc_info}, сплю {wanna_sleep_activ()} |№{acc_number}|')


            logger.success(f'Аккаунт выполнен - acc.{acc_info}\n\n')
            success_accs_w(key, adres)
            print('')
            
            wanna_sleep_accs()
            
        except Exception as e:
            logger.error(f'Ошибка на моменте: {reason}, причина: {e}')
            failed_accs_w(key, adres)
            print('')
            continue
            

            
            
