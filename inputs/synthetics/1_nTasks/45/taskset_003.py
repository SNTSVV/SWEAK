# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 4.800000
outputDirectory = "ressults/synN25/1_nTasks/45/Set003"

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
	{"name": "t01", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.160000, 0.160000], "duration": [0.001900, 0.001900], "deadline": 0.160000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 45, "priorityLO": 45, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000500, 0.000500], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 44, "priorityLO": 44, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.000300, 0.000700], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 36, "priorityLO": 36, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.000400, 0.000400], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.450000, 0.770000], "duration": [0.008300, 0.008300], "deadline": 0.450000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.050000, 0.090000], "duration": [0.000300, 0.000300], "deadline": 0.050000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 35, "priorityLO": 35, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.001400, 0.001400], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.100000, 0.100000], "duration": [0.001000, 0.001000], "deadline": 0.100000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.060000, 0.120000], "duration": [0.001100, 0.001100], "deadline": 0.060000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 43, "priorityLO": 43, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 28, "priorityLO": 28, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.000300, 0.000300], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.370000, 0.630000], "duration": [0.028900, 0.028900], "deadline": 0.370000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.430000, 0.730000], "duration": [0.000100, 0.000100], "deadline": 0.430000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.190000, 0.330000], "duration": [0.000600, 0.000600], "deadline": 0.190000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.600000, 1.000000], "duration": [0.005000, 0.005000], "deadline": 0.600000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.050000, 0.050000], "duration": [0.000600, 0.000600], "deadline": 0.050000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 27, "priorityLO": 27, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.000500, 0.000500], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.210000, 0.350000], "duration": [0.000700, 0.000700], "deadline": 0.210000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 26, "priorityLO": 26, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.000800, 0.000800], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.001300, 0.001300], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.050000, 0.050000], "duration": [0.003500, 0.003500], "deadline": 0.050000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 34, "priorityLO": 34, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.000300, 0.000300], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.040000, 0.080000], "duration": [0.004100, 0.004100], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.210000, 0.370000], "duration": [0.018900, 0.018900], "deadline": 0.210000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 31, "priorityLO": 31, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.000900, 0.000900], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t26", "partition": 0, "priorityHI": 42, "priorityLO": 42, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t27", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.430000, 0.730000], "duration": [0.005500, 0.005500], "deadline": 0.430000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t28", "partition": 0, "priorityHI": 41, "priorityLO": 41, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t29", "partition": 0, "priorityHI": 40, "priorityLO": 40, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000300, 0.000300], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t30", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.120000, 0.200000], "duration": [0.001300, 0.001300], "deadline": 0.120000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t31", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.070000, 0.130000], "duration": [0.000900, 0.000900], "deadline": 0.070000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t32", "partition": 0, "priorityHI": 30, "priorityLO": 30, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.000600, 0.000600], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t33", "partition": 0, "priorityHI": 39, "priorityLO": 39, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000200, 0.000200], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t34", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.060000, 0.100000], "duration": [0.000300, 0.000700], "deadline": 0.060000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t35", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.320000, 0.320000], "duration": [0.001200, 0.001200], "deadline": 0.320000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t36", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.040000, 0.040000], "duration": [0.000100, 0.000100], "deadline": 0.040000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t37", "partition": 0, "priorityHI": 38, "priorityLO": 38, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.000300, 0.000300], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t38", "partition": 0, "priorityHI": 33, "priorityLO": 33, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.000100, 0.000100], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t39", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.130000, 0.230000], "duration": [0.002300, 0.002300], "deadline": 0.130000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t40", "partition": 0, "priorityHI": 29, "priorityLO": 29, "offset": 0.000000, "period": [0.030000, 0.050000], "duration": [0.001500, 0.001500], "deadline": 0.030000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t41", "partition": 0, "priorityHI": 32, "priorityLO": 32, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.000300, 0.000300], "deadline": 0.020000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t42", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.120000, 0.200000], "duration": [0.002900, 0.002900], "deadline": 0.120000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t43", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.060000, 0.100000], "duration": [0.001200, 0.001200], "deadline": 0.060000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t44", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.060000, 0.100000], "duration": [0.001100, 0.001100], "deadline": 0.060000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t45", "partition": 0, "priorityHI": 37, "priorityLO": 37, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.000100, 0.000100], "deadline": 0.010000, "core": [0], "affinity": [0], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
