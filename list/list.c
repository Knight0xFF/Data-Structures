//
// Created by 曾强 on 15/11/7->
//

#include "list.h"

Status InitList(SqList *L, int length)
{
    int i;
    L->length = 0;
    printf("%d\n", length);
    printf("%d\n", L->length);
    for (i = 0; i < length; i++)
    {
        printf("%d\n", L->length);
        L->data[i] = i * 2;
        L->length++;

    }
    printf("%d\n", L->length);
    for (i = 0; i < L->length; i++)
    {
        printf("%d", L->data[i]);
    }
    return OK;
}

Status ShowList(SqList L)
{
    int i;
    for (i = 0; i < L->length; i++)
    {
        printf("%d", L->data[i]);
    }
    return OK;
}


int main()
{
    SqList list;
    InitList(&list, 12);
    ShowList(list);
    return 0;
}