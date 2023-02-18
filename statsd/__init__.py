from __future__ import absolute_import

from .client import StatsClient, TCPStatsClient


Client = StatsClient

VERSION = (4, 0, 0)
__version__ = '.'.join(map(str, VERSION))
__all__ = ['StatsClient', 'TCPStatsClient', 'Client']
