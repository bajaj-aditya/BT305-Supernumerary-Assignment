<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="BT305_Supernumerary_Assignment_0"></a>BT305 Supernumerary Assignment</h1>
<h2 class="code-line" data-line-start=1 data-line-end=2 ><a id="Aditya_Bajaj_190106006_1"></a>Aditya Bajaj; 190106006</h2>
<p class="has-line-data" data-line-start="3" data-line-end="4">Main Idea: Visualizing and Comparing Molecular Structures using MDAnalysis and py3Dmol</p>
<hr>
<h2 class="code-line" data-line-start=6 data-line-end=7 ><a id="Information_6"></a>Information</h2>
<p class="has-line-data" data-line-start="7" data-line-end="12">Progamming Language: Python3.7<br>
Notebook: Google Colab<br>
Modules used and must install: biopython, py3Dmol, MDAnalysis<br>
Link of Project in Github: <a href="https://github.com/bajaj-aditya/BT305-Supernumerary-Assignment">https://github.com/bajaj-aditya/BT305-Supernumerary-Assignment</a><br>
Zip File Contains:</p>
<ol>
<li class="has-line-data" data-line-start="12" data-line-end="13"><a href="https://github.com/bajaj-aditya/BT305-Supernumerary-Assignment/blob/main/README.md">README.MD</a></li>
<li class="has-line-data" data-line-start="13" data-line-end="14"><a href="https://nbviewer.org/github/bajaj-aditya/BT305-Supernumerary-Assignment/blob/e9474b43dfad6101aae00ea8ab78d6adc3bcbc75/BT305 Program Notebook.ipynb">BT305 Program Notebook.ipynb</a></li>
<li class="has-line-data" data-line-start="13" data-line-end="14"><a href="https://github.com/bajaj-aditya/BT305-Supernumerary-Assignment/blob/32f1ec6cea77708d397ffb487110bb4ab1c4ab43/BT305%20-%20Supernumerary%20Assignment%20Executable.py">BT305 Program Executable.py</a></li>
</ol>
<hr>
<p class="has-line-data" data-line-start="15" data-line-end="19">Important:<br>

Recommendation: The work on this BT-305 Project was done on a jupyter notebook and not a python script, the exectuable generated is an automatic generation. Would advise you to directly check the notebook. 
Incase The .ipynb file(notebook) does not render or have some issues.<br>
Click on the below link.<br>
&quot;<a href="https://nbviewer.org/github/bajaj-aditya/BT305-Supernumerary-Assignment/blob/e9474b43dfad6101aae00ea8ab78d6adc3bcbc75/BT305%20Program%20Notebook.ipynb">Static and rendered HTML version of the file.</a>&quot;</p>
<p class="has-line-data" data-line-start="20" data-line-end="21">This is the rendered version of the jupyter notebook as a static HTML web page. This is easily shareable.</p>
<hr>
<h2 class="code-line" data-line-start=23 data-line-end=24 ><a id="Introduction_23"></a>Introduction</h2>
<p class="has-line-data" data-line-start="24" data-line-end="25">The PDB file contains information of all the experimental conditions that allowed obtaining a given three-dimensional protein structure (contained in the PDB file), as well as information about the biological features of the protein and the overall features of the crystal structure (cell unit, dimensions, number of monomers, biological assembly, etc.). However, its most relevant body of corresponds to the <strong>coordinates</strong> (i.e. the three-dimensional positions) of the atoms of a structure of a given protein.</p>
<p class="has-line-data" data-line-start="26" data-line-end="27"><img src="https://raw.githubusercontent.com/pb3lab/ibm3202/master/images/pdbformat_01.png" alt="alt text"></p>
<p class="has-line-data" data-line-start="28" data-line-end="29">In which <strong>ATOM</strong> (or HETATM) indicates that the line contains information of atomic coordinates, a unique number for each atom (a list that is also referred to as index), its atom type, the residue name to which a given atom belongs to, the polypeptide chain in which this residue is located, the position or number of the residue in the primary sequence, and the cartesian atomic coordinates of each atom. Any molecule (protein or not) can be written in this format, as long as we have the cartesian coordinates for each of its atoms.</p>
<h2 class="code-line" data-line-start=30 data-line-end=31 ><a id="Installation_30"></a>Installation</h2>
<p class="has-line-data" data-line-start="31" data-line-end="32">Use without the ‘!’ if running the script instead of the notebook.</p>
<pre><code class="has-line-data" data-line-start="33" data-line-end="38" class="language-sh">! pip install biopython
! pip install py3Dmol
! pip install MDAnalysis
! pip install wget
</code></pre>
<h2 class="code-line" data-line-start=40 data-line-end=41 ><a id="Part1_Retrieving_and_visualizing_structures_from_PDB_40"></a>Part.1) Retrieving and visualizing structures from PDB</h2>
<ul>
<li class="has-line-data" data-line-start="42" data-line-end="43">Choosing 6ANE.pdb</li>
<li class="has-line-data" data-line-start="43" data-line-end="44">Code to retrieve 6ANE.pdb</li>
<li class="has-line-data" data-line-start="44" data-line-end="45">Checking basic information like chains and residues.</li>
<li class="has-line-data" data-line-start="45" data-line-end="46">Using Biopython to get information from PDB of each chain.</li>
<li class="has-line-data" data-line-start="46" data-line-end="47">Installing and using py3Dmol to visualising the structure.</li>
<li class="has-line-data" data-line-start="47" data-line-end="48">Finding different uses and ways to visualise.</li>
</ul>
<h2 class="code-line" data-line-start=51 data-line-end=52 ><a id="Part2_Loading_and_Simulating_MD_Trajectory_51"></a>Part.2) Loading and Simulating MD Trajectory</h2>
<ul>
<li class="has-line-data" data-line-start="53" data-line-end="54">Installing and Importing MDAnalyis</li>
<li class="has-line-data" data-line-start="54" data-line-end="55">Getting trajectory and topology files</li>
<li class="has-line-data" data-line-start="55" data-line-end="56">Creating MD_visualization function</li>
<li class="has-line-data" data-line-start="56" data-line-end="58">Simulating Trajectory</li>
</ul>
<h2 class="code-line" data-line-start=58 data-line-end=59 ><a id="Part3_3D_Protein_Imaging_and_Simulation_using_py3Dmol_58"></a>Part.3) 3D Protein Imaging and Simulation using py3Dmol</h2>
<ul>
<li class="has-line-data" data-line-start="60" data-line-end="61">Exploring xyz view and different styles</li>
<li class="has-line-data" data-line-start="61" data-line-end="62">Color by Temperature Factors</li>
<li class="has-line-data" data-line-start="62" data-line-end="63">Generating an Inline Image of what’s in the viewer</li>
</ul>
<h2 class="code-line" data-line-start=66 data-line-end=67 ><a id="Thank_you_66"></a>Thank you</h2>
<p class="has-line-data" data-line-start="68" data-line-end="71"><strong>Thank you,<br>
Aditya Bajaj<br>
190106006</strong></p>
