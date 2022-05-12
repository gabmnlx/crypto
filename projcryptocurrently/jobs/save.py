from datetime import datetime

t=datetime.now()

if t.hour % 2 == 0:
    save_destination = "sentiment_analyzer/out/"
    graph_destination = "projcryptocurrently/static/graphs/"
    graph_view = "graphs2"
else:
    save_destination = "sentiment_analyzer/out2/"
    graph_destination = "projcryptocurrently/static/graphs2/"
    graph_view = "graphs"

def return_save():
    return save_destination

def return_graph_save():
    return graph_destination

def return_graph_view():
    return graph_view