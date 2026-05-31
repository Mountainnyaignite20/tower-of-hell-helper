#include "utils.h"

std::string calculateOptimalJump(int stage) {
    if (stage < 3) return "Short hop";
    if (stage < 7) return "Medium jump";
    return "Long jump";
}