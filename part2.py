from random import random, uniform
from collections import namedtuple

P_INFECTION = 0.2
P_RECOVERY_YOUNG = 0.02
P_RECOVERY_OLD = 0.01

State = namedtuple("State", ["t", "S", "I", "R"])

class Person:
    def __init__(self, state, age):
        self.state = state
        self.age = age

    def update(self, foi):
        if self.state == "S":
            if random() < foi:
                self.state = "I"

        elif self.state == "I":
            if random() < self.recovery_probability():
                self.state = "R"

        elif self.state == "R":
            pass

    def recovery_probability(self):
        if self.age < 50:
            return P_RECOVERY_YOUNG
        else:
            return P_RECOVERY_OLD

    def __repr__(self):
        return f"Person(state={self.state}, age={self.age})"

class Model:
    def __init__(self, size, infected):
        self.population = list()
        self.size = size

        for i in range(infected):
            self.population.append(Person("I", uniform(0, 100)))
        for i in range(size - infected):
            self.population.append(Person("S", uniform(0, 100)))

    def update(self):
        foi = P_INFECTION * sum([1 for p in self.population if p.state == "I"]) / self.size

        for p in self.population:
            p.update(foi)

    def count(self, state):
        return sum([1 for p in self.population if p.state == state])

    def run(self, n):
        data = []
        for t in range(n):
            self.update()
            data.append(State(t, self.count('S'), self.count('I'), self.count('R')))

        return data

m = Model(100, 5)
data = m.run(100)

import matplotlib.pyplot as plt
plt.figure()
plt.plot([x.S for x in data], label="S")
plt.plot([x.I for x in data], label="I")
plt.plot([x.R for x in data], label="R")
plt.legend()
