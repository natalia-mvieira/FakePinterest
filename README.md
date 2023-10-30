# *FakePinterest*

O projeto FakePinterest recria uma versão da página do Pinterest, a qual permite adicionar imagens e compartilhar imagens de outros usuários.

A página foi criada utilizando-se a linguagem **Python**, com o uso de **Flask**.
Como o site envolve um sistema de criação de conta, foi feita inicialmente a criação de um banco de dados em SQLite, conectada ao código por meio de SQLAlchemy. Além disso, para garantir a segurança do sistema, também foi aplicada a extensão Flask-Bcrypt para criptografia das senhas.

O site apresenta as seguintes rotas:

### Homepage:
Onde é feito o processo de login e também permite direcionamento à rota de Criar Conta;

<div align="center">
    <img src="https://github.com/natalia-mvieira/FakePinterest/assets/144560412/5d5e81df-9907-481e-83d1-85124b6299f8" width="700px"/>
</div>

### CriarConta:
Permite a criação de uma nova conta, com sistema de checagem de senhas e de repetição de e-mail;

<div align="center">
    <img src="https://github.com/natalia-mvieira/FakePinterest/assets/144560412/bf3c7099-fe29-409b-a299-c005c83b8c30" width="700px"/>
</div>

### Perfil:
A rota conta com a variável de *id* que permite a visualização do perfil de um usuário específico.

<div align="center">
    <img src="https://github.com/natalia-mvieira/FakePinterest/assets/144560412/e3d939bf-3fe6-401e-ba23-776902c01877" width="700px"/>
</div>

Assim que a conta é criada ou o *login* é realizado, o usuário já é direcionado ao seu próprio perfil. 

Ele pode checar outros perfis pelas imagens do *feed* e também clicando nas imagens que ele compartilhou de outras contas. 

Para retornar a seu próprio perfil, basta ele clicar em "Perfil" na barra de navegação no topo da página;

### Logout:
Na barra de navegação é sempre possível que o usuário clique em "Sair" para realizar o *logout*;

### Feed: 
Ao clicar na logo FakePinterest, a página é direcionada ao "Feed", onde as imagens compartilhadas pelo usuário atual e por demais usuários podem ser visualizadas. 

Aqui, as imagens aparecerão quando forem adicionadas originalmente e sempre que forem compartilhadas por outros perfis.

<div align="center">
    <img src="https://github.com/natalia-mvieira/FakePinterest/assets/144560412/498a1d69-ed2b-4baa-84d6-675436a3e9d1" width="700px"/>
</div>

### Visualizar:

<div align="center">
    <img src="https://github.com/natalia-mvieira/FakePinterest/assets/144560412/f14c712d-d6f5-416d-a4bd-3ed491e087c5" width="700px"/>
</div>

#### Pelo Feed
Ao clicar em qualquer imagem no *feed*, o usuário será direcionado a uma página que lhe dará duas opções: ver o perfil que a compartilhou ou fazer a adição da imagem em seu próprio perfil.

#### Pelo Perfil
Caso o usuário tenha optado por ver o perfil, ele também pode clicar sobre uma imagem que estiver ali dentro, sendo direcionado a uma nova página de visualização. Nesta, ele também terá a opção de adicionar a foto ou de ver o perfil original que a colocou no site.

<div align="center">
    <img src="https://github.com/natalia-mvieira/FakePinterest/assets/144560412/a9646f40-181f-404d-992a-05e59da66530" width="700px"/>
</div>

### Adicionar: 
Permite o usuário adicionar ao próprio perfil qualquer foto já postada. É o compartilhamento.

<div align="center">
    <img src="https://github.com/natalia-mvieira/FakePinterest/assets/144560412/619a7639-110f-4b5f-96a8-0cbb8c91a115" width="700px"/>
</div>

### Editar: 
Quando o usuário atual está vendo o seu próprio perfil, ele pode clicar sobre uma das fotos para visualizar o perfil do qual ele compartilhou a imagem ou pode deletá-la;

<div align="center">
    <img src="https://github.com/natalia-mvieira/FakePinterest/assets/144560412/d92af0ae-f484-4570-a222-897f8412a351" width="700px"/>
</div>

### Deletar: 
Permite que uma imagem seja deletada do perfil.
Se o usuário atual é o "dono" da foto, ou seja, o primeiro a adicioná-la ao site, a imagem é apagada do banco de dados, sendo excluída das outras contas que a tiverem compartilhado. 

Mas, se ele apenas tiver compartilhado a imagem de outro perfil, ela será deletada apenas do seu.

## Banco de dados:

Para administrar o site, foram criadas três tabelas no banco de dados: Usuario, Foto e FotoCompartilhada.

Em Usuario, estão os dados de todos os usuários da plataforma.

Em Foto, estão os dados de todas as imagens adicionadas originalmente.

Em FotoCompartilhada, são armazenadas as informações de quando uma foto foi postada pela primeira vez e também quando uma imagem é compartilhada. Por meio das chaves estrangeiras, ela se conecta à Usuario e à Foto.


<s>Observação</s>: este projeto foi feito acompanhando o curso Python Impressionador da Hashtag Treinamentos. O curso forneceu a parte visual do site (front-end). O projeto inicial, guiado pelo curso, sugere a criação de conta, login, adição de uma imagem a partir do computador, visualização do feed e de páginas de outros usuários a partir do id. A possibilidade de visualizar a imagem em outra página, compartilhamento, edição, ver o perfil que a compartilhou e ver o perfil original foram implementações pessoais no projeto, sendo necessário, dentre outras mudanças, a alteração da estrutura do banco de dados.
Para o visual da página, foi utilizado **CSS** e **HTML**.
