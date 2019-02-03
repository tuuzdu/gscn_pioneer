cmake_minimum_required(VERSION 2.8.3)
project(gscn_pioneer_ap)

find_package(catkin REQUIRED 
    COMPONENTS
        mavros
)

catkin_package()

install(
    DIRECTORY
        launch/
    DESTINATION
        ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)
