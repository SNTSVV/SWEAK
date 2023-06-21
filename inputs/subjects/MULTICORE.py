# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0
runTime = 3.480000
outputDirectory = "results/APS_EXP/multicore/Set000"

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
numCores = 2
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
	{"name": "t01", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.0052, 0.0056], "deadline": 0.030000, "core": [1], "affinity": [1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.060000, 0.100000], "duration": [0.0034, 0.0034], "deadline": 0.060000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.0010, 0.0016], "deadline": 0.010000, "core": [1], "affinity": [1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.0012, 0.0012], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.290000, 0.290000], "duration": [0.0164, 0.0188], "deadline": 0.290000, "core": [1], "affinity": [1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.0010, 0.0014], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.0010, 0.0010], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.0010, 0.0010], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.0034, 0.0042], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.0002, 0.0006], "deadline": 0.010000, "core": [0,1], "affinity": [0,1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.470000, 0.790000], "duration": [0.0234, 0.0242], "deadline": 0.470000, "core": [0,1], "affinity": [0,1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.180000, 0.300000], "duration": [0.0244, 0.0730], "deadline": 0.180000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.030000, 0.070000], "duration": [0.0060, 0.0072], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.0004, 0.0004], "deadline": 0.020000, "core": [1], "affinity": [1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.290000, 0.290000], "duration": [0.0210, 0.0630], "deadline": 0.290000, "core": [1], "affinity": [1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.0002, 0.0002], "deadline": 0.010000, "core": [0,1], "affinity": [0,1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.500000, 0.840000], "duration": [0.1582, 0.1614], "deadline": 0.500000, "core": [0,1], "affinity": [0,1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.0004, 0.0004], "deadline": 0.040000, "core": [0,1], "affinity": [0,1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.180000, 0.300000], "duration": [0.0132, 0.0144], "deadline": 0.180000, "core": [0,1], "affinity": [0,1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.0006, 0.0010], "deadline": 0.010000, "core": [0,1], "affinity": [0,1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.060000, 0.060000], "duration": [0.0014, 0.0022], "deadline": 0.060000, "core": [1], "affinity": [1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.400000, 0.680000], "duration": [0.0254, 0.0270], "deadline": 0.400000, "core": [0,1], "affinity": [0,1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.050000, 0.090000], "duration": [0.0048, 0.0064], "deadline": 0.050000, "core": [1], "affinity": [1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.0010, 0.0010], "deadline": 0.010000, "core": [1], "affinity": [1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.0002, 0.0002], "deadline": 0.010000, "core": [0,1], "affinity": [0,1], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
