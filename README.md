<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Calculadora de Juros Compostos</title>
</head>
<body>

<h1>Calculadora de Juros Compostos</h1>

<p>Este repositório contém um projeto de uma calculadora de juros compostos. A calculadora permite que o usuário simule o crescimento de um capital inicial, com ou sem contribuições periódicas, levando em consideração diferentes taxas de juros e unidades de tempo.</p>

<h2>Funcionalidades</h2>

<ul>
  <li><strong>Definir Unidade de Tempo:</strong> O usuário pode escolher a unidade de tempo para os cálculos entre "ano", "mês" ou "dia".</li>
  <li><strong>Calcular Montante Final:</strong> Calcula o montante final do investimento sem considerar contribuições periódicas.</li>
  <li><strong>Simular Contribuições Periódicas:</strong> Simula o efeito das contribuições periódicas no montante final do investimento, além do crescimento do capital inicial.</li>
  <li><strong>Mostrar Gráfico:</strong> Exibe o gráfico da evolução do montante ao longo do tempo, com ou sem contribuições periódicas.</li>
</ul>

<h2>Como Usar</h2>

<ol>
  <li>Clone o repositório em sua máquina local.</li>
  <li>Instale as dependências necessárias (se houver), como o <code>matplotlib</code> para geração do gráfico:</li>
  <pre><code>pip install matplotlib</code></pre>
  <li>Execute o arquivo principal <code>main.py</code> no seu terminal ou IDE preferida.</li>
  <li>O programa solicitará a entrada de dados como capital, taxa de juros, tempo de investimento e contribuições periódicas.</li>
  <li>Após inserir os dados, o programa calculará e exibirá o montante final, além de gerar o gráfico de evolução do investimento ao longo do tempo.</li>
</ol>

<h2>Estrutura do Projeto</h2>

<ul>
  <li><strong>calculator.py:</strong> Contém as funções principais da calculadora, como cálculo de juros compostos e simulação com contribuições periódicas.</li>
  <li><strong>graphics.py:</strong> Contém a função para gerar o gráfico de evolução do investimento.</li>
  <li><strong>main.py:</strong> Arquivo principal para rodar a calculadora, onde o usuário interage com o programa.</li>
</ul>

<h2>Exemplo de Uso</h2>

<p>Ao executar o programa, será exibido um menu de opções. O usuário pode escolher entre as seguintes opções:</p>
<ul>
  <li>Definir unidade de tempo (ano, mês ou dia)</li>
  <li>Calcular montante final</li>
  <li>Simular montante com contribuições periódicas</li>
  <li>Mostrar gráfico de evolução do investimento</li>
  <li>Encerrar o programa</li>
</ul>

<h2>Licença</h2>

<p>Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para mais detalhes.</p>

</body>
</html>
