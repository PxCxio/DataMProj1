import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, fpgrowth, association_rules

f = open('playlists4000.txt','r')
Lines = f.readlines()



#dataset = [
#    ["Milk", "Eggs", "Bread"],
#    ["Milk", "Eggs"],
#    ["Milk", "Bread"],
#    ["Eggs", "Apple"],
#]

te = TransactionEncoder()
te_array = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_array, columns=te.columns_)

frequent_itemsets_ap = apriori(df, min_support=0.01, use_colnames=True)
frequent_itemsets_fp = fpgrowth(df, min_support=0.01, use_colnames=True)

rules_ap = association_rules(frequent_itemsets_ap, metric="confidence", min_threshold=0.8)
rules_fp = association_rules(frequent_itemsets_fp, metric="confidence", min_threshold=0.8)


print(dataset)
print()
print(df)
print()
print(frequent_itemsets_ap)
print()
print(frequent_itemsets_fp)
print()
print(rules_ap)
print()
print(rules_fp)
