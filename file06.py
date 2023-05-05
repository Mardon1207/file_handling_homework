def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open('txt_file/data03.txt',mode='r')
    txt=f.read()
    s=txt.split('/n')
    m=str()
    l=[]
    k=0
    for i in s:
        k=len(i)
        l=l.append(k)
    return l
# Read data from file
data=str()
print(main('txt_file\data06.txt'))
