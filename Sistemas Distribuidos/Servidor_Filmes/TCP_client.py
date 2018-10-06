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
    respostaJSON = tcpServer.recv(1024).decode('utf-8')
    print(respostaJSON)
    msg = input()
tcpServer.close()