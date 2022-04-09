<h1 class="code-line" data-line-start=0 data-line-end=1 ><a id="BT305_Supernumerary_Assignment_0"></a>BT305 Supernumerary Assignment</h1>
<h2 class="code-line" data-line-start=1 data-line-end=2 ><a id="Aditya_Bajaj_190106006_1"></a>Aditya Bajaj; 190106006</h2>
<p class="has-line-data" data-line-start="3" data-line-end="4">Main Idea: Visualizing and Comparing Molecular Structures using MDAnalysis and py3Dmol</p>
<p class="has-line-data" data-line-start="5" data-line-end="7">Introduction:<br>
The PDB file contains information of all the experimental conditions that allowed obtaining a given three-dimensional protein structure (contained in the PDB file), as well as information about the biological features of the protein and the overall features of the crystal structure (cell unit, dimensions, number of monomers, biological assembly, etc.). However, its most relevant body of corresponds to the <strong>coordinates</strong> (i.e. the three-dimensional positions) of the atoms of a structure of a given protein.</p>
<p class="has-line-data" data-line-start="8" data-line-end="9"><img src="https://raw.githubusercontent.com/pb3lab/ibm3202/master/images/pdbformat_01.png" alt="alt text"></p>
<p class="has-line-data" data-line-start="10" data-line-end="11">In which <strong>ATOM</strong> (or HETATM) indicates that the line contains information of atomic coordinates, a unique number for each atom (a list that is also referred to as index), its atom type, the residue name to which a given atom belongs to, the polypeptide chain in which this residue is located, the position or number of the residue in the primary sequence, and the cartesian atomic coordinates of each atom. Any molecule (protein or not) can be written in this format, as long as we have the cartesian coordinates for each of its atoms.</p>
<p class="has-line-data" data-line-start="12" data-line-end="16">##Important<br>
Progamming Language: Python3.7<br>
Notebook: Google Colab<br>
Modules used and must install: biopython, py3Dmol, MDAnalysis</p>
<h2 class="code-line" data-line-start=16 data-line-end=17 ><a id="Installation_16"></a>Installation</h2>
<pre><code class="has-line-data" data-line-start="19" data-line-end="23" class="language-sh">! pip install biopython
! pip install py3Dmol
! pip install MDAnalysis
</code></pre>
<h2 class="code-line" data-line-start=25 data-line-end=26 ><a id="Part1_Retrieving_and_visualizing_structures_from_PDB_25"></a>Part.1) Retrieving and visualizing structures from PDB</h2>
<ul>
<li class="has-line-data" data-line-start="27" data-line-end="28">Choosing 6ANE.pdb</li>
<li class="has-line-data" data-line-start="28" data-line-end="29">Code to retrieve 6ANE.pdb</li>
<li class="has-line-data" data-line-start="29" data-line-end="30">Checking basic information like chains and residues.</li>
<li class="has-line-data" data-line-start="30" data-line-end="31">Using Biopython to get information from PDB of each chain.</li>
<li class="has-line-data" data-line-start="31" data-line-end="32">Installing and using py3Dmol to visualising the structure.</li>
<li class="has-line-data" data-line-start="32" data-line-end="33">Finding different uses and ways to visualise.</li>
</ul>
<h2 class="code-line" data-line-start=36 data-line-end=37 ><a id="Part2_Loading_and_Simulating_MD_Trajectory_36"></a>Part.2) Loading and Simulating MD Trajectory</h2>
<ul>
<li class="has-line-data" data-line-start="38" data-line-end="39">Installing and Importing MDAnalyis</li>
<li class="has-line-data" data-line-start="39" data-line-end="40">Getting trajectory and topology files</li>
<li class="has-line-data" data-line-start="40" data-line-end="41">Creating MD_visualization function</li>
<li class="has-line-data" data-line-start="41" data-line-end="43">Simulating Trajectory</li>
</ul>
<h2 class="code-line" data-line-start=43 data-line-end=44 ><a id="Part3_3D_Protein_Imaging_and_Simulation_using_py3Dmol_43"></a>Part.3) 3D Protein Imaging and Simulation using py3Dmol</h2>
<p class="has-line-data" data-line-start="46" data-line-end="47">For production environments…</p>
<pre><code class="has-line-data" data-line-start="49" data-line-end="52" class="language-sh">npm install --production
NODE_ENV=production node app
</code></pre>
<h2 class="code-line" data-line-start=53 data-line-end=54 ><a id="Plugins_53"></a>Plugins</h2>
<p class="has-line-data" data-line-start="55" data-line-end="57">Dillinger is currently extended with the following plugins.<br>
Instructions on how to use them in your own application are linked below.</p>
<table class="table table-striped table-bordered">
<thead>
<tr>
<th>Plugin</th>
<th>README</th>
</tr>
</thead>
<tbody>
<tr>
<td>Dropbox</td>
<td><a href="https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md">plugins/dropbox/README.md</a></td>
</tr>
<tr>
<td>GitHub</td>
<td><a href="https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md">plugins/github/README.md</a></td>
</tr>
<tr>
<td>Google Drive</td>
<td><a href="https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md">plugins/googledrive/README.md</a></td>
</tr>
<tr>
<td>OneDrive</td>
<td><a href="https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md">plugins/onedrive/README.md</a></td>
</tr>
<tr>
<td>Medium</td>
<td><a href="https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md">plugins/medium/README.md</a></td>
</tr>
<tr>
<td>Google Analytics</td>
<td><a href="https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md">plugins/googleanalytics/README.md</a></td>
</tr>
</tbody>
</table>
<h2 class="code-line" data-line-start=67 data-line-end=68 ><a id="Development_67"></a>Development</h2>
<p class="has-line-data" data-line-start="69" data-line-end="70">Want to contribute? Great!</p>
<p class="has-line-data" data-line-start="71" data-line-end="73">Dillinger uses Gulp + Webpack for fast developing.<br>
Make a change in your file and instantaneously see your updates!</p>
<p class="has-line-data" data-line-start="74" data-line-end="75">Open your favorite Terminal and run these commands.</p>
<p class="has-line-data" data-line-start="76" data-line-end="77">First Tab:</p>
<pre><code class="has-line-data" data-line-start="79" data-line-end="81" class="language-sh">node app
</code></pre>
<p class="has-line-data" data-line-start="82" data-line-end="83">Second Tab:</p>
<pre><code class="has-line-data" data-line-start="85" data-line-end="87" class="language-sh">gulp watch
</code></pre>
<p class="has-line-data" data-line-start="88" data-line-end="89">(optional) Third:</p>
<pre><code class="has-line-data" data-line-start="91" data-line-end="93" class="language-sh">karma <span class="hljs-built_in">test</span>
</code></pre>
<h4 class="code-line" data-line-start=94 data-line-end=95 ><a id="Building_for_source_94"></a>Building for source</h4>
<p class="has-line-data" data-line-start="96" data-line-end="97">For production release:</p>
<pre><code class="has-line-data" data-line-start="99" data-line-end="101" class="language-sh">gulp build --prod
</code></pre>
<p class="has-line-data" data-line-start="102" data-line-end="103">Generating pre-built zip archives for distribution:</p>
<pre><code class="has-line-data" data-line-start="105" data-line-end="107" class="language-sh">gulp build dist --prod
</code></pre>
<h2 class="code-line" data-line-start=108 data-line-end=109 ><a id="Docker_108"></a>Docker</h2>
<p class="has-line-data" data-line-start="110" data-line-end="111">Dillinger is very easy to install and deploy in a Docker container.</p>
<p class="has-line-data" data-line-start="112" data-line-end="115">By default, the Docker will expose port 8080, so change this within the<br>
Dockerfile if necessary. When ready, simply use the Dockerfile to<br>
build the image.</p>
<pre><code class="has-line-data" data-line-start="117" data-line-end="120" class="language-sh"><span class="hljs-built_in">cd</span> dillinger
docker build -t &lt;youruser&gt;/dillinger:<span class="hljs-variable">${package.json.version}</span> .
</code></pre>
<p class="has-line-data" data-line-start="121" data-line-end="124">This will create the dillinger image and pull in the necessary dependencies.<br>
Be sure to swap out <code>${package.json.version}</code> with the actual<br>
version of Dillinger.</p>
<p class="has-line-data" data-line-start="125" data-line-end="128">Once done, run the Docker image and map the port to whatever you wish on<br>
your host. In this example, we simply map port 8000 of the host to<br>
port 8080 of the Docker (or whatever port was exposed in the Dockerfile):</p>
<pre><code class="has-line-data" data-line-start="130" data-line-end="132" class="language-sh">docker run <span class="hljs-operator">-d</span> -p <span class="hljs-number">8000</span>:<span class="hljs-number">8080</span> --restart=always --cap-add=SYS_ADMIN --name=dillinger &lt;youruser&gt;/dillinger:<span class="hljs-variable">${package.json.version}</span>
</code></pre>
<blockquote>
<p class="has-line-data" data-line-start="133" data-line-end="134">Note: <code>--capt-add=SYS-ADMIN</code> is required for PDF rendering.</p>
</blockquote>
<p class="has-line-data" data-line-start="135" data-line-end="137">Verify the deployment by navigating to your server address in<br>
your preferred browser.</p>
<pre><code class="has-line-data" data-line-start="139" data-line-end="141" class="language-sh"><span class="hljs-number">127.0</span>.<span class="hljs-number">0.1</span>:<span class="hljs-number">8000</span>
</code></pre>
<h2 class="code-line" data-line-start=142 data-line-end=143 ><a id="License_142"></a>License</h2>
<p class="has-line-data" data-line-start="144" data-line-end="145">MIT</p>
<p class="has-line-data" data-line-start="146" data-line-end="147"><strong>Free Software, Hell Yeah!</strong></p>
