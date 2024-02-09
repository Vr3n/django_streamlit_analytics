from datetime import datetime
from ninja import Schema

class CustomerBase(Schema):
	name: str
	gender: int
	age: int
	favorite_number: int

class CustomerIn(CustomerBase):
	...

class CustomerOut(CustomerBase):
	id: int
	created_at: datetime
	updated_at: datetime
