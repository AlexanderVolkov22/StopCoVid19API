import datetime


async def gettime():
    dateandtime = str(datetime.datetime.now())
    date1 = dateandtime.split(" ")[-2]
    date = date1.split("-")[-1]
    month = date1.split("-")[-2]
    year = date1.split("-")[-3]
    date = date + "." + month + "." + year
    return date
