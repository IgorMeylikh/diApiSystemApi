SERVICE_URL = 'http://esb:8052/'
REQUETS_ID = '1'
SENDER_SYSTEM = 'meylikh'

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
CREATE_ONE_CATEGORY_JSON = {"items":[{"categorySystemid": "meylikh_1_id","name": "meylikh_1_name"}]}       
CREATE_SEVERAL_CATEGORIES_JSON = {"items":[{"categorySystemid": "test_1_id","name": "test_1_name"}, {"categorySystemid": "test_2_id","name": "test_2_name"}, {"categorySystemid": "test_3_id","name": "test_3_name"}, {"categorySystemid": "test_4_id","name": "test_4_name"}, {"categorySystemid": "test_5_id","name": "test_5_name"}]}     
CREATE_REPEAT_ONE_CATEGORY_JSON = {"items":[{"categorySystemid": "meylikh_1_id","name": "meylikh_1_name"}]} 
CREATE_VALIDATE_CATEGORY_AND_REPEAT_CATEGORY_JSON = {"items":[{"categorySystemid": "meylikh_2_id","name": "meylikh_2_name"}, {"categorySystemid": "meylikh_1_id","name": "meylikh_1_name"}]}
CREATE_VALIDATE_CATEGORY_AND_REPEAT_HIMSELF_CATEGORY_JSON = {"items":[{"categorySystemid": "meylikh_3_id","name": "meylikh_3_name"}, {"categorySystemid": "meylikh_3_id","name": "meylikh_3_name"}]}
# CREATE_NOT_REQUIRED_JSON = {"items":[{"categorySystemid": "meylikh_nr"}]}
CREATE_NOT_VALID_JSON = '{"items":[{"categorySystemid": "meylikh_1_id","name": "meylikh_1_name",}]}'
CREATE_CATEGORY_WITHOUT_CATEGORY_SYSTEM_ID_JSON = {"items":[{"name": "meylikh_without_categorySystemid"}]}    
CREATE_CATEGORY_WITHOUT_NAME_JSON = {"items":[{"categorySystemid": "meylikh_without_name"}]}

# JSON'ы для работы с категориями (Создание подкатегории)
CREATE_ONE_SUBCATEGORY_JSON = {"items":[{"categorySystemid": "submeylikh_1_id","name": "submeylikh_1_name", "parentSystemId": "meylikh_1_id"}]} 
CREATE_REPEAT_ONE_SUBCATEGORY_JSON = {"items":[{"categorySystemid": "submeylikh_1_id","name": "submeylikh_1_name", "parentSystemId": "meylikh_1_id"}]}

# JSON'ы для работы с категориями (Обновление)
UPDATE_ONE_CATEGORY_JSON = {"items":[{"categorySystemid": "submeylikh_1_id","name": "submeylikh_2_name"}]}      
UPDATE_SEVERAL_CATEGORIES_JSON = {"items":[{"categorySystemid": "test_4_id","name": "test_4_name_update"}, {"categorySystemid": "test_5_id","name": "test_5__name_update"}]}   
UPDATE_SEVERAL_CATEGORIES_ONE_NOT_ISSET_JSON = {"items":[{"categorySystemid": "test_4_id","name": "test_4_name_update_2"}, {"categorySystemid": "test_5_id","name": "test_5_name_update_2"}, {"categorySystemid": "test_8_id","name": "test_6_name_update_2"}]}  
UPDATE_CATEGORY_ONE_NOT_ISSET_CATEGORY_JSON = {"items":[{"categorySystemid": "submeylikh_2_id","name": "submeylikh_1_name_update_2"}]}   
UPDATE_CATEGORY_NOT_VALID_JSON = '{"items":[{"categorySystemid": "submeylikh_1_id","name": "submeylikh_1_name_update_3",}]}'
UPDATE_CATEGORY_WITHOUT_CATEGORY_SYSTEM_ID_JSON = {"items":[{"name": "meylikh_1_name_update_4",}]} 
UPDATE_CATEGORY_WITHOUT_OPTIONAL_JSON = {"items":[{"categorySystemId": "submeylikh_1_id"}]}

# JSON'ы для работы с категориями (Удаление)
DELETE_ONE_CATEGORY_JSON = {"items": [{"categorySystemId": "test_1_id"}]}
DELETE_SEVERAL_CATEGORIES_JSON = {"items": [{"categorySystemId": "test_2_id"}, {"categorySystemId": "test_3_id"}]}
DELETE_ONE_NOT_ISSET_CATEGORY_JSON = {"items": [{"categorySystemId": "test_7_id"}]}

# JSON'ы для работы с товарами (создание)
CREATE_ONE_PRODUCT_WITH_OPTIONAL_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "name": "Тестовый товар 1", "sku": "TEST-SKU-1", "type": "product", "categorySystemId": "meylikh_1_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}]}
CREATE_ONE_PRODUCT_WITHOUT_OPTIONAL_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-2", "name": "Тестовый товар 2", "sku": "TEST-SKU-2", "type": "product"}]}
CREATE_ONE_PRODUCT_WITH_REPEAT_GUID_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "name": "REPEAT GUID", "sku": "TEST-GUID-REPEAT", "type": "product", "categorySystemId": "meylikh_1_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}]}
CREATE_ONE_PRODUCT_WITH_REPEAT_SKU_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-SKU-REPEAT", "name": "REPEAT SKU", "sku": "TEST-SKU-1", "type": "product", "categorySystemId": "meylikh_1_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}]}
CREATE_SEVERAL_PRODUCTS_WITH_OPTIONAL_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-3", "name": "Тестовый товар 3", "sku": "TEST-SKU-3", "type": "product", "categorySystemId": "meylikh_2_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}, 
                                                        {"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-4", "name": "Тестовый товар 4", "sku": "TEST-SKU-4", "type": "product", "categorySystemId": "meylikh_2_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}, 
                                                        {"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-5", "name": "Тестовый товар 5", "sku": "TEST-SKU-5", "type": "product", "categorySystemId": "meylikh_3_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}, 
                                                        {"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-6", "name": "Тестовый товар 6", "sku": "TEST-SKU-6", "type": "product", "categorySystemId": "meylikh_3_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}]}
CREATE_SEVERAL_PRODUCTS_WITHOUT_OPTIONAL_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-7", "name": "Тестовый товар 7", "sku": "TEST-SKU-7", "type": "product"}, 
                                                        {"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-8", "name": "Тестовый товар 8", "sku": "TEST-SKU-8", "type": "product"}, 
                                                        {"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-9", "name": "Тестовый товар 9", "sku": "TEST-SKU-9", "type": "product"}, 
                                                        {"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-10", "name": "Тестовый товар 10", "sku": "TEST-SKU-10", "type": "product"}]}
CREATE_ONE_PRODUCT_WITHOUT_PRODUCT_SYSTEM_ID_JSON = {"items": [{"name": "Тестовый товар 11", "sku": "TEST-SKU-11", "type": "product"}]}
CREATE_ONE_PRODUCT_WITHOUT_NAME_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-12", "sku": "TEST-SKU-12", "type": "product"}]}
CREATE_ONE_PRODUCT_WITHOUT_SKU_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-13", "name": "Тестовый товар 13", "type": "product"}]}
CREATE_ONE_PRODUCT_WITHOUT_TYPE_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-14", "name": "Тестовый товар 14", "sku": "TEST-SKU-14"}]}
CREATE_ONE_SERVICE_WITH_OPTIONAL_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-15", "name": "Тестовый сервис 1", "sku": "TEST-SKU-15", "type": "service", "categorySystemId": "meylikh_3_id", "previewLink": "https://www.kaumediagroup.com/wp-content/uploads/2020/11/KMG_Chat_Feature.jpg"}]}
CREATE_ONE_WORK_WITH_OPTIONAL_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-16", "name": "Тестовая работа 1", "sku": "TEST-SKU-16", "type": "work", "categorySystemId": "meylikh_3_id", "previewLink": "https://www.kaumediagroup.com/wp-content/uploads/2020/11/KMG_Chat_Feature.jpg"}]}
CREATE_SEVERAL_PRODUCTS_WITH_REPEAT_GUID_WITH_OPTIONAL_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-17", "name": "Тестовый товар 17", "sku": "TEST-SKU-17", "type": "product", "categorySystemId": "meylikh_2_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}, 
                                                                         {"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "name": "SEVERAL-REPEAT-GUID", "sku": "TEST-SEVERAL-REPEAT-GUID", "type": "product", "categorySystemId": "meylikh_2_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}]}
CREATE_SEVERAL_PRODUCTS_WITH_REPEAT_SKU_WITH_OPTIONAL_JSON =  {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-19", "name": "Тестовый товар 19", "sku": "TEST-SKU-19", "type": "product", "categorySystemId": "meylikh_2_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}, 
                                                                         {"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-20", "name": "SEVERAL-REPEAT-SKU", "sku": "TEST-SKU-1", "type": "product", "categorySystemId": "meylikh_2_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}]}
CREATE_ONE_SERVICE_WITH_JS_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-JS", "name": "Тестовый сервис JS", "sku": "TEST-SKU-JS", "type": "service", "categorySystemId": "meylikh_3_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg\" onclick=\"alert('Клик!')\""}]}
CREATE_ONE_PRODUCT_IN_NOT_ISSET_CATEGORY_SYSTEM_ID_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-notIssetCategorySystemId", "name": "Тестовый товар notIssetCategorySystemId", "sku": "TEST-SKU-NOT-ISSET-CATEGORY-ID", "type": "product", "categorySystemId": "meylikh_not_isset"}]}

# JSON'ы для работы с товарами (обновление)
UPDATE_ONE_PRODUCT_WITH_OPTIONAL_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "name": "Тестовый товар 1 update", "sku": "TEST-SKU-1-UPDATE", "type": "product", "categorySystemId": "meylikh_2_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}]}
UPDATE_SEVERAL_PRODUCTS_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "name": "Тестовый товар 1 update several", "sku": "TEST-SKU-1-UPDATE-SEVERAL", "type": "work", "categorySystemId": "meylikh_2_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"},
                                          {"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-2", "name": "Тестовый товар 2 update several", "sku": "TEST-SKU--SEVERAL", "type": "work"}]}
UPDATE_ONE_PRODUCT_ONLY_NAME_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "name": "Тестовый товар 1 only name"}]}
UPDATE_ONE_PRODUCT_ONLY_SKU_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "sku": "TEST-SKU-1-ONLY-SKU"}]}
UPDATE_ONE_PRODUCT_ONLY_TYPE_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "type": "service"}]}
UPDATE_ONE_PRODUCT_ONLY_CATEGORY_SYSTEM_ID_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "categorySystemId": "meylikh_1_id"}]}
UPDATE_ONE_PRODUCT_ONLY_PREVIEW_LINK_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}]}

UPDATE_ONE_PRODUCT_WITHOUT_OPTIONAL_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1"}]}
UPDATE_PRODUCT_NOT_VALID_JSON = '{"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-1", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg",}]}'
UPDATE_PRODUCT_NOT_ISSET_PRODUCT_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-not-isset", "name": "Тестовый товар 1 update", "sku": "TEST-SKU-1-UPDATE", "type": "product", "categorySystemId": "meylikh_2_id", "previewLink": "https://oriontech.ru/upload/iblock/541/541d7aeaa46a115b3c922572fdbcc275.jpg"}]}

# JSON'ы для работы с товарами (удаление)
DELETE_ONE_PRODUCT_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-19"}]}
DELETE_SEVERAL_PRODUCTS_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-10"}, {"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-17"}]}
DELETE_ONE_NOT_ISSET_PRODUCT_JSON = {"items": [{"productSystemId": "not-isset-product-guid"}]}
DELETE_SEVERAL_PRODUCTS_ONE_PRODUCT_NOT_ISSET_JSON = {"items": [{"productSystemId": "7781c7c7-4281-40ab-bf6e-146c78f94a76-7"}, {"productSystemId": "not-isset-product-guid-for-several"}]}

# JSON'ы для получения всех товаров
GET_ALL_PRODUCTS = {"items": [{"companyId": "meylikh"}]}

