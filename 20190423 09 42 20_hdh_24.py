# coding=utf8
__author__ = 'HanDonghao'

import time
import math
import numpy as np
import pandas as pd
from FactorModule.FactorBase import FactorBase
from DataReaderModule.Constants import ALIAS_FIELDS as t


class Factor(FactorBase):

    # def __init__(self, not_run=0):
    def __init__(self):
        # print('not_run', not_run)
        # if not_run == 0:
        super(Factor, self).__init__()
        self.neutral = True
        self.factorName = __name__.split('.')[-1]
        self.needFields = [t.NETPCMTTM, t.SELL_TRADES_SMALL_ORDER, t.ADJFCT]  # 设置需要的字段

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData# 计算所需数据

        a = needData[t.NETPCMTTM]
        b = needData[t.SELL_TRADES_SMALL_ORDER]
        c = needData[t.ADJFCT]

        factor = self.calculator.Sum(a-b,num=20)/self.calculator.Sum(b-c,num=20)

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()


fct = Factor()
fct.run_factor()
