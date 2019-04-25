# campo das variaveis/funções:
from time import sleep
info_colida = {}
v_cabaco = {}
bebedeira = {}
fumante = {}
TB_f = 'Nada'
opc = 's'
d = 'x'
l = 'x'

print("  ")
print("Abrindo o programa")
sleep(1)
print("Carregando as variaveis ...")
sleep(2)
print("..... aguarde ....")


for x in range(1, 100, 18):
    print(x, "%")
    sleep(0.6)
print("100 %")

while opc.lower() == "s" or opc.lower() == "sim":

    print("  ")
    sleep(1)
    print("Oi!")
    print("  ")
    print("Iremos lhe fazer algumas perguntas.")
    print("Não nos responsabilizamos pelo teor das perguntas e resposta.")
    print("Ao responder digite sempre em letra minúscula conforme o exemplo acima das perguntas que exigem texto.")
    print("Não deixe nenhuma resposta em branco, pois pode gerar complicações no programa.")
    print("Não é possível alterar a resposta das perguntas anteriores.")
    print("Favor responda da forma mais sincera possível.")
    print("  ")
    print(" Você deseja continuar, aceitando todos os nossos termos?")
    print("  ")

    R = input(" s = Sim / n = Não :")
    if R.lower() == "s" or R.lower() == "sim":
        R = "Sim"
        info_colida["Termos do questionário"] = R
        print("Ok, Bora la!")

        print("  ")

        nome = input("Qual é o seu nome? :")
        info_colida["Nome"] = nome

        idade = int(input("Qual a sua idade? :"))
        info_colida["Idade"] = idade

        altura = input("Qual a sua altura? :")
        altura = altura + "m"
        info_colida["Altura"] = altura

        peso = float(input("Quanto você pesa? :"))
        info_colida["Peso"] = peso
        if peso >= 75.99:
            print("♤ Ok, entendi você é gordo. ")

        print("  ")
        

        print("Estado civil:")
        print("Dentre as opções abaixo qual você melhor se encaixa? :")
        print ("|1. Casado (a) ")
        print ("|2. Noivando (a) ")
        print ("|3. Separado (a) ")
        print ("|4. Ficando ")
        print ("|5. Namorando ")
        print ("|6. Vários contatihos ")
        print ("|7. Passando o rodo ")
        print ("|8. Não, tó de boa. ")
        print ("|9. Livre, leve e solto (a). ")
        print("-Digite apenas o numero da opção desejada")
        estado_civil = input("E ai em que situação você está ? :")
        if estado_civil == "1" or estado_civil == "1.":
            print("♤ Aaah meus sinceros pêsames. ")
            estado_civil = "Casado (a) "
        elif estado_civil == "2" or estado_civil == "2.":
            print("♤ IH! K7, corre que ainda da tempo. ")
            estado_civil = "Noivando (a) "
        elif estado_civil == "3" or estado_civil == "3.":
            print("♤ Kkk. Cansou da vida de casado. ")
            estado_civil = "Separado (a) "
        elif estado_civil == "4" or estado_civil == "4.":
            print("♤ Isso, fica só nisso mesmo. ")
            estado_civil = "Ficando "
        elif estado_civil == "5" or estado_civil == "5.":
            print("♤ É isso aí, mas não passa disso. Fica dica. ")
            estado_civil = "Namorando "
        elif estado_civil == "6" or estado_civil == "6.":
            print("♤ Aaaeehh caria, só aprenda a administrar. ")
            estado_civil = "Vários contatihos "
        elif estado_civil == "7" or estado_civil == "7.":
            print("♤ Eita, só cuidado para não contrair nenhuma doença. ")
            estado_civil = "Passando o rodo "
        elif estado_civil == "8" or estado_civil == "8.":
            print("♤ Isso aí continue assim.")
            estado_civil = "Não, tó de boa. "
        elif estado_civil == "9" or estado_civil == "9.":
            print("♤ Isso aí continue assim.")
            estado_civil = "Livre, leve e solto (a). "
        
        info_colida["Estado civil"] = estado_civil
        
        
        print("  ")

        print(" f = Feminino / m = Masculino ")
        sexo = input("Sexo? :")

        if sexo.lower() == "m" or sexo.lower() == "masculino":
            sexo = "Masculino"
            info_colida["Sexo"] = sexo

            print("  ")

            print(" s = Sim / n = Não ")
            v = input("Ja perdeu o cabaço? :")
            if idade >= 15 and v.lower() == "n" or v.lower() == "ñ" or v.lower() == "nao" or v.lower() == "não":
                print("♤ Ja ta na hora de perder o cabaço!!!")
                v = "Não"
                info_colida["Ja perdeu o cabaço"] = v
                v_cabaco["Ja perdeu o cabaço"] = v
                v_cabaco["Resposta do código"] = "♤ Ja ta na hora de perder o cabaço!!!"
            elif idade >= 15 and v.lower() == "s" or v.lower() == "sim":
                print("♤ Aaaaaaeeeeee PORRA!!!!!!")
                v = "Sim"
                info_colida["Ja perdeu o cabaço"] = v
                v_cabaco["Ja perdeu o cabaço"] = v
                v_cabaco["Resposta do código"] = "♤ Aaaaaaeeeeee PORRA!!!!!!"
            elif idade <= 15 and v.lower() == "s" or v.lower() == "sim":
                print("♤ Eita porra, tu não perde tempo!")
                v = "Sim"
                info_colida["Ja perdeu o cabaço"] = v
                v_cabaco["Ja perdeu o cabaço"] = v
                v_cabaco["Resposta do código"] = "♤ Eita porra, tu não perde tempo!"

        print("  ")

        if sexo == "Masculino" and v == "Sim":
            print(" s = Sim / n = Não ")
            c = input("Você sabe usar uma camisinha? :")
            if c.lower() == "n" or c.lower() == "ñ" or c.lower() == "nao" or c.lower() == "não":
                print("♤ Você é idiota, quer ter um filho inesperado K7! ")
                print("♤ Vai aprender a colocar uma antes de foder alguém! ")
                print("♤ Aqui vai uma dica para você: https://www.youtube.com/watch?v=oJZVFnPs9ao ")
                print("_I•D•I•O•T•A_")
                c = "Não"
                v_cabaco["Sabe usar uma camisinha"] = c
                info_colida["Resposta do código"] = "♤ Aqui vai uma dica para você: https://www.youtube.com/watch?v=oJZVFnPs9ao /// _I•D•I•O•T•A_"
                v_cabaco["Resposta do código"] = "♤ Aqui vai uma dica para você: https://www.youtube.com/watch?v=oJZVFnPs9ao /// _I•D•I•O•T•A_"
            elif idade <= 15 and c.lower() == "s" or c.lower() == "sim":
                print("♤ Isso aí, já estava na hora mesmo. ")
                print("♤ Agora só aproveita! ")
                c = "Sim"
                v_cabaco["Sabe usar uma camisinha"] = c
                info_colida["Resposta do código"] = "♤ Isso aí, já estava na hora mesmo."
                v_cabaco["Resposta do código"] = "♤ Isso aí, já estava na hora mesmo."
            elif idade >= 15 and c.lower() == "s" or c.lower() == "sim":
                print("♤ Bom garoto, continue assim! ")
                print("♤ Agora só aproveita! ")
                c = "Sim"
                v_cabaco["Sabe usar uma camisinha"] = c
                info_colida["Resposta do código"] = "♤ Bom garoto, continue assim!"
                v_cabaco["Resposta do código"] = "♤ Bom garoto, continue assim!"

        print("  ")

        print(" s = Sim / n = Não ")
        alcool = input("Você bebê? :")
        if idade <= 17 and alcool.lower() == "s" or alcool.lower() == "sim":
            print("♤ É então, não deveria mas, isso ai. ")
            alcool = "Sim"
            info_colida["Você bebê"] = alcool
            bebedeira["Você bebê"] = alcool
            bebedeira["Resposta do código"] = "♤ É então, não deveria mas, isso ai."
            print("  ")
        elif idade <= 17 and alcool.lower() == "n" or alcool.lower() == "ñ" or alcool.lower() == "nao" or alcool.lower() == "não":
            print("♤ Boa!!! ")
            alcool = "Não"
            info_colida["Você bebê"] = alcool
            bebedeira["Você bebê"] = alcool
            bebedeira["Resposta do código"] = "♤ Boa!!!"
            print("  ")
        elif idade >= 18 and alcool.lower() == "n" or alcool.lower() == "ñ" or alcool.lower() == "nao" or alcool.lower() == "não":
            print("♤ Coitado(a), ainda não provas tes da água sagrada. ")
            alcool = "Não"
            info_colida["Você bebê"] = alcool
            bebedeira["Você bebê"] = alcool
            bebedeira["Resposta do código"] = "♤ Coitado(a), ainda não provas tes da água sagrada."
            print("  ")

        if alcool.lower() == "s" or alcool.lower() == "sim":
            print("   Por favor, escolha um padrão para cálculo da bebida:")
            print("-"*64)
            print("  1 Latinha == Latinha de cerveja, com o teor alcoólico de 5%.")
            print("  1 Dose == Dose de vodka, com teor alcoólico de 35%.")
            print("_"*64)

            print("  ")
            print(" d = Dose / l = Latinha ")
            ld = input("Qual você prefere usar como padrão para o calculo? :")
            print("  ")

            if ld.lower() == "d" or ld.lower() == "dose":
                ld = "Dose"
                bebedeira["Escolha de padrão para calculo"] = ld
                print(" Em uma escala de 1 a 10:")
                print(" 1 == 1 Dose, assim 10 == 10 Doses")
                print("  ")
                print(" OK !? ")
                print("  ")
                d = float(input("Quantas Doses você bebê? :"))
                bebedeira["Quantas Doses você bebê"] = d
                if d <= 0:
                    print("♤ Então, Por que você colocou Sim na pergunta ,Se você bebia. ")
                    print(" I•D•I•O•T•A _|_ ")
                    bebedeira["Resposta do código"] = " I•D•I•O•T•A _|_ "
                elif d >= 0.1 and d <= 1.99:
                    print("♤ Ééh você esta bem, comtinui assim. ")
                    bebedeira["Resposta do código"] = "♤ Ééh você esta bem, comtinui assim."
                elif d >= 2.0 and d <= 2.99:
                    print("♤ Fica nisso que ta suave. ")
                    bebedeira["Resposta do código"] = "♤ Fica nisso que ta suave."
                elif d >= 3.0 and d <= 3.99:
                    print("♤ Pronto para fazer varias merdas e não lembrar depois. ")
                    bebedeira["Resposta do código"] = "♤ Pronto para fazer varias merdas e não lembrar depois."
                elif d >= 4.0 and d <= 4.99:
                    print("♤ Iih FUDEO, não lembra de nada que aconteceu no dia/noite passada. ")
                    bebedeira["Resposta do código"] = "♤ Iih FUDEO, não lembra de nada que aconteceu no dia/noite passada."
                elif d >= 5.0 and d <= 5.99:
                    print("♤ Sintomas de um pocível PT. ")
                    bebedeira["Resposta do código"] = "♤ Sintomas de um pocível PT."
                elif d >= 6.0 and d <= 6.99:
                    print("♤ Esse aí da PT direto, sem duvida. ")
                    bebedeira["Resposta do código"] = "♤ Esse aí da PT direto, sem duvida."
                elif d >= 7.0 and d <= 7.99:
                    print("♤ Acho que seu figado ja está pedindo arrego. ")
                    bebedeira["Resposta do código"] = "♤ Acho que seu figado ja está pedindo arrego."
                elif d >= 8.0 and d <= 8.99:
                    print("♤ Falência múltipla dos órgãos. ")
                    bebedeira["Resposta do código"] = "♤ Falência múltipla dos órgãos."
                elif d >= 9.0 and d <= 10.0:
                    print("👽 Tio, NA MORAL, como você está vivo até hoje!!¿ ")
                    bebedeira["Resposta do código"] = "👽 Tio, NA MORAL, como você está vivo até hoje!!¿"

            if ld.lower() == "l" or ld.lower() == "latinha":
                ld = "Latinha"
                bebedeira["Escolha de padrão para calculo"] = ld
                print(" Em uma escala de 1 a 10:")
                print(" 1 == 1 Latinha, assim 10 == 10 Latinhas")
                print("  ")
                print(" OK !? ")
                print("  ")
                l = float(input("Quantas Latinhas você bebê? :"))
                bebedeira["Quantas Latinhas você bebê"] = l
                if l <= 0:
                    print("♤ Então, Por que você colocou Sim na pergunta ,Se você bebia. ")
                    print(" I•D•I•O•T•A _|_ ")
                    bebedeira["Resposta do código"] = " I•D•I•O•T•A _|_ "
                elif l >= 0.1 and l <= 1.99:
                    print("♤ Ééh você esta bem, comtinui assim. ")
                    bebedeira["Resposta do código"] = "♤ Ééh você esta bem, comtinui assim."
                elif l >= 2.0 and l <= 2.99:
                    print("♤ Fica nisso que ta suave. ")
                    bebedeira["Resposta do código"] = "♤ Fica nisso que ta suave."
                elif l >= 3.0 and l <= 3.99:
                    print("♤ Pronto para fazer varias merdas e não lembrar depois. ")
                    bebedeira["Resposta do código"] = "♤ Pronto para fazer varias merdas e não lembrar depois."
                elif l >= 4.0 and l <= 4.99:
                    print("♤ Iih FUDEO, não lembra de nada que aconteceu no dia/noite passada. ")
                    bebedeira["Resposta do código"] = "♤ Iih FUDEO, não lembra de nada que aconteceu no dia/noite passada."
                elif l >= 5.0 and l <= 5.99:
                    print("♤ Sintomas de um pocível PT. ")
                    bebedeira["Resposta do código"] = "♤ Sintomas de um pocível PT."
                elif l >= 6.0 and l <= 6.99:
                    print("♤ Esse aí da PT direto, sem duvida. ")
                    bebedeira["Resposta do código"] = "♤ Esse aí da PT direto, sem duvida."
                elif l >= 7.0 and l <= 7.99:
                    print("♤ Acho que seu figado ja está pedindo arrego. ")
                    bebedeira["Resposta do código"] = "♤ Acho que seu figado ja está pedindo arrego."
                elif l >= 8.0 and l <= 8.99:
                    print("♤ Falência múltipla dos órgãos. ")
                    bebedeira["Resposta do código"] = "♤ Falência múltipla dos órgãos."
                elif l >= 9.0 and l <= 10.0:
                    print("👽 Tio, NA MORAL, como você está vivo até hoje!!¿ ")
                    bebedeira["Resposta do código"] = "👽 Tio, NA MORAL, como você está vivo até hoje!!¿"

        print("  ")

        print(" s = Sim / n = Não ")
        f = input("Você fuma ou já fumo? :")
        if idade <= 17 and f.lower() == "n" or f.lower() == "ñ" or f.lower() == "nao" or f.lower() == "não":
            print("♤ Ótimo, e nunca faça isso. ")
            info_colida ["Você fuma ou já fumo?"] = "Não"
            fumante ["Você fuma ou já fumo?"] = "Não"
            fumante ["Resposta do código"] = "♤ Ótimo, e nunca faça isso."
        elif idade >= 17 and f.lower() == "n" or f.lower() == "ñ" or f.lower() == "nao" or f.lower() == "não":
            print("♤ Muito bem, continue assim !!! ")
            info_colida ["Você fuma ou já fumo?"] = "Não"
            fumante ["Você fuma ou já fumo?"] = "Não"
            fumante ["Resposta do código"] = "♤ Muito bem, continue assim !!!"
        elif idade <= 17 and f.lower() == "s" or f.lower() == "sim":
            print("♤ Que coisa feia. ")
            print("♤ Sua mãe sabe que você fuma ...? ")
            info_colida ["Você fuma ou já fumo?"] = "Sim"
            fumante ["Você fuma ou já fumo?"] = "Sim"
            fumante ["Resposta do código"] = "♤ Que coisa feia. Sua mãe sabe que você fuma ...?"
#           ----- Para analise (talvez uma função)-----
        elif idade >= 17 and f.lower() == "s" or f.lower == "sim":
            print("♤ Que coisa feia. ")
            print("♤ Não deveria mas ok.")
            info_colida ["Você fuma ou já fumo?"] = "Sim"
            fumante ["Você fuma ou já fumo?"] = "Sim"
            fumante ["Resposta do código"] = "♤ Que coisa feia. Não deveria mas ok."
            print("  ")
            print("♤ Bora continuar")

            sleep(1)
            print("  ")
            print("...abrindo o menu...")

            sleep(0.5)
            print("  ")
            print("Quais das opções abaixo você fuma ou já fumo? :")
            print(" 1.  Cigarro \n 2.  Grama \n 3.  Maconha \n 4.  Crack \n 5.  Margine \n 6.  Vaper \n 7. Outro(s) ")
            ops_f = int(input("Digite o número da opção de que você fuma: "))

            if ops_f == 1:
                print("OK")
                print("  ")
                print("Sua escolha foi Cigarro.")
                TB_f = "Cigarro"
                sleep(2.5)
                print("..Carregando.....")
                print("  ")
                print("--Pre definido pelo programador, como padrão para cálculo (Dia). ")
                vz = float(input("No período de um dia, você costuma fumar quantos Cigarros? : "))
                if vz <= 0:
                    print("♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. ")
                    print(" I•D•I•O•T•A _|_ ")
                    fumante ["Resposta do código"] = "♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. I•D•I•O•T•A _|_ "
                elif vz >= 0.1 and vz <= 1.99:
                    print("♤ Então mal começou e já pode parar. ")   
                    fumante ["Resposta do código"] = "♤ Então mal começou e já pode parar."             
                elif vz >= 2.0 and vz <= 2.99:
                    print("♤ Então mal começou e já pode parar. ") 
                    fumante ["Resposta do código"] = "♤ Então mal começou e já pode parar."                   
                elif vz >= 3.0 and vz <= 3.99:
                    print("♤ Então, já pode parar com isso. ")
                    print("♤ Ainda da tempo!! ")
                    fumante ["Resposta do código"] = "♤ Então, já pode parar com isso. Ainda da tempo!!"
                elif vz >= 4.0 and vz <= 4.99:
                    print("♤ Para de fuma k7!!! ")
                    print("♤ ISSO MATA!!!!! ")
                    fumante ["Resposta do código"] = "♤ Para de fuma k7!!! ISSO MATA!!!!!" 
                elif vz >= 5.0 and vz <= 5.99:
                    print("♤ Para de fuma k7, essa porra mata!!!!! ")
                    print("♤ Ainda da tempo!! ")
                    fumante ["Resposta do código"] = "♤ Para de fuma k7, essa porra mata!!!!! Ainda da tempo!!"
                elif vz >= 6.0 and vz <= 6.99:
                    print("♤ Tio para com essa merda, sério!! ")
                    fumante ["Resposta do código"] = "♤ Tio para com essa merda, sério!! "
                elif vz >= 7.0 and vz <= 7.99:
                    print("♤ Isso vicia, e não tem volta!! ")
                    sleep(1,5)
                    print("♤ Mentira tem volta sim, mas é complicado. ")
                    fumante ["Resposta do código"] = "♤ Isso vicia, e não tem volta!! Mentira tem volta sim, mas é complicado."
                elif vz >= 8.0 and vz <= 8.99:
                    print("♤ Tio para, para, para que isso não dá certo. ")
                    print("♤ Teu pulmão não vai aguentar k7. ")
                    fumante ["Resposta do código"] = "♤ Tio para, para, para que isso não dá certo. Teu pulmão não vai aguentar k7."
                elif vz >= 9.0 and vz <= 9.99:
                    print("♤ Tio teu pulmão não vai aguentar. ")
                    print("♤ Para com isso! ")
                    fumante ["Resposta do código"] = "♤ Tio teu pulmão não vai aguentar. Para com isso!" 
                elif vz >= 10.0 and vz <= 10.99:
                    print("♤ OK, você fuma, mas deveria para urgente. ")
                    print("♤ Fica o aviso. ")
                    fumante ["Resposta do código"] = "♤ OK, você fuma, mas deveria para urgente. Fica o aviso."
                elif vz >= 10.99 and vz <= 40.99:
                    print("♤ CUIDADO ♤")
                    print("😵 Ministério da saúde adverte, fumar é prejudicial à saúde e pode causar câncer. ")
                    print("😵 Para não dizer que isso é falso... ")
                    sleep(1)
                    print("😵 Aqui está a prova: https://saudebrasilportal.com.br/eu-quero-parar-de-fumar ")
                    fumante ["Resposta do código"] = "😵 Ministério da saúde adverte, fumar é prejudicial à saúde e pode causar câncer."
                elif vz >= 50.00:
                    print("👽 Sério, como você está vivo até hoje ¡¿ ")
                    print("♤ CUIDADO ♤")
                    print("😵 Ministério da saúde adverte, fumar é prejudicial à saúde e pode causar câncer.")
                    print("😵 Para não dizer que isso é falso...")
                    sleep(1)
                    print("😵 Aqui está a prova: https://saudebrasilportal.com.br/eu-quero-parar-de-fumar ")
                    fumante ["Resposta do código"] = "😵 Ministério da saúde adverte, fumar é prejudicial à saúde e pode causar câncer."


            elif ops_f == 2:
                print("OK")
                print("  ")
                print("Sua escolha foi Grama.")
                TB_f = "Grama"
                sleep(2.5)
                print("..Carregando.....")
                print("  ")
                print("--Pre definido pelo programador, como padrão para cálculo (Dia). ")
                vz = float(input("No período de um dia, você costuma fumar quanta Grama? : "))
                if vz <= 0:
                    print("♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. ")
                    print(" I•D•I•O•T•A _|_ ")
                    fumante ["Resposta do código"] = "♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. I•D•I•O•T•A _|_ "
                elif vz >= 0.1 and vz <= 40.99:
                    print("♤ Porra tio você fuma grama, k7. ")
                    print("♤ Como¿")
                    fumante ["Resposta do código"] = "♤ Porra tio você fuma grama, k7. Como¿"
                    print()   
                    print()    
                    sleep (1.5)
                    print ("Sério me conte mais de como é fumar GRAMA? :")
                    sleep (1)         
                    print ("Digite alguma das opções abaixo:")
                    print ("|1. = Está bem eu conto. ")
                    print ("|2. = Hhhha, sem comentários quanto a isso. ")
                    print ("|3. = Mas é claro que eu conto. ")
                    print ("|4. = Foda-se eu não vou contar. ")
                    print("-Digite apenas o numero da opção desejada")
                    pqg = input("#E ai vai contar ou não? :")
                    if pqg == "1" or pqg == "1." and pqg == "3" or pqg == "3.":
                        print("Aaaaaeeh porra!")
                        print("Bora lá então....")
                        sleep (1.7)
                        print(" Digite o seu texto em uma única linha, após terminar de digitar aperte “Enter” para finalizar e salvar o seu texto. ")
                        print(" ! ATENÇÃO ! = Após o envio de seu texto não tem como edita-lo. ")
                        digite_g = input("Escreve ai: ")
                        sleep (3)
                        print("....Guardando o seu depoimento ..............")
                        fumante ["Depoimento"] = "Sim"
                        fumante ["Como é fumar GRAMA"] = digite_g
                        sleep (2.5)
                        print("Salvo com sucesso.")
                        print("  ")
                        print("  ")
                    elif pqg == "2" or pqg == "2." and pqg == "4" or pqg == "4.":
                        print("Blz")
                        print("Vamos continuar então....")
                        fumante ["Depoimento"] = "Não"
                        print("  ")
                        print("  ")


            elif ops_f == 3:
                print("OK")
                print("  ")
                print("Sua escolha foi Maconha.")
                TB_f = "Maconha"
                sleep(2.5)
                print("..Carregando.....")
                print("  ")
                print("--Pre definido pelo programador, como padrão para cálculo (Dia). ")
                vz = float(input("No período de um dia, você costuma fumar Maconha quantas vezes no dia? : "))
                if vz <= 0:
                    print("♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. ")
                    print(" I•D•I•O•T•A _|_ ")
                    fumante ["Resposta do código"] = "♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. I•D•I•O•T•A _|_ "
                elif vz >= 0.1 and vz <= 1.99:
                    print("♤ Até ai tudo bem. ")
                    print("♤ Mas cuidado, que essa porra vicia! ")
                    fumante ["Resposta do código"] = "♤ Até ai tudo bem. Mas cuidado, que essa porra vicia!"
                elif vz >= 2.0 and vz <= 2.99:
                    print("♤ Até ai tudo bem. ")
                    print("♤ Mas cuidado, que essa porra vicia! ")
                    fumante ["Resposta do código"] = "♤ Até ai tudo bem. Mas cuidado, que essa porra vicia!"
                elif vz >= 3.0 and vz <= 3.99:
                    print("♤ Para com isso que n da certo. ")
                    fumante ["Resposta do código"] = "♤ Para com isso que n da certo."
                elif vz >= 4.0 and vz <= 4.99:
                    print("♤ Para com isso que n da certo. ")
                    print("♤ Fica o aviso. ")
                    fumante ["Resposta do código"] = "♤ Para com isso que n da certo. Fica o aviso."
                elif vz >= 5.0 and vz <= 5.99:
                    print("♤ Kkkkkk, já é caso perdido. ")
                    print("♤ Tem volta mas é complicado. ")
                    fumante ["Resposta do código"] = "♤ Kkkkkk, já é caso perdido. Tem volta mas é complicado."
                elif vz >= 8.0 and vz <= 40.99:
                    print("♤ K7, kkkkkkkk. ")
                    print("😵 Já está no nível que vira zumbi. ")
                    print("😵 Éh bem provável que já está viciado. ")
                    print("😵 Foi mal dizer isso, mas é a vdd. ")
                    fumante ["Resposta do código"] = "😵 Éh bem provável que já está viciado."
                elif vz >= 50.00:
                    print("♤ K7, kkkkkkkk. ")
                    print("👽 Sério, como você está vivo até hoje ¡¿ ")
                    print("😵 Já está no nível que vira zumbi. ")
                    print("😵 Éh bem provável que já está viciado. ")
                    print("😵 Foi mal dizer isso, mas é a vdd. ")
                    fumante ["Resposta do código"] = "👽 Sério, como você está vivo até hoje ¡¿"


            elif ops_f == 4:
                print("OK")
                print("  ")
                print("Sua escolha foi Crack.")
                TB_f = "Crack"
                sleep(2.5)
                print("..Carregando.....")
                print("  ")
                print("--Pre definido pelo programador, como padrão para cálculo (Dia). ")
                vz = float(input("No período de um dia, você costuma fumar quanto de Crack? : "))
                if vz <= 0:
                    print("♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. ")
                    print(" I•D•I•O•T•A _|_ ")
                    fumante ["Resposta do código"] = "♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. I•D•I•O•T•A _|_ "
                elif vz >= 0.1 and vz <= 1.99:
                    print("♤ Mas cuidado, que essa porra vicia! ")
                elif vz >= 2.0 and vz <= 2.99:
                    print("♤ Ok, mas cuidado que isso é química pura. ")
                    print("♤ Aah outra coisa, cuidado, que essa porra vicia. ")
                elif vz >= 3.0 and vz <= 3.99:
                    print("♤ Ok, mas cuidado que isso é química pura. ")
                    print("♤ Aah outra coisa, cuidado, que essa porra vicia. ")
                elif vz >= 4.0 and vz <= 4.99:
                    print("♤ Pesado, mas se controla ai. ")
                    print("♤ Disso para menos. ")
                elif vz >= 5.0 and vz <= 5.99:
                    print("♤ Muito pesado, isso é pura química!! ")
                elif vz >= 6.0 and vz <= 6.99:
                    print("♤ Muito pesado, isso é pura química!! ")
                    print("♤ Para que já deu o que tinha que da, Kkk. ")
                elif vz >= 10.0 and vz <= 20.99:
                    print("♤ Pesado em. ")
                    print("😵 Para que já deu o que tinha que da, Kkk. ")
                    print("😵 Olha ai os efeitos do crack: ----- https://www.infoescola.com/drogas/crack/ ")
                elif vz >= 30.00:
                    print("♤ Pesado em. ")
                    print("👽 Sério, como você está vivo até hoje ¡¿ ")
                    print("😵 Para que já deu o que tinha que da, Kkk. ")
                    print("😵 Olha ai os efeitos do crack: ----- https://www.infoescola.com/drogas/crack/ ")


            elif ops_f == 5:
                print("OK")
                print("  ")
                print("Sua escolha foi Margine.")
                TB_f = "Margine"
                sleep(2.5)
                print("..Carregando.....")
                print("  ")
                print("--Pre definido pelo programador, como padrão para cálculo (Dia). ")
                vz = float(input("No período de um dia, você costuma fumar o Margine quantas vezes? : "))
                if vz <= 0:
                    print("♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. ")
                    print(" I•D•I•O•T•A _|_ ")
                    fumante ["Resposta do código"] = "♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. I•D•I•O•T•A _|_ "
                elif vz >= 0.1 and vz <= 1.99:
                    print("♤ Então mal começou e já pode parar. ")  
                    fumante ["Resposta do código"] = "♤ Então mal começou e já pode parar."                    
                elif vz >= 2.0 and vz <= 2.99:
                    print("♤ Então mal começou e já pode parar. ") 
                    fumante ["Resposta do código"] = "♤ Então mal começou e já pode parar."                 
                elif vz >= 3.0 and vz <= 3.99:
                    print("♤ Então, já pode parar com isso. ")
                    print("♤ Ainda da tempo!! ")
                    fumante ["Resposta do código"] = "♤ Então, já pode parar com isso. Ainda da tempo!!"
                elif vz >= 4.0 and vz <= 4.99:
                    print("♤ Para de fuma k7!!! ")
                    print("♤ ISSO MATA!!!!! ")
                    fumante ["Resposta do código"] = "♤ Para de fuma k7!!! ISSO MATA!!!!!"
                elif vz >= 5.0 and vz <= 5.99:
                    print("♤ Para de fuma k7, essa porra mata!!!!! ")
                    print("♤ Ainda da tempo!! ")
                elif vz >= 6.0 and vz <= 6.99:
                    print("♤ Tio para com essa merda, sério!! ")
                    fumante ["Resposta do código"] = "♤ Tio para com essa merda, sério!!"
                elif vz >= 7.0 and vz <= 7.99:
                    print("♤ Isso vicia, e não tem volta!! ")
                    sleep(1)
                    print("♤ Mentira tem volta sim, Só para de fumar. ")
                    print("♤ Simples não¿ ")
                    fumante ["Resposta do código"] = "♤ Mentira tem volta sim, Só para de fumar."
                elif vz >= 8.0 and vz <= 8.99:
                    print("♤ Tio para, para, para que isso não dá certo. ")
                    print("♤ Teu pulmão não vai aguentar k7. ")
                    fumante ["Resposta do código"] = "♤ Tio para, para, para que isso não dá certo."
                elif vz >= 9.0 and vz <= 9.99:
                    print("♤ Tio teu pulmão não vai aguentar. ")
                    print("♤ Para com isso! ")
                    fumante ["Resposta do código"] = "♤ Tio teu pulmão não vai aguentar."
                elif vz >= 10.0 and vz <= 10.99:
                    print("♤ OK, você fuma, mas deveria para urgente. ")
                    print("♤ Fica o aviso. ")
                    fumante ["Resposta do código"] = "♤ OK, você fuma, mas deveria para urgente."
                elif vz >= 10.99 and vz <= 40.99:
                    print("♤ CUIDADO ♤")
                    print("😵 Seu pulmão não vai aguentar, fica a dica. ")
                    print("😵 Aah outra coisa, qual é pior cigarro ou Margine??? ")
                    sleep(1.5)
                    print("😵 R: O Margine ---- (fonte: https://vejasp.abril.com.br/blog/saude/narguile-ou-cigarro-qual-o-pior-para-a-saude/ ) ")
                    fumante ["Resposta do código"] = "😵 Seu pulmão não vai aguentar, fica a dica."
                elif vz >=50.00:
                    print("♤ CUIDADO ♤")
                    print("👽 Sério, como você está vivo até hoje ¡¿ ")
                    print("😵 Seu pulmão não vai aguentar, fica a dica. ")
                    print("😵 Aah outra coisa, qual é pior cigarro ou Margine??? ")
                    sleep(1.5)
                    print("😵 R: O Margine ---- (fonte: https://vejasp.abril.com.br/blog/saude/narguile-ou-cigarro-qual-o-pior-para-a-saude/ ) ")
                    fumante ["Resposta do código"] = "👽 Sério, como você está vivo até hoje ¡¿"


            elif ops_f == 6:
                print("OK")
                print("  ")
                print("Sua escolha foi Vaper.")
                TB_f = "Vaper"
                sleep(2.5)
                print("..Carregando.....")
                print("  ")
                print("--Pre definido pelo programador, como padrão para cálculo (Dia). ")
                vz = float(input("No período de um dia, você costuma fumar o Vaper quantas vezes? : "))
                if vz <= 0:
                    print("♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. ")
                    print(" I•D•I•O•T•A _|_ ")
                    fumante ["Resposta do código"] = "♤ Então, Por que você colocou Sim na pergunta ,Se você não fuma. I•D•I•O•T•A _|_ "
                elif vz >= 0.1 and vz <= 1.99:
                    print("♤ Então mal começou e já pode parar. ") 
                    fumante ["Resposta do código"] = "♤ Então mal começou e já pode parar."                  
                elif vz >= 2.0 and vz <= 2.99:
                    print("♤ Então mal começou e já pode parar. ")  
                    fumante ["Resposta do código"] = "♤ Então mal começou e já pode parar."                  
                elif vz >= 3.0 and vz <= 3.99:
                    print("♤ Então, já pode parar com isso. ")
                    print("♤ Ainda da tempo!! ")
                    fumante ["Resposta do código"] = "♤ Então, já pode parar com isso. Ainda da tempo!!"
                elif vz >= 4.0 and vz <= 4.99:
                    print("♤ Para de fuma k7!!! ")
                    print("♤ ISSO MATA!!!!! ")
                    fumante ["Resposta do código"] = "♤ Para de fuma k7!!! ISSO MATA!!!!!"
                elif vz >= 5.0 and vz <= 5.99:
                    print("♤ Para de fuma k7, essa porra mata!!!!! ")
                    print("♤ Ainda da tempo!! ")
                    fumante ["Resposta do código"] = "♤ Para de fuma k7, essa porra mata!!!!!"
                elif vz >= 6.0 and vz <= 6.99:
                    print("♤ Tio para com essa merda, sério!!  ")
                    fumante ["Resposta do código"] = "♤ Tio para com essa merda, sério!!"
                elif vz >= 7.0 and vz <= 7.99:
                    print("♤ Isso vicia, e não tem volta!! ")
                    sleep(1)
                    print("♤ Mentira tem volta sim, Só para de fumar. ")
                    print("♤ Simples ou não ¿?")
                    fumante ["Resposta do código"] = "♤ Isso vicia, e não tem volta!! Mentira tem volta sim, Só para de fumar."
                elif vz >= 8.0 and vz <= 8.99:
                    print("♤ Tio para, para, para que isso não dá certo. ")
                    print("♤ Teu pulmão não vai aguentar k7. ")
                    fumante ["Resposta do código"] = "♤ Tio para, para, para que isso não dá certo. Teu pulmão não vai aguentar k7."
                elif vz >= 9.0 and vz <= 9.99:
                    print("♤ Tio teu pulmão não vai aguentar. ")
                    print("♤ Para com isso! ")
                    fumante ["Resposta do código"] = "♤ Tio teu pulmão não vai aguentar. Para com isso!"
                elif vz >= 10.0 and vz <= 10.99:
                    print("♤ OK, você fuma, mas deveria para urgente. ")
                    print("♤ Fica o aviso. ")
                    fumante ["Resposta do código"] = "♤ OK, você fuma, mas deveria para urgente. Fica o aviso."
                elif vz >= 10.99 and vz <= 40.99:
                    print("♤ CUIDADO ♤")
                    print("😵 Seu pulmão não vai aguentar, fica a dica. ")
                    print("😵 Aah outra coisa ")
                    print("😵 Apesar do “Cigarro eletrônico” não ser tão prejudicial a saúde quanto o Cigarro comum, \n ele ainda pode lhe causar alguma doença. --\n-- (fonte: https://www.cancer.org.br/os-riscos-do-cigarro-eletronico/ )  ")
                    fumante ["Resposta do código"] = "😵 Seu pulmão não vai aguentar, fica a dica. "
                elif vz >= 50.00:
                    print("♤ CUIDADO ♤")
                    print("👽 Sério, como você está vivo até hoje ¡¿ ")
                    print("😵 Seu pulmão não vai aguentar, fica a dica. ")
                    print("😵 Aah outra coisa ")
                    print("😵 Apesar do “Cigarro eletrônico” não ser tão prejudicial a saúde quanto o Cigarro comum, \n ele ainda pode lhe causar alguma doença. --\n-- (fonte: https://www.cancer.org.br/os-riscos-do-cigarro-eletronico/ )  ")
                    fumante ["Resposta do código"] = "😵 Seu pulmão não vai aguentar, fica a dica."


            elif ops_f == 7:
                print("OK")
                print(" s = Sim / n = Não ")
                f_oq = print(" Você pode me dizer o que você fuma?  ")
                if f_oq.lower() == "n" or f_oq.lower() == "ñ" or f_oq.lower() == "nao" or f_oq.lower() == "não":
                    print("♤ OK então segue a vida. ")
                elif f_oq.lower() == "s" or f_oq.lower() == "sim":
                    print(" Digite o seu texto em uma única linha, após terminar de digitar aperte “Enter” para finalizar e salvar o seu texto. ")
                    print(" ! ATENÇÃO ! = Após o envio de seu texto não tem como edita-lo. ")
                    digite_f = input("Então Blz, escreve ai: ")
                    sleep (2.5)
                    print("....Guardando o seu depoimento ..............")
                    sleep (2)
                    print("Salvo com sucesso.")
                    print("  ")
                    print("♤ Valeu pelo depoimento, Kkkk. ")

                    fumante ["O que você Fuma?"] = digite_f
                    fumante ["Resposta do código"] = "♤ Valeu pelo depoimento, Kkkk."

        info_colida ["O que você Fuma?"] = TB_f
        fumante ["O que você Fuma?"] = TB_f

        print("  ")
# ------///////----------------------//////////------------Fim.
        print("  ")

        print("🎉 Aeeeehh acabou finalmente PORRA!!!! ")
        print("👑 O programador agradece pela sua paciência e atenção.")
        sleep(1.5)
        print("Blz. Vou gerar as respostas aqui e irei lhe fazer as ultimas perguntas para gerar o \n arquivo completo para você.")

        print("  ")
        print("  ")

        TB = input("Deseja ver as respostas bruta colhida? :")
        if TB.lower() == "s" or TB.lower() == "sim":
            print("Tabela com as respostas “brutas”:")
            print("  ")

            print("TB_1")
            print(info_colida)
            print("  ")

            print("TB_2")
            print(v_cabaco)
            print("  ")

            print("TB_3")
            print(bebedeira)
            print("  ")

            print("TB_4")
            print(fumante)
            print("  ")

        else:
            print("OK, então ultima pergunta.")
            
        print("  ")
        print("  ")

        arquivo_c = input("Você quer ler o ‘texto’ que preparei de conclusão final ? :")
        if arquivo_c.lower() == "s" or arquivo_c.lower() == "sim":
            
            arq = open("Respostas.txt", "a+")
            texto1 = f"RESPOSTAS BRUTAS: \nTB_1: \n 1.{info_colida} \nTB_2: \n 2.{v_cabaco} \nTB_3: \n 3.{bebedeira} \nTB_4: \n 4.{fumante} "
            
            texto2 = f"Conclusao final"      #-------------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            

            arq.write(texto1 + "\n ")
            arq.write("="*40 + "\n\n")
            arq.write(texto2 + "\n\n | The end. \n")
            arq.close()
            
            print(" |Colhendo todos os dados.... ")
            sleep(3.2)
            
            print(" |Compactando... ")
            sleep(2.5)
            
            print("💾 Pronto salvo ")
            print("📄 Vai lá ler o arquivo, Eeeehh cabo.")
            print("  ")
            print("  ")
            
            sleep(3.3)
            arq = open("Respostas.txt", "r")
            end = arq.read()
            print(end)
            arq.close()
            
            print("  ")
            print("  ")
            sleep(1.2)
            print(" | The end. ")
        
        else:
            print("|Já que você não quer ler o arquivo, então cabo. ")
            print("| The end. ")


    else:
        print("  ")
        print("Arrombado, fez eu carregar as variaveis atoa.")

    print("="*80)

    print("  ")
    print(" s = Sim / n = Não ")
    opc = input("Deseja refazer o teste? :")
