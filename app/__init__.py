from flask import Flask


#создаёт экземпляр класса Flask (переменную app)
app = Flask(__name__)
app.config['SECRET_KEY'] = 'bolshoy_secret_dlya_malenkoy_kompanii'

from app import routes