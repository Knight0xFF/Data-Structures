//
// Created by 曾强 on 15/11/7.
//

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#ifndef DATA_STRUCT_LIST_H
#define DATA_STRUCT_LIST_H
#define MAXSIZE 20
#define OK 1
#define ERROR 0
#define FALSE 0
#define True 1
typedef int Status;
typedef int ElemType;
typedef struct
{
    ElemType data[MAXSIZE];
    int length;
} SqList;
#endif //DATA_STRUCT_LIST_H
