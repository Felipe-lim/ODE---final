import json


with open('C:/Users/Felilpe Lima/Desktop/ODE job/txt/found_accounts.txt', 'r') as txt:
    found_accounts = json.load(txt)


with open('C:/Users/Felilpe Lima/Desktop/ODE job/txt/false_accounts.txt', 'r') as txt:
    false_accounts = json.load(txt)


with open('C:/Users/Felilpe Lima/Desktop/ODE job/txt/true_accounts.txt', 'r') as txt:
    true_accounts = json.load(txt)



accounts = []

for item in found_accounts:
    if not ( item in false_accounts or item in true_accounts ):
        accounts.append(item)

print(accounts)
