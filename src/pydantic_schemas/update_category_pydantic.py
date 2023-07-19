from pydantic import BaseModel, validator, Field
from typing import Any, List, Dict, Type

class UpdateCategorySuccessItem(BaseModel):
    categoryId: str
    categorySystemId: str
    name: str
    parentId: str
    parentSystemId: str

class UpdateCategorySuccessStatusCode(BaseModel):
    description: str
    items: List[UpdateCategorySuccessItem]

class UpdateCategorySuccessResponse(BaseModel):
    responses: dict[int, List[UpdateCategorySuccessStatusCode]]

# {
# 	"responses": {
# 		"200": [
# 			{
# 				"description": "Updated items.",
# 				"items": [
# 					{
# 						"categoryId": "a1484222-4fff-4ca8-804a-ea14fc9f3cdd",
# 						"categorySystemId": "submeylikh_1",
# 						"name": "Все товары",
# 						"parentId": "4456f616-0cd7-49af-99a3-d6cc30c1f0db",
# 						"parentSystemId": "meylikh_1"
# 					}
# 				]
# 			}
# 		]
# 	}
# }