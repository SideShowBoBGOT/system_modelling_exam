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
                if e.get_tnext() < self.tnext:
                    self.tnext = e.get_tnext()
                    self.event = index

            print(f'\nIt\'s time for event in {self.list[self.event].get_name()}, time = {self.tnext}')
            for e in self.list:
                e.do_statistic(self.tnext - self.tcurr)
            self.tcurr = self.tnext
            for e in self.list:
                e.set_tcurr(self.tcurr)
            self.list[self.event].out_act()
            for e in self.list:
                if e.get_tnext() == self.tcurr:
                    e.out_act()
            self.print_info()
        self.print_result()

    def print_info(self):
        for e in self.list:
            e.print_info()

    def print_result(self):
        print('\nResult:')
        for e in self.list:
            e.print_result()
            if isinstance(e, Process):
                print(f'Середня довжина черги = {e.get_mean_queue() / self.tcurr} '
                      f'\nЙмовірність відмови = {e.get_failure() / (e.get_quantity() + e.get_failure())}'
                      f'\nСереднє навантаження = {e.r_aver / self.tcurr}')
            print()
        print(f'Середня кількість клієнтів = '
              f'{(self.list[1].aver_customers + self.list[2].aver_customers) / self.tcurr}')
        print(f'Середній інтервал часу між від\'їздами клієнтів від вікон = '
              f'{self.tcurr / (self.list[1].get_quantity() + self.list[2].get_quantity())}')
        print(f'Середній час перебування клієнта в банку = '
              f'{(self.list[1].procs[0].customer_presence_time + self.list[2].procs[0].customer_presence_time) / (self.list[1].get_quantity() + self.list[2].get_quantity())}')
        overall_failures = self.list[1].get_failure()
        print(f'Середнє число клієнтів у кожній черзі = '
              f'{overall_failures / (self.list[1].get_quantity()+self.list[2].get_quantity()+overall_failures) * 100}%')

