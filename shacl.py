import pyshacl

data_graph = """
@prefix study: <http://ontology.bms.com/ontologies/Study#> .
@prefix metadata: <http://topbraid.org/metadata#> .
@prefix ncit:  <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix sh:    <http://www.w3.org/ns/shacl#> .
@prefix teamwork: <http://topbraid.org/teamwork#> .
@prefix study_ontology: <http://ontology.bms.com/ontologies/Study_Ontology#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dash:  <http://datashapes.org/dash#> .

ncit:C63536#CN162-016
    a ncit:C63536 ;
    ncit:C63536studyId "CN138-652";
    ncit:C63536studyId "CN138-651".
    
"""
# "C:/Users/pc/PycharmProjects/star/Study_output_triples.ttl"
shapes_graph = """

@prefix ncit:  <http://ncicb.nci.nih.gov/xml/owl/EVS/Thesaurus.owl#> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix owl:   <http://www.w3.org/2002/07/owl#> .
@prefix sh:    <http://www.w3.org/ns/shacl#> .
@prefix study_ontology: <http://ontology.bms.com/ontologies/Study_Ontology#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs:  <http://www.w3.org/2000/01/rdf-schema#> .
@prefix dash:  <http://datashapes.org/dash#> .

ncit:StudyShape
    a sh:NodeShape ;
    sh:targetClass ncit:C63536 ;
    sh:property [
        sh:path ncit:C63536studyId ;
        sh:datatype xsd:string ;
        sh:name "Study Id" ;
        sh:minCount     1 ;
        sh:maxCount     1 ;
        sh:severity     sh:Violation ;
    ] .
"""
# "C:/Users/pc/PycharmProjects/star/study_ontologyx.ttl"



results = pyshacl.validate(
    data_graph,
    shacl_graph=shapes_graph,
    data_graph_format="ttl",
    shacl_graph_format="ttl",
    inference="rdfs",
    debug=True,
    serialize_report_graph="ttl",
)

conforms, report_graph, report_text = results

print("conforms", conforms)
