#!/usr/bin/python
from poetry import cu_gala as gala
from poetry import _options


filename = 'pn2d.xml'
build_method = gala.XMLReader(filename)
perform_config = gala.PerformConfig(_options.gpu)
all_info = gala.AllInfo(build_method, perform_config)

dt = 0.001
app = gala.Application(all_info, dt)

neighbor_list = gala.NeighborList(all_info, 1.5, 0.1)#(,rcut,rbuffer)

lj = gala.LJForce(all_info, neighbor_list, 1.5)# force rcut
lj.setParams("A0", "A0", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B0', 'B0', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A0', 'B0', 1.0, 1.0, 1.0, 2**(1.0/6.0))

lj.setParams("A1", "A1", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B1', 'B1', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A1', 'B1', 1.0, 1.0, 1.0, 2**(1.0/6.0))

lj.setParams("A2", "A2", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B2', 'B2', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A2', 'B2', 1.0, 1.0, 1.0, 2**(1.0/6.0))

lj.setParams("A3", "A3", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B3', 'B3', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A3', 'B3', 1.0, 1.0, 1.0, 2**(1.0/6.0))

lj.setParams("A4", "A4", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B4', 'B4', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A4', 'B4', 1.0, 1.0, 1.0, 2**(1.0/6.0))

lj.setParams("A5", "A5", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B5', 'B5', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A5', 'B5', 1.0, 1.0, 1.0, 2**(1.0/6.0))


lj.setParams("A6", "A6", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B6', 'B6', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A6', 'B6', 1.0, 1.0, 1.0, 2**(1.0/6.0))

lj.setParams("A7", "A7", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B7', 'B7', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A7', 'B7', 1.0, 1.0, 1.0, 2**(1.0/6.0))

lj.setParams("A8", "A8", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B8', 'B8', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A8', 'B8', 1.0, 1.0, 1.0, 2**(1.0/6.0))

lj.setParams("A9", "A9", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B9', 'B9', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A9', 'B9', 1.0, 1.0, 1.0, 2**(1.0/6.0))

lj.setParams("A10", "A10", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B10', 'B10', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A10', 'B10', 1.0, 1.0, 1.0, 2**(1.0/6.0))

lj.setParams("A11", "A11", 1.0, 1.0, 1.0, 2**(1.0/6.0)) # type1, type2, epsilon, sigma, alpha, r
lj.setParams('B11', 'B11', 1.0, 1.0, 1.0, 2**(1.0/6.0))
lj.setParams('A11', 'B11', 1.0, 1.0, 1.0, 2**(1.0/6.0))
app.add(lj)

all_info.addBondTypeByPairs()
all_info.addAngleTypeByPairs()

bf = gala.BondForceHarmonic(all_info)
bf.setParams('A0-B0',   1250.0, 1.0)#(,K0, R0)
bf.setParams('A1-B1',   1250.0, 1.0)#(,K0, R0)
bf.setParams('A2-B2',   1250.0, 1.0)#(,K0, R0)
bf.setParams('A3-B3',   1250.0, 1.0)#(,K0, R0)
bf.setParams('A4-B4',   1250.0, 1.0)#(,K0, R0)
bf.setParams('A5-B5',   1250.0, 1.0)#(,K0, R0)
bf.setParams('A6-B6',   1250.0, 1.0)#(,K0, R0)
bf.setParams('A7-B7',   1250.0, 1.0)#(,K0, R0)
bf.setParams('A8-B8',   1250.0, 1.0)#(,K0, R0)
bf.setParams('A9-B9',   1250.0, 1.0)#(,K0, R0)
bf.setParams('A10-B10', 1250.0, 1.0)#(,K0, R0)
bf.setParams('A11-B11', 1250.0, 1.0)#(,K0, R0)

bf.setParams('B0-B0', 1250.0, 1.0)#(,K0, R0)
bf.setParams('B1-B1', 1250.0, 1.0)#(,K0, R0)
bf.setParams('B2-B2', 1250.0, 1.0)#(,K0, R0)
bf.setParams('B3-B3', 1250.0, 1.0)#(,K0, R0)
bf.setParams('B4-B4', 1250.0, 1.0)#(,K0, R0)
bf.setParams('B5-B5', 1250.0, 1.0)#(,K0, R0)

bf.setParams('B6-B6', 1250.0, 1.0)#(,K0, R0)
bf.setParams('B7-B7', 1250.0, 1.0)#(,K0, R0)
bf.setParams('B8-B8', 1250.0, 1.0)#(,K0, R0)
bf.setParams('B9-B9', 1250.0, 1.0)#(,K0, R0)
bf.setParams('B10-B10', 1250.0, 1.0)#(,K0, R0)
bf.setParams('B11-B11', 1250.0, 1.0)#(,K0, R0)
app.add(bf)

af = gala.AngleForceHarmonic(all_info)
af.setParams('B0-A0-B0', 1000.0, 120)#(,K0, R0)
af.setParams('B1-A1-B1', 1000.0, 120)#(,K0, R0)
af.setParams('B2-A2-B2', 1000.0, 120)#(,K0, R0)
af.setParams('B3-A3-B3', 1000.0, 120)#(,K0, R0)
af.setParams('B4-A4-B4', 1000.0, 120)#(,K0, R0)
af.setParams('B5-A5-B5', 1000.0, 120)#(,K0, R0)
af.setParams('B6-A6-B6', 1000.0, 120)#(,K0, R0)
af.setParams('B7-A7-B7', 1000.0, 120)#(,K0, R0)
af.setParams('B8-A8-B8', 1000.0, 120)#(,K0, R0)
af.setParams('B9-A9-B9', 1000.0, 120)#(,K0, R0)
af.setParams('B10-A10-B10', 1000.0, 120)#(,K0, R0)
af.setParams('B11-A11-B11', 1000.0, 120)#(,K0, R0)

af.setParams('A0-B0-B0', 1000.0, 180)#(,K0, R0)
af.setParams('A1-B1-B1', 1000.0, 180)#(,K0, R0)
af.setParams('A2-B2-B2', 1000.0, 180)#(,K0, R0)
af.setParams('A3-B3-B3', 1000.0, 180)#(,K0, R0)
af.setParams('A4-B4-B4', 1000.0, 180)#(,K0, R0)
af.setParams('A5-B5-B5', 1000.0, 180)#(,K0, R0)
af.setParams('A6-B6-B6', 1000.0, 180)#(,K0, R0)
af.setParams('A7-B7-B7', 1000.0, 180)#(,K0, R0)
af.setParams('A8-B8-B8', 1000.0, 180)#(,K0, R0)
af.setParams('A9-B9-B9', 1000.0, 180)#(,K0, R0)
af.setParams('A10-B10-B10', 1000.0, 180)#(,K0, R0)
af.setParams('A11-B11-B11', 1000.0, 180)#(,K0, R0)
app.add(af)

group = gala.ParticleSet(all_info,'all')
comp_info = gala.ComputeInfo(all_info, group)

T = 1.0                                    #reduced unit
bd=gala.LangevinNVT(all_info, group, T, 123) # all_info, group, T, seed
app.add(bd)

sort_method = gala.Sort(all_info)
sort_method.setPeriod(100)# (period)
app.add(sort_method)

comp_info = gala.ComputeInfo(all_info, group)
DInfo = gala.DumpInfo(all_info, comp_info, 'data.log')
DInfo.setPeriod(200)# (period)
app.add(DInfo)

xml = gala.XMLDump(all_info, 'p')
xml.setPeriod(2000000)# (period)
xml.setOutputMass(True)
xml.setOutputImage(True)
xml.setOutputBond(True)
xml.setOutputAngle(True)
xml.setOutputInit(True)
xml.setOutputCris(True)
app.add(xml)

ljc = gala.LJConstrainForce(all_info, group, 0.5*2**(1.0/6.0))
ljc.setParams("A0", 1.0, 0.5, 1.0)
ljc.setParams("B0", 1.0, 0.5, 1.0)
ljc.setParams("A1", 1.0, 0.5, 1.0)
ljc.setParams("B1", 1.0, 0.5, 1.0)
ljc.setParams("A2", 1.0, 0.5, 1.0)
ljc.setParams("B2", 1.0, 0.5, 1.0)
ljc.setParams("A3", 1.0, 0.5, 1.0)
ljc.setParams("B3", 1.0, 0.5, 1.0)
ljc.setParams("A4", 1.0, 0.5, 1.0)
ljc.setParams("B4", 1.0, 0.5, 1.0)
ljc.setParams("A5", 1.0, 0.5, 1.0)
ljc.setParams("B5", 1.0, 0.5, 1.0)
ljc.setParams("A6", 1.0, 0.5, 1.0)
ljc.setParams("B6", 1.0, 0.5, 1.0)
ljc.setParams("A7", 1.0, 0.5, 1.0)
ljc.setParams("B7", 1.0, 0.5, 1.0)
ljc.setParams("A8", 1.0, 0.5, 1.0)
ljc.setParams("B8", 1.0, 0.5, 1.0)
ljc.setParams("A9", 1.0, 0.5, 1.0)
ljc.setParams("B9", 1.0, 0.5, 1.0)
ljc.setParams("A10", 1.0, 0.5, 1.0)
ljc.setParams("B10", 1.0, 0.5, 1.0)
ljc.setParams("A11", 1.0, 0.5, 1.0)
ljc.setParams("B11", 1.0, 0.5, 1.0)
ljc.addSphere(0.0, 0.0, 0.0, 8.5)
ljc.addSphere(0.0, 0.0, 0.0, 11.5)
ljc.addSphere(0.0, 0.0, 0.0, 14.5)
ljc.addSphere(0.0, 0.0, 0.0, 17.5)
ljc.addSphere(0.0, 0.0, 0.0, 20.5)
ljc.addSphere(0.0, 0.0, 0.0, 23.5)
ljc.addSphere(0.0, 0.0, 0.0, 26.5)
ljc.addSphere(0.0, 0.0, 0.0, 29.5)
ljc.addSphere(0.0, 0.0, 0.0, 32.5)
ljc.addSphere(0.0, 0.0, 0.0, 35.5)
ljc.addSphere(0.0, 0.0, 0.0, 38.5)
ljc.addSphere(0.0, 0.0, 0.0, 41.5)
app.add(ljc)
#ready ro run 
app.run(20000)
for i in range(1000):
    ljc.clearSphere()
    ljc.addSphere(0.0, 0.0, 0.0, 8.5)
    ljc.addSphere(0.0, 0.0, 0.0, 11.5-float(i)*0.002)
    ljc.addSphere(0.0, 0.0, 0.0, 14.5-float(i)*0.004)
    ljc.addSphere(0.0, 0.0, 0.0, 17.5-float(i)*0.006)
    ljc.addSphere(0.0, 0.0, 0.0, 20.5-float(i)*0.008)
    ljc.addSphere(0.0, 0.0, 0.0, 23.5-float(i)*0.010)
    ljc.addSphere(0.0, 0.0, 0.0, 26.5-float(i)*0.012)
    ljc.addSphere(0.0, 0.0, 0.0, 29.5-float(i)*0.014)
    ljc.addSphere(0.0, 0.0, 0.0, 32.5-float(i)*0.016)
    ljc.addSphere(0.0, 0.0, 0.0, 35.5-float(i)*0.018)
    ljc.addSphere(0.0, 0.0, 0.0, 38.5-float(i)*0.020)
    ljc.addSphere(0.0, 0.0, 0.0, 41.5-float(i)*0.022)
    app.run(2000)

ab=2.0
lj.setParams("A0", "A1", ab, 1.0, 1.0, 1.5) # type1, type2, epsilon, sigma, alpha, rcut
lj.setParams('A0', 'B1', ab, 1.0, 1.0, 1.5)
lj.setParams('B0', 'A1', ab, 1.0, 1.0, 1.5)
lj.setParams('B0', 'B1', ab, 1.0, 1.0, 1.5)

lj.setParams("A1", "A2", ab, 1.0, 1.0, 1.5) # type1, type2, epsilon, sigma, alpha, rcut
lj.setParams('A1', 'B2', ab, 1.0, 1.0, 1.5)
lj.setParams('B1', 'A2', ab, 1.0, 1.0, 1.5)
lj.setParams('B1', 'B2', ab, 1.0, 1.0, 1.5)

lj.setParams("A2", "A3", ab, 1.0, 1.0, 1.5) # type1, type2, epsilon, sigma, alpha, rcut
lj.setParams('A2', 'B3', ab, 1.0, 1.0, 1.5)
lj.setParams('B2', 'A3', ab, 1.0, 1.0, 1.5)
lj.setParams('B2', 'B3', ab, 1.0, 1.0, 1.5)

lj.setParams("A3", "A4", ab, 1.0, 1.0, 1.5) # type1, type2, epsilon, sigma, alpha, rcut
lj.setParams('A3', 'B4', ab, 1.0, 1.0, 1.5)
lj.setParams('B3', 'A4', ab, 1.0, 1.0, 1.5)
lj.setParams('B3', 'B4', ab, 1.0, 1.0, 1.5)

lj.setParams("A4", "A5", ab, 1.0, 1.0, 1.5) # type1, type2, epsilon, sigma, alpha, rcut
lj.setParams('A4', 'B5', ab, 1.0, 1.0, 1.5)
lj.setParams('B4', 'A5', ab, 1.0, 1.0, 1.5)
lj.setParams('B4', 'B5', ab, 1.0, 1.0, 1.5)

lj.setParams("A5", "A6", ab, 1.0, 1.0, 1.5) # type1, type2, epsilon, sigma, alpha, rcut
lj.setParams('A5', 'B6', ab, 1.0, 1.0, 1.5)
lj.setParams('B5', 'A6', ab, 1.0, 1.0, 1.5)
lj.setParams('B5', 'B6', ab, 1.0, 1.0, 1.5)

lj.setParams("A6", "A7", ab, 1.0, 1.0, 1.5) # type1, type2, epsilon, sigma, alpha, rcut
lj.setParams('A6', 'B7', ab, 1.0, 1.0, 1.5)
lj.setParams('B6', 'A7', ab, 1.0, 1.0, 1.5)
lj.setParams('B6', 'B7', ab, 1.0, 1.0, 1.5)

lj.setParams("A7", "A8", ab, 1.0, 1.0, 1.5) # type1, type2, epsilon, sigma, alpha, rcut
lj.setParams('A7', 'B8', ab, 1.0, 1.0, 1.5)
lj.setParams('B7', 'A8', ab, 1.0, 1.0, 1.5)
lj.setParams('B7', 'B8', ab, 1.0, 1.0, 1.5)

lj.setParams("A8", "A9", ab, 1.0, 1.0, 1.5) # type1, type2, epsilon, sigma, alpha, rcut
lj.setParams('A8', 'B9', ab, 1.0, 1.0, 1.5)
lj.setParams('B8', 'A9', ab, 1.0, 1.0, 1.5)
lj.setParams('B8', 'B9', ab, 1.0, 1.0, 1.5)

lj.setParams("A9", "A10", ab, 1.0, 1.0, 1.5) # type1, type2, epsilon, sigma, alpha, rcut
lj.setParams('A9', 'B10', ab, 1.0, 1.0, 1.5)
lj.setParams('B9', 'A10', ab, 1.0, 1.0, 1.5)
lj.setParams('B9', 'B10', ab, 1.0, 1.0, 1.5)

lj.setParams("A10", "A11", ab, 1.0, 1.0, 1.5) # type1, type2, epsilon, sigma, alpha, rcut
lj.setParams('A10', 'B11', ab, 1.0, 1.0, 1.5)
lj.setParams('B10', 'A11', ab, 1.0, 1.0, 1.5)
lj.setParams('B10', 'B11', ab, 1.0, 1.0, 1.5)
app.run(2000000)

Ebar=2.77
Ebind=8.0


# Period2: start the reaction
reaction = gala.Polymerization(all_info, neighbor_list, 2**(1.0/6.0), 123)
reaction.setEnergyBar(Ebar)
reaction.setPr("B0", "B0", 1.0)
reaction.setPr("B1", "B1", 1.0)
reaction.setPr("B2", "B2", 1.0)
reaction.setPr("B3", "B3", 1.0)
reaction.setPr("B4", "B4", 1.0)
reaction.setPr("B5", "B5", 1.0)
reaction.setPr("B6", "B6", 1.0)
reaction.setPr("B7", "B7", 1.0)
reaction.setPr("B8", "B8", 1.0)
reaction.setPr("B9", "B9", 1.0)
reaction.setPr("B10", "B10", 1.0)
reaction.setPr("B11", "B11", 1.0)
reaction.setNewBondTypeByPairs()
reaction.setNewAngleTypeByPairs()
reaction.generateAngle(True)
reaction.setMaxCris("B0",1)
reaction.setMaxCris("B1",1)
reaction.setMaxCris("B2",1)
reaction.setMaxCris("B3",1)
reaction.setMaxCris("B4",1)
reaction.setMaxCris("B5",1)
reaction.setMaxCris("B6",1)
reaction.setMaxCris("B7",1)
reaction.setMaxCris("B8",1)
reaction.setMaxCris("B9",1)
reaction.setMaxCris("B10",1)
reaction.setMaxCris("B11",1)
reaction.setInitInitReaction(True)
reaction.setPeriod(2000)
app.add(reaction)
#DInfo.setPeriod(1)# (period)

rever = gala.DePolymerization(all_info, T, 16361)
rever.setParams('B0-B0',   1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind+1.0, 1.0, gala.DePolyFunc.harmonic)
rever.setParams('B1-B1',   1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind,     1.0, gala.DePolyFunc.harmonic)
rever.setParams('B2-B2',   1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind,     1.0, gala.DePolyFunc.harmonic)
rever.setParams('B3-B3',   1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind,     1.0, gala.DePolyFunc.harmonic)
rever.setParams('B4-B4',   1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind,     1.0, gala.DePolyFunc.harmonic)
rever.setParams('B5-B5',   1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind,     1.0, gala.DePolyFunc.harmonic)
rever.setParams('B6-B6',   1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind,     1.0, gala.DePolyFunc.harmonic)
rever.setParams('B7-B7',   1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind,     1.0, gala.DePolyFunc.harmonic)
rever.setParams('B8-B8',   1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind,     1.0, gala.DePolyFunc.harmonic)
rever.setParams('B9-B9',   1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind,     1.0, gala.DePolyFunc.harmonic)
rever.setParams('B10-B10', 1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind,     1.0, gala.DePolyFunc.harmonic)
rever.setParams('B11-B11', 1250.0, 1.0, 1.0, 1000.0, 180.0, Ebar+Ebind,     1.0, gala.DePolyFunc.harmonic)
# sets bondname, K, r_0, b_0, epsilon0, Pr, and function.
rever.setPeriod(2000)
rever.setCountUnbonds(100000)
# sets how many steps to react.
app.add(rever)
#app.add(reaction)

app.run(1000000000)
# Period3: relaxation after the reaction
neighbor_list.printStats()
#
#
