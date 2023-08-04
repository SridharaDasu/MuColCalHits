import sys
import uproot

try:
    input_file = sys.argv[1]
except Exception:
    print(f"Command Syntax: python {sys.argv[0]} [root file name]")
    exit(1)

input = uproot.open(input_file)

events = input["events"]

print(f"Content of the file {input_file}")
print('The content of the events = input["events"] is:')

for item in events.items():
    print(item[0])

print('You can access the elements as array = events["Particle"]["Particle.E"].array()')
print("You may want to use np.squeeze(array)")
