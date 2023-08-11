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
# caloHitEnergy = caloHits["AllCaloHitContributionsCombined.energy"]
# energies = ak.flatten(caloHitEnergy.arrays(), axis=None)

stepPositionX = caloHits["AllCaloHitContributionsCombined.stepPosition.x"]
stepPositionY = caloHits["AllCaloHitContributionsCombined.stepPosition.y"]
xHits = ak.flatten(stepPositionX.arrays(), axis=None)
yHits = ak.flatten(stepPositionY.arrays(), axis=None)

# plt.hist2d(xHits, yHits)
# plt.show()


fig, ax = plt.subplots(ncols=1)
fig.subplots_adjust(hspace=0.5, left=0.07, right=0.93)
hb = ax.hexbin(xHits, yHits, gridsize=100, cmap='YlGn')
ax.set_title("Hexagon binned calo hits: x vs y")
cb = fig.colorbar(hb, ax=ax)
cb.set_label('counts')
plt.show()
