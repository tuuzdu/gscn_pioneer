# -*- coding: utf-8 -*-

import rospy
from mavros_msgs.msg import Waypoint, WaypointList
from mavros_msgs.srv import WaypointClear, WaypointPush, WaypointSetCurrent, CommandBool

class Mission:

    MAV_GLOBAL_FRAME = 3
    MAV_CMD_WAYPOINT = 16
    MAV_CMD_RTL = 20
    MAV_CMD_LAND = 21
    MAV_CMD_TAKEOFF = 22

    def __init__(self):
        rospy.init_node('mission_node')
        rospy.loginfo('Waiting mavros for services...')

    def push_mission(self, waypoints):
        rospy.wait_for_service('mavros/mission/clear')
        try:
            service = rospy.ServiceProxy('mavros/mission/clear', WaypointClear)
            service()
        except rospy.ServiceException as e:
            rospy.loginfo('Service call failed: {0}'.format(e))
        rospy.wait_for_service('mavros/mission/push')
        try:
            service = rospy.ServiceProxy('mavros/mission/push', WaypointPush)
            service(0, waypoints)
        except rospy.ServiceException as e:
            rospy.loginfo('Service call failed: {0}'.format(e))

    def set_current(self, wp_seq):
        rospy.wait_for_service('mavros/mission/set_current')
        try:
            service = rospy.ServiceProxy('mavros/mission/set_current', WaypointSetCurrent)
            service()
        except rospy.ServiceException as e:
            rospy.loginfo('Service call failed: {0}'.format(e))


    def arming(self):
         rospy.wait_for_service('mavros/cmd/arming')
         try:
             service = rospy.ServiceProxy('mavros/cmd/arming', CommandBool)
             service(True)
         except rospy.ServiceException as e:
             rospy.loginfo('Service call failed: {0}'.format(e))

    def mission_create (self):
        param = rospy.get_param('~waypoints')
        rospy.loginfo('Waypoints from parameter server: %s', param)
        # rospy.logdebug(param)

        wl = WaypointList()
        wp = Waypoint()
        wp.frame = self.MAV_GLOBAL_FRAME
        wp.command = self.MAV_CMD_TAKEOFF  # takeoff
        wp.is_current = True
        wp.autocontinue = True
        wp.param1 = param[0]['alt']  # takeoff altitude
        wp.param2 = 0
        wp.param3 = 0
        wp.param4 = 0
        wp.x_lat = 0
        wp.y_long = 0
        wp.z_alt = param[0]['alt']
        wl.waypoints.append(wp)

        for index in range(len(param)):
            wp = Waypoint()
            wp.frame = self.MAV_GLOBAL_FRAME
            wp.command = self.MAV_CMD_WAYPOINT  # simple point
            wp.is_current = False
            wp.autocontinue = True
            wp.param1 = 0  # takeoff altitude
            wp.param2 = 0
            wp.param3 = 0
            wp.param4 = 0

            wp.x_lat = param[index]['lat']
            wp.y_long = param[index]['lon']
            wp.z_alt = param[index]['alt']
            wl.waypoints.append(wp)

        wp = Waypoint()
        wp.frame = 2 
        wp.command = MAV_CMD_RTL
        wp.is_current = False
        wp.autocontinue = True
        wl.waypoints.append(wp)
        
        rospy.loginfo('Waypoints %s', wl)
        self.push_mission(wl.waypoints)
        self.arming()
        rospy.sleep(2)
        self.set_current(0)

        # def gps_cb(data): 
        #     lat = data.latitude
        #     lon = data.longitude
        # rospy.Subscriber("mavros/global_position/global", NavSatFix, gps_cb)

        rospy.spin()

    def start(self):
        self.mission_create()
