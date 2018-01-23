import baseClient
import requests

class getId(baseClient.BaseClient):
    BASE_URL = 'https://api.vk.com/method/'
    method = 'users.get'

    nickname = ""

    def __init__(self, nickname):
        self.nickname = nickname

    def get_params(self):
        return {'user_ids':self.nickname}

    def _get_data(self, method, http_method):
        r = None

        r = requests.get(self.generate_url(self.method), params=self.get_params())

        return self.response_handler(r)

    def response_handler(self, response):

        ids = []

        data = response.json()
        if data.get('response'):
            for user in data['response']:
                ids.append(user.get('uid'))
        else:
            print(data)

        return ids
