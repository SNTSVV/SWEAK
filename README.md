# SWEAK
SWEAK (<u>S</u>afe <u>W</u>CET analysis method for w<u>EAK</u>ly hard real-time system) is a tool for estimating probabilistic safe Worst-Case Execution Times (WCET) of weakly hard real-time systems using search and machine learning. 


### Overview
Weakly hard real-time systems can, to some degree, tolerate deadline misses, but their schedulability still needs to be analyzed to ensure their quality of service. Such analysis usually occurs at early design stages to provide implementation guidelines to engineers so that they can make better design decisions. Estimating worst-case execution times (WCET) is a key input to schedulability analysis. However, early on during system design, estimating WCET values is challenging and engineers usually determine them as plausible ranges based on their domain knowledge. Our approach aims at finding restricted, safe WCET sub-ranges given a set of ranges initially estimated by experts in the context of weakly hard real-time systems. To this end, we leverage (1) multi-objective search aiming at maximizing the violation of weakly hard constraints in order to find worst-case scheduling scenarios and (2) polynomial logistic regression to infer safe WCET ranges with a probabilistic interpretation. We evaluated our approach by applying it to an industrial system in the satellite domain and several realistic synthetic systems. The results indicate that our approach significantly outperforms a baseline relying on random search without learning, and estimates safe WCET ranges with a high degree of confidence in practical time (< 23h).

 
### Folders and files description
* `inputs`: containing the input task descriptions for the experiments of the tool SWEAK
* `outputs`: containing output from the tool SWEAK for the inputs
* `results`: containing the three experiment results for EXP1, EXP2, and EXP3


