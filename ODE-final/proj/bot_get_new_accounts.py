from instabot import Bot
import shutil
import json

try:
    shutil.rmtree('config', ignore_errors=True)
except: pass

bot = Bot()

#fazer login
#bot.login(username="auroragatabranca@gmail.com", password="pitocofiona")
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
    


if __name__ == "__main__":
    print(name_list)



shutil.rmtree('config', ignore_errors=True)

