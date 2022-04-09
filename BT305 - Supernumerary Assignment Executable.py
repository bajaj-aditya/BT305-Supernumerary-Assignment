# -*- coding: utf-8 -*-
"""lab02_molviz.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/bajaj-aditya/BT305-Supernumerary-Assignment/blob/main/BT305%20Program%20Notebook.ipynb

BT305 Supernumerary assignment – Visualizing and Comparing Molecular Structures using MDAnalysis and py3Dmol

Name: Aditya Bajaj;
Roll No: 190106006

###Part 1. Retrieving and visualizing structures from PDB
"""

##Code to retrieve 6ANE.pdb!
!wget http://www.rcsb.org/pdb/files/6ANE.pdb.gz 
!gunzip 6ANE.pdb.gz

#To check how many chains are contained in the PDB
!grep 'COMPND'.*'CHAIN' 6ANE.pdb

#Checking residues using awk!
!awk '$1=="ATOM" && $3=="CA" && $5=="A" {print $0}' 6ANE.pdb | wc -l

"""As the 6ane.pdb has 3 different chains, here we use the **BioPDB module** from BioPython to split our multichain PDB into three different ones:

"""

#We would use Biopython to get information from PDB of each chain
!pip install biopython

#Here, we import Bio.PDB to use it to manipulate PDB files
from Bio.PDB import *
#And we set up a parser for our PDB
parser = PDBParser()
io=PDBIO()
structure = parser.get_structure('X', '6ANE.pdb')

#This will separate each chain into its own PDB file
for chain in structure.get_chains():
    io.set_structure(chain)
    io.save("6ANE_" + chain.get_id() + ".pdb")

#We install py3Dmol
!pip install py3Dmol

#importing py3Dmol
import py3Dmol

"""##### Visualizing 6ANE!"""

#Visualizing PDB
#First we assign the py3Dmol.view as view
view=py3Dmol.view()
#The following lines are used to add the addModel class
#to read the PDB files of chain B and C
view.addModel(open('6ANE_B.pdb', 'r').read(),'pdb')
view.addModel(open('6ANE_C.pdb', 'r').read(),'pdb')
#Zooming into all visualized structures 
view.zoomTo()
#Here we set the background color as white
view.setBackgroundColor('white')
#Here we set the visualization style for chain B and C
view.setStyle({'chain':'B'},{'cartoon': {'color':'purple'}})
view.setStyle({'chain':'C'},{'cartoon': {'color':'yellow'}})
#And we finally visualize the structures using the command below
view.show()

"""As we can see, we are able to load chains B and C of 6ANE in cartoon representation, but they are far from each other. In case we want to compare the conformations of different residues in these two chains, we are going to use the **Bio.PDB python module** again, which is implemented in the following script, to: 
1. Superimpose 6ANE chain B to chain C
2. Print the RMSD
3. Save the superimposed PDB of chain B
"""

#The following code was created by Anders Steen Christensen
#from the University of Basel and is available at
#https://gist.github.com/andersx/6354971

import Bio.PDB
import os

# Select what residue numbers you wish to align
# and put them in a list
start_id = 1
end_id   = 262
atoms_to_be_aligned = range(start_id, end_id + 1)

# Start the parser
pdb_parser = Bio.PDB.PDBParser(QUIET = True)

# Get the structures
ref_structure = pdb_parser.get_structure("reference", "6ANE_C.pdb")
sample_structure = pdb_parser.get_structure("sample", "6ANE_B.pdb")

# Use the first model in the pdb-files for alignment
# Change the number 0 if you want to align to another structure
ref_model    = ref_structure[0]
sample_model = sample_structure[0]

# Make a list of the atoms (in the structures) you wish to align.
# In this case we use CA atoms whose index is in the specified range
ref_atoms = []
sample_atoms = []

# Iterate of all chains in the model in order to find all residues
for ref_chain in ref_model:
  # Iterate of all residues in each model in order to find proper atoms
  for ref_res in ref_chain:
    # Check if residue number ( .get_id() ) is in the list
    if ref_res.get_id()[1] in atoms_to_be_aligned:
      # Append CA atom to list
      ref_atoms.append(ref_res['CA'])

# Do the same for the sample structure
for sample_chain in sample_model:
  for sample_res in sample_chain:
    if sample_res.get_id()[1] in atoms_to_be_aligned:
      sample_atoms.append(sample_res['CA'])

# Now we initiate the superimposer:
super_imposer = Bio.PDB.Superimposer()
super_imposer.set_atoms(ref_atoms, sample_atoms)
super_imposer.apply(sample_model.get_atoms())

# Print RMSD:
print('The calculated RMSD is:')
print (str(super_imposer.rms) + ' Å')

# Save the aligned version of one of the chains of 6ANE
io = Bio.PDB.PDBIO()
io.set_structure(sample_structure) 
io.save("6ANE_B_aligned.pdb")

#loading the superimposed structure in py3dmol
view=py3Dmol.view()
view.addModel(open('6ANE_B_aligned.pdb', 'r').read(),'pdb')
view.addModel(open('6ANE_C.pdb', 'r').read(),'pdb')
view.zoomTo()
view.setBackgroundColor('white')
view.setStyle({'chain':'B'},{'cartoon': {'color':'purple'}})
view.setStyle({'chain':'C'},{'cartoon': {'color':'yellow'}})
view.show()

#Let's say We want to inspect differnet conformers of Tryptophan 158 b/w chains B and C of 6ANE
#For this, we select specific residues using addStyle classes
view=py3Dmol.view()
view.addModel(open('6ANE_B_aligned.pdb', 'r').read(),'pdb')
view.addModel(open('6ANE_C.pdb', 'r').read(),'pdb')
view.zoomTo()
view.setBackgroundColor('white')
#Set a visualization style for chain B
view.setStyle({'chain':'B'},{'cartoon': {'color':'purple'}})
#Add a visualization style for residue 158 in chain B
view.addStyle({'chain':'B','resi':158},{'stick':{'colorscheme':'grayCarbon'}})
#Set a visualization style for chain C
view.setStyle({'chain':'C'},{'cartoon': {'color':'yellow'}})
#Add a visualization style for residue 158 in chain C
view.addStyle({'chain':'C','resi':158},{'stick':{'colorscheme':'skyblueCarbon'}})
view.show()

"""Sometimes we might want to show several residues in our visualization. Instead of writing a line of code per residue, py3Dmol can also work with residue selections:
A sequence of residues can be given as a range using square brackets:

> ["158-168"]

"""

view=py3Dmol.view()
view.addModel(open('6ANE_B_aligned.pdb', 'r').read(),'pdb')
view.addModel(open('6ANE_C.pdb', 'r').read(),'pdb')
view.zoomTo()
view.setBackgroundColor('white')
#Setting style for chain B
view.setStyle({'chain':'B'},
              {'cartoon': {'color':'purple'}}
             )
#Adding selection residue and choosing a color scheme in the next line
view.addStyle({'chain':'B','resi':['158-168']},
              {'stick':{'colorscheme':'green'}})
#Setting style for chain C
view.setStyle({'chain':'C'},
              {'cartoon': {'color':'yellow'}}
             )
#Adding different representation for residue 158 with a different color scheme 
view.addStyle({'chain':'C','resi':['158-168']},
              {'stick':{'colorscheme':'blue'}}
             )
view.show()

"""TO show residues **around a given distance radius** of Trp158? We can use **_within_** selections in your _addStyle_ classes as shown in the following lines of code"""

view=py3Dmol.view()
view.addModel(open('6ANE_B_aligned.pdb', 'r').read(),'pdb')
view.addModel(open('6ANE_C.pdb', 'r').read(),'pdb')
view.zoomTo()
view.setBackgroundColor('white')
#Setting styles for chains B and C 
view.setStyle({'chain':'B'},
              {'cartoon': {'color':'purple'}})
view.setStyle({'chain':'C'},
              {'cartoon': {'color':'yellow'}})
#See residues that are a distance X from the residue 158
view.addStyle({'within':{'distance': 7,
                         'sel':{'resi':158}
                         }
               }
              ,{'stick':{'colorscheme':'greenCarbon'}
                }
              )
#After you made your selection, change colors for the Trp from both chains
view.addStyle({'chain':'B','resi':158},
              {'stick':{'colorscheme':'blueCarbon'}})
view.addStyle({'chain':'C','resi':158},
              {'stick':{'colorscheme':'skyblueCarbon'}})
view.show()

"""For other representations, such as the **van der Waals** representation of the atoms? We can display the atom surface using vDW through the _**addSurface**_ class, as shown in the following line of code:"""

view=py3Dmol.view()
view.addModel(open('6ANE_B_aligned.pdb', 'r').read(),'pdb')
view.addModel(open('6ANE_C.pdb', 'r').read(),'pdb')
view.zoomTo()
view.setBackgroundColor('white')
view.setStyle({'chain':'B'},{'cartoon': {'color':'blue'}})
view.setStyle({'chain':'C'},{'cartoon': {'color':'skyblue'}})
view.addStyle({'within':{'distance': 7, 'sel':{'resi':158}}},{'stick':{'colorscheme':'grayCarbon'}})
view.addStyle({'chain':'B','resi':158},{'stick':{'colorscheme':'purpleCarbon'}})
view.addStyle({'chain':'C','resi':158},{'stick':{'colorscheme':'greenCarbon'}})
#VDW Surface
view.addSurface(py3Dmol.VDW,{'opacity':0.7,'color':'white'}, {'chain':'B'})
view.addSurface(py3Dmol.VDW,{'opacity':0.7,'color':'yellow'}, {'chain':'C'})
view.show()

"""Finally, if you want to identify the residues in your visualization, you can also add **text labels** using the _**addLabel**_ class. However, we first need to know the names of the residues that we would like to label.

The first code cell shows how to easily obtain the name for residue number 158. If all works well, you should get "TRP" as an answer, as you already know.

The second code cell incorporates the _**addLabel**_ class to add a "W158" text label for residue 158.
"""

#To know the residue type of the selected residues we use awk! 
#there are more elegant ways to do this but for now...
!awk '$6=="158" && $3=="CA" {print $4}' 6ANE_B.pdb
#Try yourself for residue 210, 179 and 133

view=py3Dmol.view()
view.addModel(open('6ANE_B_aligned.pdb', 'r').read(),'pdb')
view.addModel(open('6ANE_C.pdb', 'r').read(),'pdb')
view.zoomTo()
view.setBackgroundColor('white')
view.setStyle({'chain':'B'},{'cartoon': {'color':'purple'}})
view.addStyle({'chain':'B','resi':158},{'stick':{'colorscheme':'blueCarbon'}})
view.setStyle({'chain':'C'},{'cartoon': {'color':'yellow'}})
view.addStyle({'chain':'C','resi':158},{'stick':{'colorscheme':'skyblueCarbon'}})
#Using this line of code we can specify "The text","Opacity of the label","A selection of residues" 
view.addLabel("W158",{'fontOpacity':1},{'resi':158})

view.spin("y")

#Visualize the structure
view.show()

#EXPERIMENTAL TRICK
#The following trick sets an input and a 10 sec delay to print out a PNG
#You can right click on the image to save it
#NOTE: There is a bug on Safari that generates the PNG image upside down
''' 
import time
input("Press enter. Now you have 10 seconds to choose your visualization")
view.show()
time.sleep(10)    
view.png() '''

"""
#Part.2) Loading and Simulating MD Trajectory
using MDAnalysis and py3Dmol



"""

#!pip install MDAnalysis py3Dmol
#getting trajectory and topology files
!wget https://github.com/pb3lab/ibm3202/raw/master/files/md_files/1ihv_mon_protPBC.xtc
!wget https://github.com/pb3lab/ibm3202/raw/master/files/md_files/1ihv_mon_protPBC.gro

! pip install MDAnalysis
import MDAnalysis as mda 
import py3Dmol

"""In order to visualize an MD simulation we'll need a file with the **topology** of the protein simulated (this could be a *pdb, gro, etc* and in this case this correspond to the `1ihv_mon_protPBC.gro` file) and a file with the **trajectory** (`1ihv_mon_protPBC.xtc`). We'll create variables with the path related to each one: """

top = '1ihv_mon_protPBC.gro'
traj_end = '1ihv_mon_protPBC.xtc'

"""The `MDAnalysis.Universe` class allows us to read the results of the simulation. The first argument of the function correspond to the topology file and the second to the trajectory. In addition we must specify the number of frames of the simulation as the size of the trajectory. """

# Instance of the Universe class
u = mda.Universe(top, traj_end)

# The number of frames in the simulation
number_frames_analysis = len(u.trajectory)

if number_frames_analysis > 10:
  stride_animation = number_frames_analysis/100
else:
  stride_animation = 1

"""These classes will be neccesary to read and create the simulation PDB files."""

# Helper classes to read and get PDB fields
import warnings
warnings.filterwarnings('ignore')
!rm [0-9]?.pdb 2> /dev/null

class Atom(dict):
  def __init__(self, line):
    self["type"] = line[0:6].strip()
    self["idx"] = line[6:11].strip()
    self["name"] = line[12:16].strip()
    self["resname"] = line[17:20].strip()
    self["resid"] = int(int(line[22:26]))
    self["x"] = float(line[30:38])
    self["y"] = float(line[38:46])
    self["z"] = float(line[46:54])
    self["sym"] = line[76:78].strip()

  def __str__(self):
    line = list(" " * 80)
    line[0:6] = self["type"].ljust(6)
    line[6:11] = self["idx"].ljust(5)
    line[12:16] = self["name"].ljust(4)
    line[17:20] = self["resname"].ljust(3)
    line[22:26] = str(self["resid"]).ljust(4)
    line[30:38] = str(self["x"]).rjust(8)
    line[38:46] = str(self["y"]).rjust(8)
    line[46:54] = str(self["z"]).rjust(8)
    line[76:78] = self["sym"].rjust(2)
    return "".join(line) + "\n"
        
class Molecule(list):
  def __init__(self, file):
    for line in file:
      if "ATOM" in line or "HETATM" in line:
        self.append(Atom(line))
            
    def __str__(self):
      outstr = ""
      for at in self:
        outstr += str(at)
      return outstr

"""In the next step we will divide the trajectory positions into frames for the animation. For each frame we will save a PDB file (many files will appear in your working directory, don't panic)."""

# Write out frames for animation
# IMPORTANT: This line will filter the WATER molecules.
protein = u.select_atoms('not (resname WAT)') 
i = 0
for ts in u.trajectory[0:len(u.trajectory):int(stride_animation)]: 
    if i > -1:
        with mda.Writer('' + str(i) + '.pdb', protein.n_atoms) as W:
            W.write(protein)
    i = i + 1
# Load frames as molecules (py3Dmol let us visualize a single "molecule" per frame)
molecules = []
for i in range(int(len(u.trajectory)/int(stride_animation))):
    with open('' + str(i) + '.pdb') as ifile:
        molecules.append(Molecule(ifile))

models = ""
for i in range(len(molecules)):
  models += "MODEL " + str(i) + "\n"
  for j,mol in enumerate(molecules[i]):
    models += str(mol)
  models += "ENDMDL\n"

"""Finally, we will create our simulation of the trajectory. This section will take some time (**~1 minute**). """

# Animation
view = py3Dmol.view(width=800, height=600)
view.addModelsAsFrames(models)
for i, at in enumerate(molecules[0]):
    default = {"cartoon": {'color': 'spectrum'}}
    view.setStyle({'model': -1, 'serial': i+1}, at.get("pymol", default))

view.zoomTo()
# We can make an infinite loop with the animation or reduce the animation time with the reps argument. 
# reps: 0 means infinite loop
view.animate({'loop': "forward", 'reps': 0})
view.show()

"""I have compiled the above code in single function for ease of use."""

def MD_visualization(top, traj_end):
  """
  Inputs: 
  top : path to the topology file
  traj_end : path to the trajectory file
  """
  # Instance of the Universe class
  u = mda.Universe(top, traj_end)

  # The number of frames in the simulation
  number_frames_analysis = len(u.trajectory)
  if number_frames_analysis > 10:
    stride_animation = number_frames_analysis/100
  else:
    stride_animation = 1

  # Deleting previously stored frames as PDBs and removing warnings
  import warnings
  warnings.filterwarnings('ignore')
  !rm [0-9]?.pdb 2> /dev/null
  
    # Helper classes to read and get PDB fields
  class Atom(dict):
    def __init__(self, line):
      self["type"] = line[0:6].strip()
      self["idx"] = line[6:11].strip()
      self["name"] = line[12:16].strip()
      self["resname"] = line[17:20].strip()
      self["resid"] = int(int(line[22:26]))
      self["x"] = float(line[30:38])
      self["y"] = float(line[38:46])
      self["z"] = float(line[46:54])
      self["sym"] = line[76:78].strip()

    def __str__(self):
      line = list(" " * 80)
      line[0:6] = self["type"].ljust(6)
      line[6:11] = self["idx"].ljust(5)
      line[12:16] = self["name"].ljust(4)
      line[17:20] = self["resname"].ljust(3)
      line[22:26] = str(self["resid"]).ljust(4)
      line[30:38] = str(self["x"]).rjust(8)
      line[38:46] = str(self["y"]).rjust(8)
      line[46:54] = str(self["z"]).rjust(8)
      line[76:78] = self["sym"].rjust(2)
      return "".join(line) + "\n"
          
  class Molecule(list):
    def __init__(self, file):
      for line in file:
        if "ATOM" in line or "HETATM" in line:
          self.append(Atom(line))
              
      def __str__(self):
        outstr = ""
        for at in self:
          outstr += str(at)
        return outstr
  # Write out frames for animation
  # IMPORTANT: This line will filter the WATER molecules.
  protein = u.select_atoms('not (resname WAT)') 
  i = 0
  for ts in u.trajectory[0:len(u.trajectory):int(stride_animation)]: 
      if i > -1:
          with mda.Writer('' + str(i) + '.pdb', protein.n_atoms) as W:
              W.write(protein)
      i = i + 1
  # Load frames as molecules (py3Dmol let us visualize a single "molecule" per frame)
  molecules = []
  for i in range(int(len(u.trajectory)/int(stride_animation))):
      with open('' + str(i) + '.pdb') as ifile:
          molecules.append(Molecule(ifile))

  models = ""
  for i in range(len(molecules)):
    models += "MODEL " + str(i) + "\n"
    for j,mol in enumerate(molecules[i]):
      models += str(mol)
    models += "ENDMDL\n"

  # Animation
  view = py3Dmol.view(width=800, height=600)
  view.addModelsAsFrames(models)
  for i, at in enumerate(molecules[0]):
      default = {"cartoon": {'color': 'spectrum'}}
      view.setStyle({'model': -1, 'serial': i+1}, at.get("pymol", default))

  view.zoomTo()
  view.animate({'loop': "forward", 'reps': 0})
  return view

view = MD_visualization(top, traj_end)
view.show()

"""Using the *nglview* python library

**NGLview** have a widget for Python and Jupyter Notebooks, but unfortunately does not work in google colab
"""

!pip install nglview
import nglview as nv

# This is esential in order to display de nglview widget in Colab.
from google.colab import output
output.enable_custom_widget_manager()

protein = mda.Universe(top, traj_end)
view = nv.show_mdanalysis(protein)
view

"""# 3D protein Imaging using py3Dmol

"""

##Here write down the code to install py3Dmol
!pip install py3Dmol

import py3Dmol

p = py3Dmol.view(query='mmtf:1ycr')
p.setStyle({'cartoon': {'color':'spectrum'}})
p.addStyle({'within':{'distance': 5, 'sel':{'resi':21}}},{'stick':{'colorscheme':'blue'}})

xyz = '''4
* (null), Energy   -1000.0000000
N     0.000005    0.019779   -0.000003   -0.157114    0.000052   -0.012746
H     0.931955   -0.364989    0.000003    1.507100   -0.601158   -0.004108
H    -0.465975   -0.364992    0.807088    0.283368    0.257996   -0.583024
H    -0.465979   -0.364991   -0.807088    0.392764    0.342436    0.764260
'''

xyzview = py3Dmol.view(width=400,height=400)
xyzview.addModel(xyz,'xyz',{'vibrate': {'frames':10,'amplitude':1}})
xyzview.setStyle({'stick':{}})
xyzview.setBackgroundColor('0xeeeeee')
xyzview.animate({'loop': 'backAndForth'})
xyzview.zoomTo()
xyzview.show()

"""Display local file."""

benz='''
     RDKit          3D

  6  6  0  0  0  0  0  0  0  0999 V2000
   -0.9517    0.7811   -0.6622 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.2847    1.3329   -0.3121 C   0  0  0  0  0  0  0  0  0  0  0  0
    1.2365    0.5518    0.3512 C   0  0  0  0  0  0  0  0  0  0  0  0
    0.9517   -0.7811    0.6644 C   0  0  0  0  0  0  0  0  0  0  0  0
   -0.2847   -1.3329    0.3144 C   0  0  0  0  0  0  0  0  0  0  0  0
   -1.2365   -0.5518   -0.3489 C   0  0  0  0  0  0  0  0  0  0  0  0
  1  2  2  0
  2  3  1  0
  3  4  2  0
  4  5  1  0
  5  6  2  0
  6  1  1  0
M  END
$$$$'''
view = py3Dmol.view()
view.addModel(benz,'sdf')
view.setStyle({'stick':{}})
view.setStyle({'model':0},{'stick':{'colorscheme':'cyanCarbon'}})
view.zoomTo()

"""You can create a single canvas object with multiple viewers arrayed in a grid (3Dmol.createViewerGrid)."""

view = py3Dmol.view(query='pdb:1dc9',linked=False,viewergrid=(2,2))
view.setViewStyle({'style':'outline','color':'black','width':0.1})
view.setStyle({'cartoon':{'arrows':True, 'tubes':True, 'style':'oval', 'color':'white'}},viewer=(0,1))
view.setStyle({'stick':{'colorscheme':'greenCarbon'}},viewer=(1,0))
view.setStyle({'cartoon':{'color':'spectrum'}},viewer=(1,1))
view.removeAllModels(viewer=(0,0))
view.addModel(benz,'sdf',viewer=(0,0))
view.setStyle({'stick':{}},viewer=(0,0))
view.zoomTo(viewer=(0,0))
view.render()

view = py3Dmol.view(query='pdb:1ycr')
chA = {'chain':'A'}
chB = {'chain':'B'}
view.setStyle(chA,{'cartoon': {'color':'spectrum'}})
view.addSurface(py3Dmol.VDW,{'opacity':0.7,'color':'white'}, chA)
view.setStyle(chB,{'stick':{}})
view.show()

view = py3Dmol.view(query='pdb:5ire',options={'doAssembly':True})
view.setStyle({'cartoon':{'color':'spectrum'}})
view.show()

"""


Color by temperature factors"""

view = py3Dmol.view(query='pdb:1ycr')
view.setStyle({'cartoon': {'color':'white'}})
view.addSurface(py3Dmol.VDW,{'opacity':0.7,'colorscheme':{'prop':'b','gradient':'sinebow','min':0,'max':70}})

"""Generate an inline image of what is currently in the viewer (all white if the structure hasn't loaded yet)."""

png = view.png()
png

import requests, base64
r = requests.get('https://mmtf.rcsb.org/v1.0/full/5lgo')
view = py3Dmol.view()
view.addModel(base64.b64encode(r.content).decode(),'mmtf')
view.addUnitCell()
view.zoomTo()