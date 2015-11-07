//
// Created by 曾强 on 15/11/7.
//

#include <stdlib.h>
#include <stdio.h>
#include "binary.h"
typedef enum
{
    Link,
    Thread
} PointerTag;

typedef struct BiThrNode
{
    char ch;
    struct BiThrNode *lchild, *rchild;
    PointerTag LTag;
    PointerTag RTag;
} BiThrNode, *BiThrTree;

BiThrTree pre;

void InThreading(BiThrTree T)
{
    if (T)
    {
        InThreading(T->lchild);
        if (!T->lchild)
        {
            T->LTag = Thread;
            T->lchild = pre;
        }
        if (!pre->rchild)
        {
            pre->RTag = Thread;
            pre->rchild = p;
        }
        pre = p;
        InThreading(T->rchild);
    }
}

void InOrderThr(BiThrTree T)
{
    BiThrTree p;
    p = T->lchild;
    while (p != T)
    {
        while (p->LTag == Link)
            p = p->lchild;
        printf("%c", p->ch);
        while (p->RTag == Thread && p->rchild != T)
        {
            p = p->rchild;
            printf("%c", p->ch);
        }
        p = p->rchild;
    }
}

int main()
{


}
