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
                        "file": "../Example/source.json"
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
    
 
    start = time.time() #start time

    os.system('java -jar Helio/helio.jar --mappings=../Mappings --config=config.json --write=../RDF/'+ fileName +'.ttl --close --clean')
    
    
    proc = subprocess.Popen(["curl", "--digest", "--verbose" , "--user", "dba:mysecret", "--url", 'http://virtuoso_db:8890/sparql-graph-crud-auth?graph-uri=http://virtuoso_db:8890/rpisensor', "-T", "../RDF/"+ fileName +".ttl"], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out, err) = proc.communicate()
    lastCode = str(err).split('HTTP/1.1 ')[-1].split(" ")[0]
    if lastCode == "200":
        print("All OK")
    elif lastCode == "201":
        print("Created Graph")
    elif lastCode == "401":
        print("Error with Authorization")
    else:
        print("You did something wrong")
    
    end = time.time()
    print("Elapsed time is  {}".format(end-start))
