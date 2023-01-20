import pickle

from steps.StepsConfiguration import StepsConfiguration
from twitter.TwitterClient import TwitterClient
from twitter.TwitterConfiguration import TwitterConfiguration


class StepOne:
    __twitter_client = None
    __steps_configuration = None

    def __init__(self, steps_configuration: StepsConfiguration, twitter_configuration: TwitterConfiguration):
        self.__twitter_client = TwitterClient(twitter_configuration)
        self.__steps_configuration = steps_configuration

    def run(self, query, users_count, friends_count, tweets_count):
        users = self.__collect_users(query, users_count)
        friends = self.__collect_friends(users, friends_count)
        tweets = self.__collect_tweets(users, tweets_count)
        test_data = self.__generate_test_data(tweets)

        self.__summarize(users, friends, test_data)

    def __collect_users(self, query, count):
        users = self.__twitter_client.get_users(query, count)

        users_file = open(self.__steps_configuration.users_filename, 'wb')
        pickle.dump(users, users_file)

        return users

    def __collect_friends(self, users, count):
        friends = self.__twitter_client.get_friends_for_users(users, count)

        friends_file = open(self.__steps_configuration.friends_filename, 'wb')
        pickle.dump(friends, friends_file)

        return friends

    def __collect_tweets(self, users, count):
        tweets = self.__twitter_client.get_tweets(users, count)

        tweets_file = open(self.__steps_configuration.tweets_filename, 'wb')
        pickle.dump(tweets, tweets_file)

        return tweets

    def __generate_test_data(self, tweets):
        data = []

        for key, val in tweets.items():
            for tweet in val:
                data.append(tweet['text'])

        return data

    def __summarize(self, users, friends, test_data):
        data = [
            len(TwitterClient.get_user_names(users)) + TwitterClient.get_friends_count_from_users(users, friends),
            len(test_data)
        ]

        summarize_file = open(self.__steps_configuration.summarize_filename, 'wb')
        pickle.dump(data, summarize_file)
