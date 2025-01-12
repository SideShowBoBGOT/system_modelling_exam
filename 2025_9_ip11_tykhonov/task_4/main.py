from create import Create
from model import Model
from process import Process
from route import Route

c = Create(0.5)
p1 = Process(1.8, num_procs=1)
p2 = Process(1.8, num_procs=3)
p3 = Process(1.8, num_procs=6)

c.set_route_choice("probability")
p1.set_route_choice("probability")
p2.set_route_choice("probability")
p3.set_route_choice("probability")

c.set_routes([Route(p1, 0.8), Route(p2, 0.8)])
p1.set_routes([Route(p3, 1)])
p2.set_routes([Route(p3, 1)])
p3.set_routes([Route(p1, 0.05), Route(None, 0.95)])

p1.set_max_queue(float('inf'))
p2.set_max_queue(0)
p3.set_max_queue(10)

c.set_name('Прибуття елементів')
p1.set_name('СМО 1')
p2.set_name('СМО 2')
p3.set_name('СМО 3')

c.set_distribution('exp')
p1.set_distribution('exp')
p2.set_distribution('exp')
p3.set_distribution('exp')

elements = [c, p1, p2, p3]

model = Model(elements)
model.simulate(1000)
