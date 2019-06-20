# gcc151_av4-projeto
Repositório destinado à prova 4 (projeto) da disciplina Processamento de Línguas Naturais(GCC151)

# Sobre o projeto
Este projeto consiste em um sumarizador de textos de propósito geral, ou seja, dado um texto qualquer de entrada, a rotina <em>sumarize</em> produzirá um novo texto curto(uma sentença) que sintetiza as idéias do texto inicial.

## Etapas

Tarefas na construção do nosso sumarizador abstrativo:
 - Carregar dados de um dataset de treinamento
 - Obter uma lista de todos os tokens lidos anteriormente e processá-la adequadamente para:
 - Converter os tokens para representações vetoriais(usando o word2vec, glove, etc.)
 - Usar uma arquitetura neural codificador-decodificador para gerar uma sequência de palavras a partir de outra sequência de palavras(Provavelmente usaremos LSTM RNNs)
 - Adicionar um mecanismo de atenção para identificar os tokens mais relevantes na geração dos resumos
