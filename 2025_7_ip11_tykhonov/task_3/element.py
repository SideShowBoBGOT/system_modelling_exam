from fun_rand import exp, norm, unif
from random import choices


class Element:
    nextId = 0

    def __init__(self, name_of_element='anonymous', delay=1.0):
        self.name = name_of_element
        self.tnext = 0.0
        self.delay_mean = delay
        self.distribution = 'exp'
        self.tcurr = self.tnext
        self.state = 0
        self.id_ = Element.nextId
        Element.nextId += 1
        self.name = 'element' + str(self.id_)
        self.delay_dev = 0.0
        self.quantity = 0
        self.route_choice = None
        self.routes = None
        self.customer = None
        self.customer_presence_time = 0


    def get_delay(self):
        delay = self.delay_mean
        if self.distribution.lower() == 'exp':
            delay = exp(self.delay_mean)
        elif self.distribution.lower() == 'norm':
            delay = norm(self.delay_mean, self.delay_dev)
        elif self.distribution.lower() == 'unif':
            delay = unif(self.delay_mean, self.delay_dev)
        return delay

    def get_delay_dev(self):
        return self.delay_dev

    def set_delay_dev(self, delay_dev):
        self.delay_dev = delay_dev

    def get_distribution(self):
        return self.distribution

    def set_distribution(self, distribution):
        self.distribution = distribution

    def get_quantity(self):
        return self.quantity

    def get_tcurr(self):
        return self.tcurr

    def set_tcurr(self, tcurr):
        self.tcurr = tcurr

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def set_route_choice(self, route_choice):
        self.route_choice = route_choice

    def set_routes(self, routes):
        self.routes = routes

    def get_next_element(self):
        if self.route_choice is None:
            return None
        if self.route_choice == "priority":
            routes_by_queue = sorted(self.routes, key=lambda r: r.element.get_queue())
            return routes_by_queue[0].element

        elif self.route_choice == "probability":
            return choices([route.element for route in self.routes], [route.port_terminal for route in self.routes])[0]

        raise ValueError(f"Incorrect route_choice value. Must be 'priority' or 'probability', got {self.route_choice} "
                         f"instead.")

    def in_act(self):
        pass

    def out_act(self):
        self.quantity += 1
        if self.customer:
            self.customer_presence_time += (self.tcurr - self.customer.enter_time)

    def get_tnext(self):
        return self.tnext

    def set_tnext(self, tnext):
        self.tnext = tnext

    def get_delay_mean(self):
        return self.delay_mean

    def set_delay_mean(self, delay_mean):
        self.delay_mean = delay_mean

    def get_id(self):
        return self.id_

    def set_id(self, id_):
        self.id_ = id_

    def print_result(self):
        print(f'{self.name} quantity = {self.quantity}')

    def print_info(self):
        print(f'{self.name} state = {self.state} quantity = {self.quantity} tnext = {self.tnext}')

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def do_statistic(self, delta):
        pass

    def get_customer(self):
        return self.customer

    def set_customer(self, customer):
        self.customer = customer

