import seaborn as sb

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
  X = {k:[] for k in 'SIR'}
  for t in range(P['t_max']):
    S += -P['eff_rate']*S*I/N
    I += +P['eff_rate']*S*I/N -1/P['inf_dur']*I
    R +=                      +1/P['inf_dur']*I
    X['S'].append(S)
    X['I'].append(I)
    X['R'].append(R)
  return(X)

def plot(X):
  h = sb.relplot(X,kind='line')
  h.savefig('pyplots.pdf')

P = params()
X = solve(P)
plot(X)
