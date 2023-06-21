
# Configuration information for the simulation of the
# Neutrino schedulers

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0          # Need to set zero when you actually experiment
runTime = 60.000100

# =========================================================
# Hardware Information
# =========================================================
numCores = 1
IPITime = (4e-07, 7e-07, 1e-07, 1e-06)

# the core number to which the clock tick
# interrupt is directed
tickInterval = 1.0E-3           # 1ms
rrTickCore = 0   # tick processing core (only for round robin??)
clockResolution = 1E-7          # 100 ns

# Context switching times (normal distribution (min, median, stdev, max))
StartupTime = (1.2e-05, 1.7e-05, 1e-06, 2.2e-05)
ExitTime = (1.2e-05, 1.7e-05, 1e-06, 2.2e-05)

# SAFE Settings
psResolution = 1.0E-06
swResolution = 1.0E-04
# =========================================================
# APS Parameters
#
# Note that the following APS characteristics are not
# suppported:
# - critical budgets
# - maximum budgets
# - modification of parameters in a running system
# - powering on/off of cores dynamically for power-saving
# =========================================================
windowSize = 0.100
numPartitions = 1
partitionBudgets = [ 1.00 ]
apsPolicy = "default"         # This can be "default", "local" or "ftbr"
apsAlgorithm = "PRACTICAL"
RES = 128
log2RES = 7
rrTicks = 4.0    # round robin interval

# =========================================================
# Thread definition
# =========================================================


threads = [
	{"name":"T1", "offset":0.000000, "priorityHI":25, "priorityLO":25, "period":[0.010000, 0.010000], "duration":[0.000200, 0.000300], "deadline":0.010000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T2", "offset":0.000000, "priorityHI":24, "priorityLO":24, "period":[0.050000, 0.050000], "duration":[0.000500, 0.000600], "deadline":0.050000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T3", "offset":0.000000, "priorityHI":23, "priorityLO":23, "period":[0.100000, 0.100000], "duration":[0.000400, 0.000500], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T4", "offset":0.000000, "priorityHI":22, "priorityLO":22, "period":[0.100000, 0.100000], "duration":[0.000100, 0.000200], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T5", "offset":0.000000, "priorityHI":21, "priorityLO":21, "period":[0.100000, 0.100000], "duration":[0.002000, 0.002100], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T6", "offset":0.000000, "priorityHI":20, "priorityLO":20, "period":[0.100000, 30.000000], "duration":[0.001000, 0.001100], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T7", "offset":0.000000, "priorityHI":19, "priorityLO":19, "period":[0.100000, 30.000000], "duration":[0.002000, 0.002100], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T8", "offset":0.000000, "priorityHI":18, "priorityLO":18, "period":[0.100000, 30.000000], "duration":[0.001000, 0.001100], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T9", "offset":0.000000, "priorityHI":17, "priorityLO":17, "period":[0.100000, 60.000000], "duration":[0.002000, 0.002100], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T10", "offset":0.000000, "priorityHI":16, "priorityLO":16, "period":[0.100000, 60.000000], "duration":[0.002000, 0.002100], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T11", "offset":0.000000, "priorityHI":15, "priorityLO":15, "period":[0.100000, 0.100000], "duration":[0.000500, 0.000600], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T12", "offset":0.000000, "priorityHI":14, "priorityLO":14, "period":[0.100000, 0.100000], "duration":[0.000500, 0.000600], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T13", "offset":0.000000, "priorityHI":13, "priorityLO":13, "period":[0.100000, 0.100000], "duration":[0.000500, 0.000600], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T14", "offset":0.000000, "priorityHI":12, "priorityLO":12, "period":[0.200000, 0.200000], "duration":[0.000300, 0.000400], "deadline":0.100000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T15", "offset":0.000000, "priorityHI":11, "priorityLO":11, "period":[0.250000, 0.250000], "duration":[0.000200, 0.000300], "deadline":0.250000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T16", "offset":0.000000, "priorityHI":10, "priorityLO":10, "period":[0.250000, 0.250000], "duration":[0.015000, 0.015100], "deadline":0.250000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T17", "offset":0.000000, "priorityHI":9, "priorityLO":9, "period":[0.500000, 0.500000], "duration":[0.000500, 0.000600], "deadline":0.500000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T18", "offset":0.000000, "priorityHI":8, "priorityLO":8, "period":[1.000000, 1.000000], "duration":[0.000500, 0.000600], "deadline":1.000000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T19", "offset":0.000000, "priorityHI":7, "priorityLO":7, "period":[1.000000, 1.000000], "duration":[0.001000, 0.001100], "deadline":1.000000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T20", "offset":0.000000, "priorityHI":6, "priorityLO":6, "period":[2.000000, 2.000000], "duration":[0.000500, 0.001100], "deadline":2.000000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T21", "offset":0.000000, "priorityHI":5, "priorityLO":5, "period":[1.000000, 2.000000], "duration":[0.000600, 0.000600], "deadline":1.000000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T22", "offset":0.000000, "priorityHI":4, "priorityLO":4, "period":[1.000000, 2.000000], "duration":[0.000100, 0.900000], "deadline":1.000000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T23", "offset":0.000000, "priorityHI":3, "priorityLO":3, "period":[1.000000, 60.000000], "duration":[0.005500, 0.005600], "deadline":1.000000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T24", "offset":0.000000, "priorityHI":2, "priorityLO":2, "period":[60.000000, 60.000000], "duration":[0.000100, 20.000000], "deadline":20.000000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
	{"name":"T25", "offset":0.000000, "priorityHI":1, "priorityLO":1, "period":[5.000000, 5.000000], "duration":[0.000300, 0.000300], "deadline":5.000000, "quantity":1, "core":[0], "affinity":[0], "partition":0, "policy":"FIFO", "replenInterval": 0.0, "execBudget": 0.0 },
]
