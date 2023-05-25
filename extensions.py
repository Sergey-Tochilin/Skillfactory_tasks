import requests
import json
from config import rate_list

class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(base, quote, amount):

        if base.upper() not in rate_list.keys():
            raise APIException(f'Валюта "{base.upper()}" недоступна!')
        if quote.upper() not in rate_list.keys():
            raise APIException(f'Валюта "{quote.upper()}" недоступна!')
        if base.upper() == quote.upper():
            raise APIException(f'Невозможно перевести одинаковые валюты "{base.upper()}" в "{quote.upper()}"!')
        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Количество валюты -"{amount}" должно быть числом!')


        url = f"https://api.apilayer.com/exchangerates_data/convert?to={quote}&from={base}&amount={amount}"
        headers = {"apikey": "7QsR1Ku5NfrmVkJ90Dy1aAeRZHpIA4ic"}

        response = requests.get(url, headers=headers)
        resp = json.loads(response.content)

        result = round(resp['info']['rate'] * amount, 2)  # Возвращает цену за количество
        answer = f'Цена {int(amount)} {base.upper()} в {quote.upper()}: {result}'
        return answer
