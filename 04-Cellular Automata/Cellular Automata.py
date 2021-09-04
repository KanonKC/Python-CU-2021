# Homework 4: 1D cellular automata
# apply rule1 19 times

cell = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
def run20(p0):
 print(p0)
 pin = list(p0)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
 print(pout)
 pin = list(pout)
 pout = runrule(pin)
#  . . .
# cell index 0..19
# neibourhood 5
# apply rule to cell index 2..17
def runrule(p):
 pp = 20*[0] # initialise output
 pp[2] = rule1(p,2)
 pp[3] = rule1(p,3)
 pp[4] = rule1(p,4)
 pp[5] = rule1(p,5)
 pp[6] = rule1(p,6)
 pp[7] = rule1(p,7)
 pp[8] = rule1(p,8)
 pp[9] = rule1(p,9)
 pp[10] = rule1(p,10)
 pp[11] = rule1(p,11)
 pp[12] = rule1(p,12)
 pp[13] = rule1(p,13)
 pp[14] = rule1(p,14)
 pp[15] = rule1(p,15)
 pp[16] = rule1(p,16)
 pp[17] = rule1(p,17)
 return pp

def rule1(p,i):
 sample_cell = p[i-2:i+3]
#  print(sample_cell)
 if sample_cell == list("10100") or sample_cell == list("01000"):
     return "1"
 return "0"

def prettyprint(p):
 s = "".join([str(e) for e in p])
 print(s)
# p0 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
def main():
 p0 = "01010101010101010101"#input()
 run20(p0)
main()
# -----------------