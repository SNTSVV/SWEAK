# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 1.170000
outputDirectory = "ressults/synN25/7_nCores/6/Set018"

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
numCores = 6
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
	{"name": "t01", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.006900, 0.006900], "deadline": 0.030000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.015700, 0.015700], "deadline": 0.040000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.000700, 0.000700], "deadline": 0.020000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.260000, 0.440000], "duration": [0.095100, 0.095100], "deadline": 0.260000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.001200, 0.001200], "deadline": 0.030000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.070000, 0.130000], "duration": [0.003200, 0.003200], "deadline": 0.070000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.002100, 0.002100], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.140000, 0.140000], "duration": [0.010100, 0.016900], "deadline": 0.140000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.060000, 0.100000], "duration": [0.015800, 0.015800], "deadline": 0.060000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.000400, 0.000400], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.002900, 0.002900], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.220000, 0.380000], "duration": [0.048600, 0.048600], "deadline": 0.220000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.005300, 0.005300], "deadline": 0.020000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.003100, 0.003100], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.007000, 0.007000], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.690000, 1.170000], "duration": [0.312300, 0.312300], "deadline": 0.690000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.020000, 0.020000], "deadline": 0.030000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.680000, 1.140000], "duration": [0.203400, 0.203400], "deadline": 0.680000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.004200, 0.004200], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.002100, 0.002100], "deadline": 0.020000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.002100, 0.002100], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.540000, 0.920000], "duration": [0.005000, 0.005000], "deadline": 0.540000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.440000, 0.740000], "duration": [0.075300, 0.125700], "deadline": 0.440000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.080000, 0.140000], "duration": [0.027700, 0.027700], "deadline": 0.080000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
