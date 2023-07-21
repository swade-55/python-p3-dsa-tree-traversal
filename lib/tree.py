class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_visit = [self.root]
    while nodes_to_visit:
      current = nodes_to_visit.pop()
      if current['id'] == id:
        return current
      nodes_to_visit = nodes_to_visit + current['children']
    return None
      
      

# def dfs(node):
#   nodes_to_visit = [node]
#   result = []
#   while len(nodes_to_visit)>0:
#     node = nodes_to_visit.pop(0)
#     result.append(node['value'])
#     nodes_to_visit = node['children'] + nodes_to_visit
#   return result