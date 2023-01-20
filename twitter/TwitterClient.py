import sys
import time
from TwitterAPI import TwitterAPI

from twitter import TwitterConfiguration


class TwitterClient:
    __client = None

    def __init__(self, twitter_configuration: TwitterConfiguration):
        self.__client = TwitterAPI(
            twitter_configuration.consumer_key,
            twitter_configuration.consumer_secret,
            twitter_configuration.access_token_key,
            twitter_configuration.access_token_secret)

    def __request(self, resource, params, max_tries=3):
        for i in range(max_tries):
            request = self.__client.request(resource, params)

            if request.status_code == 200:
                return request

            print('[Error] %s \nsleeping for 15 minutes.' % request.text)

            sys.stderr.flush()
            time.sleep(60 * 16)

    def get_users(self, query, count):
        params = {
            'q': query,
            'count': count
        }

        return self.__request('users/search', params).json()

    def get_friends_for_users(self, users, count):
        data = {}
        user_names = self.get_user_names(users)

        for user_name in user_names:
            params = {
                'screen_name': user_name,
                'count': count
            }

            data[user_name] = self.__request('friends/ids', params).json()

        return data

    def get_tweets(self, users, count):
        data = {}
        user_names = self.get_user_names(users)

        for user_name in user_names:
            params = {
                'screen_name': user_name,
                'count': count,
                'lang': 'en'
            }

            data[user_name] = self.__request('statuses/user_timeline', params).json()

        return data

    @staticmethod
    def get_friends_count_from_users(users, friends):
        count = 0

        for user in users:
            user_name = user['screen_name']
            count += len(friends[user_name]['ids'])

        return count

    @staticmethod
    def get_user_names(users):
        return [user['screen_name'] for user in users]
