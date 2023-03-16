"""_summary_

Returns:
    _type_: _description_
"""

import  sys

class   CsvReader:
    """_summary_
    """
    
    def __init__(self, filename=None, sep=',', header=False, skip_top=0, skip_bottom=0) -> None:
        self.filename = filename
        self._f = open(filename, 'r')
        self.sep = sep
        self.header = header
        with open(filename, 'r') as _faux:
            line = str(_faux.readline())
            columns = line.count(sep)
            while line:
                if line.count(sep) != columns:
                    print("Error: Broken file!")
                    sys.exit()
                line = _faux.readline()
        with open(filename, 'r') as _faux:
            self._header = _faux.readline()
            _faux.close()
        self.skip_top = skip_top
        self.skip_bottom = skip_bottom

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Return:
            nested list (list(list, list, ...)) representing the data.
        """

        line = str(self._f.readline())
        columns = line.count(self.sep) + 1
        general = []
        for i in range(columns):
            general.append([])
        line = str(self._f.readline())
        while line:
            splited = line.replace("\n","").split(self.sep)
            for i in range(columns):
                general[i].append(splited[i])
            line = str(self._f.readline())
        return general

    def getheader(self):
        """ Retrieves the header from csv file. 
        Returns:
            list: representing the data (when self.header is True).
            None: (when self.header is False).
        """
        
        return self._header

if __name__ == "__main__":
    with CsvReader('txt.csv') as file:
        data = file.getdata()
        header1 = file.getheader()
    print(data)
    print()
    print(header1)
