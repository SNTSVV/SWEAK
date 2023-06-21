# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 3.600000
outputDirectory = "ressults/synN25/7_nCores/6/Set014"

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
	{"name": "t01", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.006100, 0.006100], "deadline": 0.030000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.002000, 0.002000], "deadline": 0.020000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.060000, 0.060000], "duration": [0.019400, 0.019400], "deadline": 0.060000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.540000, 0.920000], "duration": [0.158900, 0.158900], "deadline": 0.540000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.520000, 0.880000], "duration": [0.097200, 0.097200], "deadline": 0.520000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.007100, 0.007100], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.004300, 0.004300], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.110000, 0.190000], "duration": [0.025000, 0.025000], "deadline": 0.110000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.060000, 0.120000], "duration": [0.010300, 0.010300], "deadline": 0.060000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.050000, 0.050000], "duration": [0.005600, 0.005600], "deadline": 0.050000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.500000, 0.840000], "duration": [0.054900, 0.091500], "deadline": 0.500000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.002900, 0.002900], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.080000, 0.080000], "duration": [0.047300, 0.047300], "deadline": 0.080000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.003600, 0.003600], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.010500, 0.010500], "deadline": 0.020000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.001500, 0.001500], "deadline": 0.030000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.006900, 0.006900], "deadline": 0.040000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.030000, 0.070000], "duration": [0.009900, 0.009900], "deadline": 0.030000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.360000, 0.360000], "duration": [0.031400, 0.031400], "deadline": 0.360000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.600000, 1.000000], "duration": [0.011100, 0.011100], "deadline": 0.600000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.003500, 0.003500], "deadline": 0.040000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.090000, 0.150000], "duration": [0.018900, 0.018900], "deadline": 0.090000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.420000, 0.700000], "duration": [0.138200, 0.230400], "deadline": 0.420000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000800, 0.000800], "deadline": 0.010000, "core": [0,1,2,3,4,5], "affinity": [0,1,2,3,4,5], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
