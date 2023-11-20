// 定义链表节点结构体
typedef struct node {
    int data; // 节点存储的数据
    struct node *next; // 指向下一个节点的指针
} node;

// 创建一个新的节点，返回其指针
node *create_node(int data) {
    node *new_node = (node *)malloc(sizeof(node)); // 分配内存空间
    new_node->data = data; // 设置节点数据
    new_node->next = NULL; // 设置节点指针为空
    return new_node; // 返回节点指针
}

// 在链表的头部添加一个新的节点，返回新的头节点指针
node *add_node(node *head, int data) {
    node *new_node = create_node(data); // 创建新节点
    new_node->next = head; // 新节点指向原来的头节点
    head = new_node; // 更新头节点为新节点
    return head; // 返回新的头节点指针
}

// 在链表中删除一个指定的节点，返回新的头节点指针
node *delete_node(node *head, int data) {
    node *cur = head; // 当前节点指针
    node *prev = NULL; // 前一个节点指针
    while (cur != NULL) { // 遍历链表
        if (cur->data == data) { // 找到要删除的节点
            if (prev == NULL) { // 要删除的节点是头节点
                head = cur->next; // 更新头节点为下一个节点
            } else { // 要删除的节点不是头节点
                prev->next = cur->next; // 前一个节点指向下一个节点
            }
            free(cur); // 释放要删除的节点的内存空间
            break; // 结束循环
        }
        prev = cur; // 更新前一个节点指针
        cur = cur->next; // 更新当前节点指针
    }
    return head; // 返回新的头节点指针
}

// 在链表中查找一个指定的节点，返回其指针，如果不存在则返回NULL
node *find_node(node *head, int data) {
    node *cur = head; // 当前节点指针
    while (cur != NULL) { // 遍历链表
        if (cur->data == data) { // 找到要查找的节点
            return cur; // 返回节点指针
        }
        cur = cur->next; // 更新当前节点指针
    }
    return NULL; // 没有找到节点，返回NULL
}
