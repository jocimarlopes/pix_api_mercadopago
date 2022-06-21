# Pix API Mercado Pago
#
### Api para receber pagamentos Pix via Mercado Pago
#
#### Rotas 
* `/get_payment` Solicita um pagamento recebendo os parâmetros de *price* e *description* no body.
* `/verify_payment` Verifica o **status** do pagamento recebendo o parâmetro *id* no body com o ID do Pagamento.
