import pickle

import matplotlib.pyplot as plt
import networkx as nx

from steps.StepsConfiguration import StepsConfiguration


class StepTwo:
    __steps_configuration = None
    __graph = None

    def __init__(self, steps_configuration: StepsConfiguration):
        self.__steps_configuration = steps_configuration

    def run(self, network_image_name=None):
        users_file = open(self.__steps_configuration.users_filename, 'rb')
        friends_file = open(self.__steps_configuration.friends_filename, 'rb')

        users = pickle.load(users_file)
        friends = pickle.load(friends_file)

        self.__create_graph(users, friends)

        print('graph created with %s nodes and %s edges' % (len(self.__graph.nodes()), len(self.__graph.edges())))

        if network_image_name is not None:
            self.__print_network(network_image_name)

        clusters = self.__partition()

        nodes_count = 0

        for cluster in clusters:
            nodes_count += cluster.number_of_nodes()

        data = [
            len(clusters),
            nodes_count / len(clusters)
        ]

        summarize_file = open(self.__steps_configuration.summarize_filename, 'ab')
        pickle.dump(data, summarize_file)

    def __create_graph(self, users, friends):
        edges = []
        self.__graph = nx.Graph()

        for user in users:
            self.__graph.add_node(user['id'])

            unique_friend_ids = set(friends[user['screen_name']]['ids'])

            for friend_id in unique_friend_ids:
                edges.append((user['id'], friend_id))

        self.__graph.add_edges_from(edges)

    def __print_network(self, network_image_name):
        plt.figure(figsize=(50, 50))

        nx.draw_networkx(
            self.__graph,
            node_color='r',
            labels={node: node for node in self.__graph.nodes()},
            width=.1,
            node_size=100)

        plt.axis("off")
        plt.savefig(network_image_name)

    def __partition(self):
        data = []
        initial_graph = self.__graph.copy()

        betweenness_centrality = nx.betweenness_centrality(self.__graph)
        betweenness_centrality_items = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)
        components = [component for component in nx.connected_component_subgraphs(initial_graph)]

        while len(components) == 1:
            initial_graph.remove_edge(*betweenness_centrality_items[0][0])
            del betweenness_centrality_items[0]
            components = [component for component in nx.connected_component_subgraphs(initial_graph)]

        for component in components:
            data.append(component)

        return data
