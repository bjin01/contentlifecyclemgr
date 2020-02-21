# contentlifecyclemgr
SUSE Manager v4.x comes with a new feature "Content Lifecycle Management" (CLM) which helps to prepare channel clonning and staging by using Web UI. CLM is great new feature but spacecmd does not provide and commandline possibilities to automate the build and promote tasks. If someone need to trigger the build and promote tasks with certain schedules the only way to achieve is using API.

This script helps admins to trigger "build" and "promote" tasks which can be scheduled by using contab on SUSE Manager v4.x host.

```This scripts helps to manage content lifecycle management projects. 
Sample command:
              python clm_run.py -s bjsuma.bo2go.home -u bjin -p suse1234 --listProject
              python clm_run.py -s bjsuma.bo2go.home -u bjin -p suse1234 --listEnvironment --projLabel myprojlabel
              python clm_run.py -s bjsuma.bo2go.home -u bjin -p suse1234 --build --projLabel myprojlabel 
               python clm_run.py -s bjsuma.bo2go.home -u bjin -p suse1234 --promote --projLabel myprojlabel --envLabel teststage  
 The script can build project, update and promote stages or environments.
Check taskomatic logs in order to monitor the status of the build and promote tasks e.g. # tail -f /var/log/rhn/rhn_taskomatic_daemon.log. 

optional arguments:
  -h, --help            show this help message and exit
  --listProject
  --listEnvironment
  --build
  --promote
  -s SERVER, --server SERVER
                        Enter your suse manager host address e.g.
                        myserver.abd.domain
  -u USERNAME, --username USERNAME
                        Enter your suse manager loginid e.g. admin
  -p [PASSWORD]         Enter your password
  --projname PROJNAME   Enter the desired project name. e.g. myproject
  --projLabel PROJLABEL
                        Enter the project label. e.g. mytest
  --envLabel ENVLABEL   Enter the environment label. e.g. dev```
  
  

