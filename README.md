# wheel-diagram
Plot wheel diagram for alpha-helix.

# DEMO
Demonstration for a sequence "LEQLEQDCNDICERMKNVEKDFSN" from formin Fus1 in *Schizosaccharomyces pombe*.  
![Demo](./LEQLEQDC_wheel.png)
 
# Features
 
 The Kyte and Doolittle's hydrophobicity is used.  
 The hydrophobic moment is normalized by the sequence length.
 
# Requirement (validated version)
- Python (3.7.8)
 - matplotlib (3.3.1)
 
# Installation
  
Copy plot_wheel_diagram.py to wherever you like.
 
# Usage
  
```bash
python plot_wheel_diagram.py YOUR_SEQUENCE
```

Web version is also available [here](https://sites.google.com/view/morita-rikuri/%E3%83%84%E3%83%BC%E3%83%AB/plot-wheel-diagram).

# Note
  Helvetica is specified for default font.  
  If you have an error, remove font specification.  
  
  HTML version is available on the index.html.
# Author
 
- Rikuri Morita
- Center for Computational Sciences, University of Tsukuba
- morita@ccs.tsukuba.ac.jp
 
# License 
This script is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
