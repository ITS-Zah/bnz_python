class Rule:
    def __init__(self,cоnsequens, antecedents):
        self.Cоnsequens = cоnsequens
        self.Antecedents = antecedents
    def getRule(self):
        rule = "IF "
        for idx, con in enumerate(self.Antecedents):
            rule  += f"{con.nameLp} {con.nameTerm}"
            if(idx < len(self.Antecedents) - 1):
                rule += " AND "
            else:
                rule += f" THEN {self.Cоnsequens.NameLP} {self.Cоnsequens.Name}"
        return  rule
    def getIdRule(self):
        rule = ""
        for idx, con in enumerate(self.Antecedents):
            rule += f"{con.NameLP} {con.Name}"
        return hash(rule)




