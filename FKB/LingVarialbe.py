class LingVariable:
    def __init__(self, nameLP,minVal,maxVal):
        self.Name = nameLP
        self.terms = []
        self.min = minVal
        self.max = maxVal
    def addTerm(self, term):
        self.terms.append(term)
