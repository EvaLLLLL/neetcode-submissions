class ListNode:
    def __init__(self, key: int):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.num_buckets = 10**4
        self.table = [ListNode(0) for _ in range(self.num_buckets)]
    
    def _get_node(self, key: int) -> int:
        return self.table[key % self.num_buckets]
        
    def add(self, key: int) -> None:
        cur = self._get_node(key)
        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)

    def remove(self, key: int) -> None:
        cur = self._get_node(key)
        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self._get_node(key)
        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False