#include <stdlib.h>
#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: the PyObject list
 */
void print_python_list_info(PyObject *p)
{
    int size, mem_alloc;
    int a;
    PyObject *ptr;

    size = PyList_Size(p);
    mem_alloc = ((PyListObject *)p)->allocated;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", mem_alloc);

    if (size > 0) {
        for (a = 0; a < size; a++)
        {
            ptr = PyList_GetItem(p, a);
            if (ptr == NULL) {
                printf("Element %d: NULL\n", a);
            } else {
                printf("Element %d: %s\n", a, Py_TYPE(ptr)->tp_name);
            }
        }
    }
}

