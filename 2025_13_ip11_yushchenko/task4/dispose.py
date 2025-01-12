import numpy as np
from element import Element

class Dispose(Element):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.t_next = [np.inf]
        self.delta_t_finished = 0
        self.type_cnt = 0

    def in_act(self, t_start):
        self.delta_t_finished += self.t_curr - t_start
        self.type_cnt += 1
        # виконуємо збільшення лічильника кількості
        super().out_act()