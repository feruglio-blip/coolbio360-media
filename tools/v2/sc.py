import sys,datetime
A='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
def date(sc):
    n=0
    for c in sc[:11]: n=n*64+A.index(c)
    ms=(n>>23)+1314220021721
    return datetime.datetime.utcfromtimestamp(ms/1000).date()
if __name__=='__main__':
    for s in sys.argv[1:]: print(s,date(s))
