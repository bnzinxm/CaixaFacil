# CaixaFacil
Um sistema PDV completo!
-
![Logo](<./markdown/banner.png>)
<br>
CaixaFácil é um sistema simples de PDV (Ponto de Venda) desenvolvido para gerenciar produtos e vendas, com funcionalidades de registro de produtos, registro de vendas e itens de cada venda. O sistema utiliza um banco de dados MySQL para armazenar as informações.
## Como Usar no Supermercado
### 1. **Adicionar Produtos**
- Registre os produtos no sistema, incluindo nome, preço e estoque. Isso garante que os itens estejam disponíveis para vendas no supermercado.
### 2. **Registrar Vendas**
- Quando um cliente realizar uma compra, registre a venda no sistema. O sistema criará um registro com a data e o total da venda.
### 3. **Registrar Itens na Venda**
- Para cada produto que o cliente comprou, registre o item de venda no sistema, especificando o produto, a quantidade comprada e o subtotal (preço \* quantidade).
### Fluxo de Uso
1. O operador cadastra os **produtos** no sistema com o nome, preço e quantidade disponível no estoque.
2. Quando o cliente compra, o operador registra a **venda** no sistema.
3. Para cada produto na compra, o operador adiciona um **item de venda**, incluindo a quantidade comprada e o subtotal.
4. O sistema calcula automaticamente o **total da venda**, subtrai a quantidade vendida do estoque e mantém o controle de tudo.
## Estrutura do Banco de Dados
O banco de dados `caixafacil` contém as seguintes tabelas:
- **produtos**: Contém informações sobre os produtos no estoque.
- **vendas**: Registra as vendas realizadas.
- **itens_venda**: Registra os produtos vendidos em cada venda.
## Tecnologias Utilizadas
- **MySQL**: Banco de dados relacional para armazenamento de informações.
- **Node.js**: Plataforma para desenvolvimento do backend.
- **Express**: Framework para construção do servidor backend.
## Contribuindo
1. Faça o fork deste repositório.
2. Crie uma branch para sua modificação (`git checkout -b minha-modificacao`).
3. Realize a alteração desejada.
4. Faça o commit das suas mudanças (`git commit -am 'Adiciona nova funcionalidade'`).
5. Envie para a branch principal (`git push origin minha-modificacao`).
6. Abra um Pull Request para revisão.
