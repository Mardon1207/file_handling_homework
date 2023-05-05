def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f=open('txt_file\data06.txt', mode='r')
    txt=f.read()
    lst=[]
    s=txt.split('\n')
    for i in s:
        lst.append(len(i))
    return lst
print(main('txt_file/data06.txt'))
