import math
import random


def generate_exponential(time_mean):
    a = 0
    while a == 0:
        a = random.random()
    a = -time_mean * math.log(a)
    return a


def generate_uniform(time_min, time_max):
    a = 0
    while a == 0:
        a = random.random()
    a = time_min + a * (time_max - time_min)
    return a


def generate_normal(time_mean, time_deviation):
    a = time_mean + time_deviation * random.gauss()
    return a


def generate_erlang(time_mean, k):
    lambda_ = k / time_mean
    sum_random_values = sum(math.log(random.random()) for _ in range(k))
    return (-1 / lambda_) * sum_random_values
