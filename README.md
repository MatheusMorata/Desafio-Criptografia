# Desafio criptografia

## Objetivo 
<p>Desenvolver uma API que solucionasse o desafio: https://github.com/backend-br/desafios/blob/master/cryptography/PROBLEM.md</p>

## Requisitos

- Python
- Flask
- VirtualEnv
- MySQL
 
Nome do Banco: Desafio<br>
Tabela usada: 

CREATE TABLE creditCard(
    id INTEGER NOT NULL, 
    userDocument VARCHAR(255) NOT NULL, 
    creditCardToken VARCHAR(255) NOT NULL, 
    Value INTEGER NOT NULL)



## ENDPOINTS


### POST /create


<pre>

    {
        "id": 90,
        "userDocument": "111.111.111-22"
        "creditCardToken": "4111111111111111",
        "Value": 100000
    }

</pre>


### GET /read


<pre>

    Sem payload

</pre>


### POST /update/<int:id>


<pre>

    {
        "id": 90,
        "userDocument": "111.111.111-22"
        "creditCardToken": "4111111111111111",
        "Value": 100000
    }

</pre>


### GET /delete/<int:id>


<pre>

    Sem payload

</pre>