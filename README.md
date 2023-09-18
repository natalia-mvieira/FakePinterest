# *FakePinterest*

O projeto FakePinterest recria uma versão da página do Pinterest, a qual permite adicionar imagens e compartilhar imagens de outros usuários.

A página foi criada utilizando-se a linguagem **Python**, com o uso de **Flask**.
Como o site envolve um sistema de criação de conta, foi feita inicialmente a criação de um banco de dados em SQLite, conectada ao código por meio de SQLAlchemy. Além disso, para garantir a segurança do sistema, também foi aplicada a extensão Flask-Bcrypt para criptografia das senhas.

O site apresenta as seguintes rotas:

### Homepage:
Onde é feito o processo de login e também permite direcionamento à rota de Criar Conta;

### CriarConta:
Permite a criação de uma nova conta, com sistema de checagem de senhas e de repetição de e-mail;

### Perfil:
A rota conta com a variável de *id* que permite a visualização do perfil de um usuário específico.

Assim que a conta é criada ou o *login* é realizado, o usuário já é direcionado ao seu próprio perfil. 

Ele pode checar outros perfis pelas imagens do *feed* e também clicando nas imagens que ele compartilhou de outras contas. 

Para retornar a seu próprio perfil, basta ele clicar em "Perfil" na barra de navegação no topo da página;

### Logout:
Na barra de navegação é sempre possível que o usuário clique em "Sair" para realizar o *logout*;

### Feed: 
Ao clicar na logo FakePinterest, a página é direcionada ao "Feed", onde as imagens compartilhadas pelo usuário atual e por demais usuários podem ser visualizadas. 

Aqui, as imagens aparecerão quando forem adicionadas originalmente e sempre que forem compartilhadas por outros perfis.

### Visualizar:

#### Pelo Feed
Ao clicar em qualquer imagem no *feed*, o usuário será direcionado a uma página que lhe dará duas opções: ver o perfil que a compartilhou ou fazer a adição da imagem em seu próprio perfil.

#### Pelo Perfil
Caso o usuário tenha optado por ver o perfil, ele também pode clicar sobre uma imagem que estiver ali dentro, sendo direcionado a uma nova página de visualização. Nesta, ele também terá a opção de adicionar a foto ou de ver o perfil original que a colocou no site.

### Adicionar: 
Permite o usuário adicionar ao próprio perfil qualquer foto já postada. É o compartilhamento.

### Editar: 
Quando o usuário atual está vendo o seu próprio perfil, ele pode clicar sobre uma das fotos para visualizar o perfil do qual ele compartilhou a imagem ou pode deletá-la;

### Deletar: 
Permite que uma imagem seja deletada do perfil.
Se o usuário atual é o "dono" da foto, ou seja, o primeiro a adicioná-la ao site, a imagem é apagada do banco de dados, sendo excluída das outras contas que a tiverem compartilhado. 

Mas, se ele apenas tiver compartilhado a imagem de outro perfil, ela será deletada apenas do seu.

## Banco de dados:

Para administrar o site, foram criadas três tabelas no banco de dados: Usuario, Foto e FotoCompartilhada.

Em Usuario, estão os dados de todos os usuários da plataforma.

Em Foto, estão os dados de todas as imagens adicionadas originalmente.

Em FotoCompartilhada, são armazenadas as informações de quando uma foto foi postada pela primeira vez e também quando uma imagem é compartilhada. Por meio das chaves estrangeiras, ela se conecta à Usuario e à Foto.

Para o visual da página, foi utilizado **CSS** e **HTML**.