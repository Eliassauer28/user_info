## Requisitos para subir o projeto Localmente
* Docker com docker-compose

## Como Construir os Contêineres
* No diretório raiz do projeto, onde está localizado o arquivo `docker_compose.yml`, execute o seguinte comando: `docker-compose up --build -d`

## Informações Detalhadas sobre as Requisições para as Rotas do Aplicativo

* **Rota:** `http://localhost:5005/add_user`, **Método:** POST
    * Essa rota é usada para adicionar um novo usuário. 
    * A requisição para esta rota deve ser uma solicitação POST contendo um corpo em JSON. 

    **Exemplo de Corpo de Requisição:**
    ```json
    {
        "name": "Elias",
        "email": "elias@gmail.com",
        "role_id": 1, 2 ou 3 
    }
    ```
    Aqui, `"name"` é o nome do usuário, `"email"` é o endereço de email do usuário e `"role_id"` representa o papel do usuário que pode ser 1, 2 ou 3.

* **Rota:** `http://localhost:5005/users`, **Método:** GET
    * Essa rota é utilizada para recuperar uma lista de todos os usuários.
    * Essa solicitação é do tipo GET e não requer um corpo de requisição.

* **Rota:** `http://localhost:5005/role?role_id=3`, **Método:** GET
    * Essa rota é usada para recuperar informações sobre um papel específico com base no seu ID.
    * Essa requisição é do tipo GET e requer o parâmetro de consulta `role_id`. 
    * Por exemplo, para buscar informações sobre o papel com ID 3, o URL da requisição seria `http://localhost:5005/role?role_id=3`.

# Guia de Execução de Testes

Siga os passos abaixo para executar os testes na sua aplicação:

1. **Acesso ao Container da Aplicação**

    Primeiro, é necessário acessar o container onde a aplicação está sendo executada. Utilize o seguinte comando:

    ```sh
    docker exec -it code-api-1 /bin/bash
    ```

    Uma vez dentro do container, você pode executar os testes com um dos seguintes comandos, de acordo com o tipo de teste desejado:

    - Para testes unitários:

    ```sh
    pytest tests/unit
    ```

    - Para testes end-to-end (e2e):

    ```sh
    pytest tests/e2e
    ```

## Como Executar Esta Aplicação em Produção

1. Copie os arquivos `Dockerfile` e `docker-compose.yml` para o servidor de hospedagem. Você pode fazer isso usando uma ferramenta de transferência de arquivos, como SCP (Secure Copy), ou através de um repositório de código, como o Git.

2. Acesse o servidor de hospedagem através de SSH ou qualquer outro método de acesso remoto.

3. Certifique-se de que o Docker e o docker-compose estão instalados no servidor de hospedagem.

4. Navegue até o diretório onde os arquivos `Dockerfile` e `docker-compose.yml` estão localizados.

5. Execute o seguinte comando para construir e iniciar os contêineres:

```sh
docker-compose up --build -d
```