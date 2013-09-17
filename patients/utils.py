import os, csv

def get_cie10():
    """This Must be lazy!!!!!!! REDO
    """
    directory = os.path.dirname(os.path.abspath(__file__))
    resoureces_dir = os.path.join(directory, 'resources', 'CSV_CIE10.csv')
    result = []
    with open(resoureces_dir, 'r') as inputfile:
        data = csv.reader(inputfile, delimiter=',')
        #dont use head
        data.next()
        for line in data:
            result.append((line[0], ','.join([line[0], line[1]])))
    return result