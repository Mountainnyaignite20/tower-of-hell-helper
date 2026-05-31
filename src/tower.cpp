#include "tower.h"
#include "utils.h"

int getCurrentStage() {
    return 5; // Mock value
}

std::string getRecommendedJump() {
    return calculateOptimalJump(getCurrentStage());
}