# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 1.200000
outputDirectory = "ressults/synN25_2/7_nCores/10/Set066"

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
numCores = 10
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
	{"name": "t01", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.009300, 0.009300], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.023800, 0.023800], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.240000, 0.240000], "duration": [0.011200, 0.011200], "deadline": 0.240000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.710000, 1.190000], "duration": [0.189400, 0.189400], "deadline": 0.710000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.360000, 0.600000], "duration": [0.054600, 0.054600], "deadline": 0.360000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.490000, 0.830000], "duration": [0.132500, 0.132500], "deadline": 0.490000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.060000, 0.120000], "duration": [0.020500, 0.020500], "deadline": 0.060000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.200000, 0.200000], "duration": [0.093400, 0.093400], "deadline": 0.200000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.008100, 0.008100], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.006600, 0.006600], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.090000, 0.150000], "duration": [0.041100, 0.041100], "deadline": 0.090000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.004500, 0.004500], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.015800, 0.015800], "deadline": 0.020000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.011800, 0.011800], "deadline": 0.020000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.002700, 0.004500], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.002400, 0.002400], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.630000, 1.070000], "duration": [0.078900, 0.078900], "deadline": 0.630000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.007600, 0.007600], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.090000, 0.150000], "duration": [0.021300, 0.035700], "deadline": 0.090000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.003200, 0.003200], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.080000, 0.080000], "duration": [0.068700, 0.068700], "deadline": 0.080000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.007100, 0.007100], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.120000, 0.220000], "duration": [0.040800, 0.040800], "deadline": 0.120000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.100000, 0.180000], "duration": [0.046900, 0.046900], "deadline": 0.100000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
