

lambda_daugyba = lambda x, y: x * y
lambda_suma = lambda x, y: x + y
lambda_dalyba = lambda x, y: x / y
lambda_atimtis =lambda x, y: x - y


def count_numbers(a, b , function):
    veiksmas = input('Iveskite koki veiksma norite atlikti:')
    if veiksmas =='daugyba': function = lambda_daugyba
    elif veiksmas == 'dalyba' : function = lambda_dalyba
    elif veiksmas == 'suma' : function = lambda_suma
    elif veiksmas == 'atimtis' : function = lambda_atimtis
    else:
     print('Nera tokio operatoriaus!')
    break
    return function (a, b)

print(count_numbers(5,7, lambda_dalyba))

