import random
import time

def gen_emodji():
    emodji = [emoji.emojize(':herb:'), emoji.emojize(':teacup_without_handle:'), emoji.emojize(':green_heart:'), emoji.emojize(':seedling:')]
    return random.choice(emodji)
