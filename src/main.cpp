#include <iostream>
#include "tower.h"
#include "utils.h"

int main() {
    std::cout << "Tower of Hell Helper\n";
    std::cout << "Current stage: " << getCurrentStage() << "\n";
    std::cout << "Recommended jump: " << getRecommendedJump() << "\n";
    return 0;
}