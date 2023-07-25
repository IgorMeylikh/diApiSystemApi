SERVICE_URL = 'http://esb:8052/'
REQUETS_ID = '1'
SENDER_SYSTEM = 'erpdhecom'

INTERNAL_LOGIN = 'system@di-house.ru'
INTERNAL_PASSWORD = 'Password1!'
HEADERS = {'Content-type': 'application/json', 'Accept': 'text/plain', 'requestId': REQUETS_ID, 'senderSystem': SENDER_SYSTEM}

EXTERNAL_LOGIN = 'consumer@di-house.ru'
EXTERNAL_PASSWORD = 'Password1!'

CREATE_CATEGORIES_PAGE = 'internal/categories/create'               #Страница создания категории
UPDATE_CATEGORIES_PAGE = 'internal/categories/update'               #Страница обновления категории
DELETE_CATEGORIES_PAGE = 'internal/categories/delete'               #Страница удаления категории
CLEAR_CATEGORIES_PAGE = 'internal/categories/clear'                 #Страница очистки всех категорий

CREATE_PRODUCTS_PAGE = 'internal/products/create'                   #Страница создания продукта
UPDATE_PRODUCTS_PAGE = 'internal/products/update'                   #Страница обновления продукта
DELETE_PRODUCTS_PAGE = 'internal/products/delete'                   #Страница удаления продукта
CLEAR_PRODUCTS_PAGE = 'internal/products/clear'                     #Страница очистки всех продуктов
GETTING_PRODUCTS_PAGE = 'external/products'                         #Страница получения всех продуктов для внешних систем

UPDATE_STOCKS_PAGE = 'internal/stocks/update'                       #Страница обновления остатков
CLEAR_STOCKS_PAGE = 'internal/stocks/clear'                         #Страница очистки остатков
GETTING_STOCKS_PAGE = 'external/stocks'                             #Страница получения всех остатков для внешних систем

UPDATE_PRICES_PAGE = 'internal/prices/update'                       #Страница обновления цен
CLEAR_PRICES_PAGE = 'internal/prices/clear'                         #Страница очистки цен
GETTING_PRICES_PAGE = 'external/prices'                             #Страница получения всех цен для внешних систем

CREATE_ORDERS_PAGE = 'external/orders/create'                       #Страница создания заказа для внешних систем
UPDATE_ORDERS_PAGE = 'external/orders/update'                       #Страница обновления заказа для внешних систем
DELETE_ORDERS_PAGE = 'internal/orders/delete'                       #Страница удаления заказа для внешних систем
CLEAR_ORDERS_PAGE = 'internal/orders/clear'                         #Страница очистки заказов
GETTING_ORDERS_STATUS_PAGE = 'external/orders/status'               #Страница получения статуса заказа для внешних систем
UPDATE_EXT_ORDERS_STATUS_PAGE = 'external/orders/status/update'     #Страница обновления статуса заказа для внешних систем
UPDATE_INT_ORDERS_STATUS_PAGE = 'internal/orders/status/update'     #Страница получения статуса заказа

DIAPISYSTEM_RESPONSES_ORDERS_CREATE = 'responses/orders/create'     #Страница создания заказа через diApi
DIAPISYSTEM_RESPONSES_ORDERS_UPDATE = 'responses/orders/update'     #Страница обновления заказа через diApi
                                                                    #Тут должна быть страница обновления статуса заказа, но её нет в описании взаимодействия.

# Пустой JSON
EMPTY_JSON = {}

# JSON'ы для работы с категориями (Создание)
CREATE_ONE_CATEGORY_JSON = {"items":[{"categorySystemid": "meylikh_1","name": "meylikh_1"}]}       
CREATE_SEVERAL_CATEGORIES_JSON = {"items":[{"categorySystemid": "test_1","name": "test_1"}, {"categorySystemid": "test_2","name": "test_2"}, {"categorySystemid": "test_3","name": "test_3"}, {"categorySystemid": "test_4","name": "test_4"}, {"categorySystemid": "test_5","name": "test_5"}]}     
CREATE_REPEAT_ONE_CATEGORY_JSON = {"items":[{"categorySystemid": "meylikh_1","name": "meylikh_1"}]} 
CREATE_VALIDATE_CATEGORY_AND_REPEAT_CATEGORY_JSON = {"items":[{"categorySystemid": "meylikh_2","name": "meylikh_2"}, {"categorySystemid": "meylikh_1","name": "meylikh_1"}]}
CREATE_VALIDATE_CATEGORY_AND_REPEAT_HIMSELF_CATEGORY_JSON = {"items":[{"categorySystemid": "meylikh_3","name": "meylikh_3"}, {"categorySystemid": "meylikh_3","name": "meylikh_3"}]}
# CREATE_NOT_REQUIRED_JSON = {"items":[{"categorySystemid": "meylikh_nr"}]}
CREATE_NOT_VALID_JSON = '{"items":[{"categorySystemid": "meylikh_1","name": "meylikh_1",}]}'
CREATE_CATEGORY_WITHOUT_CATEGORY_SYSTEM_ID_JSON = {"items":[{"name": "meylikh_without_categorySystemid"}]}    
CREATE_CATEGORY_WITHOUT_NAME_JSON = {"items":[{"categorySystemid": "meylikh_without_name"}]}

# JSON'ы для работы с категориями (Создание подкатегории)
CREATE_ONE_SUBCATEGORY_JSON = {"items":[{"categorySystemid": "submeylikh_1","name": "submeylikh_1", "parentSystemId": "meylikh_1"}]} 
CREATE_REPEAT_ONE_SUBCATEGORY_JSON = {"items":[{"categorySystemid": "submeylikh_1","name": "submeylikh_1", "parentSystemId": "meylikh_1"}]}

# JSON'ы для работы с категориями (Обновление)
UPDATE_ONE_CATEGORY_JSON = {"items":[{"categorySystemid": "submeylikh_1","name": "submeylikh_1"}]}      
UPDATE_SEVERAL_CATEGORIES_JSON = {"items":[{"categorySystemid": "test_3","name": "test_6"}, {"categorySystemid": "test_4","name": "test_7"}]}   
UPDATE_SEVERAL_CATEGORIES_ONE_NOT_ISSET_JSON = {"items":[{"categorySystemid": "test_6","name": "test_3"}, {"categorySystemid": "test_7","name": "test_4"}, {"categorySystemid": "test_8","name": "test_6"}]}  
UPDATE_NOT_REQUIRED_JSON = {"items":[{"categorySystemId": "submeylikh_1"}]} # Отсутствует хотя бы один обязательный параметр   
UPDATE_ONE_NOT_ISSET_CATEGORY_JSON = {"items":[{"categorySystemid": "submeylikh_2","name": "submeylikh_1"}]}   
UPDATE_NOT_VALID_JSON = '{"items":[{"categorySystemid": "submeylikh_1","name": "submeylikh_1",}]}'
UPDATE_CATEGORY_WITHOUT_CATEGORY_SYSTEM_ID_JSON = {"items":[{"name": "meylikh_1",}]} 

# JSON'ы для работы с категориями (Удаление)
DELETE_ONE_CATEGORY_JSON = {"items": [{"categorySystemId": "test_1"}]}
DELETE_SEVERAL_CATEGORIES_JSON = {"items": [{"categorySystemId": "test_2"}, {"categorySystemId": "test_3"}]}
DELETE_ONE_NOT_ISSET_CATEGORY_JSON = {"items": [{"categorySystemId": "test_7"}]}

# JSON'ы для работы с товарами (создание)
CREATE_ONE_PRODUCT_WITH_OPTIONAL_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "name": "Тестовый ноутбук 1", "sku": "TEST-SKU-1", "type": "product", "categorySystemId": "meylikh_1", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}]}
CREATE_ONE_PRODUCT_WITHOUT_OPTIONAL_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-2", "name": "Тестовый ноутбук 2", "sku": "TEST-SKU-2", "type": "product"}]}
CREATE_ONE_PRODUCT_WITHOUT_PRODUCT_SYSTEM_ID_JSON = {"items": [{"name": "Тестовый ноутбук 1", "sku": "TEST-SKU-1", "type": "product"}]}
CREATE_ONE_PRODUCT_WITHOUT_NAME_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "sku": "TEST-SKU-1", "type": "product"}]}
CREATE_ONE_PRODUCT_WITHOUT_SKU_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-2", "name": "Тестовый ноутбук 2", "type": "product"}]}
CREATE_ONE_PRODUCT_WITHOUT_TYPE_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "name": "Тестовый ноутбук 1", "sku": "TEST-SKU-1"}]}