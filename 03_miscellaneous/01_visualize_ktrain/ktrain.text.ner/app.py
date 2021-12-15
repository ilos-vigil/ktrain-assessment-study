from graphviz import Digraph, Graph, ENGINES

engines = list(ENGINES)
engines.sort()
engine = engines[1]

g = Digraph(f'ktrain_text_ner_{engine}', filename=f'ktrain_text_ner_{engine}.gv', engine=engine)
g.attr('node', shape='box')

g.node('text.textutils')
g.node('text.preprocessor')

with g.subgraph(name='cluster_text.ner') as c:
    c.node('text.ner.learner')
    c.node('text.ner.models')
    c.node('text.ner.data')
    c.node('text.ner.preprocessor')
    c.node('text.ner.predictor')

    with c.subgraph(name='cluster_text.ner.anago') as sc:
        sc.node('text.ner.anago.callbacks')
        sc.node('text.ner.anago.models')
        sc.node('text.ner.anago.preprocessing')
        sc.node('text.ner.anago.trainer')
        sc.node('text.ner.anago.tagger')
        sc.node('text.ner.anago.wrapper')
        sc.node('text.ner.anago.layers')
        sc.node('text.ner.anago.utils')
        sc.node('text.ner.anago.layers_standalone')

        sc.attr(label='ktrain.text.ner.anago')
    c.attr(label='ktrain.text.ner')

edges = [
    ['text.ner.anago.models', 'text.ner.models'],
    ['text.ner.anago.tagger', 'text.ner.anago.wrapper'],
    ['text.ner.anago.callbacks', 'text.ner.anago.trainer'],
    ['text.ner.anago.models', 'text.ner.anago.wrapper'],
    ['text.ner.anago.preprocessing', 'text.ner.anago.wrapper'],
    ['text.ner.anago.trainer', 'text.ner.anago.wrapper'],
    ['text.ner.anago.utils', 'text.ner.predictor'],
    ['text.ner.anago.utils', 'text.ner.anago.preprocessing'],
    ['text.ner.anago.utils', 'text.ner.anago.trainer'],
    ['text.ner.anago.utils', 'text.ner.anago.wrapper'],
    ['text.ner.preprocessor', 'text.ner.data'],
    ['text.ner.preprocessor', 'text.ner.models'],
    ['text.ner.preprocessor', 'text.ner.predictor'],
    ['text.textutils', 'text.ner.predictor'],
    ['text.textutils', 'text.ner.data'],
    ['text.preprocessor', 'text.ner.predictor']
]

for e in edges:
    g.edge(e[0], e[1])

# fake edge to make result more beautiful
g.edge('text.textutils', 'text.preprocessor', style='invis')
g.edge('text.preprocessor', 'text.ner.models', style='invis')

# g.attr(label=r'\nktrain.text.ner module block diagram')
# g.attr(fontsize='20')

print(g.source)

g.render(format='png', view=False)