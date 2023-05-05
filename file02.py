def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    data=open('txt_file\data02.txt')
    l=data.read()
    n=len(l)
    return n
# Read data from file
data=str()
print(main(data))