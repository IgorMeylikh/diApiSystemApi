SERVICE_URL = 'http://esb:8052/'
REQUETS_ID = ''
SENDER_SYSTEM = 'sys0'

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