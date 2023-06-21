# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 2.640000
outputDirectory = "ressults/synN25/1_nTasks/15/Set003"

# =========================================================
# Processor Environment type 1
# =========================================================
rrTickCore = 0
tickInterval = 0.001
rrTicks = 4.0
clockResolution = 1E-7 

# =========================================================
# Processor Environment type 2
# =========================================================
numCores = 1
StartupTime = (1.20E-05, 1.70E-05, 1.00E-06, 2.20E-05)
ExitTime = (1.20E-05, 1.70E-05, 1.00E-06, 2.20E-05)
IPITime = (4.00E-07, 7.00E-07, 1.00E-07, 1.00E-06)

# =========================================================
# APS Parameters
# =========================================================
windowSize = 0.1
numPartitions = 1
partitionBudgets = [1.00]
apsPolicy = "default"
apsAlgorithm = "PRACTICAL"
RES = 128
log2RES = 7

# =========================================================
# Details of each Thread
# =========================================================
threads = [
	{"name": "t01", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000300], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.310000, 0.530000], "duration": [0.017800, 0.017800], "deadline": 0.310000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.002100, 0.002100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.160000, 0.280000], "duration": [0.001200, 0.001200], "deadline": 0.160000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.220000, 0.220000], "duration": [0.030800, 0.030800], "deadline": 0.220000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.080000, 0.140000], "duration": [0.015600, 0.015600], "deadline": 0.080000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.001800, 0.001800], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.050000, 0.090000], "duration": [0.001600, 0.001600], "deadline": 0.050000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.110000, 0.190000], "duration": [0.002000, 0.002000], "deadline": 0.110000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.001400, 0.001400], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.400000, 0.680000], "duration": [0.002800, 0.002800], "deadline": 0.400000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.110000, 0.110000], "duration": [0.001700, 0.001700], "deadline": 0.110000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.240000, 0.240000], "duration": [0.003800, 0.003800], "deadline": 0.240000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.180000, 0.320000], "duration": [0.005400, 0.009000], "deadline": 0.180000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.060000, 0.060000], "duration": [0.002500, 0.002500], "deadline": 0.060000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
