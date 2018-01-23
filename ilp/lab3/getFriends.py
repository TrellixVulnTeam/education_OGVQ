import baseClient
import datetime
import requests

class getFriends(baseClient.BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'friends.get'

    id = ""

    def __init__(self, id):
        self.id = id

    def get_params(self):
        return {'user_id':self.id, 'fields':'bdate'}

    def _get_data(self, method, http_method):
        r = None

        r = requests.get(self.generate_url(self.method), params=self.get_params())

        return self.response_handler(r)

    def response_handler(self, response):

        ages = []

        data = response.json()
        if data.get('response'):
            for user in data['response']:
                bd = user.get('bdate')
                if bd:
                    today = datetime.date.today()
                    try:
                        print(datetime.datetime.strptime('17.6.1996', '%d.%m.%Y'))
                        bd = datetime.datetime.strptime(bd, '%d.%m.%Y')
                    except:
                        try:
                            bd = datetime.datetime.strptime(bd, '%m.%Y')
                        except:
                            try:
                                bd = datetime.datetime.strptime(bd, '%Y')
                            except:
                                bd = None
                    if bd:
                        age = today.year - bd.year - ((today.month, today.day) < (bd.month, bd.day))
                        ages.append(age)
        return ages[::-1]
