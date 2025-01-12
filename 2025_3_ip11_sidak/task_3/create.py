from element import Element
from customer import Customer
import random


class Create(Element):

    def __init__(self, delay):
        super().__init__(delay=delay)
        self.tnext = 0.0
        self.failures = 0

    def out_act(self):
        super().out_act()
        self.tnext = self.tcurr + self.get_delay()
        customer = Customer(self.tcurr)
        route1, route2 = self.routes
        if route1.element.queue + route2.element.queue == route1.element.max_queue + route2.element.max_queue:
            self.failures += 1
        else:
            if route1.element.queue == route2.element.queue:
                next_element = random.choice([route1.element, route2.element])
            else:
                next_element = route1.element if route1.element.queue < route2.element.queue else route2.element

            next_element.in_act(customer)
