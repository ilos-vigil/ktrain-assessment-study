from graphviz import Digraph, Graph, ENGINES

engines = list(ENGINES)
engines.sort()
engine = engines[1]
print(engine)

g = Digraph(f'ktrain_text_{engine}', filename=f'ktrain_text_{engine}.gv', engine=engine)
g.attr('node', shape='box')

with g.subgraph(name='cluster_text') as s:
    s.node('text.data')
    s.node('text.eda')
    s.node('text.learner')
    s.node('text.models')
    s.node('text.predictor')
    s.node('text.preprocessor')
    s.node('text.qa.core')
    s.node('text.summarization.core')
    s.node('text.textutils')
    s.node('text.translation.core')
    s.node('text.zsl.core')
    s.node('text.ner')

    with s.subgraph(name='cluster_text.shallownlp') as c:
        c.attr('node', shape='box')

        c.node('text.shallownlp.classifier')
        c.node('text.shallownlp.imports')
        c.node('text.shallownlp.ner')
        c.node('text.shallownlp.searcher')
        c.node('text.shallownlp.utils')
        # c.node('text.shallownlp.version')

        c.attr(label='ktrain.text.shallownlp')

    s.attr(label="ktrain.text")


g.edges([
    ('text.preprocessor', 'text.data'),
    ('text.textutils', 'text.data'),
    ('text.preprocessor', 'text.eda'),
    ('text.textutils', 'text.eda'),
    ('text.preprocessor', 'text.learner'),
    ('text.preprocessor', 'text.models'),
    ('text.preprocessor', 'text.predictor'),
    ('text.textutils', 'text.preprocessor'),
    ('text.textutils', 'text.qa.core'),
    ('text.preprocessor', 'text.qa.core'),
])
g.edges([
    ('text.textutils', 'text.ner'),
    ('text.preprocessor', 'text.ner'),
])

# dummpy edge for better UI
g.edge('text.data', 'text.shallownlp.utils', style='invis')

# print(g.source)


# g.attr(label=r'\nktrain.text module block diagram')
# g.attr(fontsize='20')

g.render(format='png', view=False)