class Graph:
    def __init__(self, directed=False):
        self._graph = {}
        self._directed = directed
        
    def add_edge(self, node1, node2, w=1):
        # node1 -> node2
        if node1 not in self._graph.keys():
            self._graph[node1] = set()
        self._graph[node1].add((node2, w))
        
        # node2 -> node1 if not directed
        if not self._directed:
            if node2 not in self._graph.keys():
                self._graph[node2] = set()
            self._graph[node2].add((node1, w))
        
    def delete_edge(self, node1, node2):
        # node1 -> node2
        if node1 in self._graph.keys():
            for n, w in self._graph[node1]:
                if n == node2:
                    self._graph[node1].discard((n, w))
                    break
            if self._graph[node1] == set():
                del self._graph[node1]
        
        # node2 -> node1 if not directed
        if not self._directed:
            if node2 in self._graph.keys():
                for n, w in self._graph[node2]:
                    if n == node1:
                        self._graph[node2].discard((n, w))
                        break
                if self._graph[node2] == set():
                    del self._graph[node2]
                
    def are_connected(self, node1, node2):
        if node1 not in self._graph.keys():
            return False
        else:
            for n, w in self._graph[node1]:
                if n == node2:
                    return True
        return False
        
    def adj_list(self):
        return self._graph
        
    def find_path(self, node1, node2, path=[]):
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph.keys():
            return None
        for new_node, new_w in self._graph[node1]:
            if new_node not in path:
                new_path = self.find_path(new_node, node2, path)
                if new_path:
                    return new_path
        return None
        
    def find_all_paths(self, node1, node2, path=[]):
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph.keys():
            return None
        all_paths = []
        for new_node, new_w in self._graph[node1]:
            if new_node not in path:
                new_paths = self.find_all_paths(new_node, node2, path)
                if new_paths:
                    if isinstance(new_paths[0], list):
                        all_paths = all_paths + new_paths
                    else:
                        all_paths = all_paths + [new_paths]
        if all_paths == []:
            return None
        return all_paths
        
    def find_shortest_path(self, node1, node2, path=[], current_weight=0):
        path = path + [node1]
        if node1 == node2:
            return (path, current_weight)
        if node1 not in self._graph.keys():
            return None
        shortest_path = None
        for new_node, new_w in self._graph[node1]:
            if new_node not in path:
                new_path = self.find_shortest_path(new_node, node2, path, current_weight + new_w)
                if shortest_path is None or new_path[1] < shortest_path[1]:
                    shortest_path = new_path
        return shortest_path
        
    def dijkstras_algorithm(self, node):
        # Initialize
        nodes_left = set()
        dist = {}
        prev = {}        
        for n in self._graph.keys():
            nodes_left.add(n)
            dist[n] = 999
            prev[n] = None
        dist[node] = 0
        
        # Loop through nodes
        while nodes_left != set():
            nodes_left_dist = {i:dist[i] for i in dist if i in nodes_left}
            current_node = min(nodes_left_dist, key=nodes_left_dist.get)
            nodes_left.remove(current_node)
            for new_node, new_weight in self._graph[current_node]:
                new_dist = dist[current_node] + new_weight
                if new_dist < dist[new_node]:
                    dist[new_node] = new_dist
                    prev[new_node] = current_node
        
        # Package up results
        out = {}
        for n in self._graph.keys():
            if n == node:
                out[n] = ([], dist[n])
            elif prev[n] == node:
                out[n] = ([prev[n]], dist[n])
            else:
                path = [prev[n]]
                while prev[path[0]] is not None:
                    path = [prev[path[0]]] + path
                out[n] = (path, dist[n])
        
        return out