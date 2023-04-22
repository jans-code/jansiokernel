"""Main module"""
#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import jansiokernel
IPKernelApp.launch_instance(kernel_class=jansiokernel)
