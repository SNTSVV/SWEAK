# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 1.590000
outputDirectory = "ressults/synN25/7_nCores/7/Set009"

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
numCores = 7
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
	{"name": "t01", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.530000, 0.530000], "duration": [0.181400, 0.302400], "deadline": 0.530000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.004400, 0.004400], "deadline": 0.010000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.002000, 0.002000], "deadline": 0.010000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.003200, 0.003200], "deadline": 0.010000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.008400, 0.008400], "deadline": 0.030000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.001200, 0.001200], "deadline": 0.030000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.007600, 0.007600], "deadline": 0.030000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.430000, 0.730000], "duration": [0.027200, 0.027200], "deadline": 0.430000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.007100, 0.007100], "deadline": 0.010000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.530000, 0.890000], "duration": [0.109000, 0.109000], "deadline": 0.530000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.210000, 0.350000], "duration": [0.006800, 0.006800], "deadline": 0.210000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000900, 0.000900], "deadline": 0.010000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.001100, 0.001100], "deadline": 0.010000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.060000, 0.120000], "duration": [0.003800, 0.003800], "deadline": 0.060000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.004400, 0.007400], "deadline": 0.010000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.004100, 0.004100], "deadline": 0.010000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.120000, 0.220000], "duration": [0.016300, 0.016300], "deadline": 0.120000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.003000, 0.003000], "deadline": 0.010000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.560000, 0.940000], "duration": [0.007300, 0.007300], "deadline": 0.560000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.380000, 0.640000], "duration": [0.198100, 0.198100], "deadline": 0.380000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.013300, 0.013300], "deadline": 0.020000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.000400, 0.000400], "deadline": 0.020000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.007300, 0.007300], "deadline": 0.010000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.670000, 1.130000], "duration": [0.254300, 0.254300], "deadline": 0.670000, "core": [0,1,2,3,4,5,6], "affinity": [0,1,2,3,4,5,6], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
