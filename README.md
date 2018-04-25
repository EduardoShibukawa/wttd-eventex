# Eventex

Sistema de eventos encomentado pela morena.

## Como desenvolver?

1. Clone o respositório
2. Crie um virtualenv com o python 3.5
3. Ative o virtualenv
4. Instale as dependêcias.
5. Configure a instância como .env
6. Execute os testes.

```console
git clone https://github.com/EduardoShibukawa/wttd-eventex.git
cd wttd-eventex
python -m venv .wttd
source .wttd/bin/activate
pip install -r requirements.txt
cp contrib/env-sample .env 
python manage.py test        
```

## Como Fazer o deploy

1. Crie uma instância no heroku.
2. Envie as configurações para o heroku.
3. Defina uma SECRET_KEY segura para a instância.
4. Defina DEBUG=false.
5. Configure o serviço de email.
6. Envie o código para o heroku.

```console
heroku create:minhainstancia
heroku config:push
heroku config:set SECRET_KEY='python contrib/secret_gen.py'
heroku config:set DEBUG=false
#Configuro email
git push heroku master --force
```