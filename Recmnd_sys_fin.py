
lis=[['bucket','mug'],['mug','soaps'],['bucket','mug','soaps'],['soaps','bucket'],['mug','bucket','shampoos']]
itms=[]
for i in range(len(lis)):
    ele=lis[i]
    for j in range(len(ele)):
        if ele[j] not in itms:
            itms.append(ele[j])

d={}
for i in range(len(lis)-1):
    count=0
    for j in range(len(lis)):
        if itms[i] in lis[j]:
            count+=1
    d[itms[i]]=count
    #print(itms[i],count)

d1={}
for i in range(len(itms)-1):
    for j in range(i,len(itms)):
        count=0
        if itms[i]!=itms[j]:
                    for m in range(len(lis)):
                        if itms[i] in lis[m]:
                            if itms[j] in lis[m]:
                                count+=1
                                #print(itms[i],itms[j],lis[m],count)
                    if itms[i]==itms[j]:
                        continue
                    else:
                        #print(itms[i],itms[j],count)
                        d1[itms[i],itms[j]]=count

                        

print("\n","***************************************************"*3)

print("\n","\t"*6,"__THE DATA ANALYSIS OF ITEMS AND ITEMSETS__")

print("\n","***************************************************"*3)

                        
print("\n >> List of ItemSets of Transactions:\n\n")
t=1
for i in lis:
    print(" \tT",t,": >",i,"\n")
    t+=1
print("\n\n >> Sum of Appearance of a single Item in all ItemSets:\n\n")
for i in d:
    print(" \t>",i,":",d[i],"\n")
print("\n\n >> Sum of Appearance of each pair of Items in all ItemSets:\n\n")
for i in d1:
    print(" \t>",i,":",d1[i],"\n")


supC_dict={}
le_itms=len(itms)
for i in range(le_itms):
    sup=int( ( d[itms[i]] / le_itms )*100 )
    #print(sup,itms[i])
    supC_dict[itms[i]]=sup
print("\n\n >> Support counts of each item:\n\n")
for i in supC_dict:
    print(" \t>",i,":",supC_dict[i],"\n")

d1_lis=list(d1.keys())
#print(d1_lis)
conf_pairs=[]
itms_c=[]
conf_vals=[]
conf=0
for i in range(len(d1_lis)):
    for j in range(le_itms):
        if itms[j] in d1_lis[i]:
            #print(itms[j],d1_lis[i])
            #print(d1[d1_lis[i]],d[itms[j]])
            conf=int((d1[d1_lis[i]]/d[itms[j]])*100)
            #print(conf)
            conf_vals.append(conf)
            itms_c.append(itms[j])
            conf_pairs.append(d1_lis[i])
            conf=0

#print(conf_pairs,"\n",itms_c,"\n",conf_vals)
            
            

print("\n","***************************************************"*3)

print("\n","\t"*6,"__THE STATEMENTS OF RECOMENDATION ARE AS FOLLOWS__ ")

print("\n","***************************************************"*3)


temp=[]
conf_dict={}
for i in range(len(conf_pairs)):
    if conf_vals[i]<=0:
        continue
    else:
        temp=conf_pairs[i]
        ele=0
        if itms_c[i]!=temp[0]:
            print("\n >> Those who bought-",itms_c[i],", also bought-",temp[0],", with a confidence of:",conf_vals[i],".")
            conf_dict[itms_c[i],temp[0]]=conf_vals[i]
        else:
            print("\n >> Those who bought-",itms_c[i],", also bought-",temp[1],", with a confidence of:",conf_vals[i],".")
            conf_dict[itms_c[i],temp[1]]=conf_vals[i]

#print("\n\n >> THE DICTIONARY OF RECOMENDATIONS:\n")
#print(conf_dict)

print("\n\n","***************************************************"*3)
        




    
