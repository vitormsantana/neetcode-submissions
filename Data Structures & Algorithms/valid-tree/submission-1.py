class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        hash_table_nodes = {}
        prerequisites = edges
        numCourses = n

        for prereq in prerequisites:
            hash_table_nodes[prereq[0]] = hash_table_nodes.get(prereq[0], [])
            hash_table_nodes[prereq[0]].append(prereq[1])

            hash_table_nodes[prereq[1]] = hash_table_nodes.get(prereq[1], [])
            hash_table_nodes[prereq[1]].append(prereq[0])

        for i in range(numCourses):
            if i not in hash_table_nodes:
                hash_table_nodes[i] = None
        print(f'hash_table_nodes: {hash_table_nodes}')

        def dfs(course, hash_set, parent):
            if course in hash_set:
                return False
            hash_set.add(course)
            if course in hash_table_nodes and hash_table_nodes[course] is not None:
                for prereq in hash_table_nodes[course]:
                    if prereq == parent:
                        continue
                    if dfs(prereq, hash_set, course) == False:
                        return False
            return True
        
        hash_set = set()
        if dfs(0, hash_set, -1) == False:
            return False
        return len(hash_set) == n