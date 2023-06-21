# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 3.120000
outputDirectory = "ressults/synN25/9_partitions/8/Set002"

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
numPartitions = 8
partitionBudgets = [0.13, 0.13, 0.13, 0.13, 0.12, 0.12, 0.12, 0.12]
apsPolicy = "default"
apsAlgorithm = "PRACTICAL"
RES = 128
log2RES = 7

# =========================================================
# Details of each Thread
# =========================================================
threads = [
	{"name": "t01", "partition": 2, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.002500, 0.002500], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 5, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.350000, 0.590000], "duration": [0.003700, 0.003700], "deadline": 0.350000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 1, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.001100, 0.001100], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 7, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.210000, 0.370000], "duration": [0.022200, 0.022200], "deadline": 0.210000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 3, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.240000, 0.420000], "duration": [0.027600, 0.027600], "deadline": 0.240000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 2, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.520000, 0.880000], "duration": [0.038200, 0.038200], "deadline": 0.520000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 6, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.001200, 0.001200], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.000700, 0.000700], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 7, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000300, 0.000700], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 1, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.070000, 0.130000], "duration": [0.000100, 0.000300], "deadline": 0.070000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 5, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 4, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.001200, 0.001200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 1, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 3, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.000500, 0.000500], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 5, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.140000, 0.240000], "duration": [0.004700, 0.004700], "deadline": 0.140000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 3, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000900, 0.000900], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 3, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.210000, 0.370000], "duration": [0.003300, 0.003300], "deadline": 0.210000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 6, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 3, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.240000, 0.240000], "duration": [0.009200, 0.009200], "deadline": 0.240000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 5, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.000400, 0.000400], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 4, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.001000, 0.001000], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 5, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 5, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.390000, 0.390000], "duration": [0.004300, 0.004300], "deadline": 0.390000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 5, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.610000, 1.030000], "duration": [0.012800, 0.012800], "deadline": 0.610000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 5, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.350000, 0.590000], "duration": [0.028900, 0.028900], "deadline": 0.350000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
