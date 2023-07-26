import os

fileobj = open("test.cir","r")
data = fileobj.read()
fileobj.close()


prevaluesA  = (0,0,0,0)
prevaluesB = (0,0,0,0)
for A in range(0,16):
    (A3,A2,A1,A0) = (A>>3 &1,A>>2 &1,A>>1 &1,A>>0 &1)
    data = data.replace(f"VinA0 nodeA0 0 dc = {prevaluesA[3]}\n",f"VinA0 nodeA0 0 dc = {A0}\n")
    data = data.replace(f"VinA1 nodeA1 0 dc = {prevaluesA[2]}\n",f"VinA1 nodeA1 0 dc = {A1}\n")
    data = data.replace(f"VinA2 nodeA2 0 dc = {prevaluesA[1]}\n",f"VinA2 nodeA2 0 dc = {A2}\n")
    data = data.replace(f"VinA3 nodeA3 0 dc = {prevaluesA[0]}\n",f"VinA3 nodeA3 0 dc = {A3}\n")
    prevaluesA = (A3,A2,A1,A0)

    for B in range(0,16):
        (B3,B2,B1,B0) = (B>>3 &1,B>>2 &1,B>>1 &1,B>>0 &1)
        data = data.replace(f"VinB0 nodeB0 0 dc = {prevaluesB[3]}\n",f"VinB0 nodeB0 0 dc = {B0}\n")
        data = data.replace(f"VinB1 nodeB1 0 dc = {prevaluesB[2]}\n",f"VinB1 nodeB1 0 dc = {B1}\n")
        data = data.replace(f"VinB2 nodeB2 0 dc = {prevaluesB[1]}\n",f"VinB2 nodeB2 0 dc = {B2}\n")
        data = data.replace(f"VinB3 nodeB3 0 dc = {prevaluesB[0]}\n",f"VinB3 nodeB3 0 dc = {B3}\n")
        prevaluesB = (B3,B2,B1,B0)
        fileobj = open("test.cir","w")
        fileobj.write(data)
        fileobj.close()

        os.system("ngspice test.cir")


fileobj = open("test.cir","r")
data = fileobj.read()
fileobj.close()

data = data.replace(f"VinA0 nodeA0 0 dc = {A0}",f"VinA0 nodeA0 0 dc = 0")
data = data.replace(f"VinA1 nodeA1 0 dc = {A1}",f"VinA1 nodeA1 0 dc = 0")
data = data.replace(f"VinA2 nodeA2 0 dc = {A2}",f"VinA2 nodeA2 0 dc = 0")
data = data.replace(f"VinA3 nodeA3 0 dc = {A3}",f"VinA3 nodeA3 0 dc = 0")

data = data.replace(f"VinB0 nodeB0 0 dc = {B0}",f"VinB0 nodeB0 0 dc = 0")
data = data.replace(f"VinB1 nodeB1 0 dc = {B1}",f"VinB1 nodeB1 0 dc = 0")
data = data.replace(f"VinB2 nodeB2 0 dc = {B2}",f"VinB2 nodeB2 0 dc = 0")
data = data.replace(f"VinB3 nodeB3 0 dc = {B3}",f"VinB3 nodeB3 0 dc = 0")
fileobj = open("test.cir","w")
fileobj.write(data)
fileobj.close()