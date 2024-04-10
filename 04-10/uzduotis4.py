'''
Exercise 4: Iterate a given list and check if a given element
exists as a key’s value in a dictionary. If not, delete it from the list
Given:

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}
Expected Outcome:

After removing unwanted elements from list [47, 69, 76, 97]
'''

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'John':47, 'Emma':69, 'Kelly':76, 'Jason':97}

def remove_elements(listas, samplai):
    result= []
    for i in listas:
        if i in samplai.values():
            result.append(i)
    return result

print(remove_elements(roll_number, sample_dict))