# Simple little program that runs for a while and then dies.
# Reports statistics about how long the process has been running, and how long until it dies
#
# This is to test the ability for Kubernetes to schedule services during upgrades. If the time-to-live
# is less than zero, the pod was not able to be killed. 

from prometheus_client.core import GaugeMetricFamily, CounterMetricFamily, REGISTRY
from prometheus_client import start_http_server

import time
import math

RUN_MINUTES = 10
RUN_SECONDS = RUN_MINUTES * 60

startup_time = time.time()
die_time = math.floor(startup_time + RUN_SECONDS)

class UptimeCollector(object):
    def collect(self):
        now = time.time()
        yield CounterMetricFamily('process_uptime', 'Seconds since the process starterd', value=now - startup_time)
        yield GaugeMetricFamily('process_remaining_time', 'Seconds until the process should die', value=die_time - now)

REGISTRY.register(UptimeCollector())

if __name__ == "__main__":
    start_http_server(8000)
    # Sleep until we die
    time.sleep(RUN_SECONDS)
