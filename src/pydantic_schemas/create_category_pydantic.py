from pydantic import BaseModel, validator, Field
from typing import Any, List, Dict, Type

class SuccessItem(BaseModel):
    categoryId: str
    categorySystemId: str
    name: str

class SuccessStatusCode(BaseModel):
    description: str
    items: List[SuccessItem]

class SuccessResponse(BaseModel):
    responses: dict[int, List[SuccessStatusCode]]






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


# from pydantic import List, BaseModel, Field

# class CategoryItem(BaseModel): category_id = Field(str) system_id = Field(str, alias='categorySystemId') name = Field(str)

# class ListResponse(BaseModel): responses = List[CategoryItem]

# # Создание объекта `ListResponse` с описанием `{ "201": [ { "описаниес": "Создан", "элементы ": [ { "категория_идентификатор": "fce923ac - 06c3 - 45ff - 819b - c036a3926d9d ", "идентификация_системы_категории": "товары 3 ", "наименование": "Весь товар "} ]} ]}`

# list_response = ListResponse(responses=[CategoryItem(category_id='fce923ac-06c3-45ff-819b-c036a3926d9d', system_id='products3', name='Все товары')])

# print(list_response.responses[0].