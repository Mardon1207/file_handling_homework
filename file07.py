def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open('txt_file/data07.txt',mode='r')
    txt=f.read()
    s=0
    lst=[]
    for i in txt:
        if i.isdigit():
            s+=int(i)
    return s
# Read data from file
print(main('txt_file/data07.txt'))