import csv     # imports the csv module
import sys      # imports the sys module

n=input("Enter the file name without '.csv ': ")
f = open(n+'.csv', 'rb') # opens the csv file
lines = (line.decode('utf-8') for line in f)


def getIndex(s,a):
    for each in a:
        if(each==s):
            return(a.index(s))
    else:
        print("column not found.")
        return(-1)

def getCol(data,index):
    filename = 'col_'+str(index+1)+'.txt'
    f = open(filename,'w')#new file
    #col = []
    for i in range(len(data)):
        #col.append(data[i][index])
        f.write(data[i][index]+'\n') # python will convert \n to os.linesep
    f.close()
        #print(data[i][index])
    print("Saved as: "+filename)
    #return col



def run():
    word = input("Enter the exact column name: ")
    if(getIndex(word,l1) != -1):
        index = getIndex(word,l1); #column index
        dataset = lines_list[1:] #dataset without headers
        getCol(dataset,index)

def preprocess(lines_list):
    for i in range(len(lines_list)):
        if(len(lines_list[i])!= header_length):
            lines_list = lines_list[:i]
            break
    return lines_list
        

allLines = list(csv.reader(lines))
l1 = list(allLines[0]) #line
header_length = len(l1)

lines_list = preprocess(allLines)
    
for i in range(header_length):
    print(str(i+1)+" -> "+l1[i])
while(True):
    run()



