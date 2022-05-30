class Game:
    def __init__(self, title, genre, description, stock_quantity, buying_price, selling_price, developer, id = None):
        self.title = title
        self.genre = genre
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_price = buying_price
        self.selling_price = selling_price
        self.developer = developer
        self.id = id

    def get_mark_up(self):
        return (self.selling_price - self.buying_price)/self.buying_price * 100