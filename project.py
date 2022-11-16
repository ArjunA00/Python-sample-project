# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 20:29:04 2020

@author: USER
"""
t1=0
totalscore=0
cheobj=['atomic absorption','atomic emission','electron absorption','electron emission']
cheobj2=['rutherford','marie curie','henri becquerel','enrico fermi']
phyobj=['Hydrometer','Hygrometer','Lactometer','Barometer']
phyobj2=['air','water','noise','thermal']
biobj=['pyruvic acid','glucose','fructose','glycolate']
biobj2=['capsomere','nucleoid','prion','virion']
phylist=['objective','descriptive']
chelist=['objective','descriptive']
biolist=['objective','descriptive']
sublist=['physics','chemistry','biology']
p1=['every','action','equal','opposite','reaction']
p2=['current','flowing','conductor','proportional','potential difference','temperature','physical','conditions','through','unchanged']
c1=['chemical','bonding','involves','contains','electrostatic','attraction','between','oppositely','charged','ions'] 
c2=['polymerization','process','forming','higher','molecular','mass','macromolecules','consists','contains','repeating','structural','units','derived','monomers']



b1=['bacteria','carrying','foreign','gene','bacterial','plasmid','genome','transgenic']

b2=['gene','therapy','correction','malfunctioning','manipulating','repairing','insertng','required','normal']


def sepp1(a):
    k=0
    for i in range(0,len(p1)):
        if(a.find(p1[i],0)==-1):
            continue
        else:
            k+=1
       
    return k
def sepp2(a):
    k=0
    for i in range(0,len(p2)):
        if(a.find(p2[i],0)==-1):
            continue
        else:
            k+=1
        
    return k
def sepc1(a):
    k=0
    for i in range(0,len(c1)):
        if(a.find(c1[i],0)==-1):
            continue
        else:
            k+=1
            
        
    return k

def sepc2(a):
    k=0
    for i in range(0,len(c2)):
        if(a.find(c2[i],0)==-1):
            continue
        else:
            k+=1        
        
    return k

def sepb1(a):
    k=0
    for i in range(0,len(b1)):
        if(a.find(b1[i],0)==-1):
            continue
        else:
            k+=1        
        
    return k
   
def sepb2(a):
    k=0
    for i in range(0,len(b2)):
        if(a.find(b2[i],0)==-1):
            continue
        else:
            k+=1        
        
    return k








def physics():
    t1=0
    for i1 in range(0,len(phylist)):
        print(i1,phylist[i1])
    id1 = int(input("select question type"))
    print()
    print()
    
    if(phylist[id1]=='objective'):
        print(" find the instrument that measures and records relative humidity of air ")
        for i2 in range(0,4):
            print(i2,phyobj[i2])
        k=int(input("enter the answer"))
        if(phyobj[k]=='Hygrometer'):
            t1=1
        print("electrostatic precipitator is used to control the pollution of ")
        for i3 in range(0,4):
            print(i3,phyobj2[i3])
        k1=int(input("enter the answer"))
        if(phyobj2[k1]=='air'):
            t1=t1+1
        phylist.remove('objective')
        return t1
    if(phylist[id1]=='descriptive'):
        print("state newtons 3rd law of motion")
        a1=input()
        pk=sepp1(a1)
        print("state OHMS LAW")
        a2=input()
        pk=pk+sepp2(a2)
        phylist.remove('descriptive')
        return pk
    

def chemistry():
    t1=0
    for i1 in range(0,len(chelist)):
        print(i1,chelist[i1])
    id1 = int(input("select question type"))
    print()
    print()
    
    if(chelist[id1]=='objective'):
        print("Why does mercury and sodium street lamps light up ")
        for i2 in range(0,4):
            print(i2,cheobj[i2])
        k=int(input("enter the answer"))
        if(cheobj[k]=='atomic emission'):
            t1=1
            
        print("natural radioactivity was discovered by")
        for i3 in range(0,4):
            print(i3,cheobj2[i3])
        k1=int(input("enter the answer"))
        if(cheobj2[k1]=='henri becquerel'):
            t1=t1+1

        chelist.remove('objective')
        return t1
    if(chelist[id1]=='descriptive'):
        print("what is ionic bond")
        a1=input()
        pk=sepc1(a1)
        print("what is polymerization")
        a2=input()
        pk=pk+sepc2(a2)
        chelist.remove('descriptive')
        return pk
    
    
def biology():
    t1=0
    for i1 in range(0,len(biolist)):
        print(i1,biolist[i1])
    id1 = int(input("select question type"))
    print()
    print()
    
    if(biolist[id1]=='objective'):
        print("What is the substrate of photo-respiration  ")
        for i2 in range(0,4):
            print(i2,biobj[i2])
        k=int(input("enter the answer"))
        if(biobj[k]=='pyruvic acid'):
            t1=1
        
        print("the virus without capsid but only with nucleic acids is called")
        for i3 in range(0,4):
            print(i3,biobj2[i3])
        k1=int(input("enter the answer"))
        if(biobj2[k1]=='nucleoid'):
            t1=t1+1
    
        biolist.remove('objective')
        return t1
    if(biolist[id1]=='descriptive'):
        print("what is transgenic bacteria")
        a1=input()
        pk=sepb1(a1)
        print("what is gene therapy")
        a2=input()
        pk=pk+sepb2(a2)
        biolist.remove('descriptive')
        return pk
           
        
        
        
flag1=2
flag2=3
flag3=4
while(len(sublist)>0): 
    if(len(sublist)==0):
        break
    else:
        if(flag1!=6):
            if(len(phylist)==0):
                sublist.remove('physics')
                flag1=6
        if(flag2!=7):
            if(len(chelist)==0):
                sublist.remove('chemistry')
                flag2=7
        if(flag3!=9):
            if(len(biolist)==0):
                sublist.remove('biology')
                flag3=9
        print()
        print(len(sublist),"length of subjctlist")
        print()
        if(len(sublist)==0):
            print("total score is ",totalscore)
            break
        print("subjects included")
        for i in range(0,len(sublist)):
            print(i,sublist[i])
        print("press 9 to exit")
        id=int(input("select subject id"))
        if(id==9):
            print("Application closing")
            print("totalscore=",totalscore)
            break
        if(sublist[id]=='physics'):
            totalscore=totalscore + physics()
        elif(sublist[id]=='chemistry'):
            totalscore=totalscore + chemistry()
        elif(sublist[id]=='biology'):
            totalscore=totalscore + biology()
            
        
    
    
   
    
        