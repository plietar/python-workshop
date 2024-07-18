---
theme: solarized
revealOptions:
  transition: none
---

## Introduction to Python
### Jesse Knight & Paul Liétar

---

## Outline

0. slides
1. basic syntax
2. compartmental model
3. individual-based model

---

## When would you want to use Python

![](images/venn.svg)

---

## When would you want to use Python

- Domain-specific ecosystems
    - Machine learning (TensorFlow, PyTorch)
    - Climate modeling
- Building complex applications
- Faster*
- Because people around you do

---

## R vs Python: Notable Differences

Feature               R              Python
--------------------- -------------- ---------------
whitespace            ignored        meaningful
data frames & stats   out-of-box     need package
packages              fussy          easy
operate on language   yes            no
modifying variables   copy-on-modify modify-in-place
variable assignment   `<-` (madness) `=` (sane)

---

## Object oriented programming

- Objects = Data + Behaviour
- Classes are blueprints for creating objects
\pause
```py
class Person():
  def __init__(self,name,age):
    self.name = name
    self.age = age
  def birthday(self):
    self.age += 1
```

---

## General Python Resources

- Python Language Reference:
  [`docs`](https://docs.python.org/3/library)
- Python Package Index:
  [`pypi`](https://pypi.org)

## Task View: Packages

- Vectors & Arrays:
  [`numpy`](https://numpy.org/)
- Dataframes:
  [`pandas`](https://pandas.pydata.org/),
  [`polars`](https://pola.rs/)
- Plotting:
  [`matplotlib`](https://matplotlib.org/),
  [`seaborn`](https://seaborn.pydata.org/)
- Statistics & Algorithms:
  [`scipy`](https://scipy.org)
- Orderly:
  [`outpack-py`](https://github.com/mrc-ide/outpack-py)

## Example Model Code

- Optima HIV:
  [`github`](https://github.com/optimamodel/optima)
- HIV in Eswatini:
  [`github`](https://github.com/mishra-lab/hiv-model-eswatini)
- Toy HIV-like model:
  [`github`](https://github.com/mishra-lab/epa-model-toy)
