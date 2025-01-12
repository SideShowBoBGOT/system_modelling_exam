from create import Create
from model import Model
from process import Process
from route import Route

creator = Create(2.5)
processor1 = Process(1.5)
processor2 = Process(1.5)

creator.route_choice = 'priority'
creator.routes = [Route(processor1), Route(processor2)]

processor1.max_queue = 3
processor2.max_queue = 3

creator.name = 'Clients arrival'
processor1.name = 'Cashier 1'
processor2.name = 'Cashier 2'

creator.distribution = 'exp'
processor1.distribution = 'exp'
processor2.distribution = 'exp'

elements = [creator, processor1, processor2]
model = Model(elements)
model.simulate(1000)
