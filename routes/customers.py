from flask import Blueprint, render_template, request
from database.customers import CUSTOMERS

customersRoute = Blueprint('customer', __name__) 

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

@customersRoute.route('/')
def customersList():
    return render_template('customersList.html', customers=CUSTOMERS)

@customersRoute.route('/', methods=['POST'])
def createCostumer():
    data = request.json
    print(data)
    customer = {
        'id': len(CUSTOMERS),
        'name': data['name'],
        'email': data['email']
    }
    CUSTOMERS.append(customer)
    return render_template('customerItem.html', customer=customer)

@customersRoute.route('/new')
def customerForm():
    return render_template('customerForm.html')

@customersRoute.route('/<int:customerId>') 
def getCustomer(customerId):
    customer = None
    for c in CUSTOMERS:
        if c['id'] == customerId:
            customer = c
    return render_template('specificCustomer.html', customer=customer)

@customersRoute.route('/<int:customerId>/edit') 
def customerEditForm(customerId):
    customer = None
    for c in CUSTOMERS:
        if c['id'] == customerId:
            customer = c
    return render_template('customerForm.html', customer=customer)

@customersRoute.route('/<int:customerId>/update', methods=['PUT']) 
def updateCostumer(customerId):
    data = request.json
    print(data)
    customer = None
    for c in CUSTOMERS:
        if c['id'] == customerId:
            c['name'] = data['name']
            c['email'] = data['email']
            customer = c
    return render_template('customerItem.html', customer=customer)

@customersRoute.route('/<int:customerId>/delete', methods=['DELETE']) 
def deleteCustomer(customerId):
    global CUSTOMERS
    CUSTOMERS = [c for c in CUSTOMERS if c['id'] != customerId]
    return {'delete': 'ok'}