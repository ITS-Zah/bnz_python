from sklearn.cluster import KMeans
import numpy as np
from exelreader import *
from plotter import *
from FKB.FKB import *
from FKB.LingVarialbe import *
from FKB.Rule import *
from FKB.Term import *
from FKB.Cleaner import *
import json
import time

start = time.time()
isPlot = False
table = ReadFromExel("Ekologiya.xlsx", "FirstList")
counter = 0
listLingVar = []
listRule = []
for row in table["Зразки"]:
    rule = Rule(Term("","",0,0,0),[])
    listRule.append(rule)
for idx, col in enumerate(table.columns.values):
    if col != "Зразки":
        LingVar = LingVariable(col,min(table[col]),max(table[col]))
        X = np.array(table[col]).reshape(-1,1)
        kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
        arrFroCenter = sorted(kmeans.cluster_centers_)

        term = Term(LingVar.Name,"low",LingVar.min,arrFroCenter[0][0],arrFroCenter[1][0])
        LingVar.addTerm(term)
        term = Term(LingVar.Name, "middle", arrFroCenter[0][0], arrFroCenter[1][0], arrFroCenter[2][0])
        LingVar.addTerm(term)
        term = Term(LingVar.Name, "height", arrFroCenter[1][0], arrFroCenter[2][0], LingVar.max)
        LingVar.addTerm(term)
        listLingVar.append(LingVar)

        for idx2, row in enumerate(table[col]):
            var = kmeans.predict([[row]])
            cluster = kmeans.cluster_centers_[var]
            indexCluster = arrFroCenter.index(cluster)
            switcher = {
                0: Term(LingVar.Name,"low",LingVar.min,arrFroCenter[0][0],arrFroCenter[1][0]),
                1: Term(LingVar.Name, "middle", arrFroCenter[0][0], arrFroCenter[1][0], arrFroCenter[2][0]),
                2: Term(LingVar.Name, "height", arrFroCenter[1][0], arrFroCenter[2][0], LingVar.max),
            }
            if idx < len(table.columns) - 1:
                listRule[idx2].Antecedents.append(switcher.get(indexCluster, "Invalid number"))
            else:
                if idx == len(table.columns) - 1:
                    listRule[idx2].Cоnsequens = switcher.get(indexCluster, "Invalid number")
        if isPlot:
            plt.figure(counter)
            counter += 1
            for znach in table[col]:
                ax = plt.subplot(1, 1, 1)
                ax.scatter([znach], [0.1])
            PlotFP(plt,LingVar)

listRule = CleanRules(listRule)

fkb = FKB(listRule,listLingVar)
end = time.time()
t = end - start
print((end - start))
with open("Output.txt", "w") as text_file:
    text_file.write(json.dumps(fkb, default=lambda o:o.__dict__))
#for ru in listRule:
#    print(ru.getRule())
if isPlot:
    plt.show()

