from time import sleep

def batida():
    print('Toc')
    sleep(1)

def apresentacao():
    print('Tem alguém ai ?')
    sleep(3)
    print('Pelo visto não tem ninguém...')

for x in range(0,2):
    batida()
apresentacao()