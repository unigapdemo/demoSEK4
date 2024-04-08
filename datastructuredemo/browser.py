# demo stack
class Node:
    def __init__(self, data:str):
        self.data = data
        self.next = None
        self.max_val = data

# data strucuture
class Stack:
    def __init__(self):
        self.top = None # head
        self.currentPeek = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top # old top - new node la top moi
        self.top = new_node
        self.currentPeek = self.top

    def pop(self):
        # Remove a top ele of the stack
        if self.top is None:  # Print error if the stack is empty
            return print('Cannot pop an empty stack!')
        else:  # Else assign previous ele's value to the top
            print(f'Popped {self.top.data} out of the stack!')
            self.top = self.top.next

    def print_ele(self):
        cur_node = self.top
        count = 0
        while cur_node is not None:
            print(str(count) + " " + cur_node.data)
            count += 1
            cur_node = cur_node.next


    def currentPeekPrint(self):
        if self.currentPeek == None:
            print("minh dang o trang tab moi")
        else:
            print(currentPeek.data)

    def isCurrentPeekIsHeadOfStack(self):
        if self.currentPeek == self.top:
            return True
        else:
            return False

    def popToCurrentPeek(self):
        while self.currentPeek != self.top:
            self.pop()

    def changeCurrentPeek(self):
        if self.currentPeek != None:
            self.currentPeek = self.currentPeek.next

    def getPreviousCurrentPeekNode(self):
        temp = self.top
        if temp == self.currentPeek:
            return temp
        else:
            while temp.next != self.currentPeek:
                temp = temp.next
            return temp


class Browser:
    def __init__(self):
        self.stack = Stack()

    def goto(self, url):
        if self.stack.isCurrentPeekIsHeadOfStack():
            self.stack.push(url)
        else:
            self.stack.popToCurrentPeek()
            self.stack.push(url)

    def back(self):
        self.stack.changeCurrentPeek()

    def forward(self):
        # TODO
        previous_page = self.stack.getPreviousCurrentPeekNode()
        self.stack.currentPeek = previous_page

    def print_all_page_in_browser(self):
        self.stack.print_ele()
        print("last ----- new tab")


b = Browser()

b.goto("google")
b.goto("facebook")
b.goto("tiktok")
b.goto("insta")
b.goto("messenger")

# b.print_all_page_in_browser()

# test vao trang moi o giua
# b.back()
# b.back()

# b.goto("dantri")
# b.print_all_page_in_browser()

# test back forward
# b.back()
# b.back()
# b.back()

# b.forward()
# b.forward()

# b.goto("dantri")
# b.print_all_page_in_browser()
