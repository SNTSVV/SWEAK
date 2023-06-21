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
outputDirectory = "ressults/synN25/9_partitions/3/Set007"

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
numPartitions = 3
partitionBudgets = [0.34, 0.33, 0.33]
apsPolicy = "default"
apsAlgorithm = "PRACTICAL"
RES = 128
log2RES = 7

# =========================================================
# Details of each Thread
# =========================================================
threads = [
	{"name": "t01", "partition": 1, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.150000, 0.150000], "duration": [0.003600, 0.003600], "deadline": 0.150000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 1, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.000300, 0.000300], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 2, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.000200, 0.000200], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 2, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.001600, 0.001600], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 1, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.070000, 0.130000], "duration": [0.000200, 0.000200], "deadline": 0.070000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 1, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000400, 0.000400], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 1, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.003900, 0.006700], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.090000, 0.090000], "duration": [0.002100, 0.002100], "deadline": 0.090000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 2, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.002200, 0.003800], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 2, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.230000, 0.390000], "duration": [0.006300, 0.006300], "deadline": 0.230000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.001100, 0.001100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 1, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.240000, 0.240000], "duration": [0.004900, 0.004900], "deadline": 0.240000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 1, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.001400, 0.001400], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 1, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.080000, 0.140000], "duration": [0.003600, 0.003600], "deadline": 0.080000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 1, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.600000, 1.000000], "duration": [0.045900, 0.045900], "deadline": 0.600000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 1, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.370000, 0.630000], "duration": [0.012400, 0.012400], "deadline": 0.370000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 1, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 1, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.480000, 0.800000], "duration": [0.020300, 0.020300], "deadline": 0.480000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 1, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.120000, 0.220000], "duration": [0.001300, 0.001300], "deadline": 0.120000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 1, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.090000, 0.170000], "duration": [0.004600, 0.004600], "deadline": 0.090000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 1, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.000700, 0.000700], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 1, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.000900, 0.000900], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
