from routes.home import homeRoute
from routes.customers import customersRoute
from db.database import db
from db.models.customers import Customer

def allConfig(app):
    routeConfig(app)
    dbConfig()

def routeConfig(app):
    app.register_blueprint(homeRoute)
    app.register_blueprint(customersRoute, url_prefix='/customers')

def dbConfig():
    db.connect()
    db.create_tables([Customer])