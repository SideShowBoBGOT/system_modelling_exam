from element import Element
from customer import Customer


class Create(Element):

    def __init__(self, delay):
        super().__init__(delay=delay)
        super().set_tnext(0.0)

    def out_act(self):
        super().out_act()
        super().set_tnext(super().get_tcurr() + super().get_delay())
        next_element = super().get_next_element()
        if next_element:
            next_element.in_act()

