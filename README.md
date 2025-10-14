# 🎵 MusicSorter – Sistema de Ordenação de Músicas

## Aluno

| Matrícula | Nome                     |
| --------- | ------------------------ |
| 202017521 | Algusto Rodrigues Caldas |

* * *

## Descrição do Projeto

O **MusicSorter** é um projeto desenvolvido para demonstrar o funcionamento de **algoritmos de ordenação clássicos** (Bubble Sort, Insertion Sort e Quick Sort) aplicados em uma base de músicas.

Cada música possui os seguintes atributos:

* **Título**
* **Artista**
*  **Duração**

O usuário pode escolher qual algoritmo deseja utilizar e qual atributo será usado como critério de ordenação, além de visualizar o **tempo de execução** de cada método.

* * *

## Funcionalidades

* Inserir novas músicas na base.
* Listar todas as músicas.
* Ordenar por **título**, **artista** ou **duração**.
* Escolher o algoritmo:
  *  Bubble Sort
  *  Insertion Sort
  *  Quick Sort
* Comparar o **tempo de execução** entre os algoritmos.

* * *

## Conceitos de Estrutura de Dados aplicados

* Estruturas de dados: listas e objetos.
* Implementação manual de algoritmos clássicos de ordenação.
* Análise de tempo de execução (`time.perf_counter()`).
* Comparação prática de desempenho.

* * *

## Guia de Instalação

### Requisitos

* Python 3.10 ou superior

###  Como Executar o Projeto

1. Clone o repositório:
  
      git clone https://github.com/EDAII/Ordenacao_MusicSorter.git
  
2. Acesse o diretório:
  
      cd Ordenacao_MusicSorter
  
3. Execute o programa:
  
      python main.py
  

* * *

## Exemplo de Execução

    === MusicSorter ===
    1. Inserir música
    2. Listar músicas
    3. Ordenar músicas
    4. Sair
    Escolha uma opção: 3
    
    Ordenar por:
    1. Título
    2. Artista
    3. Duração
    Critério: 1
    
    Escolha o algoritmo:
    1. Bubble Sort
    2. Insertion Sort
    3. Quick Sort
    Algoritmo: 3
    
    Ordenação concluída em 0.00031 segundos.

* * *

## Objetivos de Aprendizado

* Compreender o funcionamento de diferentes algoritmos de ordenação.
* Aplicar conceitos de análise de complexidade.
* Comparar empiricamente o desempenho entre métodos distintos.
* Desenvolver raciocínio lógico e modularização em Python.

* * *

## Disciplina

**Estrutura de Dados — Engenharia de Software – Universidade de Brasília (FGA)**

* * *

##  Apresentação do Projeto

> *(Link do vídeo quando disponível)*

* * *

## Estrutura de Arquivos

    Ordenacao_MusicSorter/
    │
    ├── main.py                  # Código principal com menu e ordenações
    ├── musicas_base.py          # Base de músicas iniciais
    ├── README.md                # Documentação do projeto
    └── assets/                  # Imagens ou vídeos complementares (opcional)

* * *