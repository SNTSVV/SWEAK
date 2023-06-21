# =========================================================
# Parameters for SAFE approach
# =========================================================
psResolution = 1E-7
swResolution = 1.00E-04

# =========================================================
# Parameters for the Simulation
# =========================================================
seed = 0 
runTime = 4.200000
outputDirectory = "ressults/synN25_2/7_nCores/9/Set003"

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
numCores = 9
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
	{"name": "t01", "partition": 0, "priorityHI": 25, "priorityLO": 25, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.000400, 0.000400], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t02", "partition": 0, "priorityHI": 17, "priorityLO": 17, "offset": 0.000000, "period": [0.060000, 0.120000], "duration": [0.010600, 0.010600], "deadline": 0.060000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t03", "partition": 0, "priorityHI": 20, "priorityLO": 20, "offset": 0.000000, "period": [0.020000, 0.040000], "duration": [0.000300, 0.000300], "deadline": 0.020000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t04", "partition": 0, "priorityHI": 1, "priorityLO": 1, "offset": 0.000000, "period": [0.660000, 1.120000], "duration": [0.321200, 0.321200], "deadline": 0.660000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t05", "partition": 0, "priorityHI": 24, "priorityLO": 24, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.007100, 0.007100], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t06", "partition": 0, "priorityHI": 14, "priorityLO": 14, "offset": 0.000000, "period": [0.070000, 0.130000], "duration": [0.016700, 0.016700], "deadline": 0.070000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t07", "partition": 0, "priorityHI": 10, "priorityLO": 10, "offset": 0.000000, "period": [0.150000, 0.250000], "duration": [0.021700, 0.021700], "deadline": 0.150000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t08", "partition": 0, "priorityHI": 8, "priorityLO": 8, "offset": 0.000000, "period": [0.210000, 0.210000], "duration": [0.066900, 0.066900], "deadline": 0.210000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t09", "partition": 0, "priorityHI": 5, "priorityLO": 5, "offset": 0.000000, "period": [0.320000, 0.540000], "duration": [0.018300, 0.030500], "deadline": 0.320000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t10", "partition": 0, "priorityHI": 9, "priorityLO": 9, "offset": 0.000000, "period": [0.150000, 0.150000], "duration": [0.053100, 0.053100], "deadline": 0.150000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t11", "partition": 0, "priorityHI": 16, "priorityLO": 16, "offset": 0.000000, "period": [0.060000, 0.060000], "duration": [0.013700, 0.013700], "deadline": 0.060000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t12", "partition": 0, "priorityHI": 18, "priorityLO": 18, "offset": 0.000000, "period": [0.030000, 0.030000], "duration": [0.021600, 0.021600], "deadline": 0.030000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t13", "partition": 0, "priorityHI": 23, "priorityLO": 23, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.004300, 0.004300], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t14", "partition": 0, "priorityHI": 13, "priorityLO": 13, "offset": 0.000000, "period": [0.070000, 0.070000], "duration": [0.067600, 0.067600], "deadline": 0.070000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t15", "partition": 0, "priorityHI": 22, "priorityLO": 22, "offset": 0.000000, "period": [0.010000, 0.010000], "duration": [0.004900, 0.004900], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t16", "partition": 0, "priorityHI": 21, "priorityLO": 21, "offset": 0.000000, "period": [0.010000, 0.030000], "duration": [0.005400, 0.005400], "deadline": 0.010000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t17", "partition": 0, "priorityHI": 7, "priorityLO": 7, "offset": 0.000000, "period": [0.280000, 0.280000], "duration": [0.101000, 0.101000], "deadline": 0.280000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t18", "partition": 0, "priorityHI": 12, "priorityLO": 12, "offset": 0.000000, "period": [0.070000, 0.070000], "duration": [0.017500, 0.017500], "deadline": 0.070000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t19", "partition": 0, "priorityHI": 2, "priorityLO": 2, "offset": 0.000000, "period": [0.480000, 0.800000], "duration": [0.084100, 0.084100], "deadline": 0.480000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t20", "partition": 0, "priorityHI": 19, "priorityLO": 19, "offset": 0.000000, "period": [0.020000, 0.020000], "duration": [0.006700, 0.006700], "deadline": 0.020000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t21", "partition": 0, "priorityHI": 11, "priorityLO": 11, "offset": 0.000000, "period": [0.070000, 0.130000], "duration": [0.061200, 0.061200], "deadline": 0.070000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t22", "partition": 0, "priorityHI": 6, "priorityLO": 6, "offset": 0.000000, "period": [0.310000, 0.530000], "duration": [0.144000, 0.240200], "deadline": 0.310000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t23", "partition": 0, "priorityHI": 15, "priorityLO": 15, "offset": 0.000000, "period": [0.060000, 0.060000], "duration": [0.023600, 0.023600], "deadline": 0.060000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t24", "partition": 0, "priorityHI": 4, "priorityLO": 4, "offset": 0.000000, "period": [0.350000, 0.590000], "duration": [0.086800, 0.086800], "deadline": 0.350000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
	{"name": "t25", "partition": 0, "priorityHI": 3, "priorityLO": 3, "offset": 0.000000, "period": [0.390000, 0.670000], "duration": [0.026400, 0.026400], "deadline": 0.390000, "core": [0,1,2,3,4,5,6,7,8], "affinity": [0,1,2,3,4,5,6,7,8], "policy": "FIFO", "replenInterval": 0.0, "execBudget": 0.0, "quantity": 1, "comment": "", },
]
