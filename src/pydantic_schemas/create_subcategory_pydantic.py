from pydantic import BaseModel, validator, Field
from typing import Any, List, Dict, Type

class CreateSubcategorySuccessItem(BaseModel):
    categoryId: str
    categorySystemId: str
    name: str
    parentId: str
    parentSystemId: str

class CreateSubcategorySuccessStatusCode(BaseModel):
    description: str
    items: List[CreateSubcategorySuccessItem]

class CreateSubcategorySuccessResponse(BaseModel):
    responses: dict[int, List[CreateSubcategorySuccessStatusCode]]






# {
# 	"responses": {
# 		"201": [
# 			{
# 				"description": "Created items.",
# 				"items": [
# 					{
# 						"categoryId": "4df04419-61ff-44fd-9c97-eb035dad408e",
# 						"categorySystemId": "submeylikh_2",
# 						"name": "Все товары",
# 						"parentId": "33e67fcc-c360-4ee5-beba-1da5248f8463",
# 						"parentSystemId": "meylikh_1"
# 					}
# 				]
# 			}
# 		]
# 	}
# }


# from pydantic import List, BaseModel, Field

# class CategoryItem(BaseModel): category_id = Field(str) system_id = Field(str, alias='categorySystemId') name = Field(str)

# class ListResponse(BaseModel): responses = List[CategoryItem]

# # Создание объекта `ListResponse` с описанием `{ "201": [ { "описаниес": "Создан", "элементы ": [ { "категория_идентификатор": "fce923ac - 06c3 - 45ff - 819b - c036a3926d9d ", "идентификация_системы_категории": "товары 3 ", "наименование": "Весь товар "} ]} ]}`

# list_response = ListResponse(responses=[CategoryItem(category_id='fce923ac-06c3-45ff-819b-c036a3926d9d', system_id='products3', name='Все товары')])

# print(list_response.responses[0].