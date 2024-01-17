## 💻 Projeto

Projeto desenvolvido com finalidade de encontrar logs especificas para o jogo O servidor meu servidor DOOM PROJECT do jogo Project Zomboid.
A ideia do projeto é reproduzir minimamente as funcionalidades de leitura e escrita de arquivos com finalidade de ver logs de jogadores presentes no servidor. Tendo como propósito, o aprendizado de novas tecnologias para desenvolvimento de software ao mesmo tempo que a demanda da administração do servidor para geração de relatórios do jogo.

## 📷 Entendendo a estrutura de pastas

<kbd>
  <img src="https://cdn.discordapp.com/attachments/1021611773587099750/1197249480358113410/image.png?ex=65ba9477&is=65a81f77&hm=77ca69fe8f72b7c770c42f87f504a857f5e5df27010e1a7a4ef8262e52a8ffca&" width="300"/>
</kbd>

O Project Zomboid conta com uma estrutura de pastas, onde o diretório 'logs' consta todas as interações feitas por jogadores do servidor.

---

<kbd>
  <img src="https://cdn.discordapp.com/attachments/1021611773587099750/1197249912694374510/image.png?ex=65ba94df&is=65a81fdf&hm=0e8c38d00b7b7b97067f3e3f0852d3c38456c5d79283e78694b2d9df7ba918bf&" width="300"/>
</kbd>

---

Dentro desta pasta constam diversos arquivos .txt contento diversas informações dos players e registros gerais do servidor.

<kbd>
  <img src="https://cdn.discordapp.com/attachments/1021611773587099750/1197250054898057226/image.png?ex=65ba9500&is=65a82000&hm=09e4443f44261c2ad5c6a8941c8c515b6ec956a6e6b6f9fbfc410c24b1c0e9fc&" width="300"/>
</kbd>

Dentro do arquivo 'item.txt', constam registros de movimentações de itens realizadas por jogadores dentro do jogo. E com este script em python é possível filtrar registros específicos digitando o nome de usuários e data da movimentação do item feita pelo jogador.
