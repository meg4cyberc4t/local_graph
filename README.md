# LocalGraph

## `graph.py`
Graph implementation in the form of abstraction.
//
_Реализация графа в виде абстракции._


## Usage example / Пример использования

```python
from graph import LocalGraph

lg = LocalGraph.from_adjacency_map({'A': ('B', 'C'), 'B': ('A', 'C'), 'C': ('A', 'B')})
lg.add_node('E')
lg.add_edge(('C', 'A'))
print(lg.to_adjacency_map())
```
