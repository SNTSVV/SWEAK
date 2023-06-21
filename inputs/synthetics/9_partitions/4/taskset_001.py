# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 0.900000
outputDirectory = "ressults/synN25/9_partitions/4/Set011"

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
numPartitions = 4
partitionBudgets = [0.25, 0.25, 0.25, 0.25]
apsPolicy = "default"
apsAlgorithm = "PRACTICAL"
RES = 128
log2RES = 7

# =========================================================
# Details of each Thread
# =========================================================
threads = [
	{"name": "t01", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.130000, 0.230000], "duration": [0.001700, 0.001700], "deadline": 0.130000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 1, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.000400, 0.000400], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 1, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.490000, 0.830000], "duration": [0.020700, 0.020700], "deadline": 0.490000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 3, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.000100, 0.000100], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 2, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.030000, 0.070000], "duration": [0.002700, 0.002700], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 1, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.005300, 0.005300], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000300, 0.000300], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.540000, 0.900000], "duration": [0.015000, 0.015000], "deadline": 0.540000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.000200, 0.000200], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 3, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.000500, 0.000500], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 3, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.001000, 0.001000], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 2, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.000700, 0.000700], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 2, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.060000, 0.100000], "duration": [0.001100, 0.001900], "deadline": 0.060000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.030000, 0.070000], "duration": [0.000100, 0.000100], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 3, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.050000, 0.090000], "duration": [0.009900, 0.009900], "deadline": 0.050000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 2, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.100000, 0.100000], "duration": [0.000600, 0.000600], "deadline": 0.100000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 3, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.000500, 0.000500], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 3, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000600, 0.000600], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 3, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000800, 0.000800], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 3, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 2, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.060000, 0.100000], "duration": [0.000700, 0.000700], "deadline": 0.060000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.420000, 0.720000], "duration": [0.050700, 0.050700], "deadline": 0.420000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.240000, 0.400000], "duration": [0.008200, 0.008200], "deadline": 0.240000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.002600, 0.004400], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
