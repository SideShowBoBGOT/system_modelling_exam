from create import Create
from model import Model
from process import Process
from route import Route

c = Create(2)
p1 = Process(9)
p2 = Process(9)
p3 = Process(9)
p4 = Process(9)
p5 = Process(9)

c.set_route_choice("priority")

c.set_routes([Route(p1, 1), Route(p2, 1), Route(p3, 1), Route(p4, 1), Route(p5, 1)])

c.set_name('Прибуття клієнтів')
p1.set_name('Касир 1')
p2.set_name('Касир 2')
p3.set_name('Касир 3')
p4.set_name('Касир 4')
p5.set_name('Касир 5')

c.set_distribution('exp')
p1.set_distribution('exp')
p2.set_distribution('exp')
p3.set_distribution('exp')
p4.set_distribution('exp')
p5.set_distribution('exp')

elements = [c, p1, p2, p3, p4, p5]

model = Model(elements)
model.simulate(1000)
