import sys
import uproot
import numpy as np
import awkward as ak
import hist
import matplotlib.pyplot as plt
try:
    input_file = sys.argv[1]
except Exception:
    input_file = "mumu_H_bb_3TeV_sim_edm4hep.root"
input = uproot.open(input_file)
events = input["events"]
caloHits = events["AllCaloHitContributionsCombined"]
caloHitEnergy=caloHits["AllCaloHitContributionsCombined.energy"]
energies = ak.flatten(caloHitEnergy.arrays(), axis=None)
fig, ax = plt.subplots()
ax.set_xlabel('Energy (GeV)')
ax.set_ylabel('Events per GeV')
ax.hist(energies, bins=200)
ax.set(xlim=(0, 0.05))
plt.yscale('symlog')
plt.show()
