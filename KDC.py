def crip(texto,chave):
    aq = []
    for cont in range (len(texto)):
        if texto[cont] == (chr(32)) or (chr(97)<=texto[cont]<=chr(122)):
            if texto[cont] == " ":
                aq.append(" ")
            else:
                crip = ord(texto[cont])
                if chr(crip+chave) <= chr(122):
                    crip = chr(crip + chave)
                    aq.append(crip)
                elif chr(crip+chave) > chr(122):
                    numero = (crip + chave)
                    numero = numero - 122
                    crip = chr(96 + numero)
                    aq.append(crip)
    aq = "".join(aq)
    return(aq)

def quebraCrip(texto):
    for a in range(0,26):
        b = crip(texto,a)
        print(f"{a+1}- {b}")

def desCrip(texto,chave):
    aq = []
    for cont in range (len(texto)):
        if texto[cont] == (chr(32)) or (chr(97)<=texto[cont]<=chr(122)):
            if texto[cont] == " ":
                aq.append(" ")
            else:
                crip = ord(texto[cont])
                if chr(crip-chave) >= chr(97):
                    crip = chr(crip - chave)
                    aq.append(crip)
                elif chr(crip-chave) < chr(97):
                    numero = (crip - chave)
                    numero = 97 - numero
                    crip = chr(123 - numero)
                    aq.append(crip)
    aq = "".join(aq)
    return(aq)

def funcaoNonce(v):
    novoValor = v - 7
    return (novoValor)

from random import randint
key1= randint(1,50)
key2= randint(1,50)
nome1=(input("Bem vindo ao sistema KDC, digite seu nome: "))
print(f"Olá {nome1}, sua chave é: ({key1})")
print("\n")

nome2=(input("Bem vindo ao sistema KDC, digite seu nome: "))
print(f"Olá {nome2}, sua chave é: ({key2})")
print("\n")


print(f"{nome1}, voce esta recebendo agora duas msgs criptografadas chamadas X e Y, onde X precisara de sua chave para Descriptografar, e Y a chave da {nome2}.")
x=0
print("\n")
while x != key1:
    x = int(input(f"{nome1} digite sua chave para a Descriptografia de X: "))
keysessao= randint(1,26)
print(f"Verificacao realizada com sucesso, {nome1} sua chave de Sessao com o KDC é {keysessao}")
print("\n")
print(f"{nome1} esta enviando a msg criptografada Y para {nome2}...")
print("\n")

print(f"{nome2}, voce esta recebendo agora uma msg criptografada chamada Y, que precisara de sua chave para Descriptografar.")
y=0
print("\n")
while y != key2:
    y = int(input(f"{nome2} digite sua chave para a Descriptografia: "))
print(f"Verificacao realizada com sucesso, {nome2} sua chave de Sessao com o KDC é {keysessao}")
print("\n")

nonce = randint(1,100)
print(f"{nome2} Voce está recebendo o valor Nonce, que é ({nonce}), agora repasse para o {nome1}, porém criptografado em uma msg Z, onde {nome1} usará a chave de sessão para Descriptografar.")
print("\n")

print(f"{nome2} está enviando a msg Z para {nome1}...")
print("\n")
z = 0
while z != keysessao:
    z = int(input(f"Olá {nome1}, {nome2} te enviou uma msg criptografada Z, digite a chave de sessão para Descriptografar: "))
print("\n")
print(f"{nome1}, a chave de sessão está correta, o valor Nonce é ({nonce})")
print("\n")
print(f"{nome1} ira digitar o valor Nonce em uma funcao, na qual {nome2} também tem acesso a função, e ira mandar o novo valor obtido, criptografado para {nome2}...")
print("\n")
print(f"{nome1}, está digitando o valor na função...")
print("\n")

v = funcaoNonce(nonce)
print(f"{nome1}, o novo valor de Nonce, chamado N* é ({v})")
print("\n")
print(f"{nome1} esta enviando N* criptografado em uma msg P para {nome2} Descriptografar ultilizando a chave de sessao, assim também obtendo o valor N*...")
print("\n")

p = 0
while p != keysessao:
    p = int(input(f"Olá {nome2}, {nome1} te enviou uma msg criptografada P, digite a chave de sessão para Descriptografar: "))

print(f"{nome2}, o valor de N* obtido por {nome1} é ({v}), agora, digite o valor Nonce original em sua função e compare se é o mesmo N* que {nome1} te enviou")
print("\n")
print(f"{nome2} está digitando o valor na função...")
print("\n")

v = funcaoNonce(nonce)
print(f"{nome2}, o novo valor de Nonce obtido pela função é ({v}), que é o mesmo que {nome1} te enviou.")
print("\n")
print(f"Sendo assim, a Segurança de vocês está confirmada com sucesso, agora vocês dois poderão ter uma conversa totalmente segura !!.")