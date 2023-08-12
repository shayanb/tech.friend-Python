import requests

class techFriends:
    
    BASE_URL = "https://prod-api.kosetto.com"
    
    DEFAULT_HEADERS = {
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Mobile/14E304 Safari/605.1.15',
        'Accept': '*/*',
        'Accept-Language': 'en-CA,en-US;q=0.7,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://www.friend.tech/',
        'Origin': 'https://www.friend.tech',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'Connection': 'keep-alive'
    }

    @staticmethod
    def check_user(user_id, headers=DEFAULT_HEADERS):
        response = requests.get(f"{techFriends.BASE_URL}/users/{user_id}", headers=headers)
        return response.json()

    @staticmethod
    def get_recently_joined(headers=DEFAULT_HEADERS):
        response = requests.get(f"{techFriends.BASE_URL}/lists/recently-joined", headers=headers)
        return response.json()

    @staticmethod
    def top_by_price(headers=DEFAULT_HEADERS):
        response = requests.get(f"{techFriends.BASE_URL}/lists/top-by-price", headers=headers)
        return response.json()

    @staticmethod
    def most_active(headers=DEFAULT_HEADERS):
        response = requests.get(f"{techFriends.BASE_URL}/lists/most-active-host", headers=headers)
        return response.json()

    @staticmethod
    def global_activity(headers=DEFAULT_HEADERS):
        response = requests.get(f"{techFriends.BASE_URL}/global-activity", headers=headers)
        return response.json()

    @staticmethod
    def chat_rooms(user_id, headers=DEFAULT_HEADERS):
        response = requests.options(f"{techFriends.BASE_URL}/notifications/chatRooms/{user_id}", headers=headers)
        return response.json()

    @staticmethod
    def a_users_token_holders(user_id, headers=DEFAULT_HEADERS):
        response = requests.get(f"{techFriends.BASE_URL}/users/{user_id}/token/holders", headers=headers)
        return response.json()

    @staticmethod
    def a_users_holding_tokens(user_id, headers=DEFAULT_HEADERS):
        response = requests.get(f"{techFriends.BASE_URL}/users/{user_id}/token-holdings", headers=headers)
        return response.json()

    @staticmethod
    def users_trade_activity(user_id, headers=DEFAULT_HEADERS):
        response = requests.get(f"{techFriends.BASE_URL}/users/{user_id}/trade-activity", headers=headers)
        return response.json()

# Usage:
tf = techFriends()
user_data = tf.check_user("0xADDRESS")
recently_joined_data = tf.get_recently_joined()

