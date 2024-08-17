from flask import Flask
from routes.home import homeRoute
from routes.customers import customersRoute

app = Flask(__name__)

app.register_blueprint(homeRoute)
app.register_blueprint(customersRoute, url_prefix='/customers')

app.run(debug=True)