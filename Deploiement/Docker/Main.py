from pprint import pprint
import yaml
import argparse
import time
import sys
import os
from pexpect import pxssh
import threading
from threading import Thread
import docker
import itertools
import threading

done = False

def animate():
    global done
    done = False
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            return
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)

def Deployer (ip):

    client = docker.DockerClient(base_url = ip)
    client.images.pull("trexcisco/trex:2.36")
    c = client.containers.run("trexcisco/trex:2.36", ports = {4501:4501, 4500:4500, 4507:4507}, name = "trexserver", privileged = True, cap_add = ["ALL"], tty = True, stdin_open = True, detach = True)
    c.exec_run("bash -c 'cd /var/trex/v2.36/ && ./t-rex-64 -i'", detach = True)
    global done
    done = True
    return

def Remove (ip) :

    client = docker.DockerClient(base_url = ip)
    client.images.remove("trexcisco/trex:2.36", force = True)
    global done
    done = True
    return

def Clear (ip) :

    client = docker.DockerClient(base_url = ip)
    client.containers.get("trexserver").stop()
    client.containers.get("trexserver").remove()
    global done
    done = True

def Display(dic) :
    print "\033[1;34mConf\033[1;37m"
    size = 0
    sizec = 0
    for x, v in dic.items() :
        sizec += len(str(v))
        if len(str(v)) > size :
            size = len(v)
    print "  ",
    print '-' * (sizec - size)
    for x1, v1 in dic.items() :
        print  "   |  " + str(x1),
        print " " * (size - len(x1)),
        print ":",
        print " " * (size / 2) + str(v1),
        print " " * (size - len(str(v1)) + 3) + " |"
    print "  ",
    print '-' * (sizec - size)
    print '\n'
    return

def Flux(dic) :

    if (dic['both'] == "true") :
        os.system("cd trex-core/scripts/automation/trex_control_plane/stl/examples/ ; python Stateless.py -s {0} -k {1} -d {2} -f {3} --both".format(dic['sip'], dic['kpps'], dic['duration'], dic['flux']))
    else :
        os.system("cd trex-core/scripts/automation/trex_control_plane/stl/examples/ ; python Stateless.py -s {0} -k {1} -d {2} -f {3} -p {4}".format(dic['sip'], dic['kpps'], dic['duration'], dic['flux'], dic['port']))
    global done
    done = True
    return

def myThread(choise, dic, server) :

    if choise == "Deployer" :
        Thread(target = animate).start()
        t1 = Thread(target = Deployer(server))
    elif choise == "Flux" :
        Thread(target = animate).start()
        time.sleep(3)
        t1 = Thread(target = Flux(dic))
    elif choise == "Clear" :
        Thread(target = animate).start()
        t1 = Thread(target = Clear(server))
    elif choise == "Remove" :
        Thread(target = animate).start()
        t1 = Thread(target = Remove(server))
    t1.start()
    t1.join()
    return

def Parsing(stream1, stream2, dic) :

    docs1 = yaml.load_all(stream1)
    for doc1 in docs1 :
        for k1,v1 in doc1.items() :
            dic[k1] = v1
    docs2 = yaml.load_all(stream2)
    for doc2 in docs2 :
        for k2,v2 in doc2.items() :
            dic[k2] = v2
    for key, value in dic.items() :
        if key == 'duration' or key == 'kpps' :
            if (dic.get('duration') < 1 or dic.get('kpps') < 0.1) :
                print "\033[1;31mConf error\033[1;37m"
                return 1
        if (key != 'kpps' and key != 'flux' and key != 'duration' and key != 'both' and key != 'port' and key != 'sip' and key != 'sport') :
            print "\033[1;31mConf error\033[1;37m"
            return 1
    for arg in vars(args):
        if getattr(args, arg) != "null" :
            dic[arg] = getattr(args, arg)
    return 0


def main (iconf, args, display):

    dic = {}
    
    dest1 = iconf + "trex.yaml"
    dest2 = iconf + "server.yaml"
    try:
        stream1 = open(dest1, "r")
        stream2 = open(dest2, "r")
    except IOError as e:
        print("\033[1;31mS Couldn't open or write to file (%s)." % e)
        return
    if Parsing(stream1, stream2, dic) == 1 :
        return
    if display :
        Display(dic)
    if dic['both'] ==  'false':
        print "\033[1;37mYou start a [\033[1;32m" + str(dic['flux']) + "\033[1;37m] flux on the port [\033[1;32m" + str(dic['port']) + "\033[1;37m] at [\033[1;32m" + str(dic['kpps']) + "\033[1;37m] kpps during [\033[1;32m" + str(dic['duration']) + "\033[1;37m] secs on the ip [\033[1;32m" + str(dic['sip']) + "\033[1;37m]\n"
    else :
        print "\033[1;37mYou start a [\033[1;32m" + str(dic['flux']) + "\033[1;37m] flux with \033[1;32mBoth\033[1;37m port at [\033[1;32m" + str(dic['kpps']) + "\033[1;37m] kpps during [\033[1;32m" + str(dic['duration']) + "\033[1;37m] secs on the ip [\033[1;32m" + str(dic['sip']) + "\033[1;37m]\n"
    server = str(str(dic['sip']) + ":" + str(dic['sport']))
    print "\033[1;34mDeploiement Start\033[1;37m\n"
    myThread("Deployer", dic, server)
    print "\n\n\033[1;37mDeploiement \033[1;32mOk\033[1;37m\n"
    print "\033[1;34mStateless Flux Start\033[1;37m\n"
    myThread("Flux", dic, server)
    print "\033[1;37mStateless \033[1;32mOk\033[1;37m\n"
    print "\n\033[1;34mClear Start\033[1;37m\n"
    myThread("Clear", dic, server)
    print ("\n\n\033[1;37mClear \033[1;32mOk")
    if dic['remove'] :
        print "\n\n\033[1;34mRemove Start\033[1;37m\n"
        myThread("Remove", dic, server)
        print "\n\n\033[1;37mRemove \033[1;32mOk\033[1;37m"
    return

parser = argparse.ArgumentParser(description = "Script automatisation of Trex")
parser.add_argument('-k', '--kpps',
					dest = 'kpps',
					help = 'Nbr kpps in percentage',
					default = 'null',
					type = str)
parser.add_argument('-f', '--flux',
					dest = 'flux',
					help = 'the Name of the Stateless flux python script, differents scripts are located at trex-core/scripts/stl/',
					default = 'null',
					type = str)
parser.add_argument('-c', '--conf',
					dest = 'conf',
					help = 'Directory with the conf',
					default = 'null',
					required = True,
					type = str)
parser.add_argument('-d', '--duration',
					dest = 'duration',
					help = 'Duration of the test',
					default = 'null',
					type = str)
parser.add_argument('--remove',
                    help = 'remove the images after the test',
                    action  = 'store_true')
parser.add_argument('--display',
                    help = 'Display the conf',
                    action  = 'store_true')
args = parser.parse_args()

if __name__ == "__main__":
	main(args.conf, args, args.display)