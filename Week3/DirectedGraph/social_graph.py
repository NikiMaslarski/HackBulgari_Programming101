import requests
from directed_graph import DirectedGraph


class SocialGraph:
    TOKEN = ('a0d25d1910f504538664c88fb46de2063a7d2b5d', '')
    DEPTH = 3

    def __add_followers(self, user, user_followers):
        for person in user_followers:
            self.social_tree.add_edge(user, person["login"])

    def __add_depth(self, user_followers):
        subusers
        for i in range(SocialGraph.DEPTH):


    def __init__(self, user):
        user_followers = requests.get("https://api.github.com/users/{}/followers"
                                      .format(user),
                                      auth=SocialGraph.TOKEN)

        self.social_tree = DirectedGraph()
        self.__add_followers(user, user_followers.json())

    def print_social_graph(self):
        print(self.social_tree)
