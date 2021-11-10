import os
import tempfile
import time
import subprocess
import json

def timer(fileName):
    
    tempFile = open('Mappings/mappings-source.json', 'w') # Problem with mappings changing file name in mappings-source.json
    data = {
            "datasources": [
                {
                    "id": "All Datasource",
                    "handler": {
                        "type": "JsonHandler",
                        "iterator": "$"
                    },
                    "provider": {
                        "type": "FileProvider",
                        "file": "" + fileName + ""
                    }
                },
                {
                    "id": "Sensors Datasource",
                    "handler": {
                        "type": "JsonHandler",
                        "iterator": "$.Sensors.[*]"
                    },
                    "provider": {
                        "type": "FileProvider",
                        "file": "" + fileName + ""
                    }
                }
            ]
        }
    json.dump(data, tempFile, indent=4)
    tempFile.close()
    
 
    start = time.time() #start time
    print('java -jar helio.jar --mappings=Mappings --config=Helio/config.json --write=RDF/'+ fileName.replace('/tmp/','') +'.ttl --close --clean')

    os.system('java -jar helio.jar --mappings=Mappings --config=Helio/config.json --write=RDF/'+ fileName.replace('/tmp/','') +'.ttl --close --clean')
    
    end = time.time()
    print("Elapsed time is  {}".format(end-start))
    
    proc = subprocess.Popen(["curl", "--digest", "--verbose" , "--user", "dba:mysecret", "--url", 'http://virtuoso_db:8890/sparql-graph-crud-auth?graph-uri=http://virtuoso_db:8890/rpisensordata', "-T", "RDF/"+ fileName.replace('/tmp/','') +".ttl"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = proc.communicate()
    lastCode = str(err).split('HTTP/1.1 ')[-1].split(" ")[0]
    
    os.remove('RDF/'+ fileName.replace('/tmp/','') +".ttl")
    
    if lastCode == "200":
        return ["All OK", 200]
    elif lastCode == "201":
        return ["Created Graph", 201]
    elif lastCode == "401":
        return ["Error with Authorization", 401]
    else:
        return ["You did something wrong", 500]
    
    
