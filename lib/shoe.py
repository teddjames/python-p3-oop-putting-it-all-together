class Shoe:
    def __init__(self, brand, size):
        # store brand directly
        self.brand = brand

        # set up a backing attribute for size, then call the setter
        self._size = None
        self.size = size

        # condition will be assigned when cobble() is called
        self.condition = None

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            # exactly matches test expectation
            print("size must be an integer")
        else:
            self._size = value

    def cobble(self):
        # set condition to 'New' and announce repair
        self.condition = "New"
        # match test's expected output exactly
        print("Your shoe is as good as new!")
