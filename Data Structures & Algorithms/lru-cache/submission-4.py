class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        # -- USING LIST --
        # self.cache = []
        # self.capacity = capacity

        # --- USING DOUBLY LINKED LIST
        self.capacity = capacity
        self.cache = {} # map key to node
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    
    def remove(self, node):
        # prev = node.prev
        # nxt = node.next
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self,node):
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        node.prev = prev
        self.right.prev = node

    def get(self, key: int) -> int:
        # for i in range(len(self.cache)):
        #     if self.cache[i][0] == key:
        #         tmp = self.cache.pop(i)
        #         self.cache.append(tmp)
        #         return tmp[1]
        # return -1

        # USING DOUBLY LL

        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
            
        
        return -1

    def put(self, key: int, value: int) -> None:
        # for i in range(len(self.cache)):
        #     if self.cache[i][0] == key:
        #         tmp = self.cache.pop()
        #         tmp[1] = value
        #         self.cache.append(tmp)
        #         return
            
        # if self.capacity == len(self.cache):
        #     self.cache.pop(0)
        
        # self.cache.append([key,value])

        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

