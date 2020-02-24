# content lifecycle manager - automation
SUSE Manager v4.x comes with a new feature "Content Lifecycle Management" (CLM) which helps to prepare channel cloning and staging by using Web UI. CLM is great new feature. If someone need to trigger the build and promote tasks with certain schedules the only way to achieve is using API. You can schedule this script using crontab on SUSE Manager host.

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
  --envLabel ENVLABEL   Enter the environment label. e.g. dev
  ```
  
##main features

* list projects
* list project environments by providing project label
* build project by providing project label
* promote environment (stages) by providing project label and project environment label. 

##specical checks added:
* if build or promote should run the script will check if the current status of the environment (first environment or the given environment) has status building or generating_repodata. If yes then the task will not be triggered and output the information to standard output to let user know that the build or promote is already running.


