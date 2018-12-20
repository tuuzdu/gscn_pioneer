cmake_minimum_required(VERSION 2.8.3)
project(gscn_pioneer_mission)

find_package(catkin REQUIRED 
    COMPONENTS
        mavros
        rospy
)

catkin_python_setup()

catkin_package()

catkin_install_python(
    PROGRAMS
        scripts/mission_node
    DESTINATION
        ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(
    FILES
        launch/mission.launch
        launch/gscn_mavros.launch
    DESTINATION
        ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)
