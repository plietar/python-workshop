import random
import matplotlib.pyplot as plt
from dataclasses import dataclass

P_INFECTION = 0.1
P_RECOVERY_YOUNG = 0.02
P_RECOVERY_OLD = 0.01

class Person:
    def __init__(self, state, age):
        self.state = state
        self.age = age

    def update(self, foi):
        if self.state == "S":
            if random.random() < foi * P_INFECTION:
                self.state = "I"

        elif self.state == "I":
            if random.random() < self.recovery_probability:
                self.state = "R"

        elif self.state == "R":
            pass

    @property
    def recovery_probability(self):
        if self.age < 50:
            return P_RECOVERY_YOUNG
        else:
            return P_RECOVERY_OLD

    def __repr__(self):
        return f"Person(state={self.state}, age={self.age})"


@dataclass
class DataPoint:
    S: int
    I: int
    R: int


class Model:
    def __init__(self, size, infected):
        self.population = list()
        self.size = size

        for i in range(infected):
            self.population.append(Person("I", random.uniform(0, 100)))
        for i in range(size - infected):
            self.population.append(Person("S", random.uniform(0, 100)))

    def update(self):
        foi = self.I / self.size

        for p in self.population:
            p.update(foi)

    def run(self, n):
        data = []
        for _ in range(n):
            self.update()
            data.append(DataPoint(self.S, self.I, self.R))

        return data

    @property
    def S(self):
        return self.count("S")

    @property
    def I(self):
        return self.count("I")

    @property
    def R(self):
        return self.count("R")

    def count(self, state):
        return sum([1 for p in self.population if p.state == state])


m = Model(100, 5)
data = m.run(200)

plt.figure()
plt.plot([x.S for x in data], label="S")
plt.plot([x.I for x in data], label="I")
plt.plot([x.R for x in data], label="R")
plt.legend()