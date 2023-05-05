def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open('txt_file/data05.txt',mode='r')
    txt=f.read()
    s=0
    m=0
    lst=[]
    for i in txt:
        if i.isdigit():
            s+=1
    lst.append(s)
    m=len(txt)-s
    lst.append(m)
    return lst
# Read data from file
print(main('txt_file/data05.txt'))