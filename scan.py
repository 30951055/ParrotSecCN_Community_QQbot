from api import *


def create_list(x):
    ports=[]
    x = str(x)
    if ',' in x:
        List = x.split(',')
        for i in List:
            ports.append(int(i))
        return ports
    if '-' in x:
        l = x.split('-')
        m = int(l[0])
        n = int(l[1])
        for j in range(m,n + 1):
            ports.append(j)
        return ports
    else:
        ports.append(int(x))
    return ports

def port_scan(host,port):
    ports=create_list(port)
    rsp= (portscan((host),ports).scan())
    result=''
    for i in rsp:
        result+="[+] %s open\n"%(i)
    return result


def exploit_api(url="",keyword="",search=0):
    if search and url:
        obj = exploit(keyword=keyword, url=url)
        obj.keyword2num()
        print(obj.keyword2num())
        return (obj.exploitpoc())
    elif search:
        obj = exploit(keyword=keyword, url=url)
        result = obj.keyword2num()
        return result
    else:
        if url:
            obj = exploit(url)
            if keyword == 'whatcms':
                rsp = whatweb(url).scan()
                return rsp['result']
            elif keyword == 'cms':
                obj.cms()
                return (obj.exploitpoc())
            elif keyword == 'information':
                obj.information()
                return (obj.exploitpoc())
            elif keyword == 'system':
                obj.system()
                return (obj.exploitpoc())
            elif keyword == 'hardware':
                obj.hardware()
                return (obj.exploitpoc())
            elif keyword == 'industrial':
                obj.industrial()
                return (obj.exploitpoc())
            else:
                return "Error!"
        else:
            return "Please input url"


