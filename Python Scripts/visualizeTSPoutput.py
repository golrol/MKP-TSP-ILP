import networkx as nx
import matplotlib.pyplot as plt
import json

def draw_graph_from_route(route_to_draw):
    """
    Draws the graph from a given route
    @param route_to_draw: The route to draw
    @type route_to_draw: tuple
    @param graph: The graph
    @type graph: Graph
    @return: None
    """

    colors = ['g', 'b', 'y', 'k', 'c', 'm']
    colorIndex = 0

    gr = nx.DiGraph()
    
    for sub_route in route_to_draw:
        for i in range(len(sub_route) - 1):
            gr.add_edge(sub_route[i], sub_route[i+1], color=colors[colorIndex % len(colors)])
        colorIndex += 1

    ax = plt.gca()
    ax.set_title('All the routes')
    ax.set_xlim(0, 100)
    
    # pos = nx.circular_layout(gr)
    edges = gr.edges()
    colorosDict = [gr[u][v]['color'] for u,v in edges]
    pos = GetRealLocations(route_to_draw)
    print(pos)
    pos[0] = (86,76)
    pos[10] = (0,0)

    nx.draw(gr, pos=pos, with_labels=True, arrowsize=20, edge_color = colorosDict)
    plt.show()


def parseCplexData(fileNames):
    # k = 10
    retVal = []
    for fileName in fileNames:
        routDict = {}
        with open(fileName) as f:
            for line in f:
                if "->" in line:
                    line = line.split()
                    routDict[int(line[0])] = int(line[2])

            tmpArray = [0]
            index = 0
            while True:
                tmpArray.append(routDict[index])
                index = routDict[index]
                if routDict[index] == 0:
                    break

            tmpArray.append(0)
            retVal.append(tmpArray)
            # k=k+10
    return retVal

def GetRealLocations(routes):
    retVal = {}
    with open("Catalog.json", "r") as f:
        catalog = json.load(f)
        for route in routes:
            for node in route:
                for item in catalog:
                    if item['id'] == node:
                        retVal[node] = (item["locationX"], item["locationY"])
                        print(item["locationX"], item["locationY"])
                        break
    return retVal

if __name__ == '__main__':
    #x = parseCplexData(["TSPOutput1.txt", "TSPOutput2.txt", "TSPOutput3.txt", "TSPOutput4.txt"])
    
    x = parseCplexData(["TSPOutput2.txt"])
    print(x)
    draw_graph_from_route(x)
