from selenium import webdriver
import json

def verify_and_update(accounts_to_scrap):
    #specify the path to chromedriver.exe 
    driver = webdriver.Chrome('C:/Users/Felilpe Lima/Documents/chromedriver.exe')

    n=0

    contaboa=[]
    contaruim=[]
    erro=[]

    while n < len(accounts_to_scrap):

        account = accounts_to_scrap[n]

        #guardando contas já feitas
        link = 'http://www.instagram.com/' + account

        #open the webpages
        driver.get(link)

        try:
    	    moderador= int(input('classifique \n0 bom \n1 ruim\n2 erro\n3 volta\n\n'))
        except:
    	    moderador=4

        if moderador==0:
            contaboa.append(account)
        elif moderador==1:
            contaruim.append(account)
        elif moderador==2:
            erro.append(account)
        elif moderador==3:
            n-=2
        else:
            n-=1

        print(contaboa,'\n',contaruim,'\n',erro)

        n+=1


    with open('C:/Users/Felilpe Lima/Desktop/ODE job/txt/false_accounts.txt', 'r') as txt:
        false_accounts = json.load(txt)


    with open('C:/Users/Felilpe Lima/Desktop/ODE job/txt/true_accounts.txt', 'r') as txt:
        true_accounts = json.load(txt)

    false_accounts.append(contaruim)
    true_accounts.append(contaboa)

    with open('C:/Users/Felilpe Lima/Desktop/ODE job/txt/false_accounts.txt', 'w') as txt:
        json.dump(false_accounts, txt)

    with open('C:/Users/Felilpe Lima/Desktop/ODE job/txt/true_accounts.txt', 'w') as txt:
        json.dump(true_accounts, txt)

    driver.close()

