#!/usr/bin/env python
import os, shutil
from jupyter_client.kernelspec import KernelSpecManager
json ="""{"argv":["python","-m","jansiokernel", "-f", "{connection_file}"],
 "display_name":"io"
}"""

svg = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   width="300"
   height="300"
   viewBox="0 0 79.374998 79.375"
   version="1.1"
   id="svg5"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg">
  <defs
     id="defs2" />
  <g
     id="layer1">
    <rect
       style="fill:#191919;stroke-width:1.32292;stroke-linecap:square;stroke-miterlimit:7;fill-opacity:1"
       id="rect234"
       width="79.375"
       height="79.375"
       x="0"
       y="0"
       ry="9.8798771" />
    <text
       xml:space="preserve"
       style="font-style:normal;font-weight:normal;font-size:88.1944px;line-height:1.25;font-family:sans-serif;fill:#000000;fill-opacity:1;stroke:none;stroke-width:0.264583"
       x="6.5705061"
       y="68.747551"
       id="text945"><tspan
         id="tspan943"
         style="font-style:normal;font-variant:normal;font-weight:normal;font-stretch:normal;font-size:88.1944px;font-family:MovatifW00-Bold;-inkscape-font-specification:MovatifW00-Bold;fill:#faf8ea;stroke-width:0.264583"
         x="6.5705061"
         y="68.747551">io</tspan></text>
  </g>
</svg>
"""

def install_kernelspec():
    kerneldir = "/tmp/jansiokernel/"
    print('Creating tmp files...', end="")
    os.mkdir(kerneldir)

    with open(kerneldir + "kernel.json", "w") as f:
        f.write(json)

    with open(kerneldir + "logo-svg.svg", "w") as f:
        f.write(svg)
        
    print(' Done!')
    print('Installing Jupyter kernel...', end="")
    
    ksm = KernelSpecManager()
    ksm.install_kernel_spec(kerneldir, 'jansiokernel', user=os.getenv('USER'))
    
    print(' Done!')
    print('Cleaning up tmp files...', end="")
    
    shutil.rmtree(kerneldir)
    
    print(' Done!')
    print('For uninstall use: jupyter kernelspec uninstall jansiokernel')