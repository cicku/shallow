#include <iostream>
//#include <cstring>

char* covStr_stack() {
    char str_stack[] = "This is a test of array allocated on stack.";
    return str_stack;
}

char* covStr_heap() {
    const char* str_heap = "This is a test of array allocated on heap.";
    return (char *)str_heap;
}

char* covStr_static_stack() {
    static char str_static_stack[] = "This is a test of staic array.";
    return str_static_stack;
}

// TODO: memset

int main(int argc, char* const argv[]) {
    std :: cout << "\033[1;31mWithout malloc, arrays within function will be stored on stack:\033[0m" << std :: endl;
    std :: cout << covStr_stack() << std :: endl;
    std :: cout << "\033[1;31mObviously you can't understand above, it's messy.\033[0m" << std :: endl;
    std :: cout << std :: endl;
    std :: cout << "\033[1;31mWhile arrays on heap are kept all the time:\033[0m" << std :: endl;
    std :: cout << covStr_heap() << std :: endl;
    std :: cout << std :: endl;
    std :: cout << "\033[1;31mUse static keyword to hold variable in .DATA segment:\033[0m" << std :: endl;
    std :: cout << covStr_static_stack() << std :: endl;
    //std :: cout << covStr_heap_again_from_stack() << std :: endl;
    return 0;
}
