class Goodness(object):
    def __init__(self, value='Hello world!'):
        """
            Initialize Goodness object.
            :param str value: text to output in do() method
        """
        self._value = value

    def make_it(self):
        """
           Prints some text to the console.
        """
        print(self._value)
        return False
