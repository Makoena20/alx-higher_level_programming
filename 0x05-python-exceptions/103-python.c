#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
    Py_ssize_t size, i;
    PyObject *element;

    if (!PyList_Check(p)) {
        fprintf(stderr, "[*] Python list info\n  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Python list info\n[*] Size of the Python List = %ld\n[*] Allocated = %ld\n", size, ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        element = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);

        if (PyBytes_Check(element))
            print_python_bytes(element);
        else if (PyFloat_Check(element))
            print_python_float(element);
    }
}

void print_python_bytes(PyObject *p) {
    Py_ssize_t size, i;
    char *

