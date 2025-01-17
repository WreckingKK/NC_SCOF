import sys
from rdkit import Chem
from rdkit.Chem import Draw
import numpy as np
from sys import argv
from io import StringIO
from xml.etree import cElementTree
import pandas as pd 

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

mylog = open('degree.log', mode = 'a', encoding = 'utf-8')

fnames = sys.argv[1:]
for k, fname in enumerate(fnames):
    xml = Xml(fname, needed=['position', 'bond'])
    positions = xml.nodes['position']
    bonds = xml.nodes['bond']
    num_cols = bonds.shape[1]
    new_bond = list(range(num_cols - 1, -1, -1))
    bonds = bonds[:, new_bond] 

# 创建RDKit分子对象
    mol = Chem.MolFromSmiles('')  
    molw = Chem.RWMol(mol)
#print(bonds)
    for i, (x, y, z) in enumerate(positions):
        atom = Chem.Atom('C')  # any type
        atom.SetDoubleProp('x', x)
        atom.SetDoubleProp('y', y)
        atom.SetDoubleProp('z', z)
        molw.AddAtom(atom)
    # 设置键的连接信息
    for atom1_idx, atom2_idx, bond_type in bonds:
        molw.AddBond(atom1_idx, atom2_idx, Chem.BondType.SINGLE)
    
    m = Chem.MolToSmiles(molw)    
    m = Chem.MolFromSmiles(m)
    ring_info = m.GetRingInfo()
    tar_rings = []  
# 遍历 ring_info 中的所有环
    for ring in ring_info.AtomRings():
        # 检查每个环是否由18个原子组成
        if len(ring) == 18:
            tar_rings.append(ring)
# tar_rings.append(ring)
    crysdeg = 8*100*len(tar_rings)/len(positions)
    print(str(fname), len(tar_rings), crysdeg, file = mylog)
mylog.close()

#viewer = Draw.MolToImage(molw)
#viewer.show()
