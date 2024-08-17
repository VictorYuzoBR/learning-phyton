from idlelib.pyshell import warning_stream
from operator import length_hint
from os.path import split

import requests
import json

req = None
sair = False
lista = []

def Pesquisa(t):
    lista =[]
    for i in range(1,101):
        print("pesquisando na pagina: " + str(i))
        try:
            req = requests.get("http://www.omdbapi.com/?apikey=ea95748a&s=" + t + "&type=movie&page="+str(i))
            filme = json.loads(req.text)
            auxx = filme["Response"]
            if auxx == "False":
                break
            else:
                for i in filme["Search"]:
                    string = i["Title"]
                    lista.append(string)

        except:
            print("Erro na conexão")
            exit()
    return lista


def mostrar(f):
    print("Lista de filmes")
    for x in f:
        print(x)


while not sair == True:
    op = input("digite o nome do filme ou sair para sair ")
    if op == "sair":
        print("saindo")
        exit()
    else:
        filme = Pesquisa(op)
        if length_hint(filme) == 0:
            print("filme não encontrado")
        else:
            mostrar(filme)





