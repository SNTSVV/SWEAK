# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 1.040000
outputDirectory = "ressults/synN25/7_nCores/4/Set009"

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
numCores = 4
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
	{"name": "t01", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.330000, 0.550000], "duration": [0.021700, 0.021700], "deadline": 0.330000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.080000, 0.080000], "duration": [0.007800, 0.013200], "deadline": 0.080000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.016800, 0.016800], "deadline": 0.030000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.570000, 0.950000], "duration": [0.056700, 0.056700], "deadline": 0.570000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.002200, 0.002200], "deadline": 0.010000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000300, 0.000300], "deadline": 0.010000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.001500, 0.001500], "deadline": 0.010000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.270000, 0.450000], "duration": [0.035800, 0.035800], "deadline": 0.270000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.100000, 0.180000], "duration": [0.063000, 0.063000], "deadline": 0.100000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.006100, 0.006100], "deadline": 0.010000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000800, 0.000800], "deadline": 0.010000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.090000, 0.090000], "duration": [0.019000, 0.019000], "deadline": 0.090000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.005400, 0.009200], "deadline": 0.030000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.120000, 0.120000], "duration": [0.004700, 0.004700], "deadline": 0.120000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.240000, 0.400000], "duration": [0.028700, 0.028700], "deadline": 0.240000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.005200, 0.005200], "deadline": 0.030000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.300000, 0.520000], "duration": [0.006500, 0.006500], "deadline": 0.300000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.240000, 0.400000], "duration": [0.022100, 0.022100], "deadline": 0.240000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.490000, 0.830000], "duration": [0.123700, 0.123700], "deadline": 0.490000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.007400, 0.007400], "deadline": 0.030000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.180000, 0.300000], "duration": [0.002900, 0.002900], "deadline": 0.180000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.620000, 1.040000], "duration": [0.103300, 0.103300], "deadline": 0.620000, "core": [0,1,2,3], "affinity": [0,1,2,3], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
