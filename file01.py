def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    data=open('txt_file\data01.txt',mode='r+')
    l=data.read()
    return l
# Read data from file
data=str()
print(main(data))