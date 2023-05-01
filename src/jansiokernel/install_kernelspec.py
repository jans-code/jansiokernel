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
    <path
       d="M 9.3045324,68.747551 H 21.29897 V 25.355908 H 9.3045324 Z m 0,-48.595113 H 21.29897 V 9.4809162 H 9.3045324 Z"
       style="font-size:88.1944px;line-height:1.25;stroke-width:0.264583;font-family:MovatifW00-Bold;-inkscape-font-specification:MovatifW00-Bold;fill:#faf8ea"
       id="path306" />
    <path
       d="m 47.933674,69.894078 c 3.351387,0 6.438191,-0.529166 9.172217,-1.587499 2.734027,-1.058333 5.027081,-2.645832 6.967358,-4.674303 1.940276,-1.940277 3.351387,-4.321526 4.409719,-7.143746 1.058333,-2.822221 1.5875,-5.909025 1.5875,-9.436801 0,-3.439581 -0.529167,-6.614579 -1.5875,-9.4368 -1.058332,-2.822221 -2.469443,-5.20347 -4.409719,-7.143746 -1.940277,-1.940277 -4.233331,-3.527776 -6.967358,-4.586109 -2.734026,-1.058333 -5.82083,-1.675694 -9.172217,-1.675694 -3.527776,0 -6.61458,0.617361 -9.348606,1.675694 -2.822221,1.058333 -5.115275,2.645832 -7.055552,4.586109 -1.940277,2.028471 -3.439581,4.40972 -4.497914,7.23194 -1.058333,2.822221 -1.499305,5.997219 -1.499305,9.348606 0,3.351387 0.440972,6.438191 1.499305,9.260412 1.058333,2.822221 2.469443,5.291664 4.40972,7.231941 1.940276,2.028471 4.233331,3.61597 7.055551,4.674303 2.734027,1.146527 5.909025,1.675693 9.436801,1.675693 z m 0,-10.054161 c -6.702774,0 -10.054161,-4.233331 -10.054161,-12.788188 0,-4.321525 0.793749,-7.496523 2.469443,-9.613189 1.675693,-2.028471 4.233331,-3.086804 7.584718,-3.086804 3.351387,0 5.909025,1.058333 7.584718,3.086804 1.675694,2.116666 2.557638,5.291664 2.557638,9.613189 0,8.554857 -3.439582,12.788188 -10.142356,12.788188 z"
       style="font-size:88.1944px;line-height:1.25;stroke-width:0.264583;font-family:MovatifW00-Bold;-inkscape-font-specification:MovatifW00-Bold;fill:#faf8ea"
       id="path308" />
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