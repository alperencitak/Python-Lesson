from datetime import datetime,timedelta
# from datetime import date
# from datetime import time

# import datetime

if __name__ == '__main__':
    now = datetime.now()
    result = now
    result = now.year
    result = now.day
    result = now.month
    result = now.hour
    result = datetime.today()
    result = datetime.ctime(now)
    result = datetime.strftime(now,'%D')
    result = datetime.strftime(now, '%X')
    result = datetime.strftime(now, '%Y')
    result = datetime.strftime(now, '%d')
    result = datetime.strftime(now, '%A')
    result = datetime.strftime(now, '%Y %B %A')

    t = "21 August 2019 hour 10:12:30"
    dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')
    # gun,ay,yil = t.split(" ");
    # print(gun,ay,yil)
    print(result)
    print(dt)
    print(dt.day)
    print(dt.hour)

    birtday = datetime(1983,5,9,12,30,10)
    result = datetime.timestamp(birtday)
    result = datetime.fromtimestamp(result)
    print(birtday)
    print(result)
    result = datetime.fromtimestamp(0)
    print(result)
    result = now - birtday
    print(result)
    print(result.days)
    print(result.seconds)
    result = now + timedelta(days=10)
    result = now - timedelta(days=5)
    print(result)
