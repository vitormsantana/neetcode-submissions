class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        hash_table_nodes = {}
        for prereq in prerequisites:
            hash_table_nodes[prereq[0]] = hash_table_nodes.get(prereq[0], [])
            hash_table_nodes[prereq[0]].append(prereq[1])
        for i in range(numCourses):
            if i not in hash_table_nodes:
                hash_table_nodes[i] = None
        print(f'hash_table_nodes: {hash_table_nodes}')

        def dfs(course, hash_set):
            if course in hash_set:
                return False
            hash_set.add(course)
            if course in hash_table_nodes and hash_table_nodes[course] is not None:
                for prereq in hash_table_nodes[course]:
                    if dfs(prereq, hash_set) == False:
                        return False
            hash_set.remove(course)
            return True
        
        for i in range(numCourses):
            hash_set = set()
            if dfs(i, hash_set) == False:
                print(f'falhou para o node {i}')
                return False
        return True