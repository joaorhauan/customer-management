from flask import Flask
from routes.home import homeRoute
from routes.customer import customerRoute

app = Flask(__name__)

app.register_blueprint(homeRoute)
app.register_blueprint(customerRoute, url_prefix='/customer')

app.run(debug=True)