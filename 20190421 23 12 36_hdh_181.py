# coding=utf8
__author__ = 'HanDonghao'

import time
import math
import numpy as np
import pandas as pd
from FactorModule.FactorBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t


class Factor(FactorBase):


    def __init__(self):
        super(Factor, self).__init__()
        self.neutral = True
        self.factorName = __name__.split('.')[-1]
        self.needFields = [t.SELL_TRADES_EXLARGE_ORDER, t.BUY_VALUE_SMALL_ORDER]

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData

        a = needData[t.SELL_TRADES_EXLARGE_ORDER]
        b = needData[t.BUY_VALUE_SMALL_ORDER]
        rank_b = self.calculator.Rank(b)

        factor = -1*self.calculator.Corr(a, rank_b, num=10)
        '''逻辑参考<利用交易型 alpha 捕获低频模型短期收益>,其通过股票市场短期内的趋势、反转以
        及价量相关性等特征获取超额收益。方法是刷表'''

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()