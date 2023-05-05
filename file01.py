def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data=open(data,mode='r+').read()
    read=data.read()
    s=read.split(',')
    l=[]
    for i in s:
        l.append(int(i))
    return l
# Read data from file
data=str()
print(main('txt_file\data01.txt'))