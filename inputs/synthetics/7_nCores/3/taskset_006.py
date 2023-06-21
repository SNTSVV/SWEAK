# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 2.520000
outputDirectory = "ressults/synN25/7_nCores/3/Set016"

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
	{"name": "t01", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.150000, 0.250000], "duration": [0.031500, 0.031500], "deadline": 0.150000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.270000, 0.470000], "duration": [0.060600, 0.060600], "deadline": 0.270000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.090000, 0.170000], "duration": [0.003400, 0.003400], "deadline": 0.090000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.001600, 0.001600], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.001600, 0.001600], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000400, 0.000400], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.090000, 0.170000], "duration": [0.013700, 0.022900], "deadline": 0.090000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.180000, 0.180000], "duration": [0.013400, 0.013400], "deadline": 0.180000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.009700, 0.009700], "deadline": 0.040000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.090000, 0.090000], "duration": [0.013100, 0.013100], "deadline": 0.090000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.000900, 0.000900], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.009800, 0.009800], "deadline": 0.040000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.160000, 0.280000], "duration": [0.004100, 0.004100], "deadline": 0.160000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.210000, 0.210000], "duration": [0.021400, 0.021400], "deadline": 0.210000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.000600, 0.001200], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000800, 0.000800], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.000400, 0.000400], "deadline": 0.020000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.180000, 0.320000], "duration": [0.004400, 0.004400], "deadline": 0.180000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.001200, 0.001200], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.390000, 0.650000], "duration": [0.048700, 0.048700], "deadline": 0.390000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.030000, 0.070000], "duration": [0.011400, 0.011400], "deadline": 0.030000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.220000, 0.380000], "duration": [0.040400, 0.040400], "deadline": 0.220000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.005800, 0.005800], "deadline": 0.010000, "core": [0,1,2], "affinity": [0,1,2], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
