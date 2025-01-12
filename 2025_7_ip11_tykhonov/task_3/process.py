import sys
from element import Element


class Process(Element):

    def __init__(self, delay, num_procs=1):
        super().__init__(delay=delay)
        self.procs = [Element(delay=delay) for _ in range(num_procs)]
        for process in self.procs:
            process.set_tnext(float('inf'))
        self.queue = 0
        self.max_queue = sys.maxsize
        self.mean_queue = 0.0
        self.tnext = float('inf')
        self.failure = 0
        self.r_aver = 0
        self.aver_customers = 0

    def in_act(self, customer):
        all_busy = True
        for process in self.procs:
            if process.get_state() == 0:
                all_busy = False
                process.set_state(1)
                process.set_tnext(self.get_tcurr() + self.get_delay())
                process.set_customer(customer)
                break
        if all_busy:
            if self.queue < self.max_queue:
                self.queue += 1
            else:
                self.failure += 1
        else:
            self.tnext = min(process.get_tnext() for process in self.procs)

    def out_act(self):
        for process in self.procs:
            if self.get_tcurr() >= process.get_tnext():
                super().out_act()
                process.out_act()
                process.set_tnext(float('inf'))
                process.set_state(0)

                if self.queue > 0:
                    self.queue -= 1
                    process.set_state(1)
                    process.set_tnext(self.get_tcurr() + self.get_delay())
                self.tnext = min(process.get_tnext() for process in self.procs)
                next_route = super().get_next_element()
                if next_route:
                    next_route.in_act()

    def has_free_procs(self):
        return any(process.get_state() == 0 for process in self.procs)

    def get_failure(self):
        return self.failure

    def get_queue(self):
        return self.queue

    def set_queue(self, queue):
        self.queue = queue

    def get_max_queue(self):
        return self.max_queue

    def set_max_queue(self, max_queue):
        self.max_queue = max_queue

    def print_info(self):
        for process in self.procs:
            process.print_info()
        print(f'failure = {self.failure}, queue = {self.queue}')

    def do_statistic(self, delta):
        self.mean_queue += self.queue * delta
        self.r_aver += delta * self.procs[0].get_state()
        self.aver_customers += delta * (self.procs[0].get_state() + self.queue)

    def get_mean_queue(self):
        return self.mean_queue

    def set_tcurr(self, tcurr):
        self.tcurr = tcurr
        for process in self.procs:
            process.set_tcurr(tcurr)
