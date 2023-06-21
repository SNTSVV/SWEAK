# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 4.200000
outputDirectory = "ressults/synN25/9_partitions/10/Set000"

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
numPartitions = 10
partitionBudgets = [0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10, 0.10]
apsPolicy = "default"
apsAlgorithm = "PRACTICAL"
RES = 128
log2RES = 7

# =========================================================
# Details of each Thread
# =========================================================
threads = [
	{"name": "t01", "partition": 9, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.001600, 0.001600], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 9, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.300000, 0.520000], "duration": [0.011600, 0.011600], "deadline": 0.300000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 8, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.200000, 0.200000], "duration": [0.005800, 0.005800], "deadline": 0.200000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 5, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.060000, 0.060000], "duration": [0.001300, 0.002300], "deadline": 0.060000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 3, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.110000, 0.190000], "duration": [0.003300, 0.003300], "deadline": 0.110000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 3, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 7, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.060000, 0.100000], "duration": [0.005000, 0.005000], "deadline": 0.060000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 6, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.380000, 0.640000], "duration": [0.011700, 0.011700], "deadline": 0.380000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 4, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000300, 0.000500], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 4, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 4, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.000600, 0.000600], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 5, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.150000, 0.150000], "duration": [0.001600, 0.001600], "deadline": 0.150000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 5, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.000400, 0.000400], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 1, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000700, 0.000700], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 5, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.030000, 0.070000], "duration": [0.000800, 0.000800], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 1, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.001500, 0.001500], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.170000, 0.290000], "duration": [0.012600, 0.012600], "deadline": 0.170000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 7, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.070000, 0.070000], "duration": [0.000300, 0.000300], "deadline": 0.070000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 9, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.700000, 1.180000], "duration": [0.003000, 0.003000], "deadline": 0.700000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 2, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.002000, 0.002000], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 5, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.070000, 0.130000], "duration": [0.001200, 0.001200], "deadline": 0.070000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.060000, 0.060000], "duration": [0.001000, 0.001000], "deadline": 0.060000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.240000, 0.420000], "duration": [0.018900, 0.018900], "deadline": 0.240000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 5, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.180000, 0.300000], "duration": [0.006400, 0.006400], "deadline": 0.180000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 5, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.090000, 0.170000], "duration": [0.005000, 0.005000], "deadline": 0.090000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
