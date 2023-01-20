class StepsConfiguration:
    users_filename = None
    friends_filename = None
    tweets_filename = None
    summarize_filename = None
    train_data_filename = None
    result_filename = None

    def __init__(
            self,
            users_filename='./data/users.txt',
            friends_filename='./data/friends.txt',
            tweets_filename='./data/tweets.txt',
            summarize_filename='./data/summarize.txt',
            train_data_filename='./data/train_data.csv',
            result_filename='./data/result.txt'):
        self.users_filename = users_filename
        self.friends_filename = friends_filename
        self.tweets_filename = tweets_filename
        self.summarize_filename = summarize_filename
        self.train_data_filename = train_data_filename
        self.result_filename = result_filename
