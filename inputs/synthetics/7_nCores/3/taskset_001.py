# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 0.550000
outputDirectory = "ressults/synN25/7_nCores/3/Set004"

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
numCores = 3
StartupTime = (4.00E-06, 9.00E-06, 1.00E-06, 1.40E-05)
ExitTime = (4.00E-06, 9.00E-06, 1.00E-06, 1.40E-05)
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
	{"name": "t01", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.120000, 0.220000], "duration": [0.003000, 0.003000], "deadline": 0.120000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.100000, 0.180000], "duration": [0.024000, 0.024000], "deadline": 0.100000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.080000, 0.080000], "duration": [0.010300, 0.010300], "deadline": 0.080000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.050000, 0.090000], "duration": [0.004600, 0.004600], "deadline": 0.050000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.480000, 0.480000], "duration": [0.003200, 0.003200], "deadline": 0.480000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.190000, 0.330000], "duration": [0.058000, 0.058000], "deadline": 0.190000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.240000, 0.400000], "duration": [0.002500, 0.004300], "deadline": 0.240000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.050000, 0.090000], "duration": [0.000300, 0.000300], "deadline": 0.050000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.001500, 0.001500], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.330000, 0.550000], "duration": [0.041700, 0.069700], "deadline": 0.330000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.004300, 0.004300], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000600, 0.000600], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000900, 0.000900], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.003700, 0.003700], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.120000, 0.220000], "duration": [0.001600, 0.001600], "deadline": 0.120000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.210000, 0.350000], "duration": [0.008600, 0.008600], "deadline": 0.210000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.004400, 0.004400], "deadline": 0.020000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.320000, 0.540000], "duration": [0.027200, 0.027200], "deadline": 0.320000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.001700, 0.001700], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000300, 0.000300], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000400, 0.000400], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000400, 0.000400], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.004900, 0.004900], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.002000, 0.002000], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
