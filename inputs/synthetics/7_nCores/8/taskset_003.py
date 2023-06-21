# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 3.060000
outputDirectory = "ressults/synN25/7_nCores/8/Set010"

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
	{"name": "t01", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.330000, 0.570000], "duration": [0.066400, 0.066400], "deadline": 0.330000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.270000, 0.450000], "duration": [0.193700, 0.193700], "deadline": 0.270000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.090000, 0.150000], "duration": [0.027500, 0.027500], "deadline": 0.090000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.003800, 0.003800], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.007900, 0.007900], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.330000, 0.570000], "duration": [0.033800, 0.033800], "deadline": 0.330000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.009600, 0.009600], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.060000, 0.060000], "duration": [0.001200, 0.001200], "deadline": 0.060000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.090000, 0.090000], "duration": [0.001500, 0.002700], "deadline": 0.090000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.004800, 0.004800], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.008500, 0.008500], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.690000, 1.170000], "duration": [0.113500, 0.113500], "deadline": 0.690000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.110000, 0.190000], "duration": [0.040900, 0.040900], "deadline": 0.110000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.006700, 0.006700], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.670000, 1.130000], "duration": [0.260000, 0.260000], "deadline": 0.670000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000900, 0.001500], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.060000, 0.060000], "duration": [0.010500, 0.010500], "deadline": 0.060000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.090000, 0.150000], "duration": [0.005500, 0.005500], "deadline": 0.090000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.001300, 0.001300], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.033300, 0.033300], "deadline": 0.040000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.170000, 0.170000], "duration": [0.075400, 0.075400], "deadline": 0.170000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.003500, 0.003500], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.110000, 0.190000], "duration": [0.053500, 0.053500], "deadline": 0.110000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000400, 0.000400], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.300000, 0.520000], "duration": [0.058800, 0.058800], "deadline": 0.300000, "core": [0,1,2,3,4,5,6,7], "affinity": [0,1,2,3,4,5,6,7], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
