# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 0.950000
outputDirectory = "ressults/synN25/1_nTasks/15/Set011"

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
numCores = 1
StartupTime = (1.20E-05, 1.70E-05, 1.00E-06, 2.20E-05)
ExitTime = (1.20E-05, 1.70E-05, 1.00E-06, 2.20E-05)
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
	{"name": "t01", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.002600, 0.002600], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.050000, 0.050000], "duration": [0.000600, 0.000600], "deadline": 0.050000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.005200, 0.005200], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.240000, 0.420000], "duration": [0.034900, 0.034900], "deadline": 0.240000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.001800, 0.003200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.070000, 0.070000], "duration": [0.000100, 0.000100], "deadline": 0.070000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.570000, 0.950000], "duration": [0.028700, 0.028700], "deadline": 0.570000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.340000, 0.580000], "duration": [0.017400, 0.017400], "deadline": 0.340000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.110000, 0.190000], "duration": [0.001800, 0.003000], "deadline": 0.110000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.030000, 0.070000], "duration": [0.001000, 0.001000], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.000100, 0.000100], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.001200, 0.001200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
