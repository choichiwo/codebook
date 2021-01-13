class ListNode:
    def __init__(self, x):  # __init__() : 초기화 함수
        self.val = x  # 결과값을 x로 지정
        self.next = None


class MyCircularDeque:
    def __init__(self, k: int):  # __init__() : 초기화 함수
        self.head, self.tail = ListNode(None), ListNode(None)
        self.k, self.len = k, 0  # 최대 길이를 k로 설정 현재 길이를 0으로 설정
        self.head.right, self.tail.left = self.tail, self.head

    # 이중 연결 리스트에 신규 노드 삽입
    def _add(self, node: ListNode, new: ListNode):  # PEP 8 규칙에 따라 _add()
        n = node.right
        node.right = new
        new.left, new.right = node, n
        n.left = new

    # 이중 연결 리스트에 신규 노드 삭제
    def _del(self, node: ListNode):
        n = node.right.right
        node.right = n
        n.left = node

    def insertFront(self, value: int) -> bool:
        if self.len == self.k:  # (k)최대 길이
            return False
        self.len += 1
        self._add(self.head, ListNode(value))
        return True

    def insertLast(self, value: int) -> bool:
        if self.len == self.k:
            return False
        self._add(self.tail.left, ListNode(value))
        return True

    def deleteFront(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.head)
        return True

    def deleteLast(self) -> bool:
        if self.len == 0:
            return False
        self.len -= 1
        self._del(self.tail.left.left)
        return True

    def getFront(self) -> int:
        return self.head.right.val if self.len else -1

    def getRear(self) -> int:
        return self.tail.left.val if self.len else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.k