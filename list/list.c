//
// Created by 曾强 on 15/11/7->
//

#include "list.h"

Status InitList(SqList *L, int length)
{
    int i;
    L->length = 0;
    for (i = 0; i < length; i++)
    {
        L->data[i] = (i+1) * 2;
        L->length++;

    }
    return OK;
}

Status ShowList(SqList L)
{
    int i;
    for (i = 0; i < L.length; i++)
    {
        printf("%d ", L.data[i]);
    }
    printf("\n");
    return OK;
}

Status InsertList(SqList *L, int index, ElemType e)
{
    int k;
    if (L->length == MAXSIZE || index < 1 || index > L->length)
        return ERROR;
    if (index <= L->length)
    {
        for (k = L->length - 1; k >= index - 1; k--)
        {
            L->data[k+1] = L->data[k];
        }
    }
    L->data[index-1] = e;
    L->length++;
    return OK;
}

Status DeleteList(SqList *L, int index, ElemType *e)
{
    int k;
    if (L->length == 0 || index < 1 || index > L->length)
        return ERROR;
    *e = L->data[index-1];
    if (index < L->length)
    {
        for (k = index; k < L->length; k++)
            L->data[k-1] = L->data[k];
    }
    L->length--;
    return OK;
}

Status GetItem(SqList L, int index, ElemType *e)
{
    if (index > L.length-1 || index < 1)
        return ERROR;
    *e = L.data[index-1];
    return OK;
}


int main()
{
    SqList list;
    InitList(&list, 12);
    ShowList(list);
    InsertList(&list, 5, 3);
    ShowList(list);
    ElemType item = 0;
    ElemType *p;
    DeleteList(&list, 5, &item);
    printf("Delete item is %d\n", item);
    ShowList(list);
    GetItem(list, 10, p);
    printf("Get item is %d\n", *p);
    return 0;
}