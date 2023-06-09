from time import sleep
from random import randint

from utils import logger
from config import sleep_b_activity, sleep_from_act, sleep_to_act, sleep_b_accs, sleep_accs_from, sleep_accs_to

def wanna_sleep_activ():
    if sleep_b_activity == True:
        time_to_sleep = randint(sleep_from_act, sleep_to_act)
        sleep(time_to_sleep)
        return(time_to_sleep)

def wanna_sleep_accs():
    if sleep_b_accs == True:
        time_to_sleep = randint(sleep_accs_from, sleep_accs_to)
        logger.info(f'Сплю {time_to_sleep}с между аккаунтами')
        sleep(time_to_sleep)
        return(time_to_sleep)