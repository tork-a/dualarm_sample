#!/usr/bin/env python

from geometry_msgs.msg import Pose, PoseStamped
from moveit_commander import MoveGroupCommander, conversions
import rospy


class GenericDualArmClient():
    _safe_kinematicsolver = "RRTConnectkConfigDefault"

    def __init__(self, *args, **kwargs):
        larm_name = args[0]
        rarm_name = args[1]  # "arm_right" for Motoman SDA10F
        self.r_arm = MoveGroupCommander(rarm_name)
        self.r_arm.set_planner_id(self._safe_kinematicsolver)

    def move_rarm_shift_forward(self, axis, value):
        '''
        Ref. http://docs.ros.org/indigo/api/moveit_commander/html/classmoveit__commander_1_1move__group_1_1MoveGroupCommander.html#a22f9ec1477c3d61e728660850d50ce1f
        '''
        self.r_arm.shift_pose_target(axis, value)
        self.r_arm.plan()
        self.r_arm.go()

    def move_rarm_fixedpose_forward(self):
        tpose = Pose()
        #TODO Currently the following position may work with SDA10F but not with NXO
        tpose.position.x = 0.599
        tpose.position.y = -0.379
        tpose.position.z = 1.11
        self.r_arm.set_pose_target(tpose)
        self.r_arm.plan()
        self.r_arm.go()
