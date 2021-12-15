from graphviz import Digraph, Graph, ENGINES

engines = list(ENGINES)
engines.sort()
engine = engines[1]

g = Digraph(f'ktrain_{engine}', filename=f'ktrain_{engine}.gv', engine=engine)
g.attr('node', shape='box')

# Module
with g.subgraph(name='cluster') as c:
    c.attr('node', shape='box')

    c.node('core')
    c.node('data')
    c.node('imports')
    c.node('lroptimize')
    c.node('models')
    c.node('predictor')
    c.node('preprocessor')
    c.node('utils')
    c.node('model')

    c.node('vision')
    c.node('text')
    c.node('graph')
    c.node('tabular')

    c.attr(label='ktrain')

# Edge Module
g.edges([
    ('imports', 'core'),
    ('lroptimize', 'core'),
    ('utils', 'core'),
    ('vision', 'core'),
    ('text', 'core'),
    ('graph', 'core'),
    ('tabular', 'core'),
])
g.edge('imports', 'data')
g.edge('imports', 'model')
g.edges([
    ('imports', 'predictor'),
    ('utils', 'predictor'),
])
g.edge('imports', 'preprocessor')
g.edges([
    ('imports', 'utils'),
    ('data', 'utils')
])

# graph
g.edges([
    ('core', 'graph'),
    ('imports', 'graph'),
    ('models', 'graph'),
    ('data', 'graph'),
    ('imports', 'graph'),
    ('predictor', 'graph'),
    ('utils', 'graph'),
])


# tabular
g.edges([
    ('imports', 'tabular'),
    ('models', 'tabular'),
    ('predictor', 'tabular'),
    ('utils', 'tabular'),
    ('preprocessor', 'tabular'),
])

# text
g.edges([
    ('imports', 'text'),
    ('utils', 'text'),
    ('core', 'text'),
    ('data', 'text'),
    ('preprocessor', 'text'),
])

# vision
g.edges([
    ('core', 'vision'),
    ('imports', 'vision'),
    ('predictor', 'vision'),
    ('preprocessor', 'vision'),
    ('utils', 'vision'),
])

# g.attr(label=r'\nktrain module block diagram')
g.attr(fontsize='20')

g.render(format='png', view=False)