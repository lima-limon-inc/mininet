#!/usr/bin/python

"""
Test bandwidth (using iperf) on linear networks of varying size, 
using both kernel and user datapaths.

Each network looks like:

h0 <-> s0 <-> s1 .. sN <-> h1

Note: by default, the reference controller only supports 16
switches, so this test WILL NOT WORK unless you have recompiled
your controller to support a 100 switches (or more.)
"""
   
from mininet import init, LinearNet, iperfTest

def linearBandwidthTest():

   datapaths = [ 'kernel', 'user' ]
   switchCounts = [ 1, 20, 40, 60, 80, 100 ]
   results = {}

   for datapath in datapaths:
      k = datapath == 'kernel'
      results[ datapath ] = []
      for switchCount in switchCounts: 
         print "*** Creating linear network of size", switchCount
         network = LinearNet( switchCount, k)
         bandwidth = network.run( iperfTest )
         results[ datapath ] += [ ( switchCount, bandwidth ) ]
         
   for datapath in datapaths:
      print
      print "*** Linear network results for", datapath, "datapath:"
      print
      result = results[ datapath ]  
      print "SwitchCount\tiperf Results"
      for switchCount, bandwidth in result:
         print switchCount, '\t\t', 
         print bandwidth[ 0 ], 'server, ', bandwidth[ 1 ], 'client'
      print
   print
      
if __name__ == '__main__':
   init()
   print "*** Running linearBandwidthTest"
   linearBandwidthTest()
   exit( 1 )

   