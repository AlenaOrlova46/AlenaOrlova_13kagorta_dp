import configuration
import data
import requests
#Создание  заказа
def post_new_order(body_order):
    return requests.post(configuration.URL_SERVICE + configuration.CREATING_ORDER,
                         json=body_order,
                         headers=data.headers)

#Получение заказа по треку
def get_order(track):
    return requests.get(configuration.URL_SERVICE + configuration.RECEIVE_ORDER,
                         params={"t":track},
                         headers=data.headers)
