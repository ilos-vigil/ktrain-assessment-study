from graphviz import Digraph, Graph, ENGINES

engines = list(ENGINES)
engines.sort()
engine = engines[1]

g = Digraph(f'tabular_{engine}', filename=f'tabular_{engine}.gv', engine=engine)
g.attr('node', shape='box')

with g.subgraph(name='cluster_tabular') as c:
    c.node('tabular.data')
    c.node('tabular.models')
    c.node('tabular.predictor')
    c.node('tabular.preprocessor')

    c.attr(label='ktrain.tabular')

g.edges([
    ('tabular.preprocessor', 'tabular.data'),
    ('tabular.preprocessor', 'tabular.predictor'),
])



# g.attr(label=r'\nktrain.tabular module block diagram')
g.attr(fontsize='20')

g.render(format='png', view=False)