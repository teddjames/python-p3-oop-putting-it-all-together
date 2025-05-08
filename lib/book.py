# book.py

class Book:
    def __init__(self, title, page_count):
        # store title normally
        self.title = title
        # initialize a “backing” attribute for page_count,
        # then delegate to the setter to validate/type‐check
        self._page_count = None
        self.page_count = page_count

    @property
    def page_count(self):
        # the getter simply returns the backing attribute
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # validate that the new page count is an integer
        if not isinstance(value, int):
            # if it’s not, print the required error message
            print("page_count must be an integer")
        else:
            # otherwise store it
            self._page_count = value

    def turn_page(self):
        # whenever someone calls this method, print the expected text
        print("Flipping the page...wow, you read fast!")
