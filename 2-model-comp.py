import matplotlib.pyplot as plt

def params(**kwds):
  P = {}
  P['pop_size'] = 1000
  P['inf_init'] = 10
  P['eff_rate'] = 3.0 * 0.1
  P['inf_dur']  = 7.0
  P['t_max']    = 100
  P.update(**kwds)
  return P

def solve(P):
  S = P['pop_size'] - P['inf_init']
  I = P['inf_init']
  R = 0
  N = S+I+R
  X = {k:[] for k in 'tSIR'}
  tvec = range(P['t_max'])
  for t in tvec:
    S += -P['eff_rate']*S*I/N
    I += +P['eff_rate']*S*I/N -1/P['inf_dur']*I
    R +=                      +1/P['inf_dur']*I
    X['t'].append(t)
    X['S'].append(S)
    X['I'].append(I)
    X['R'].append(R)
  return X

def plot(X):
  for k in 'SIR':
    plt.plot(X['t'],X[k],label=k)
  plt.xlabel('time (days)')
  plt.ylabel('individuals (count)')
  plt.show()

P = params()
X = solve(P)
plot(X)
