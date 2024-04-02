'''
Sukurkite funkciją, kuri grąžintų tik unikalius simbolius turinčias string reikšmes
'''
zodziai = ('Jonas,Petras,Antanas')
unikali = ('Jonas')
vienas_zodis = str
def unikalus(zodis:str, unikali:str) -> str:
    vienas_zodis = zodziai.split(',')
    for i in vienas_zodis:
        for x in len(vienas_zodis):
            print(x)





unikalus(zodziai, unikali)

print()



