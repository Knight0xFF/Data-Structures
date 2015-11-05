//
// Created by 曾强 on 15/11/5.
//

#include <stdio.h>
#include <stdlib.h>

typedef struct BiTNode
{
    char data;
    struct BiTNode *lchild, *rchild;
} BiTNode, *BiTree;

void CreateBiTree(BiTree *T)
{
    char ch;
    scanf("%c", &ch);
    if (ch == '#')
    {
        *T = NULL;
    }
    else
    {
        *T = (BiTree)malloc(sizeof(BiTNode));
        if (!*T)
        {
            perror("Create Node fail");
            exit(1);
        }
        (*T)->data = ch;
        CreateBiTree(&(*T)->lchild);
        CreateBiTree(&(*T)->rchild);
    }
}

void PreOrder(BiTree T)
{
    if (T == NULL)
    {
        return;
    }
    printf("%c", T->data);
    PreOrder(T->lchild);
    PreOrder(T->rchild);
}

void InOrder(BiTree T)
{
    if (T == NULL)
    {
        return;
    }
    InOrder(T->lchild);
    printf("%c", T->data);
    InOrder(T->rchild);
}

void PostOrder(BiTree T)
{
    if (T == NULL)
    {
        return;
    }
    PostOrder(T->lchild);
    PostOrder(T->rchild);
    printf("%c", T->data);
}

int GetLeafNum(BiTree T)
{
    static int leftNum=0;
    if (T)
    {
        if (T->lchild == NULL && T->rchild == NULL)
        {
            leftNum++;
        }
        GetLeafNum(T->lchild);
        GetLeafNum(T->rchild);
    }
    return leftNum;
}

int GetDepth(BiTree T)
{
    if (T == NULL)
    {
        return 0;
    }
    int leftDepth = GetDepth(T->lchild);
    int rightDepth = GetDepth(T->rchild);
    return leftDepth > rightDepth ? (leftDepth + 1) : (rightDepth + 1);
}

int main()
{
    BiTree *Tree;
    CreateBiTree(Tree);
    PreOrder(*Tree);
    printf("\n");
    InOrder(*Tree);
    printf("\n");
    PostOrder(*Tree);
    printf("\n");
    printf("the left number is: %d\n", GetLeafNum(*Tree));
    printf("the depth is: %d\n", GetDepth(*Tree));

    return 0;
}