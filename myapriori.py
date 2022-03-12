file = open('playlists4000.txt','r')
Lines = file.readlines()

split_list = [i.split('::') for i in Lines]
for i in split_list:
    print(split_list)

orDict = defaultdict(split_list)

for key, val in split_list:
    orDict[key].append(val)

print(orDict)

#key,value = { for i.split('::') in split_list }
#d = { key : value }

#print(d)

#Implement Apriori for fq-itemesets and interesting rules
#At every step/lvl during the frequent itemset generation, youmust print on screen the
#number of frequent intemsets found in the format:
#<Level>-itemsets::<# frequent itemsets> ---> example: 1-itemsets::100

#After Fq-Itemset gen create output file freq_<minsup>.txt that has all the fq-itemsets one perline in the format
#{songID,...,songID}::<support count> ---> example: {1,67}::10

#After gen rules from 2- & 3-itemsets create output file rules_<minsup>_<minconf>.txt that has all rules with high confidence (one per line) in the following format:

#{songID,...,songID}::{songID,...,songID}::<support count>::<confidence with 4 digits>
#---> example: {1,4,67}::{3}::99::0.7890


