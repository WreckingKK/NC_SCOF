import numpy as np
import sys
from io import StringIO
from xml.etree import cElementTree
from pandas import read_csv

def pbc(a, box):
    return a - box * np.round(a / box)

class xml_parser(object):
    def __init__(self, filename, needed=[]):
        tree = cElementTree.ElementTree(file=filename)
        root = tree.getroot()
        c = root[0]
        self.nodes = {}
        self.config = c.attrib
        for e in c:
            if e.tag == 'box':
                self.box = np.array([float(e.attrib['lx']), float(e.attrib['ly']), float(e.attrib['lz'])])
                continue
            if ((len(needed) != 0) and (e.tag not in needed)):
                continue
            if e.attrib['num'] == '0':
                continue
            self.nodes[e.tag] = read_csv(StringIO(e.text), delim_whitespace=True, squeeze=1, header=None).values

class Node(object):
    def __init__(self, head=None, layer=None):
        if type(head) in [np.ndarray, list, tuple]:
            self.head = [int(_) for _ in head]
        else:
            self.head = [int(head)]
        self.childs = []
        self.n = layer

    def add_child(self, node):
        if type(node) in [np.ndarray, list, tuple]:
            [self.childs.append(_) for _ in node]
        else:
            self.childs.append(_)

    def __repr__(self):
        return "<Node-%d nchilds-%d>" % (self.n, len(self.childs))

def analyze_topol_from_bonds(allbonds, natoms):
    atomstatus = []
    cnt_chains = 0
    allchains = []
    for i in range(natoms):
        if i in atomstatus: continue

        ichain = []

        row, col = np.where(allbonds == i)
        linkcol = np.fabs(col - 1).astype(int)

        link = allbonds[row, linkcol]

        root = Node(i, 0)
        ichilds = allbonds[row, linkcol]
        if len(ichilds) != 0:
            root.add_child(allbonds[row, linkcol])

        # append atoms into ichain
        ichain.extend(root.head)
        if len(root.childs) != 0:
            ichain.extend(root.childs)

        atomstatus.extend(root.head)
        atomstatus.extend(root.childs)

        parent = root
        if len(parent.childs) !=0:
            pass
            # print("============= %d'th chain root_atom_index:%d"%(cnt_chains, i))
            # print("0'th layers", parent.childs)

        cnt_layer = 1
        while True:
            ichilds = []
            for c in parent.childs:
                
                row, col = np.where(allbonds == c)
                if row.shape[0] == 0:
                    continue
                invcol = np.fabs(col - 1).astype(int)
                link = allbonds[row, invcol]
                for _ in link:
                    if _ not in atomstatus:
                        ichilds.append(_)
                        atomstatus.append(_)

            # break if no childs found
            if len(ichilds) == 0:
                break

            # print("%d'th layers"%(cnt_layer), ichilds)

            root = Node(parent.childs, cnt_layer)
            root.add_child(ichilds)

            # append childs to ichain
            ichain.extend(ichilds)

            # assign new parent
            parent = root

            # cnt layer increment
            cnt_layer += 1

        # print("    search statistics------ %d atoms"%(len(ichain)))
        # print("    ", ichain)


        # append ichain into allchains
        allchains.append(ichain)

        # cnt chains increment
        cnt_chains += 1

    return allchains

class Cluster(object):
    def __init__(self, units, index_frame=0):
        self.units_list = [units]
        self.nunits = [units.shape[0]]
        self.index_frame = [index_frame]
        self.index_units = [np.floor(units[:, 0] / 4).astype(int)]
        self.status = [False]

    def change_status(self):
        self.status.append(True)

    def change_units(self, units, index_frame=0):
        self.units_list.append(units)
        self.nunits.append(units.shape[0])
        self.index_frame.append(index_frame)
        self.index_units.append([np.floor(units[:, 0] / 4).astype(int)])
        self.status.append(False)

mylog = open('yield.log', mode = 'a', encoding = 'utf-8')
# main
fnames = sys.argv[1:]

ClusterList = {}
for i, fname in enumerate(fnames):
    xml = xml_parser(fname)
    time_step = xml.config['time_step']
    pos = xml.nodes['position']
    bonds = xml.nodes['bond']
    box = xml.box

    print(">>> Processing %d'th frames @time_step: %s @%s"%(i, time_step, fname))

    allchains = analyze_topol_from_bonds(bonds[:, 1:].astype(int), pos.shape[0])

    threshold_nunits = 4

    # build cluster object from chains
    for chain in allchains:
        units = np.sort(np.array(chain, dtype=int)).reshape(-1, 4)
        if units.shape[0] < 2:
            continue

        index_units = np.floor(units[:, 0] / 4).astype(int)
        name_cluster = 'frame[%s]-nunits[%d]-1st[%d]'%(time_step, index_units.shape[0], index_units[0])
        if i == 0:
            if units.shape[0] > 4:
                ClusterList[name_cluster] = Cluster(units, time_step)
        else:
            onekey = []
            for key, cls in ClusterList.items():
                # Jaccard coefficent
                sim = np.intersect1d(index_units, cls.index_units[-1]).shape[0] / np.union1d(index_units, cls.index_units[-1]).shape[0]
                onekey.append((key, sim))

            if len(onekey) == 0:
                if index_units.shape[0] <= threshold_nunits:
                    continue
                ClusterList[name_cluster] = Cluster(units, time_step)
            else:
                onekey = np.array(onekey, dtype=object)
                if onekey[:, 1].sum() == 0.0:
                    if index_units.shape[0] <= threshold_nunits:
                        continue
                    ClusterList[name_cluster] = Cluster(units, time_step)
                else:
                    index = onekey[:, 1].argmax()
                    key = onekey[index][0]
                    if ClusterList[key].status[-1] == False:
                        ClusterList[key].status[-1] = True
                        ClusterList[key].change_units(units, time_step)

    # check all cluster
    for key in list(ClusterList.keys()):
        if ClusterList[key].nunits[-1] < threshold_nunits:
            del ClusterList[key]
            print("del %s"%(key))
    
    if len(ClusterList) == 0:
        print("no nclusters found!")
    else:
        stat_nunits = np.sort(np.array([ClusterList[key].nunits[-1] for key in ClusterList.keys()]))
        print("nclusters:%d  nmax:%d nmin:%d"%(stat_nunits.shape[0], stat_nunits.max(), stat_nunits.min()), stat_nunits)
    pro = 4*100*np.sum(stat_nunits)/len(pos)
    print(str(fname), pro, file = mylog)

mylog.close()
#print(ClusterList[maxcls_name].nunits, file = mylog)
#print(ClusterList[maxcls_name].units_list)

