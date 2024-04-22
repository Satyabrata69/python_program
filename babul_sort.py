class babul:
    def __init__(self,list):
        for j in range(len(list)-1):
            for i in range((len(list)-1-j)):
                if list[i]>list[i+1]:
                    list[i],list[i+1]=list[i+1],list[i]    
        print(list)                    
ac=babul([18,13,11,9,25,16])


