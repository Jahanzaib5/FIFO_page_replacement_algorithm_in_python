def page_replace():
    page_n=int(input("Enter the number of pages: "))
    page_frm=int(input("Enter the number of page frames: "))
    print("\n")
    pages=[]
    print("Enter the page seqence: ")
    for i in range(page_n):
        pages.append(int(input()))

    sequence=[]
    page_hit=0
    page_fault=0
    p_h=[]
    p_f=[]
    count=0
    temp=[]
    for i in range(page_n):
        #sequence.append(temp)
        if (pages[i] not in temp) and (len(temp)<page_frm):
            page_fault+=1
            temp.append(pages[i])
            p_f.append(pages[i])
            #sequence.append(temp)
            print(temp)
            #print(sequence)
        elif (pages[i] not in temp) and (len(temp)==page_frm):
            if count == page_frm:
                count=0
            temp[count]=pages[i]
            p_f.append(pages[i])
            page_fault+=1
            count+=1
            #sequence.append(temp)
            print(temp)
            #print(sequence)
        elif (pages[i] in temp) and (len(temp)<=page_frm):
            #sequence.append(temp)
            p_h.append(pages[i])
            page_hit+=1
            print(temp)
            #print(sequence)
            

    #print("\n")
    #print("The sequence is: ", sequence)
    print("Page hits: ",page_hit)
    print(p_h)
    print("Page Fault: ", page_fault)
    print(p_f)
            
        
page_replace()           
        
        
    
