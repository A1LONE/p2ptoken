import requests


def create_p2p_merchant_key(token):
    data = {
        "keysPairName": "ваше название токена",
        "serverNotificationsUrl": "адрес для серверных уведомлений"
    }
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer " + token
    }
    response = requests.post("https://edge.qiwi.com/widgets-api/api/p2p/protected/keys/create", headers=headers, json=data)
    if response.status_code == 200:
        print("Ключ создан")
        print(response.json())
    elif response.status_code == 401:
        print("Ключ заблокирован")
    elif response.status_code == 403:
        print("Недостаточно прав")
    else:
        print(response.text)

     
create_p2p_merchant_key('Сюда QIWI API KEY полученый по итогу первого этапа')