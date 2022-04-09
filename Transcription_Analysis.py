counts=dict()
file=open('TRANSCRIPTION.txt','r') ##Replace it with the name of your Transcription File
words=[]
words_spoken=[]
words_spoken_raw=[]
speakers=[]
data=list()
for line in file:
    a=line.split('\n')
    
    words.append(a)
for i in range(0,len(words)):
    for j in range(1,len(words[i])):
        words[i].pop(j)
        
for i in range(0,len(words)):
    for j in range(0,len(words[i])):
        words[i][j]=words[i][j].upper()
        
lines_in_transcription=len(words)
def analyse_transcription(name):      
    for x in range(1,lines_in_transcription,3 ):
        if(words[x][0]==name):
            words_spoken_raw.append(words[x+1])
            
    length1=len(words_spoken_raw)
    for i in range(0,length1):
        WORDS=words_spoken_raw[i][0].split()
        for k in WORDS:
            words_spoken.append(k)
    for i in words_spoken:
        if(ord(i[0]) in range(48,58)):
            words_spoken.pop(words_spoken.index(i))
    
    for p in words_spoken:
        counts[p]=counts.get(p,0)+1
    temp=list()    
    for k,v in counts.items():
        temp.append((v,k))
        
    if(len(temp)<10):
        while(len(temp)<10):
            temp.append((0,0))
    temp=sorted(temp,reverse=True)
    print("\nTRANSCRIPTION ANALYSIS REPORT FOR: ",name)
    print("-------------------------------------------------")
    print("NO OF WORDS USED DURING CLASS:" +str(len(temp)))
    print("MOST FREQUENT WORDS USED ARE:")
    print()
    print("NO ANALYSIS AVAILABLE AS THE SPEAKER DIDNOT SPEAK MUCH")
    for x in range(0,10):
        for y in range(0,1):
            print(str(temp[x][y])+' X '+str(temp[x][y+1]))
 

def find_speakers():
        global counts2
        global temp2
        for x in range(1,lines_in_transcription,3 ):
            if(speakers):
                pass
            speakers.append(words[x][0])
        counts2=dict()
        temp2=list()
        for x in speakers:
            
            counts2[x]=counts2.get(x,0)+1
            temp2=list()    
            for k,v in counts2.items():
                temp2.append((v,k))
            temp2=sorted(temp2,reverse=True)
        print("\nTRANSCRIPTION ANALYSIS REPORT: ")
        print("-------------------------------------------------")
        print("PEOPLE WHO SPOKE IN THE MEETING: ")
        print()
        for i in range(0,len(temp2)):
            print(str(temp2[i][0])+' TIMES --> '+str(temp2[i][1]))

find_speakers()
NAME=input("KINDLY TYPE A NAME FROM THE TO ANALYSE: ")
analyse_transcription(NAME) 
