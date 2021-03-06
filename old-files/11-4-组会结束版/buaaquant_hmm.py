from hmmlearn.hmm import GaussianHMM
import numpy as np
import pandas as pd
import datetime
from Query import get_data,get_data_normal
from matplotlib import cm,pyplot as plt
import warnings
warnings.filterwarnings("ignore")


def hmm_explict_states(begindate,enddate):
    data = get_data_normal(stock_name='SZ002680', start_date=begindate, end_date=enddate)

    closeindex = data['end']
    volume = np.array(data['amount'][5:]).astype('float')

    max = np.array(data['max']).astype('float')

    min = np.array(data['min']).astype('float')

    deltaindex = np.log(max) - np.log(min)
    deltaindex = deltaindex[5:]

    logReturn1 = np.array(np.diff(np.log(closeindex.astype('float'))))
    logReturn1 = logReturn1[4:]
    logReturn5 = np.log(np.array(closeindex[5:]).astype('float')) - np.log(np.array(closeindex[:-5]).astype('float'))

    closeindex = closeindex[5:]

    x = np.column_stack([logReturn1, logReturn5, deltaindex, volume])
    return x

t = hmm_explict_states(begindate = datetime.datetime(2015, 1, 1),
    enddate = datetime.datetime(2015, 12, 30))
print t
model = GaussianHMM(n_components=5,covariance_type='diag',n_iter=100).fit(t)

begindate=datetime.datetime(2016,1,1)
enddate=datetime.datetime(2016,2,28)
c = hmm_explict_states(begindate, enddate)
hidden_states = model.predict(c)

data = get_data_normal(stock_name='SZ002680', start_date=begindate, end_date=enddate)
tradeDate = pd.to_datetime(data['datetime'][5:])
closeindex = data['end'][5:]
plt.figure(figsize = (15,8))
for i in range(model.n_components):
    idx = (hidden_states == i)
    plt.plot_date(tradeDate[idx],closeindex[idx],'.',label='%dth hidden states'%i,lw=1)
    plt.legend()
    plt.grid(1)
plt.show()