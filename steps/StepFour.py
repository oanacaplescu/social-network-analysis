import pickle

from steps.StepsConfiguration import StepsConfiguration


class StepFour:
    __steps_configuration = None

    def __init__(self, steps_configuration: StepsConfiguration):
        self.__steps_configuration = steps_configuration

    def run(self):
        summarize_file = open(self.__steps_configuration.summarize_filename, 'rb')
        result_file = open(self.__steps_configuration.result_filename, 'w')

        step_one = pickle.load(summarize_file)
        result_file.write('Number of users collected: ' + str(step_one[0]) + '\n')
        result_file.write('Number of messages collected: ' + str(step_one[1]) + '\n\n')

        step_two = pickle.load(summarize_file)
        result_file.write('Number of communities discovered: ' + str(step_two[0]) + '\n')
        result_file.write('Average number of users per community: ' + str(step_two[1]) + '\n\n')

        step_three = pickle.load(summarize_file)
        result_file.write('Number of instances per class found:' + '\n')
        result_file.write('\tPositive: ' + str(step_three[0]) + '\n')
        result_file.write('\tNegative: ' + str(step_three[1]) + '\n\n')

        result_file.write('One example from each class: ' + '\n')
        if step_three[2] == 4:
            result_file.write('\tResult is Positive' + '\n')
        else:
            result_file.write('\tResult is Negative' + '\n')

        result_file.write('\nMessage: ' + str(step_three[3]))
