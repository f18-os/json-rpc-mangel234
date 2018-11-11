class node:
    def __init__(self, name, children=[]):
        self.name = name
        self.children = children
        self.val = 0

    def show(self, level=0):
        print("%s%s val=%d:" % (level * "  ", self.name, self.val))
        for c in self.children:
            c.show(level + 1)


def increment(graph):
    graph.val += 1;
    for c in graph.children:
        increment(c)

# Method to turn graph into a dictionary to send over
def listToSend(graph, dictionary={}):
    # Update the dictionary to contain the whole graph
    dictionary.update({str(graph.name): graph.val})
    # make sure we trun the graph into a dictionary to send
    for x in graph.children:
        dictionary = listToSend(x, dictionary)
    return dictionary
