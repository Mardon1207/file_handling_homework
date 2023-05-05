def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open('txt_file\data10.txt', mode='r')
    txt=f.read()
    m=0
    s=txt.split('\n')
    for i in s:
        if len(i)>m:
            m=len(i)
    return m
print(main('txt_file/data10.txt'))