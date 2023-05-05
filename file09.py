def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f=open('txt_file/data09.txt',mode='r')
    txt=f.read()
    s=10
    lst=[]
    for i in txt:
        if i.isdigit():
            if int(i)<s:
                s=int(i)
    return s
# Read data from file
print(main('txt_file/data09.txt'))