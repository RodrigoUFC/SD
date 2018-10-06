import socket
import json

filmes = []
filmes.append({
    "FilmeID": "tt2674426",
    "Titulo": "Como eu era antes de voce",
    "Ano": 2016,
    "Avaliacao_IMDB": 7.4,
    "Tres_filmes_mais_relacionados": ["A culpa e das estrelas","Diario de uma paixao","Simplesmente acontece"],
    "Link_para_trailer_Youtube": "https://www.youtube.com/watch?v=PnqUs3xiAVI"
})
filmes.append({
  "FilmeID": "0001",
  "Titulo": "MyLife",
  "Ano": 2016,
  "Avaliacao_IMDB": 3,
  "Tres_filmes_mais_relacionados": ["MyLife1", "MyLife2", "MyLife3" ],
  "Link_para_trailer_Youtube": "www.youtube/0001.com"
})
filmes.append({
  "FilmeID": "0002",
  "Titulo": "MyLife2",
  "Ano": 2016,
  "Avaliacao_IMDB": 4,
  "Tres_filmes_mais_relacionados": ["MyLife1", "MyLife2", "MyLife3" ],
  "Link_para_trailer_Youtube": "www.youtube/0002.com"
})
filmes.append({
  "FilmeID": "0003",
  "Titulo": "MyLife2",
  "Ano": 2003,
  "Avaliacao_IMDB": 5,
  "Tres_filmes_mais_relacionados": ["MyLife1", "MyLife2", "MyLife3" ],
  "Link_para_trailer_Youtube": "www.youtube/0003.com"
})
filmes.append({
  "FilmeID": "0004",
  "Titulo": "MyLife2",
  "Ano": 2004,
  "Avaliacao_IMDB": 6,
  "Tres_filmes_mais_relacionados": ["MyLife1", "MyLife2", "MyLife3" ],
  "Link_para_trailer_Youtube": "www.youtube/0004.com"
})
filmesJSON = json.dumps(filmes)
HOST = ''
PORT = 5000
tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)
tcpServer.bind(origem)
tcpServer.listen(1)
while True:
    conexao, cliente = tcpServer.accept()
    print('Conectado com', cliente)
    while True:
        msg = conexao.recv(1024).decode('utf-8')
        if msg == 'Filme':
            conexao.send(filmesJSON.encode('utf-8'))
            print(cliente, msg)
        if msg == 's':
            retorno = 'Desconectando do servidor.'
            conexao.send(retorno.encode('utf-8'))
            break
        else:
            retorno = 'Opção inválida!'
            conexao.send(retorno.encode('utf-8'))
    conexao.close()

