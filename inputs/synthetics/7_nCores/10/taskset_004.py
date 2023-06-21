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
outputDirectory = "ressults/synN25_2/7_nCores/10/Set055"

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
	{"name": "t01", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.050000, 0.050000], "duration": [0.000400, 0.000400], "deadline": 0.050000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.110000, 0.190000], "duration": [0.049200, 0.049200], "deadline": 0.110000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.007300, 0.007300], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.035900, 0.035900], "deadline": 0.040000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.100000, 0.180000], "duration": [0.027600, 0.027600], "deadline": 0.100000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.000800, 0.000800], "deadline": 0.040000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.001500, 0.001500], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.004300, 0.004300], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.220000, 0.380000], "duration": [0.109100, 0.181900], "deadline": 0.220000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.150000, 0.150000], "duration": [0.009000, 0.015000], "deadline": 0.150000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.007800, 0.007800], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.240000, 0.420000], "duration": [0.090500, 0.090500], "deadline": 0.240000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.090000, 0.170000], "duration": [0.065100, 0.065100], "deadline": 0.090000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.025300, 0.025300], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.090000, 0.150000], "duration": [0.078600, 0.078600], "deadline": 0.090000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.005900, 0.005900], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.210000, 0.210000], "duration": [0.094600, 0.094600], "deadline": 0.210000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.060000, 0.100000], "duration": [0.030600, 0.030600], "deadline": 0.060000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.660000, 1.120000], "duration": [0.216800, 0.216800], "deadline": 0.660000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.080000, 0.140000], "duration": [0.005400, 0.005400], "deadline": 0.080000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.010800, 0.010800], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.026800, 0.026800], "deadline": 0.040000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.005100, 0.005100], "deadline": 0.020000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.220000, 0.380000], "duration": [0.089200, 0.089200], "deadline": 0.220000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
