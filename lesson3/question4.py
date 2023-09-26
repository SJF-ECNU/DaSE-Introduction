class Node:
    # 链表节点的定义
    def __init__(self, data, next=None):
        self.data = data  # 存储节点数据
        self.next = next  # 存储下一个节点的引用

    def AddNodeToEnd(self, new_node):
        # 添加节点到链表末尾
        if self is None:
            return new_node
        else:
            temp = self
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node
            return self

    def DeleteNode(self, data_to_delete):
        # 删除节点
        if self is None:
            return None
        else:
            temp = self
            temp_father = None  # 用于跟踪前一个节点
            while temp.data != data_to_delete and temp.next is not None:
                temp_father = temp
                temp = temp.next
            if temp.data != data_to_delete:
                return self
            if temp == self:
                self = self.next
            else:
                temp_father.next = temp.next
            return self

    def UpdateNodeValue(self, node_to_update, new_data):
        # 更新节点的值
        if self is None:
            return None
        else:
            temp = self
            while temp != node_to_update and temp.next is not None:
                temp = temp.next
            if temp is not None:
                temp.data = new_data
            return self

    def FindNode(self, data_to_find):
        # 查找节点
        if self is None:
            return None
        else:
            temp = self
            while temp.data != data_to_find and temp.next is not None:
                temp = temp.next
            if temp.data != data_to_find:
                return None
            return temp

    def PrintList(self):
        # 打印链表
        if self is None:
            print("List is empty")
        else:
            temp = self
            while temp is not None:
                print(temp.data, end=" -> ")
                temp = temp.next
            print("None")

if __name__ == "__main__":
    print("请输入链表的元素，以空格分隔：")
    input_list = input().split()
    head = Node(input_list[0])  # 创建链表头节点
    for i in input_list[1:]:
        new_node = Node(i)
        head = head.AddNodeToEnd(new_node)  # 添加节点到链表末尾
    head.PrintList()
    print("链表初始化完成，下面进行链表的操作：")
    step = 0
    print("是否在每次操作后输出链表？（y/n）")
    flag = input()
    while True:
        step = int(input("请输入要进行的操作：\n0.不进行操作\n1.删除节点\n2.更新节点\n3.查找节点\n4.插入节点\n-1.退出\n"))
        if step == -1:
            break
        elif step == 0:
            pass
        elif step == 1:
            print("请输入要删除的节点的值：")
            data_to_delete = input()
            node_to_delete = head.FindNode(data_to_delete)
            if node_to_delete is None:
                print("该节点不存在")
            else:
                head = head.DeleteNode(data_to_delete)  # 删除节点
        elif step == 2:
            print("请输入要更新的节点的值：")
            node_to_update = head.FindNode(input())
            if node_to_update is None:
                print("该节点不存在")
            else:
                print("请输入要更新的值：")
                new_data = input()
                head = head.UpdateNodeValue(node_to_update, new_data)  # 更新节点值
        elif step == 3:
            print("请输入要查找的节点的值：")
            node_to_find = head.FindNode(input())
            if node_to_find is None:
                print("该节点不存在")
            else:
                print("该节点存在")
        elif step == 4:
            print("请输入要插入的节点的值：")
            new_node = Node(input())
            head = head.AddNodeToEnd(new_node)  # 添加节点到链表末尾
        if flag == 'y':
            head.PrintList()
