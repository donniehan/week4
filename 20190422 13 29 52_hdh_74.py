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
        self.needFields = [t.S_MFD_INFLOW, t.VALUE_DIFF_INSTITUTE]

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData

        a = needData[t.S_MFD_INFLOW]
        b = needData[t.VALUE_DIFF_INSTITUTE]

        signal_1 = self.calculator.Rank(a - b)
        signal_2 = self.calculator.Rank(a + b)

        factor = signal_1 / signal_2
        '''刷表'''

        print('factor {0} done with {1} seconds'.format(self.factorName, time.time() - s))
        return factor

    def run_factor(self):
        self.run()



fct = Factor()
fct.run_factor()