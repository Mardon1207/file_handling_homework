def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open('txt_file/data04.txt',mode='r')
    txt=f.read()
    lst=[]
    for i in txt:
        lst.append(i)
    return lst
# Read data from file
print(main('txt_file/data04.txt'))