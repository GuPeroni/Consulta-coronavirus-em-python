import requests
import time

ps = str(input("Digite o país : "))
if ps != f'Brasil':
    print('Pais inválido')
    exit()
else :



    def coronaVirus():
        pais = 'Brazil'
        url = ('https://pomber.github.io/covid19/timeseries.json')
        req = requests.get(url, timeout=3000)
        retorno = req.json()
        dicionario = retorno[pais]
        info = dicionario[-1]
        print(f"""Pais : {pais}
Data : {info['date']}
Confirmados : {info['confirmed']}
Mortos : {info['deaths']}
Recuperados : {info['recovered']}""")


    coronaVirus()



while True:
    print('------------------------------------')
    consulta = int(input('Deseja realizar uma nova consulta ?\n 1 - Sim\n 2 - Não\nDigite o número : \n'))
    
    if consulta == 1:
        print('                         ')
        ps = str(input("Digite o país : "))
        print('                          ')
        coronaVirus()
    elif consulta == 2:'\n'
    time.sleep(1)
    print('Saindo....')
    break       


