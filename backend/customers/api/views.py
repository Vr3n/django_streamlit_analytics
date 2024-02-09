from typing import List
from ninja import NinjaAPI
from customers.models import Customer
from django.shortcuts import get_object_or_404

from customers.api.schemas import CustomerIn, CustomerOut

api = NinjaAPI()


@api.post("/customers")
def create_customer(request, payload: CustomerIn):
	customer = Customer.objects.create(**payload.dict())
	return {"id": customer.id}


@api.post("/customers/{customer_id}", response=CustomerOut)
def get_customer(request, customer_id: int):
	customer = get_object_or_404(Customer, id=customer_id)
	return customer


@api.get("/customers", response=List[CustomerOut])
def list_customers(request):
	qs = Customer.objects.all()
	return qs
