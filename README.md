# Pix API Mercado Pago
### Api para receber pagamentos Pix via Mercado Pago
#
#### Configurar
Para configurar precisamos das credenciais do Mercado Pago, `public_key` e `access_token`, iremos adicionar elas no arquivo **credentials.json** que se encontra na raíz do projeto.
#### Rotas 
* `/get_payment` Solicita um pagamento recebendo os parâmetros de *price* e *description* no body.
* `/verify_payment` Verifica o **status** do pagamento recebendo o parâmetro *id* no body com o ID do Pagamento.
