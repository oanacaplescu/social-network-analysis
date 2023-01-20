import pickle
import time

import pandas as pd
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer

from steps.StepsConfiguration import StepsConfiguration
from twitter.TwitterClient import TwitterClient


class StepThree:
    __steps_configuration = None

    def __init__(self, steps_configuration: StepsConfiguration):
        self.__steps_configuration = steps_configuration

    def compare_kernels(self):
        test_data = self.__generate_test_data()

        print("Results for SVC(kernel=rbf)")
        self.__train_data(test_data, 'rbf')

        print("Results for SVC(kernel=linear)")
        self.__train_data(test_data, 'linear')

        print("Results for SVC(kernel=poly)")
        self.__train_data(test_data, 'poly')

    def run(self, svc_kernel):
        test_data = self.__generate_test_data()
        prediction = self.__train_data(test_data, svc_kernel)

        pos = neg = 0

        for rating in prediction:
            if rating == 4:
                pos += 1
            else:
                neg += 1

        list_of_summarize = [
            pos,
            neg,
            prediction[0],
            test_data[0]
        ]

        summarize_file = open(self.__steps_configuration.summarize_filename, 'ab')
        pickle.dump(list_of_summarize, summarize_file)

    def __generate_test_data(self):
        users_file = open(self.__steps_configuration.users_filename, 'rb')
        tweets_file = open(self.__steps_configuration.tweets_filename, 'rb')

        users = pickle.load(users_file)
        tweets = pickle.load(tweets_file)

        user_names = TwitterClient.get_user_names(users)

        test_data = []

        for user_name in user_names:
            for tweet in tweets[user_name]:
                test_data.append(tweet['text'])

        return test_data

    def __train_data(self, test_data, svc_kernel):
        train_data_file = pd.read_csv(self.__steps_configuration.train_data_filename, encoding='utf8')
        train_data_labels = train_data_file['polarity'].tolist()
        train_data = train_data_file['text'].tolist()

        # Create feature vectors
        vectorizer = TfidfVectorizer(min_df=5, max_df=0.8, sublinear_tf=True, use_idf=True)
        train_vectors = vectorizer.fit_transform(train_data)
        test_vectors = vectorizer.transform(test_data)

        # Perform classification with SVM
        classifier = svm.SVC(kernel=svc_kernel)

        t0 = time.time()
        classifier.fit(train_vectors, train_data_labels)
        t1 = time.time()

        t2 = time.time()
        prediction = classifier.predict(test_vectors)
        t3 = time.time()

        time_train = t1 - t0
        time_predict = t3 - t2

        print("Training time: %fs\nPrediction time: %fs" % (time_train, time_predict))

        return prediction
