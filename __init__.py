import datetime

if __name__ == '__main__' :
    date1 = datetime.date.today()
    for i in range(100):
        print(i)
        print(f'{i} days after {date1} is {date1+i}')
