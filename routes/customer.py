from flask import Blueprint, render_template
from database.customer import CUSTOMERS

customerRoute = Blueprint('client', __name__) 

"""
    Customer Routes
    - /customer/ (GET) - List all customers
    - /customer/ (POST) - Create a new customers
    - /customer/new (GET) - Return a form to create a new customers
    - /customer/<id> (GET) - Return specific customer data
    - /customer/<id>/edit (GET) - return a form to edit a customer
    - /customer/<id>/update (PUT) - update customer data
    - clientes/<id>/delete (DELETE) - delete a costumer
"""

@customerRoute.route('/')
def customerList():
    return render_template('customerList.html', customers=CUSTOMERS)

@customerRoute.route('/', methods=['POST'])
def createCostumer():
    pass

@customerRoute.route('/new')
def costumerForm():
    return render_template('newCustomerForm.html')

@customerRoute.route('/<int:customerId>') 
def getCustomer(customerId):
    return render_template('specificCustomer.html')

@customerRoute.route('/<int:customerId>/edit') 
def costumerEditForm(customerId):
    return render_template('editCustomerForm.html')

@customerRoute.route('/<int:customerId>/update', methods=['PUT']) 
def updateCostumer(customerId):
    pass

@customerRoute.route('/<int:customerId>/delete', methods=['DELETE']) 
def deleteCostumer(customerId):
    pass