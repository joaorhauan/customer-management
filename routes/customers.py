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
    return render_template('newCustomerForm.html')

@customersRoute.route('/<int:customerId>') 
def getCustomer(customerId):
    return render_template('specificCustomer.html')

@customersRoute.route('/<int:customerId>/edit') 
def costumerEditForm(customerId):
    return render_template('editCustomerForm.html')

@customersRoute.route('/<int:customerId>/update', methods=['PUT']) 
def updateCostumer(customerId):
    pass

@customersRoute.route('/<int:customerId>/delete', methods=['DELETE']) 
def deleteCostumer(customerId):
    pass