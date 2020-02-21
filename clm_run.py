#!/usr/bin/python
import xmlrpclib,  argparse,  getpass,  textwrap
from datetime import datetime

class Password(argparse.Action):
    def __call__(self, parser, namespace, values, option_string):
        if values is None:
            values = getpass.getpass()

        setattr(namespace, self.dest, values)

parser = argparse.ArgumentParser()
parser = argparse.ArgumentParser(prog='PROG', formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent('''\
This scripts helps to manage content lifecycle management projects. 
Sample command:
              python clm_run.py -s bjsuma.bo2go.home -u bjin -p suse1234 --listProject
              python clm_run.py -s bjsuma.bo2go.home -u bjin -p suse1234 --listEnvironment --projLabel myprojlabel
              python clm_run.py -s bjsuma.bo2go.home -u bjin -p suse1234 --build --projLabel myprojlabel \n \
              python clm_run.py -s bjsuma.bo2go.home -u bjin -p suse1234 --promote --projLabel myprojlabel --envLabel teststage  \n \
The script can build project, update and promote stages or environments.
Check taskomatic logs in order to monitor the status of the build and promote tasks e.g. # tail -f /var/log/rhn/rhn_taskomatic_daemon.log. '''))

parser.add_argument("--listProject", action="store_true")
parser.add_argument("--listEnvironment", action="store_true")
parser.add_argument("--build", action="store_true")
parser.add_argument("--promote", action="store_true")
parser.add_argument("-s", "--server", help="Enter your suse manager host address e.g. myserver.abd.domain",  default='localhost',  required=True)
parser.add_argument("-u", "--username", help="Enter your suse manager loginid e.g. admin ", default='admin',  required=True)
parser.add_argument('-p', action=Password, nargs='?', dest='password', help='Enter your password',  required=True)
parser.add_argument("--projname", help="Enter the desired project name. e.g. myproject",  required=False)
parser.add_argument("--projLabel", help="Enter the project label. e.g. mytest",  required=False)
parser.add_argument("--envLabel", help="Enter the environment label. e.g. dev",  required=False)
args = parser.parse_args()

MANAGER_URL = "http://"+ args.server+"/rpc/api"
MANAGER_LOGIN = args.username
MANAGER_PASSWORD = args.password
client = xmlrpclib.Server(MANAGER_URL, verbose=0)
key = client.auth.login(MANAGER_LOGIN, MANAGER_PASSWORD)
today = datetime.today()
earliest_occurrence = xmlrpclib.DateTime(today)

def printzip(dict_object):
    for i in dict_object:
        keys = i.keys()
        val = i.values()
        print("Item---------------------------------------------")
        for k in keys:
            print ("{:<20}".format(k)), 
        print("\n")
        for v in val:
            print ("{:<20}".format(v)), 
        print("\n")
        print("----------------------------------------------------")
    return

def listproject(key):
    projlist = client.contentmanagement.listProjects(key)
    if projlist:
        printzip(projlist)
#        for i in projlist:
#            print("project---------------------------------------------")
#            for k,  v in i.items():
#                print("{} => {}".format(k, v))
#            print("----------------------------------------------------")
        return True
    else:
        print("no projects found")
        return False

def listEnvironment(key, projectLabel):
    envlist = client.contentmanagement.listProjectEnvironments(key, projectLabel)
    if envlist:
        printzip(envlist)
#        for i in envlist:
#            print("Environment----------------------------------------------")
#            for k,  v in i.items():
#                print("{} => {}".format(k, v))
#            print("---------------------------------------------------------")
        return True
    else:
        print("no projectEnvironments found")
        return False

def buildproject(key,  projLabel):
    try:
        buildresult = client.contentmanagement.buildProject(key, projLabel)
        print("project build task: %s"  %(str(buildresult)))
    except:
        return False
    return buildresult

def promoteenvironment(key,  projLabel,  envLabel):
    try:
        promote_result = client.contentmanagement.promoteProject(key, projLabel,  envLabel)
        print("promote %s %s task: %s"  %(projLabel, envLabel, str(promote_result)))
    except:
        return False
    return promote_result
    
if args.listProject:
    try:
        ret = listproject(key)
    except:
        print('something went wrong with listproject')
elif args.listEnvironment and args.projLabel:
    try:
        ret = listEnvironment(key, args.projLabel)
    except:
        print("something went wrong with listEnvironment.")
elif args.build and args.projLabel:
    try:
        ret = buildproject(key, args.projLabel)
    except:
        print("something went wrong with buildproject.")
elif args.promote and args.projLabel and args.envLabel:
     try:
        ret = promoteenvironment(key, args.projLabel,  args.envLabel)
     except:
        print("something went wrong with promote environment.")
else:
    print("Please verify you entered correct parameters. Exiting.")

    
