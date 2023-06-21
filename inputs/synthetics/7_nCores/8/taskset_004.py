# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 3.300000
outputDirectory = "ressults/synN25/7_nCores/8/Set011"

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
numCores = 8
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
	{"name": "t01", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.007700, 0.007700], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.008600, 0.008600], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.270000, 0.470000], "duration": [0.115300, 0.115300], "deadline": 0.270000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.050000, 0.050000], "duration": [0.000100, 0.000100], "deadline": 0.050000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.017700, 0.017700], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.090000, 0.170000], "duration": [0.069300, 0.069300], "deadline": 0.090000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.530000, 0.890000], "duration": [0.004300, 0.004300], "deadline": 0.530000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.005800, 0.009800], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.030000, 0.070000], "duration": [0.007500, 0.007500], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.050000, 0.050000], "duration": [0.022800, 0.022800], "deadline": 0.050000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.120000, 0.200000], "duration": [0.033400, 0.033400], "deadline": 0.120000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.550000, 0.930000], "duration": [0.186400, 0.186400], "deadline": 0.550000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.740000, 1.240000], "duration": [0.070500, 0.070500], "deadline": 0.740000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.110000, 0.110000], "duration": [0.022100, 0.022100], "deadline": 0.110000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.600000, 1.000000], "duration": [0.236800, 0.236800], "deadline": 0.600000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.002700, 0.004700], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.060000, 0.060000], "duration": [0.005900, 0.005900], "deadline": 0.060000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000600, 0.000600], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.000900, 0.000900], "deadline": 0.020000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.610000, 1.030000], "duration": [0.026500, 0.026500], "deadline": 0.610000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.060000, 0.060000], "duration": [0.038200, 0.038200], "deadline": 0.060000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.100000, 0.100000], "duration": [0.017500, 0.017500], "deadline": 0.100000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.017200, 0.017200], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.150000, 0.270000], "duration": [0.074000, 0.074000], "deadline": 0.150000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
