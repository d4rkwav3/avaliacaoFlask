
# Sistema genérico de agendamento

Este é meu projeto de conclusão do curso de extensão Python para Web com Flask, 
onde demostro as habilidades aprendidas durante o curso.
Esse repositório tem o objetivo de ser usado para fins avaliativos,
porém sinta-se a vontade para fazer um fork e alterá-lo como bem entender.
## Autor

- Bruno Venâncio - RA: 821135934 - USJT Campus Jabaquara


## Instalação das dependências

Esse projeto requer Python >= 3.8 ou superior e o repositório de pacotes PiP 
(normalmente vem junto com o Python).
Após instalar o Python e o PiP, instalar as dependências do projeto
através do powershell/cmd (Windows) ou pela sua shell favorita (bash, zsh, fish, etc)
caso esteja executando Linux.

```bash
  pip install Flask sqlalchemy flask_sqlalchemy flask_migrate
```

Caso o comando acima apresente algum erro e/ou não funcione,
tente a versão abaixo:

```bash
  python -m pip install Flask sqlalchemy flask_sqlalchemy flask_migrate
```

Caso nenhum dos comandos acima funcione, muito provalvemente o Python/PiP
não está configurado no PATH do seu ambiente (tente reinstalar o Python). 
## Rodando localmente

Clone o projeto:

```bash
  git clone https://github.com/d4rkwav3/avaliacaoFlask.git
```

**No diretório onde clonou o projeto**, execute o comando abaixo
(**não execute dentro da pasta do projeto**):

```bash
  flask --app /avaliacaoFlask run
```

Caso o comando acima apresente algum erro e não funcione,
tente a versão abaixo:

```bash
  python -m flask --app /avaliacaoFlask run
```

Ao executar o programa pela primeira vez, será necessário criar o banco de dados,
digite *"sim"* quando o programa perguntar:

``
"Nenhuma base de dados localizada, deseja criar uma nova? ('S'im/'N'ão)"
``
```bash
$ > Sim
```

[Opcional] O programa irá pergunta se deseja inserir dados de teste nas tabelas
do banco recém-criado, você pode digitar *"sim"* ou *"não"* [Opcional]

``
Deseja inserir dados de teste na base? ('S'im/'N'ão)
``
```bash
$ > Sim
```

Por fim, para acessar a aplicação, acesse o localhost na porta 5000 no seu 
navegador favorito:

```bash
  localhost:5000/
```