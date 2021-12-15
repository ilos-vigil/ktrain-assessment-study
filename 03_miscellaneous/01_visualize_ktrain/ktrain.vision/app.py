from graphviz import Digraph, Graph, ENGINES

engines = list(ENGINES)
engines.sort()
engine = engines[1]

g = Digraph(f'vision_{engine}', filename=f'vision_{engine}.gv', engine=engine)
g.attr('node', shape='box')

with g.subgraph(name='cluster_vision') as c:
    c.node('vision.data')
    c.node('vision.learner')
    c.node('vision.models')
    c.node('vision.predictor')
    c.node('vision.preprocessor')
    c.node('vision.wrn')

    c.attr(label='ktrain.vision')

g.edges([
    ('vision.preprocessor', 'vision.data'),
    ('vision.data', 'vision.learner'),
    ('vision.wrn', 'vision.models'),
    ('vision.preprocessor', 'vision.predictor'),
])

# g.attr(label=r'\nktrain.vision module block diagram')
g.attr(fontsize='20')

g.render(format='png', view=False)