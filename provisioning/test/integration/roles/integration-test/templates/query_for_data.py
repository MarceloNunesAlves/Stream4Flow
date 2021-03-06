from urllib import urlopen
import simplejson as json



def contains(set):
    if 40 in set:
        if 60 in set:
            if 20 in set:
                return True
    return False


def getdata():
    url = urlopen('http://{{ consumer_ip }}:{{ consumer_port }}/spark-*/_search').read()
    url = json.loads(url)
    a = []
    for i in range(0, len(url.get('hits').get('hits'))):
        a.append(url.get('hits').get('hits')[i].get('_source').get('flows'))
    return set(a)


if __name__ == "__main__":
    if contains(getdata()):
        print("Number of flows in elasticsearch is as expected")
        exit(0)
    else:
        print("Something went wrong - data are not as expected")
        exit(1)