from pydantic import BaseModel, validator, Field

class CreateCategory(BaseModel):
	"responses": {
		"201": [
			{
				"description": "Сreated items.",
				"items": [
					{
						"categoryId": "0f05166c-b92b-476a-a837-b30c04478c56",
						"categorySystemId": "products1",
						"name": "Все товары"
					}
				]
			}
		]
	}