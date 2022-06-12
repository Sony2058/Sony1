def merge(list):
    print("Splitting",list)
    if len(list)>1:
        mid = len(list)//2
        lb = list[:mid]
        ub = list[mid:]

        merge(lb)
        merge(ub)
        i=0
        j=0
        k=0
        while i<len(lb) and j<len(ub):
            if lb[i]<ub[j]:
                list[k]=lb[i]
                i=i+1
            else:
                list[k]=ub[j]
                j=j+1
            k=k+1
        while i < len(lb):
            list[k]=lb[i]
            i=i+1
            k=k+1

        while j < len(ub):
            list[k]=ub[j]
            j=j+1
            k=k+1

    print("Merging",list)

list=[1,5,3,8,9,4]
merge(list)
print(list)

