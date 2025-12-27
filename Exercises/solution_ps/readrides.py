import csv
from collections import namedtuple

def read_rides_as_tuples(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = int(row[3])
            record = (route, date, daytype, rides)
            records.append(record)
    return records

def read_rides_as_dictionary(filename):
    '''
    Read the bus ride data as a list of dictionary
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = row[3]
            record = {'route':route,
               'date':date,
               'daytype':daytype,
               'rides':rides}
            records.append(record)
    return records


class Row:
    def __init__(self,route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_class(filename):
    '''
    Read the bus ride data as a list of class
    '''
    records = []

    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = row[3]
            record = Row(route,date,daytype,rides)
            records.append(record)
            
    return records



Row_namedtuple = namedtuple('Row',['route','date','daytype','rides'])
def read_rides_as_named_tuple(filename):
    '''
    Read the bus ride data as a list of Slots
    '''
    records = []

    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = row[3]
            record = Row_namedtuple(route,date, daytype,rides)
            records.append(record)
            
    return records



class Row_slot:
    __slots__ = ['route','date','daytype','rides']
    def __init__(self,route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides


def read_rides_as_slotclass(filename):
    '''
    Read the bus ride data as a list of class
    '''
    records = []

    with open(filename) as f:
        rows = csv.reader(f)
        headings = next(rows)     # Skip headers
        for row in rows:
            route = row[0]
            date = row[1]
            daytype = row[2]
            rides = row[3]
            record = Row_slot(route,date,daytype,rides)
            records.append(record)
            
    return records

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    # rows_dict = read_rides_as_dictionary('Data/ctabus.csv')
    # rows_tuples = read_rides_as_tuples('Data/ctabus.csv')
    rows_namedtuple = read_rides_as_named_tuple('Data/ctabus.csv')
    # rows_class = read_rides_as_class('Data/ctabus.csv')
    # rows_slotclass = read_rides_as_slotclass('Data/ctabus.csv')
    # print(rows)
    # To-Do: Tracemalloc should benchmark each of these seperately
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
