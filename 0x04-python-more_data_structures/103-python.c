#include <Python.h>

/**
 * print_python_bytes - prints information about Python bytes objects
 * @p: pointer to a PyObject (Python bytes object)
 */
void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes;

    printf("[.] bytes object info\n");
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes = (PyBytesObject *)p;

    printf("  size: %ld\n", PyBytes_Size(p));
    printf("  trying string: %s\n", PyBytes_AsString(p));

    printf("  first 10 bytes: ");
    for (int i = 0; i < 10 && i < PyBytes_Size(p); i++) {
        printf("%02x ", (unsigned char)bytes->ob_sval[i]);
    }
    printf("\n");
}

/**
 * print_python_list - prints information about Python lists
 * @p: pointer to a PyObject (Python list)
 */
void print_python_list(PyObject *p) {
    PyListObject *list;
    Py_ssize_t size, i;
    PyObject *elem;

    printf("[*] Python list info\n");
    size = PyList_Size(p);
    list = (PyListObject *)p;

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list->allocated);

    for (i = 0; i < size; i++) {
        elem = PyList_GetItem(p, i);

        printf("Element %ld: %s\n", i, Py_TYPE(elem)->tp_name);

        if (PyBytes_Check(elem)) {
            print_python_bytes(elem);
        }
    }
}


