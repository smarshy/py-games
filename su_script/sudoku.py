			   
def validRow(puzzle):
    for item in puzzle:
        i=0
        while i<len(item):            
            j=i+1
            while j<len(item):
                if item[i]==item[j]:
                    return False
                j+=1
            i+=1
    return True



def validColumn(puzzle):
    counter=0
    while counter<len(puzzle):
        
        i=0
        while i<len(puzzle):
            j=i+1
            while j<len(puzzle):
                if puzzle[i][counter]==puzzle[j][counter]:
                    return False
                j+=1
            i+=1
        counter+=1
    return True
     
            
def validInput(puzzle):
    for item in puzzle:
        i=0        
        while i<len(item):
            if type(item[i])!=int or item[i]>len(item) or item[i]<=0:
                return False
            i+=1
        
    return True  
            
    
def check_sudoku(puzzle):    
    test=validInput(puzzle)
    test1=validRow(puzzle)
    test2=validColumn(puzzle)
    
    return test and test1 and test2
	
	
