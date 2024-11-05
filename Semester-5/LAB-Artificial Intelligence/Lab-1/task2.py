class CityData:
    def __init__(self,num,name,counts):
        self.num = num
        self.name = name
        self.counts = counts
        self.outCons = []
        self.seen = False
        self.pred = -1
        
def main():

    d1 = {}
    d2 = {}
    cities = []
    cityy = []
    cons = []
    with open ("pb.txt","r") as file:
        count = int(file.readline())
        
        for i in range(count):
            l = list(file.readline().split())
            cno = int(l.pop(0))
            cnm = l.pop(0).strip(",")
            ct = int(l.pop(0))
            c = CityData(cno,cnm,ct)
            cities.append(c)
            cons.append(l)
            cityy.append(cnm)
            d1[cnm] = c
        for i in range(len(cons)):
            for j in cons[i]:
                cities[i].outCons.append(cities[int(j)])
    
    def findPath(city1,city2):
        paths = []
        if city1.name in cityy:
            paths.append(city1)
            while paths:
                cc = paths.pop()
                if cc.name == city2.name:
                    pt = []
                    while cc != -1:
                        pt.append(cc.name)
                        cc = cc.pred
                    return pt
                else:
                    cc.seen = True
                    for i in cc.outCons:
                        if i.seen == False:
                            i.seen = True
                            i.pred = cc
                            paths.append(i)
                        else:
                            continue
        if len(paths) == 0 :
            return []
                        
                

    print("City List: ",cityy)
    start = input("Enter source city from aboove list: ")
    dest = input("Enter destination city from aboove list: ")
    path = findPath(d1[start],d1[dest])
    if path:
        s = ""
        for i in range (len(path)-1,-1,-1):
            s+=(path[i])
            s+= " -> "
        print(s.strip(" -> "))
    else:
        print("path not found")
main()