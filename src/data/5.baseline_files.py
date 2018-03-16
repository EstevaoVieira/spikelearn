import sys
sys.path.append('.')
from spikelearn.data import io, SHORTCUTS

for label in SHORTCUTS['groups']['DRRD']:
    baseline = io.load(label, 'epoched_spikes').baseline.unstack('unit')
    io.save(baseline, label, 'baseline')