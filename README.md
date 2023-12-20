# Desafio criptografia

## Objetivo 
<p>Desenvolver uma API que solucionasse o desafio: https://github.com/backend-br/desafios/blob/master/cryptography/PROBLEM.md</p>

### Banco de Dados

<p>
SGBD usado: MySQL<br>
Nome do Banco: Desafio<br>
Tabela usada:<br>
CREATE TABLE creditCard(id INTEGER NOT NULL, userDocument VARCHAR(255) NOT NULL, creditCardToken VARCHAR(255) NOT NULL, Value INTEGER NOT NULL)<br>
</p>

### Endpoints

Exemplos:
<hr>
<p>
- CREATE
ENDPOINT: http://localhost:5000/create
METHOD: POST
JSON:
{
    "id": <INT>
    "userDocument": "<STRING>"
    "creditCardToken": "<STRING>"
    "Value": <INT>
}

- READ
ENDPOINT: http://localhost:5000/read
METHOD: GET



- UPDATE
ENDPOINT: http://localhost:5000/update/<INT_ANTIGO>
METHOD: POST
JSON:
{
    "id": <INT_NOVO_VALOR>
    "userDocument": "<STRING_NOVO_VALOR>"
    "creditCardToken": "<STRING_NOVO_VALOR>"
    "Value": <INT_NOVO_VALOR>
}

- DELETE
ENDPOINT: http://localhost:5000/delete/<INT>
METHOD: GET
</p>