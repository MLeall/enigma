# Projeto Enigma

## Planejamento

O chatGPT sugeriu com caminho para termos de rumo:

1. Representação dos componentes: Primeiro, você precisa criar uma representação dos componentes da Enigma, como o teclado, os rotores, os refletores e as lâmpadas. Você pode usar estruturas de dados como matrizes ou dicionários para mapear as substituições de letras.

2. Definição das configurações iniciais: Assim como na Enigma real, você precisa permitir que o usuário defina as configurações iniciais dos rotores, como sua ordem, posição inicial e as ligações elétricas. Isso pode ser feito por meio de uma interface de usuário ou por meio de entradas no código.

3. Implementação das substituições de letras: Ao pressionar uma tecla, você precisa implementar a lógica de substituição de letras, passando a corrente elétrica pelos rotores e refletores. Você pode usar as configurações definidas anteriormente para realizar as substituições corretas e garantir que cada letra seja trocada por outra.

4. Rotação dos rotores: Os rotores na Enigma giram conforme as teclas são pressionadas. Você precisa implementar a lógica para girar os rotores na ordem correta e na posição correta, simulando o movimento dos rotores reais.

5. Iluminação dos caracteres: Depois de passar pelas substituições, a corrente elétrica atinge a lâmpada correspondente à letra criptografada. Você deve implementar a lógica para identificar qual lâmpada deve ser iluminada com base na letra criptografada.

6. Criptografia e decodificação: Com as etapas anteriores implementadas, você pode criar funções para criptografar e decodificar mensagens usando a simulação da Enigma. A criptografia envolverá passar uma mensagem letra por letra pelos componentes simulados, enquanto a decodificação seguirá o processo inverso.

## Ideias

Pensei em listar algumas ideias para ter no projeto final. Fiquem a vontade pra acrescentar mais.

- Utilizar pacote `tkinter` para criação de uma GUI ❌
- Criação de uma aplicação web do nosso projeto ❌