def main(data:str):
    """
    The data is from the file. Return the digits as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open('txt_file/data03.txt',mode='r')
    txt=f.read()
    lst=[]
    for i in txt:
        if i.isdigit():
            lst.append(int(i))
    return lst
# Read data from file
print(main('txt_file/data03.txt'))