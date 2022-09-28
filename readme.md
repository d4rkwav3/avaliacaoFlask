
# Sistema genérico de agendamento

Este é meu projeto de conclusão do curso de extensão Python para Web com Flask, 
onde demostro as habilidades aprendidas durante o curso.
Esse repositório tem o objetivo de ser usado para fins avaliativos,
porém sinta-se a vontade para fazer um fork e alterá-lo como bem entender.
## Autor

- Bruno Venâncio RA: 821135934
- Universidade São Judas Tadeu, Campus Jabaquara


## Instalação das dependências

Esse projeto requer Python >= 3.8 e o repositório de pacotes PiP.
Após instalar o Python e o PiP, instalar as dependências do projeto
através do powershell/cmd (Windows) ou pela sua shell favorita (bash, zsh, etc)
caso esteja executando Linux.

```bash
  pip install Flask sqlalchemy flask_sqlalchemy flask_migrate
```
    
## Rodando localmente

Clone o projeto

```bash
  git clone https://github.com/d4rkwav3/avaliacaoFlask.git
```

No diretório onde clonou o projeto, execute o comando abaixo
(não execute dentro da pasta do projeto):

```bash
  flask --app /avaliacaoFlask run
```

Caso o comando acima apresente algum erro e não funcione,
tente a versão abaixo:

```bash
  python -m flask --app /avaliacaoFlask run
```

Para acessar a aplicação, acesse o localhost na porta 5000 no seu 
navegador favorito:

```bash
  localhost:5000/
```