from pydantic import BaseModel, validator, Field
from typing import List

class SuccessResponse(BaseModel):
    description: str
    items: List[]

class SuccessItem(BaseModel):
    categoryId: str
    categorySystemId: str
    name: str



# response_data = {
#     "201": [
#         {
#             "description": "Created items.",
#             "items": [
#                 {
#                     "categoryId": "afda4588-949c-4885-9d91-bbc0b3b2aa8a",
#                     "categorySystemId": "products3",
#                     "name": "Все товары"
#                 }
#             ]
#         }
#     ]
# }