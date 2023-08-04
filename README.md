# MuColCalHits

The machines available to work in the `hep.wisc.edu` cluster are:

`cms01` (EL8)
`login01, login02, login03, login04` (EL7) - generically login.hep.wisc.edu
`mucol01` (Almalinux9) - requires setup of Wisc VPN or indirection through above machines

To login to `hep.wisc.edu` cluster, use:

```
ssh <user-name>@cms01.hep.wisc.edu
```

To get this repository to your area, use:

```
git clone git@github.com:SridharaDasu/MuColCalHits.git
```

To get the big H->b,b data to your machine, 

* if on `cms01` or `mucol01`, do:

```
ln -s /nfs_scratch/dasu/MuonCollider/mucoll-benchmarks/edm4hep/mumi_000_edm4hep.root .
ln -s /nfs_scratch/dasu/MuonCollider/mucoll-benchmarks/edm4hep/mumu_H_bb_3TeV_sim_edm4hep.root .
```

* in case you are running on personal machine, use:

```
scp cms01.hep.wisc.edu:/nfs_scratch/dasu/MuonCollider/mucoll-benchmarks/edm4hep/mumi_000_edm4hep.root .
scp cms01.hep.wisc.edu:/nfs_scratch/dasu/MuonCollider/mucoll-benchmarks/edm4hep/mumu_H_bb_3TeV_sim_edm4hep.root .
```

If working on `hep.wisc.edu` machines `python3, upwork, numpy, matplotlib` should be available on `cms01` and `mucol01`.

If working on your own local machine, I recommend making a `virtualenv` and installing required packages in that `venv`:

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
To look at the contents of the files do:

```
python inspector.py mumi_000_edm4hep.root
python inspector.py mumu_H_bb_3TeV_sim_edm4hep.root
```

Both files should have the same information as both are files created by the muon collider detector GEANT4 simulation step.

The mumi_000 file has a fraction of beam induced background from negative muons.

The mumu_H_bb_3TeV file has Higgs to b-quark pair signal events.
