from instabot import Bot
import shutil
import json
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time as tm
import random as rd
import numpy as np
import pandas as pd
from datetime import datetime



def get_new_accounts():

    try:
        shutil.rmtree('config', ignore_errors=True)
    except: pass

    bot = Bot()

    #fazer login
    bot.login(username="", password="")

    #definindo as tags
    tags = ["extensaoufpb", "proexufpb","probex2021", "editaisdaextensao","probexufpb"]

    #coletando as contas que postaram com as tags
    userids = []

    n1 = 0
    for x in tags:
        userids.append(bot.get_hashtag_users(tags[n1]))
        n1 += 1


    #separando somente as contas que postaram com as 5 tags
    tuser = []
    n=0
    for x in userids:
        for y in userids[n]:
            n2 = 0
            n3 = 0
            while n2 <= 5:
                # ao menos 2 das tags por pub ja servem
                if n3 == 2:
                    tuser.append(y)
                    n2=5
                    break
                elif n2==5:
                    break
                elif y in userids[n2]:
                    n3+=1
                n2+=1
        n+=1


    #transformando as ids em username
    name = []
    for x in tuser:
        name.append(bot.get_username_from_user_id(x))


    #limpando as repetições
    tname = set(name)

    name_list = list(tname)

    #escrevendo contas num documento de texto
    with open('C:/Users/Felilpe Lima/Desktop/ODE job/txt/found_accounts.txt', 'w') as txt:
        json.dump(name_list, txt)

    print(name_list)



    shutil.rmtree('config', ignore_errors=True)



def delete_repeated_and_errors():
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

    print("accounts to verify ",accounts)

    return accounts






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



    if len(contaruim)!=0:
        for n in range(len(contaruim)):
            false_accounts.append(contaruim[n])

        with open('C:/Users/Felilpe Lima/Desktop/ODE job/txt/false_accounts.txt', 'w') as txt:
            json.dump(false_accounts, txt)


    if len(contaboa)!=0:
        for n in range(len(contaboa)):
            true_accounts.append(contaboa[n])
        
        with open('C:/Users/Felilpe Lima/Desktop/ODE job/txt/true_accounts.txt', 'w') as txt:
            json.dump(true_accounts, txt)



    driver.close()



def scrap():

    #specify the path to chromedriver.exe 
    driver = webdriver.Chrome('C:/Users/Felilpe Lima/Documents/chromedriver.exe')

    #funcao de espera
    def espere(m):
        #m deve levar valor de 1 a 3
        if m == 0:
            tm.sleep(rd.uniform(0,1))
        if m == 1:
            tm.sleep(rd.uniform(1,6))
        elif m == 2:
            tm.sleep(rd.uniform(8, 16))
        elif m == 3:
            tm.sleep(rd.uniform(30,120))
    #função de como esperar

    def como_esperar(n):
        #fazendo o programa de espera em tempos aleatorios
        if n==0:
            espere(0)
        elif n%22==0:
            espere(3)
        elif n%40==0:
            #espera muito tempo depois de 80 contas
            tm.sleep(rd.uniform(3600,3000))
        elif n%2 == 0:
            espere(2)
        else:
            espere(1)
    #função login
    def login(account_now):

        #open the webpage
        driver.get("https://www.instagram.com/accounts/login/")

        #target username
        username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
        password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))

        my_username = ["fionagatos","aurora_gatos"]
        my_password = ["pitocofiona5","pitocofiona"]

        print('fazendo o login como',my_username[account_now])

        #enter username and password
        username.clear()
        username.send_keys(my_username[account_now])
        password.clear()
        password.send_keys(my_password[account_now])

        #target the login button and click it
        button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

        tm.sleep(5)
        alert = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Agora não")]'))).click()
        alert2 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Agora não")]'))).click()

    #encontrar a data por motivo de analise de progresso
    date=datetime.now()
    StrDate=str(date.day) + '_' + str(date.month) + '_' + str(date.year)


    #login
    my_account_now=-1
    #login(my_account_now)

    #loading accounts
    with open('C:/Users/Felilpe Lima/Desktop/ODE job/txt/true_accounts.txt', 'r') as txt:
        accounts_to_scrap = json.load(txt)
    
    f_accounts=[]
    accounts_scrap_done = []
    data=[]
    number_reapeted_errors = 0
    n=0

    espere(2)

    while n < len(accounts_to_scrap):

        account = accounts_to_scrap[n]

        #guardando contas já feitas
        accounts_scrap_done.append(account)

        link = 'http://www.instagram.com/' + account
        espere(1)

        #open the webpages
        driver.get(link)

        #espere
        como_esperar(n)

        #data = pub + seguidores + seguidos
        #procurando os elementos na pagina
        new_data=driver.find_elements_by_class_name("g47SY")

        #salvando o len dos dados antes da adicao de novos dados para anular erros
        qt1= len(data)

        #substituindo os elementos no destino
        for y in new_data:
            data.append(y.text)

        #salvando o len dos dados depois da adicao de novos dados para anular erros
        qt2= len(data)

        #comparando os lens antes e depois, caso o len seja o mesmo, novos dados não foram adicionados, então ele deve salvar todas as contas que funcionaram e as que não
        if qt1==qt2:
            f_accounts.append(account)

            #contando as contas que tiveram erro, pois caso aconteca muitas vezes, o instagram bloqueou a pesquisa
            number_reapeted_errors+=1

            #printando contas com erro
            print('w', f_accounts)

            #acrescentando ODE nas contas que deram erro
            i=0
            while i<3:
                data.append('ODE')
                i+=1



            #se ocorrerem 3 erros seguidos, outra conta deve fazer login
            if number_reapeted_errors==3:
                driver.close()

                driver = webdriver.Chrome('C:/Users/Felilpe Lima/Documents/chromedriver.exe')

                #faz novo login
                my_account_now+=1
                login(my_account_now)

                #Indica as contas que faltam fazer o scrap
                n-=3

                #remove os erros da lista de contas analisadas
                p=0
                while p<3:
                    accounts_scrap_done.pop(-1)
                    f_accounts.pop(-1)
                    p+=1

                #remove dos dados os erros das contas
                q=0
                while q <9:
                    data.pop(-1)
                    q+=1


        else:
            number_reapeted_errors=0

        #fazendo tabela de seguidores e seguidos
        columns = ['Pubs  ','seguidores  ','seguindo']

        data_for_table = np.array(data).reshape(len(accounts_scrap_done), 3 )

        pd.set_option("display.max_rows",999)
        main_table = pd.DataFrame(data=data_for_table, index=accounts_scrap_done,columns=columns)

        print('\n\n', main_table)


        print('\n', data, '\n', n)



        n+=1

    #exportando os dados até o excell
    with pd.ExcelWriter("C:/Users/Felilpe Lima\Desktop/ODE/tabelas ode/Data Ode Corrigida.xlsx", mode="a", engine="openpyxl") as writer:
        main_table.to_excel(writer, sheet_name=StrDate)


    driver.close()
    exit()
