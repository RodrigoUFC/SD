import socket
import json

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
destino = (HOST, PORT)
tcpServer.connect(destino)
print('Bem vindo! Para obter a lista de filmes, digite "Filme" no console. Para sair digite "s"')
msg = input()
while msg != 's':
    tcpServer.send(msg.encode('utf-8'))
    resposta = tcpServer.recv(4096).decode('utf-8')
    respostaJSON = json.loads(resposta)
    for i in range(len(respostaJSON)):
        print("Filme "+str(i)+"\nID: "+respostaJSON[i]['FilmeID']+"\nTítulo: "+respostaJSON[i]['Titulo']+"\nAno: "+respostaJSON[i]['Ano']+"\nAvaliação IMDB: "+respostaJSON[i]['Avaliacao_IMDB']+"\nTrês filmes mais relacionados: "+respostaJSON[i]['Tres_filmes_mais_relacionados'][0]+", "+respostaJSON[i]['Tres_filmes_mais_relacionados'][1]+", "+respostaJSON[i]['Tres_filmes_mais_relacionados'][2]+"\nLink para trailer no Youtube: "+respostaJSON[i]['Link_para_trailer_Youtube'])
    msg = input()
tcpServer.close()