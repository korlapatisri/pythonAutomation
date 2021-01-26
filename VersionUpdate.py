import os
import yaml
#install pip install pyyaml
# pip install os
#javaVersion, javaVersionLatest, tomcatVersion, tomcatVersionLatest = raw_input("Java Old Version: "), raw_input("Java New Version: "), raw_input("Tomacat Old Version: "), raw_input("Tomcat New Version: ")

updateVersion = raw_input("Enter tomcat Version: ")
javaVersion = raw_input("Enter Java Version (in the form '/apps/java/jdk8u'): ")

path = '/Users/shrikorlapati/Documents/automation/repos/servers-development/srvrs/tomcat' 

for rootdir, subdir, allfiles in os.walk(path):
      for filename in allfiles:
            filePath = os.path.join(rootdir, filename)
            if filePath.endswith(".yml"):
                  with open(filePath, 'r') as ymlFile:
                    ymlData = yaml.load(ymlFile, Loader=yaml.FullLoader)
                    # print ymlData['srv']['context'][0]['name']
                    # print ymlData['srv']['ver']
                    # print ymlData['srv']['host']
                    ymlData['server.template.version'] = updateVersion
                    ymlData['java.home'] = javaVersion

                  with open(filePath, 'w') as ymlFile:
                    yaml.dump(ymlData, ymlFile, default_flow_style=False)





                 

# with open(filePath, 'r') as tomcatfile:
#   filedata=tomcatfile.read()
#   filedata=filedata.replace(javaVersion, javaVersionLatest)
#   filedata=filedata.replace(tomcatVersion, tomcatVersionLatest)
# with open(filePath,'w') as tomcatfileupdate:
#   tomcatfileupdate.write(filedata) 