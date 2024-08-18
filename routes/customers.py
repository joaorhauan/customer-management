from flask import Blueprint, render_template, request
from db.models.customers import Customer

customersRoute = Blueprint('customer', __name__) 

@customersRoute.route('/')
def customersList():
    customer = Customer.select()
    return render_template('customersList.html', customers=customer)

@customersRoute.route('/', methods=['POST'])
def createCostumer():
    data = request.json
    newCustomer = Customer.create(name=data['name'], email=data['email'])

    return render_template('customerItem.html', customer=newCustomer)

@customersRoute.route('/new')
def customerForm():
    return render_template('customerForm.html')

@customersRoute.route('/<int:customerId>') 
def getCustomer(customerId):
    customer = Customer.get_by_id(customerId)
    return render_template('specificCustomer.html', customer=customer)

@customersRoute.route('/<int:customerId>/edit') 
def customerEditForm(customerId):
    customer = Customer.get_by_id(customerId)
    return render_template('customerForm.html', customer=customer)

@customersRoute.route('/<int:customerId>/update', methods=['PUT']) 
def updateCostumer(customerId):
    data = request.json
    customer = Customer.get_by_id(customerId)
    customer.name = data['name']
    customer.email = data['email']
    customer.save()
    return render_template('customerItem.html', customer=customer)

@customersRoute.route('/<int:customerId>/delete', methods=['DELETE']) 
def deleteCustomer(customerId):
    customer = Customer.get_by_id(customerId)
    customer.delete_instance()
    return {'delete': 'ok'}