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
        self.needFields = [t.VOLUME_DIFF_INSTITUTE_ACT, t.S_MFD_INFLOW_CLOSEVOLUME]

    def factor_definition(self):
        """
        收集派发指标
        :return:
        """
        s = time.time()
        needData = self.needData

        a = needData[t.VOLUME_DIFF_INSTITUTE_ACT]
        b = needData[t.S_MFD_INFLOW_CLOSEVOLUME]

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