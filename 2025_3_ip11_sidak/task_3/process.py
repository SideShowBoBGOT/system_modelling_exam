import sys
from element import Element


class Process(Element):

    def __init__(self, delay, num_devices=1):
        super().__init__(delay=delay)
        self.devices = [Element(delay=delay) for _ in range(num_devices)]
        for device in self.devices:
            device.tnext = float('inf')
        self.queue = 0
        self.max_queue = sys.maxsize
        self.mean_queue = 0.0
        self.tnext = float('inf')
        self.failure = 0
        self.average_load = 0
        self.aver_customers = 0

    def in_act(self, customer=None):
        system_busy = True
        for device in self.devices:
            if device.state == 0:
                system_busy = False
                device.state = 1
                device.tnext = self.tcurr + self.get_delay()
                device.customer = customer
                break
        if system_busy:
            if self.queue < self.max_queue:
                self.queue += 1
        else:
            self.tnext = min(device.tnext for device in self.devices)

    def out_act(self):
        for device in self.devices:
            if self.tcurr >= device.tnext:
                super().out_act()
                device.out_act()
                device.tnext = float('inf')
                device.state = 0

                if self.queue > 0:
                    self.queue -= 1
                    device.state = 1
                    device.tnext = self.tcurr + self.get_delay()
                self.tnext = min(device.tnext for device in self.devices)

                next_route = super().get_next_element()
                if next_route:
                    next_route.in_act()

    def is_available(self):
        return any(device.state == 0 for device in self.devices)

    def print_info(self):
        for device in self.devices:
            device.print_info()
        print(f'failure = {self.failure}, queue = {self.queue}')

    def set_tcurr(self, tcurr):
        self.tcurr = tcurr
        for device in self.devices:
            device.tcurr = tcurr

    def do_statistic(self, delta):
        self.mean_queue += self.queue * delta
        self.average_load += delta * self.devices[0].state
        self.aver_customers += delta * (self.devices[0].state + self.queue)
