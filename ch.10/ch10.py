from Array import Deque
from Array import PriorityQ


dqm = Deque.MyCircularDeque(3)
s = PriorityQ.Solution()
ListNode = PriorityQ

if __name__ == '__main__':
  print(dqm.insertFront(1))
  print(dqm.insertLast(2))
  print(dqm.deleteFront())
  print(dqm.deleteLast())
  print(dqm.getFront())
  print(dqm.getRear())
  print(dqm.isEmpty())
  print(dqm.isFull())


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)
answer = s.mergeKLists([l1,l2,l3])
if __name__ == '__main__':
  while answer is not None: # None에서 멈춤
    print(f'{answer.val}', end=" ") # f'{}' f-string는 문자열 포매팅
    answer = answer.next # 다음숫자 불러온다



