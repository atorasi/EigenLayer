def success_accs_w(privat, adr):
    with open('succes_accs.txt', 'a') as file:
        file.write(f'{privat}:{adr}\n')


def failed_accs_w(privat, adr):
    with open('failed_accs.txt', 'a') as file:
        file.write(f'{privat}:{adr}\n')