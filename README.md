# Tarefa 4 — Atacando o RSA

Neste trabalho de Criptografia Aplicada, o programa recebe um número e descobre quais dois números primos foram multiplicados para formá-lo. Esses números são parte da construção das chaves do RSA. Usamos números pequenos para conseguir acompanhar as contas à mão.

Por exemplo, você digita **35**. O programa descobre que **5 × 7 = 35**. Essa é a parte obrigatória. No bônus, você informa mais um número da chave pública e o programa usa os fatores que encontrou para calcular a chave privada do exemplo.

## Como executar e o que digitar

Com o Python 3 instalado, abra o terminal na pasta que contém o arquivo `main.py`. O terminal é a janela em que você digita comandos. No Mac, execute:

```bash
python3 main.py
```

1. Quando aparecer **“Digite o módulo RSA n”**, digite `35` e pressione Enter. O programa mostra os fatores 5 e 7.
2. Quando ele pedir o **expoente público**, digite `29` e pressione Enter. A letra `e` é o nome que o código dá a esse número. Se quiser fazer somente a parte obrigatória, deixe o campo vazio e pressione Enter.
3. Com `29`, as últimas linhas serão:

```text
Expoente privado: d = 5
Chave privada (n, d) = (35, 5)
Conferência: (29 × 5) % 24 = 1
```

## Como acompanhar o código

Abra `main.py` e procure as linhas destacadas abaixo. Em Python, uma **variável** é um nome que guarda um valor. Assim, `candidato = 2` guarda o número 2 no nome `candidato`. Uma **função** é um trecho de código que recebe um nome para ser chamado quando precisamos dele. Neste arquivo, `main()` conduz a conversa no terminal e `primeiro_divisor(numero)` faz a busca por um divisor.

### 1. O programa recebe o número 35

Na função `main()`, `input(...)` mostra uma pergunta e lê o que a pessoa digitou. A resposta chega como texto. A função `int(...)` transforma o texto `"35"` no número inteiro 35, que fica guardado em `n`. Se alguém digitar uma palavra, o bloco `except ValueError` mostra uma mensagem explicando que a entrada precisa ser um inteiro. O programa também verifica se o valor está entre 2 e 65.536, o limite da atividade.

### 2. Como ele descobre o 5?

A linha `p = primeiro_divisor(n)` pede à função que procure o primeiro divisor de 35 a partir de 2. Um divisor é um número pelo qual conseguimos dividir 35 sem deixar resto. Em Python, o sinal `%` calcula **o resto da divisão**. Por isso, `numero % candidato == 0` faz a pergunta “o resto deu zero?”.

| Candidato | Divisão feita à mão | O que o programa faz |
| --- | --- | --- |
| 2 | 35 = 2 × 17 + 1 | Sobrou 1. Tenta 3. |
| 3 | 35 = 3 × 11 + 2 | Sobrou 2. Tenta 4. |
| 4 | 35 = 4 × 8 + 3 | Sobrou 3. Tenta 5. |
| 5 | 35 = 5 × 7 + 0 | O resto é zero. Devolve 5. |

No código, `while` repete a tentativa, `candidato += 1` avança para o próximo inteiro e `return candidato` devolve o divisor encontrado. A repetição só precisa continuar enquanto `candidato * candidato <= numero`. No caso de 35, por exemplo, dois fatores que fossem ambos pelo menos 6 já dariam um produto de pelo menos 36. Por isso basta procurar o menor dos fatores.

### 3. De onde vem o 7?

Agora que `p` vale 5, a linha `q = n // p` calcula **quantas vezes 5 cabe em 35**. A resposta é 7. Compare as duas operações:

| Expressão | Pergunta | Resultado |
| --- | --- | --- |
| `35 % 5` | Quanto sobrou? | 0 |
| `35 // 5` | Quantas vezes coube? | 7 |

O exercício pede **dois primos distintos**. Um primo é um número inteiro maior que 1 cujos únicos divisores positivos são 1 e ele mesmo. O primeiro divisor que a busca encontra já é primo, pois qualquer divisor menor dele teria aparecido antes. O programa confere se o segundo fator também é primo e se os dois são diferentes. Por exemplo, `45 = 3 × 15` falha porque 15 também é divisível por 3. Já `49 = 7 × 7` falha porque os fatores são iguais. Para 35, as duas verificações passam.

### 4. Por que aparece 24 no bônus?

A chave pública deste exemplo tem dois números, escritos na ordem `(n, e)`. Já conhecemos `n = 35`. Antes de perguntar qual é o valor de `e`, o programa calcula uma quantidade chamada **φ(n)**, que se lê “fi de n”. No código, o nome dessa variável é `phi`. Para dois primos diferentes, a conta é:

```text
phi = (p − 1) × (q − 1)
phi = (5 − 1) × (7 − 1) = 4 × 6 = 24
```

O programa usa **35** para definir o intervalo permitido para `e`, de 2 a 34. Usa **24** para verificar quais valores desse intervalo permitem calcular o expoente privado. A função `gcd(e, phi)`, importada de `math`, calcula o **máximo divisor comum (MDC)**, ou seja, o maior número que divide os dois sem deixar resto.

Se você digitar **3**, o MDC de 3 e 24 é 3. O programa explica o motivo e `continue` faz a pergunta aparecer de novo. Se digitar **29**, o único divisor positivo em comum com 24 é 1. A escolha é aceita e `break` encerra a repetição das perguntas.

### 5. Como ele encontra a chave privada?

O programa procura um número chamado `d`, o **expoente privado**. Para ele servir, a multiplicação `e × d` precisa deixar resto **1** quando dividida por `phi`. A linha `for d in range(1, phi)` testa os valores de 1 a 23, em ordem, até encontrar o primeiro que funciona.

| Valor testado para d | Produto com e = 29 | Resto por 24 |
| --- | --- | --- |
| 1 | 29 | 5 |
| 2 | 58 | 10 |
| 3 | 87 | 15 |
| 4 | 116 | 20 |
| **5** | **145** | **1** |

Como **145 = 6 × 24 + 1**, o programa aceita `d = 5`. No formato usado no trabalho, a chave pública informada foi **(35, 29)** e a chave privada calculada é **(35, 5)**. O primeiro número é o módulo nas duas chaves. O segundo é o expoente de cada uma.
