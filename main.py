import csv , sys, argparse


class CSVData:
    def __init__(self,filenameDescriptor):
        self.csvObject = csv.DictReader(filenameDescriptor)

    def readColumn(self,columnName):
        for row in self.csvObject:
            print row[columnName]




if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Filename of the CSV File")
    parser.add_argument("columns", help="Columns to be merged")
    args = parser.parse_args()
    print args.filename
    #
    # if len(sys.argv)< 3 :
    #     raise  ValueError('Not enough parameter')
    # else:
    #     filename = sys.argv[1]
    #     filenameDescriptor = open(filename,'rb')
    #     csvData = CSVData(filenameDescriptor)
    #     csvData.readColumn(sys.argv[2])
