# ------ #
# Graphs #
# ------ #


class MarineAnimalNode(object):
    """Node in a graph representing a marine animal."""

    def __init__(self, name, prey=None):
        """Create a marine animal node with prey"""

        prey = prey or set()

        assert isinstance(prey, set), \
            "prey must be a set!"

        self.name = name
        self.prey = set(prey)

    def __repr__(self):
        """Debugging-friendly representation"""

        return "<MarineAnimalNode: %s>" % self.name

    def add_prey(self, prey):
        """ Add prey for animal

        >>> krill = MarineAnimalNode('krill')
        >>> squid = MarineAnimalNode('squid', set([krill]))
        >>> seal = MarineAnimalNode('seal', set(['squid']))
        >>> penguin = MarineAnimalNode('penguin', set(['tuna']))
        >>> seal.add_prey(penguin)
        >>> penguin in seal.prey
        True

        """
        # TODO: Complete this method

        pass


class MarineFoodChainGraph(object):
    """Graph holding marine animals and their predator/prey relationships."""

    def __init__(self):
        """Create an empty graph"""

        self.nodes = set()

    def __repr__(self):
        return "<MarineFoodChainGraph: %s>" % [n.name for n in self.nodes]

    def add_animal(self, animal):
        """Add an animal to our graph"""

        self.nodes.add(animal)

    def add_animals(self, animals):
        """Add animals to our graph"""

        for animal in animals:
            self.nodes.add(animal)

#####################################################################
# END OF ASSIGNMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
