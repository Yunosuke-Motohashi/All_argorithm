# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_ay
# A51 - Stack

Q = int(input())

class Stack:
    """
    スタックの実装
    リストの後ろに要素を追加、削除することでLIFOを実現
    """
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def top(self):
        return self.items[-1]

stack = Stack()
for _ in range(Q):
    query = list(input().split())
    if query[0] == "1":
        stack.push(query[1])
    elif query[0] == "2":
        print(stack.top())
    else: # query[0] == 3
        stack.pop()

#### dequeを使う場合
from collections import deque

Q = int(input())
queries = [input().split() for _ in range(Q)]
stack = deque()

for q in queries:
    if q[0] == "1":
        stack.append(q[1])
    elif q[0] == "2":
        print(stack[-1])
    else: # q[0] == 3
        stack.pop()

"""
dequeは両端キューであり、
append と pop を使えば LIFO スタック、
append と popleft を使えば FIFO キューとして動きます。
リストと異なり、先頭への要素追加、削除もオーダー(1)で行える
"""