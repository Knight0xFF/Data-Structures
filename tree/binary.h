//
// Created by 曾强 on 15/11/7.
//

#ifndef DATA_STRUCT_BINARY_H
#define DATA_STRUCT_BINARY_H
typedef struct BiTNode
{
    char data;
    struct BiTNode *lchild, *rchild;
} BiTNode, *BiTree;
#endif //DATA_STRUCT_BINARY_H
void CreateBiTree(BiTree *T);