🌳 Árvores Binárias – Implementação

Repositório contendo a implementação de diversas operações e exercícios envolvendo Árvores Binárias, cada uma organizada em arquivos separados.
Para cada questão existe também um arquivo de teste, que deve ser executado após a execução da questão correspondente.

📂 Estrutura do Repositório

Cada questão possui dois arquivos principais:

questaoX.c → Implementação da questão

questaoXteste.c → Arquivo responsável por testar a questão

Exemplo de estrutura:

├── questao1.c
├── questao1teste.c
├── questao2.c
├── questao2teste.c
├── questao3.c
├── questao3teste.c
└── ...

🚀 Como clonar o repositório

No terminal, execute:

git clone https://github.com/evellinmoura/Arvores-Binarias-Implementacao.git


Acesse a pasta:

cd Arvores-Binarias-Implementacao

🧪 Como executar os testes corretamente
⚠️ Regras importantes

Para rodar o teste de uma questão:

Compile e execute primeiro o arquivo da questão (questaoX.c)

Depois compile e execute o arquivo de teste (questaoXteste.c)

O arquivo de teste depende do código carregado no programa da questão, portanto a ordem é obrigatória.

📌 Exemplo: Rodando o teste da Questão 1
1. Compilar a questão
gcc questao1.c -o questao1

2. Executar a questão
./questao1

3. Compilar o teste
gcc questao1teste.c -o questao1teste

4. Executar o teste
./questao1teste


📌 Ordem obrigatória:
1️⃣ questao1
2️⃣ questao1teste

📌 Exemplo: Questão 2
gcc questao2.c -o questao2
./questao2

gcc questao2teste.c -o questao2teste
./questao2teste

💡 Dicas adicionais

Use gcc ou g++ conforme o tipo de arquivo.

Verifique se não há dependências entre arquivos antes de compilar.
