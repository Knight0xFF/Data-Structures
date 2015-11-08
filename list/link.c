//
// Created by 曾强 on 15/11/8.
//

#include "list.h"

void InitLinkHead(LinkList *L, int length)
{
    LinkList p;
    int i;
    srand(time(0));
    *L = (LinkList)malloc(sizeof(Node));
    (*L)->next = NULL;

    for (i = 0; i < length; i++)
    {
        p = (LinkList)malloc(sizeof(Node));
        p->data = (i + 1) * 2;
        p->next = (*L)->next;
        (*L)->next = p;
    }
}

void InitLinkTail(LinkList *L, int length)
{
    LinkList p, tail;
    int i;
    srand(time(0));
    *L = (LinkList)malloc(sizeof(Node));

    for (i = 0; i < length; i++)
    {
        p = (LinkList)malloc(sizeof(Node));
        p->data = (i + 1) * 2;
        (*L)->next = p;
        (*L) = p;
    }
    (*L) = NULL;
}

void ShowLink(LinkList L)
{
    LinkList p = L;
    while (p->next)
    {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}

Status InsertLink(LinkList *L, int index, ElemType e)
{
    int k = 1;
    LinkList p;
    NodePtr newNode;
    p = *L;
    while (p && k < index)
    {
        p = p->next;
        k++;
    }
    if (!p || k > index)
        return ERROR;
    newNode = (NodePtr)malloc(sizeof(NodePtr));
    newNode->data = e;
    newNode->next = p->next;
    p->next = newNode;

    return OK;
}

Status DeleteLink(LinkList *L, int index, ElemType *e)
{
    int k = 1;
    LinkList p = *L;
    NodePtr tempNode;
    while (p && k < index)
    {
        p = p->next;
        k++;
    }
    if (!p || k > index)
        return ERROR;
    tempNode = p->next;
    p->next = tempNode->next;
    *e = tempNode->data;
    free(tempNode);

    return OK;
}

Status ClearLink(LinkList *L)
{
    LinkList p = (*L)->next;
    NodePtr tempNode;
    while (p)
    {
        tempNode = p;
        p = p->next;
        free(tempNode);
    }
    (*L)->next = NULL;

    return OK;
}

int main()
{
    LinkList *linkHead;
    InitLinkHead(linkHead, 10);
    ShowLink(*linkHead);
    InsertLink(linkHead, 4, 100);
    ShowLink(*linkHead);
    ElemType deleteNode;
    DeleteLink(linkHead, 8, &deleteNode);
    printf("Delete Node is: %d\n", deleteNode);
    ShowLink(*linkHead);
    ClearLink(linkHead);
    ShowLink(*linkHead);

    return 0;
}