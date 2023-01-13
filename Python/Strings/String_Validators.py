if __name__ == '__main__':
    s = [x for x in input()]
    
    result = []
    result.append(len(list(filter(lambda x:  x.isalnum() == True  , s))))
    
    result.append(len(list(filter(lambda x:  x.isalpha() == True  , s))))  
    
    result.append(len(list(filter(lambda x:  x.isdigit() == True  , s))))
    
    result.append(len(list(filter(lambda x:  x.islower() == True  , s))))
    
    result.append(len(list(filter(lambda x:  x.isupper() == True  , s))))
    
    for i in result:
        if i > 0:
            print(True)
        else:
            print(False)
