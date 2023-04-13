from statsmodels.stats.weightstats import ztest
import numpy as np

chat_id = 953761952

def solution(x: np.array) -> bool:
    return ztest(x1=x, value=500, alternative='larger')[1] < 0.1
