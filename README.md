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


- CREATE<br>
ENDPOINT: http://localhost:5000/create<br>
METHOD: POST<br>
JSON:<br>
{<br>
    "id": <INT><br>
    "userDocument": "<STRING>"<br>
    "creditCardToken": "<STRING>"<br>
    "Value": <INT><br>
}<br>

<br>

- READ<br>
ENDPOINT: http://localhost:5000/read<br>
METHOD: GET<br>

<br>

- UPDATE<br>
ENDPOINT: http://localhost:5000/update/<INT_ANTIGO><br>
METHOD: POST<br>
JSON:<br>
{<br>
    "id": <INT_NOVO_VALOR><br>
    "userDocument": "<STRING_NOVO_VALOR>"<br>
    "creditCardToken": "<STRING_NOVO_VALOR>"<br>
    "Value": <INT_NOVO_VALOR><br>
}<br>

<br>

- DELETE<br>
ENDPOINT: http://localhost:5000/delete/<INT><br>
METHOD: GET<br>
