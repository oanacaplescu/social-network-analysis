from steps.StepFour import StepFour
from steps.StepOne import StepOne
from steps.StepThree import StepThree
from steps.StepTwo import StepTwo
from steps.StepsConfiguration import StepsConfiguration
from twitter.TwitterConfiguration import TwitterConfiguration

#
# Install python >= 3.6.4 https://www.python.org/downloads/
#
#
# pip install TwitterAPI
# pip install networkx
# pip install matplotlib
# pip install sklearn
# pip install scipy
# pip install pandas
#

consumer_key = 'Da9hXZDo6tXY5t93CTbnyvg5w'
consumer_secret = 'ISTWBnXSTL4ASPDTKxlMuyBG6CuAdqEJALPQmeupRV2z05vYGO'
access_token_key = '868061820-hPkiWuw97QMrp1BhhfIG3truNcZoLcsXtZmqD4xV'
access_token_secret = 'n9O5EgHsf3fVuMCz0NUk6oEvCwZLcza4gSxGr4A1cMVau'

query = 'Coffee'
users_count = 15
friends_count = 150  # max-5000
tweets_count = 300  # max-3200
network_image_name = 'network.png'
svc_kernel = 'linear'  # linear | rbf | poly


def main():
    twitter_configuration = TwitterConfiguration(consumer_key, consumer_secret, access_token_key, access_token_secret)
    steps_configuration = StepsConfiguration()

    print('\n[BEGIN]\tSTEP ONE')
    step_one = StepOne(steps_configuration, twitter_configuration)
    step_one.run(query, users_count, friends_count, tweets_count)
    print('[END]\tSTEP ONE\n')

    print('[BEGIN]\tSTEP TWO')
    step_two = StepTwo(steps_configuration)
    step_two.run(network_image_name)
    print('[END]\tSTEP TWO\n')

    print('[BEGIN]\tSTEP THREE')
    step_three = StepThree(steps_configuration)
    step_three.run(svc_kernel)
    step_three.compare_kernels()
    print('[END]\tSTEP THREE\n')

    print('[BEGIN]\tSTEP FOUR')
    step_four = StepFour(steps_configuration)
    step_four.run()
    print('[END]\tSTEP FOUR\n')


if __name__ == '__main__':
    main()
