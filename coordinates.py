from csv import DictReader
from json import dump
import networkx as nx
from pathlib import Path

gml_file = Path() / "data" / "air_line_network.gml"

### Read the gml file as a network
air_line_graph = nx.read_gml(gml_file)

with open('data/airport-codes.csv', newline='',encoding="utf-8") as csvfile:
    coord_dict = {}
    reader = DictReader(csvfile)
    icaos = [data["ICAO"] for _, data in air_line_graph.nodes(data=True)]
    for row in reader:
        if row["ident"] in icaos:
            coords = row["coordinates"]
            coord_dict[row["ident"]] = [float(c) for c in coords.split(", ")]

with open('data/coordinates.json', 'w') as fp:
    dump(coord_dict, fp,  indent=4)