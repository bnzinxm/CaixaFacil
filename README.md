<h1><strong>⚠️ Esse projeto está em desenvolmento, certas funções podem não funcionar ⚠️</strong></h1>

![Logo](<./markdown/banner.png>)

# CaixaFacil, Um sistema PDV completo!

<br>

CaixaFácil é um sistema simples de PDV (Ponto de Venda) desenvolvido para gerenciar produtos e vendas, com funcionalidades de registro de produtos, registro de vendas e itens de cada venda. O sistema utiliza um banco de dados MySQL para armazenar as informações.
## Como Usar no Supermercado
### 1. **Adicionar Produtos**
- Registre os produtos no sistema, incluindo nome, preço e estoque. Isso garante que os itens estejam disponíveis para vendas no supermercado.
### 2. **Registrar Vendas**
- Quando um cliente realizar uma compra, registre a venda no sistema. O sistema criará um registro com a data e o total da venda.
### 3. **Registrar Itens na Venda**
Para cada produto que o cliente comprou, registre o item de venda no sistema, especificando o produto, a quantidade comprada e o subtotal (preço \* quantidade).
## **Como usar localmente**
 ### Se você está usando Linux, siga as instruções abaixo:
  - 1. Baixe/clone o repositório
  - 2. Usando o terminal, execute ```chmod +x start.sh```
  - 3. Depois, execute ```./start.sh```
  - ***Após isso, em alguns segundos o programa deverá iniciar, lembre-se de configurar a database primeiro!***
 ### Se você estiver usando Windows, siga as instruções abaixo:
  - 1. Baixe/clone o repositório
  - 2. Usando o prompt de comando, execute ```start.bat``` 
  - ***Após isso, em alguns segundos o programa deverá iniciar, lembre-se de configurar a database primeiro!***

## Estrutura do Banco de Dados
O banco de dados `caixafacil` contém as seguintes tabelas:
- **produtos**: Contém informações sobre os produtos no estoque.
- **vendas**: Registra as vendas realizadas.
- **itens_venda**: Registra os produtos vendidos em cada venda.
  
## Tecnologias Utilizadas
- **MySQL**: Banco de dados relacional para armazenamento de informações.
- **Python**: Plataforma para desenvolvimento do backend.
- **PyQt6**: Framework para desenvolver a interface gráfica do aplicativo.

## Contribuindo
1. Faça o fork deste repositório.
2. Crie uma branch para sua modificação (`git checkout -b minha-modificacao`).
3. Realize a alteração desejada.
4. Faça o commit das suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
5. Envie para a branch principal (`git push origin minha-modificacao`).
6. Abra um Pull Request para revisão.
