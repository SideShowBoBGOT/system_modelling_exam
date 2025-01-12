from create import Create
from model import Model
from process import Process
from dispose import Dispose


c1 = Create(delay_mean=5, name='CREATOR', distribution='exp')
p1 = Process(max_queue=0, delay_mean=5, distribution='exp')
p2 = Process(max_queue=5, delay_mean=5, distribution='exp', n_channel=2)
d1 = Dispose(name='DISPOSE')

c1.next_element = [p1]
p1.next_element = [p2]
p2.next_element = [p1, d1]
p2.probability = [0.05, 0.95]

elements = [c1, p1, p2]
model = Model(elements)
model.simulate(1000)

