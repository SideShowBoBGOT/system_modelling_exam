from Lab_3.fun_rand import generate_exponential, generate_normal, generate_uniform
from random import choices


class Element:
    next_id = 0

    def __init__(self, name_of_element='anonymous', delay=1.0):
        self.name = name_of_element
        self.tnext = 0.0
        self.delay_mean = delay
        self.distribution = 'exp'
        self.tcurr = self.tnext
        self.state = 0
        self.id_ = Element.next_id
        Element.next_id += 1
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
            delay = generate_exponential(self.delay_mean)
        elif self.distribution.lower() == 'generate_normal':
            delay = generate_normal(self.delay_mean, self.delay_dev)
        elif self.distribution.lower() == 'generate_uniform':
            delay = generate_uniform(self.delay_mean, self.delay_dev)
        return delay

    def get_next_element(self):
        if self.route_choice is None:
            return None

        if self.route_choice == 'probability':
            return choices([route.element for route in self.routes], [route.p for route in self.routes])[0]

        elif self.route_choice == 'priority':
            routes_by_queue = sorted(self.routes, key=lambda r: r.element.queue)
            return routes_by_queue[0].element

        raise ValueError('Make sure that either "probability" or "priority" is set as the route choice')

    def in_act(self, customer):
        pass

    def out_act(self):
        self.quantity += 1
        if self.customer:
            self.customer_presence_time += (self.tcurr - self.customer.enter_time)

    def set_tcurr(self, tcurr):
        self.tcurr = tcurr

    def print_result(self):
        print(f'{self.name} quantity = {self.quantity}')

    def print_info(self):
        print(f'{self.name} state = {self.state} quantity = {self.quantity} tnext = {self.tnext}')

    def do_statistic(self, delta):
        pass
