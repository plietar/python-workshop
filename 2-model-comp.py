import matplotlib.pyplot as plt

def params(**kwds):
  P = {} # initialize empty dict
  P['pop_size'] = 1000
  P['inf_init'] = 10
  P['eff_rate'] = 3.0 * 0.1
  P['inf_dur']  = 7.0
  P['t_max']    = 100
  P.update(**kwds) # overwrite defaults
  return P # don't forget to return!

def solve(P):
  # initial conditions
  S = P['pop_size'] - P['inf_init']
  I = P['inf_init']
  R = 0
  N = S+I+R # = P['pop_size']
  X = {k:[] for k in 'tSIR'} # initialize output
  tvec = range(P['t_max'])   # integer steps
  for t in tvec:
    # modify S,I,R directly
    S += -P['eff_rate']*S*I/N
    I += +P['eff_rate']*S*I/N -1/P['inf_dur']*I
    R +=                      +1/P['inf_dur']*I
    # log state
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

# main
P = params()
X = solve(P)
plot(X)
