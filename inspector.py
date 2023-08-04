import uproot

input_file = "mumu_H_bb_3TeV_sim_edm4hep.root"

input = uproot.open(input_file)

events = input["events"]

print(f"Content of the file {input_file}")
print('The content of the events = input["Events"] is:')

for item in events.items():
    print(item[0])

print('You can access the elements as array = events["Particle"]["Particle.E"].array()')
print("You may want to use np.squeeze(array)")
