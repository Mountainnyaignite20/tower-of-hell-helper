#include "../src/tower.h"
#include "../src/utils.h"
#include <cassert>

void test_getCurrentStage() {
    assert(getCurrentStage() > 0);
}

void test_calculateOptimalJump() {
    assert(calculateOptimalJump(2) == "Short hop");
    assert(calculateOptimalJump(5) == "Medium jump");
    assert(calculateOptimalJump(8) == "Long jump");
}

int main() {
    test_getCurrentStage();
    test_calculateOptimalJump();
    return 0;
}