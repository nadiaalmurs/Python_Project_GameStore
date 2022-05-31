class Developer:
    def __init__(self, name, shipping_price, shipping_time, active = False, id = None):
        self.name = name
        self.shipping_price = shipping_price
        self.shipping_time = shipping_time
        self.active = active
        self.id = id
    
    def mark_active(self):
        self.active = True