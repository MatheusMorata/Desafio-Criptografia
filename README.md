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
    "id": Valor<br>
    "userDocument": "Valor"<br>
    "creditCardToken": "Valor"<br>
    "Value": Valor<br>
}<br>

<br>

- READ<br>
ENDPOINT: http://localhost:5000/read<br>
METHOD: GET<br>

<br>

- UPDATE<br>
ENDPOINT: http://localhost:5000/update/valor<br>
METHOD: POST<br>
JSON:<br>
{<br>
    "id": Valor<br>
    "userDocument": "Valor"<br>
    "creditCardToken": "Valor"<br>
    "Value": Valor<br>
}<br>

<br>

- DELETE<br>
ENDPOINT: http://localhost:5000/delete/valor<br>
METHOD: GET<br>
