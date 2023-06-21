# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 1.250000
outputDirectory = "ressults/synN25/1_nTasks/40/Set016"

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
	{"name": "t01", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.360000, 0.620000], "duration": [0.000300, 0.000700], "deadline": 0.360000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.002100, 0.002100], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.120000, 0.120000], "duration": [0.000100, 0.000100], "deadline": 0.120000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 40, "priorityLO": 40, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000300, 0.000300], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 39, "priorityLO": 39, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 38, "priorityLO": 38, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 37, "priorityLO": 37, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000400, 0.000400], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 36, "priorityLO": 36, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.600000, 1.000000], "duration": [0.012100, 0.012100], "deadline": 0.600000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.000500, 0.000500], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 35, "priorityLO": 35, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 34, "priorityLO": 34, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.420000, 0.700000], "duration": [0.007100, 0.007100], "deadline": 0.420000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.320000, 0.540000], "duration": [0.013100, 0.013100], "deadline": 0.320000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 33, "priorityLO": 33, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000300, 0.000300], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.000100, 0.000100], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 26, "priorityLO": 26, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.000600, 0.000600], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.260000, 0.440000], "duration": [0.009000, 0.009000], "deadline": 0.260000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.180000, 0.300000], "duration": [0.005300, 0.005300], "deadline": 0.180000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 32, "priorityLO": 32, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.750000, 1.250000], "duration": [0.021100, 0.021100], "deadline": 0.750000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 31, "priorityLO": 31, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.004100, 0.004100], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.110000, 0.190000], "duration": [0.001000, 0.001000], "deadline": 0.110000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 30, "priorityLO": 30, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000300, 0.000300], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t26", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.540000, 0.900000], "duration": [0.000400, 0.000400], "deadline": 0.540000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t27", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.000100, 0.000100], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t28", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.090000, 0.170000], "duration": [0.006000, 0.006000], "deadline": 0.090000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t29", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.360000, 0.600000], "duration": [0.002400, 0.002400], "deadline": 0.360000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t30", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.310000, 0.530000], "duration": [0.016800, 0.016800], "deadline": 0.310000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t31", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.001200, 0.001200], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t32", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.000500, 0.000500], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t33", "partition": 0, "priorityHI": 29, "priorityLO": 29, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000400, 0.000400], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t34", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.000300, 0.000300], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t35", "partition": 0, "priorityHI": 28, "priorityLO": 28, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t36", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.120000, 0.220000], "duration": [0.001900, 0.003300], "deadline": 0.120000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t37", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.080000, 0.140000], "duration": [0.003600, 0.003600], "deadline": 0.080000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t38", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.001200, 0.001200], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t39", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.080000, 0.080000], "duration": [0.000200, 0.000200], "deadline": 0.080000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t40", "partition": 0, "priorityHI": 27, "priorityLO": 27, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
