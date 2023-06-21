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
outputDirectory = "ressults/synN25_2/7_nCores/10/Set059"

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
	{"name": "t01", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.004300, 0.007300], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.380000, 0.640000], "duration": [0.283500, 0.283500], "deadline": 0.380000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.080000, 0.140000], "duration": [0.041900, 0.041900], "deadline": 0.080000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.009800, 0.009800], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.110000, 0.190000], "duration": [0.059500, 0.059500], "deadline": 0.110000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.700000, 1.180000], "duration": [0.353100, 0.353100], "deadline": 0.700000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.430000, 0.730000], "duration": [0.288800, 0.288800], "deadline": 0.430000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.210000, 0.210000], "duration": [0.049100, 0.049100], "deadline": 0.210000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.005500, 0.005500], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.009200, 0.009200], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.280000, 0.480000], "duration": [0.049400, 0.049400], "deadline": 0.280000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.280000, 0.280000], "duration": [0.182700, 0.182700], "deadline": 0.280000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.530000, 0.890000], "duration": [0.348200, 0.348200], "deadline": 0.530000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.380000, 0.640000], "duration": [0.121000, 0.121000], "deadline": 0.380000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.130000, 0.230000], "duration": [0.016700, 0.016700], "deadline": 0.130000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.180000, 0.180000], "duration": [0.062000, 0.062000], "deadline": 0.180000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.590000, 0.990000], "duration": [0.080300, 0.080300], "deadline": 0.590000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.240000, 0.400000], "duration": [0.096600, 0.096600], "deadline": 0.240000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.120000, 0.120000], "duration": [0.032000, 0.032000], "deadline": 0.120000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000400, 0.000400], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.027300, 0.027300], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.080000, 0.140000], "duration": [0.021900, 0.021900], "deadline": 0.080000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.002900, 0.004900], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8,9], "affinity": [0,1,2,3,4,5,6,7,8,9], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
