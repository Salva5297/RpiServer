from SPARQLWrapper import SPARQLWrapper, CSV
import csv
from Database.database import insert_data


def executeSPARQLquery():
    """
    Executes a SPARQL query and returns the results processed.
    """
    
    query = """ SELECT ?timestamp, ?property, ?o 
                FROM <http://virtuoso_db:8890/rpisensordata> 
                WHERE {
                    ?s <https://saref.etsi.org/core/hasValue> ?o.
                    ?s <https://saref.etsi.org/core/hasTimeStamp> ?timestamp.
                    ?s <https://saref.etsi.org/core/relatesToProperty> ?property.
                    FILTER NOT EXISTS {
                        ?s <https://saref.etsi.org/core/hasValue>/<https://saref.etsi.org/core/hasTimeStamp>/<https://saref.etsi.org/core/relatesToProperty> ?timestamp2
                        FILTER (?timestamp2 > ?timestamp)
                    }
                } ORDER BY DESC(?timestamp)
                LIMIT 100
            """
   
    sparql = SPARQLWrapper("https://sensorize.linkeddata.es/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(CSV)
    results = sparql.query().convert()
    
    results = [x.split(",") for x in results.decode("utf-8").split("\n")]
    
    newResults = [[result[0].replace('"',''), result[1].split('https://bimerr.iot.linkeddata.es/def/weather#')[1].replace('"',''), result[2].replace('"','')] for result in results[1:] if result[0] != "" and result[1].split('https://bimerr.iot.linkeddata.es/def/weather#')[1].replace('"','') != "DetailedStatus"]

    insert_data(newResults)

