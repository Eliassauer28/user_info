## Requisitos para Implementação Local do Projeto
* Docker com docker-compose

## Como Construir os Contêineres
* No diretório raiz do projeto, onde está localizado o arquivo `docker_compose.yml`, execute o seguinte comando: `docker-compose up --build -d`

## Como Executar os Testes
Para executar os testes, use os seguintes comandos:

```sh
pytest tests/unit
pytest tests/e2e
```

## Informações Sobre as Solicitações para as Rotas da Aplicação

* Rota: http://localhost:5005/add_user, método: POST
  - Solicitação:
```json
{
    "name": "Elias",
    "email": "elias@gmail.com",
    "role_id": 4
}
```

* Rota: http://localhost:5005/users, método: GET
  - Não requer corpo de requisição.

* Rota: http://localhost:5005/role?role_id=4, método: GET
  - Requer o parâmetro de consulta `role_id`.

## Como Executar Esta Aplicação em Produção

1. Copie os arquivos `Dockerfile` e `docker-compose.yml` para o servidor de hospedagem. Você pode fazer isso usando uma ferramenta de transferência de arquivos, como SCP (Secure Copy), ou através de um repositório de código, como o Git.

2. Acesse o servidor de hospedagem através de SSH ou qualquer outro método de acesso remoto.

3. Certifique-se de que o Docker e o docker-compose estão instalados no servidor de hospedagem.

4. Navegue até o diretório onde os arquivos `Dockerfile` e `docker-compose.yml` estão localizados.

5. Execute o seguinte comando para construir e iniciar os contêineres:

```sh
docker-compose up --build -d
```