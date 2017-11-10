import os
import numpy


def ascii_hist(data):
    values, bins = numpy.histogram(data)
    rows, columns = os.popen('stty size', 'r').read().split()
    hist_width = min(columns, 80)
    unit = max(values) // hist_width

    for v, (start, end) in zip(values, zip(bins[:-1], bins[1:])):
        n = int(v // unit)
        print('{:10.4f} - {:10.4f}: {} {}'.format(start, end, '|' * n + ' ' * (hist_width - n), v))
