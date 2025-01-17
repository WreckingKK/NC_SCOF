import sys
from io import StringIO
from xml.etree import cElementTree
import numpy as np
from sys import argv
import pandas as pd
from scipy.spatial import cKDTree

class Xml(object):
    def __init__(self, filename, needed=None):
        tree = cElementTree.ElementTree(file=filename)
        root = tree.getroot()
        self.nodes = {}
        needed = [] if needed is None else needed
        for key in root[0].attrib:
            self.__dict__[key] = int(root[0].attrib[key])
        for element in root[0]:
            if (len(needed) > 0) and (element.tag not in needed):
                continue
            self.nodes[element.tag] = pd.read_csv(StringIO(element.text),
                                                     delim_whitespace=True,
                                                     squeeze=1,
                                                     header=None,
                                                     ).values

lx = 200.0
ly = 200.0
lz = 200.0

fnames = sys.argv[1:]
for k, fname in enumerate(fnames):
    xml = Xml(fname, needed=['position', 'type', 'bond'])
    #pos = xml.nodes['position'][3328:4160, :] #A6
    #pos = xml.nodes['position'][4160:5120, :] #A7
    #pos = xml.nodes['position'][5120:6208, :] #A8
    #pos = xml.nodes['position'][6208:7440, :] #A9
    #pos = xml.nodes['position'][7440:8816, :] #A10
    pos = xml.nodes['position'][8816:10352, :] #A11
    #type = xml.nodes['type'][3328:4160] #A6
    #type = xml.nodes['type'][4160:5120]#A7
    #type = xml.nodes['type'][5120:6208] #A8
    #type = xml.nodes['type'][6208:7440] #A9
    #type = xml.nodes['type'][7440:8816] #A10
    type = xml.nodes['type'][8816:10352] #A11
    bonds = xml.nodes['bond']
    #ABbonds = bonds[bonds[:, 0] == 'A6-B6'][:, :]
    #ABbonds[:,1:] = ABbonds[:,1:]-3328
    #BBbonds = bonds[bonds[:, 0] == 'B6-B6'][:, :]
    #BBbonds[:,1:] = BBbonds[:,1:]-3328
    
    #ABbonds = bonds[bonds[:, 0] == 'A7-B7'][:, :]
    #ABbonds[:,1:] = ABbonds[:,1:]-4160
    #BBbonds = bonds[bonds[:, 0] == 'B7-B7'][:, :]
    #BBbonds[:,1:] = BBbonds[:,1:]-4160

    #ABbonds = bonds[bonds[:, 0] == 'A8-B8'][:, :]
    #ABbonds[:,1:] = ABbonds[:,1:]-5120
    #BBbonds = bonds[bonds[:, 0] == 'B8-B8'][:, :]
    #BBbonds[:,1:] = BBbonds[:,1:]-5120

    #ABbonds = bonds[bonds[:, 0] == 'A9-B9'][:, :]
    #ABbonds[:,1:] = ABbonds[:,1:]-6208
    #BBbonds = bonds[bonds[:, 0] == 'B9-B9'][:, :]
    #BBbonds[:,1:] = BBbonds[:,1:]-6208

    #ABbonds = bonds[bonds[:, 0] == 'A10-B10'][:, :]
    #ABbonds[:,1:] = ABbonds[:,1:]-7440
    #BBbonds = bonds[bonds[:, 0] == 'B10-B10'][:, :]
    #BBbonds[:,1:] = BBbonds[:,1:]-7440

    ABbonds = bonds[bonds[:, 0] == 'A11-B11'][:, :]
    ABbonds[:,1:] = ABbonds[:,1:]-8816
    BBbonds = bonds[bonds[:, 0] == 'B11-B11'][:, :]
    BBbonds[:,1:] = BBbonds[:,1:]-8816

    allbond = np.vstack((ABbonds, BBbonds))


    opd=open("19" + str(fname),"w")     
    opd.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    opd.write('<galamost_xml version="1.6">\n')
    opd.write('<configuration time_step="0" dimensions="3" natoms="'+str(len(pos))+'" >\n')
    opd.write('<box lx="'+str(lx)+'" ly="'+str(ly)+'" lz="'+str(lz)+'" xy="0" xz="0" yz="0"/>\n') #
    opd.write('<position num="'+str(len(pos))+'">\n')
    for i in range(0, len(pos)):
        opd.write(str(pos[i][0])+"  "+str(pos[i][1])+"  "+str(pos[i][2])+"\n")
    opd.write('</position>\n')
    opd.write('<type num="'+str(len(type))+'">\n')
    for i in range(0, len(type)):
        opd.write(type[i]+"\n")
    opd.write('</type>\n')
    opd.write('<bond num="'+str(len(allbond))+'">\n')
    for i in range(0, len(allbond)):
        opd.write(allbond[i][0]+"  "+str(allbond[i][1])+"  "+str(allbond[i][2])+"\n")
    opd.write('</bond>\n')
    opd.write('</configuration>\n')
    opd.write('</galamost_xml>\n')
    opd.close()


