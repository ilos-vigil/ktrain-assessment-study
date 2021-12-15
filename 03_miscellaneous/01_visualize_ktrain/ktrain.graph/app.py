from graphviz import Digraph, Graph, ENGINES

engines = list(ENGINES)
engines.sort()
engine = engines[1]

g = Digraph(f'graph_{engine}', filename=f'graph_{engine}.gv', engine=engine)
g.attr('node', shape='box')

with g.subgraph(name='cluster_graph') as c:
    c.node('graph.data')
    c.node('graph.learner')
    c.node('graph.models')
    c.node('graph.predictor')
    c.node('graph.preprocessor')

    c.attr(label='ktrain.graph')

g.edges([
    ('graph.preprocessor', 'graph.data'),
    ('graph.preprocessor', 'graph.predictor'),
])


# g.attr(label=r'\nktrain.graph module block diagram')
g.attr(fontsize='20')

g.render(format='png', view=False)