"""
This script generates three sets of plots:
    1. Cross-decoding performance (CDP)
    2. Weight comparison (WCp)
    3. CDP vs WCp to mean of target
        - For individual shuffles
"""

import os
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_color_codes("dark")
import pandas as pd
import numpy as np
import sys
sys.path.append('.')

import logging
logger = logging.getLogger('vis_debug')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler('spam.log')
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)

from spikelearn.data import SHORTCUTS, io, select
from spikelearn.visuals.visuals import to_video

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler((-1,1))

from itertools import product

# Data parameters
DSETS = ['medium_smoothed', 'medium_smoothed_norm',
         'narrow_smoothed', 'narrow_smoothed_norm',
         'wide_smoothed']

TMIN = 1.5
WSIZE = 50

loaddir = 'data/results/across_trials/cross_decoding/'

pred_filename = lambda label, dset: '{}/{}_cross_pred.csv'.format(label).format(loaddir+dset, label)
weight_filename = lambda label, dset: '{}/{}_cross_weight.csv'.format(label).format(loaddir+dset, label)
stats_filename = lambda label, dset: '{}/{}_cross_stats.csv'.format(label).format(loaddir+dset, label)
# Saving parameters
fsavedir = lambda label, dset : 'reports/figures/across_trials/similarity/{}/{}'.format(dset, label)

# Identifier variables
id_vars = ['logC', 'penalty']
id_combs = lambda df: product(weights.unique(df[id_]) for id_ in id_vars)

for label, dset in product(SHORTCUTS['groups']['DRRD'], DSETS):
    # Load data
    preds = pd.read_csv( pred_filename(label, dset) )
    weights = pd.read_csv( weight_filename(label, dset) )
    stats = pd.read_csv( stats_filename(label, dset) )

    # 1. Cross-decoding performance
    img_order = []
    ids =  weights.drop_duplicates(subset=id_vars)[id_vars]
    for id_ in map(tuple, ids.values):
        logger.info('CDP with ids %s'%id_)

    # 2. Weight comparison



    # 3. CDP vs WCp
