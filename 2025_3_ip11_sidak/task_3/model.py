from process import Process


class Model:

    def __init__(self, elements):
        self.list = elements
        self.tnext = 0.0
        self.event = 0
        self.tcurr = self.tnext
        self.queue_changes = 0

    def simulate(self, time):
        while self.tcurr < time:
            self.tnext = float('inf')
            for index, e in enumerate(self.list):
                if e.tnext < self.tnext:
                    self.tnext = e.tnext
                    self.event = index

            for e in self.list:
                e.do_statistic(self.tnext - self.tcurr)
            self.tcurr = self.tnext
            for e in self.list:
                e.set_tcurr(self.tcurr)
            self.list[self.event].out_act()
            for e in self.list:
                if e.tnext == self.tcurr:
                    e.out_act()
            self.check_queue_change()
        self.print_result()

    def check_queue_change(self):
        if self.list[1].queue - self.list[2].queue >= 2:
            self.list[1].queue -= 1
            self.list[2].queue += 1
            self.queue_changes += 1
        elif self.list[2].queue - self.list[1].queue >= 2:
            self.list[2].queue -= 1
            self.list[1].queue += 1
            self.queue_changes += 1

    def print_info(self):
        for e in self.list:
            e.print_info()

    def print_result(self):
        print('\n-------------RESULTS-------------')
        for e in self.list:
            e.print_result()
            if isinstance(e, Process):
                print(f'\taverage load = {e.average_load / self.tcurr}')
            print()

        print(f'lost customers percentage = {self.list[0].failures / self.list[0].quantity}')
        print(f'average customer time in bank = '
              f'{(self.list[1].devices[0].customer_presence_time + self.list[2].devices[0].customer_presence_time) / (self.list[1].quantity + self.list[2].quantity)}')
