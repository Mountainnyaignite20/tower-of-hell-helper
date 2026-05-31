cmake_minimum_required(VERSION 3.10)
project(tower-of-hell-helper)

set(CMAKE_CXX_STANDARD 17)

add_executable(toh-helper
    src/main.cpp
    src/tower.cpp
    src/utils.cpp
)

target_include_directories(toh-helper PRIVATE src)
target_link_libraries(toh-helper PRIVATE curl)