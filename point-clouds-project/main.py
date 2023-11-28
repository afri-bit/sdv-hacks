import sys
import time

import ecal.core.core as ecal_core
from ecal.core.subscriber import ProtoSubscriber
from ros.sensor_msgs.PointCloud2_pb2 import PointCloud2

import ros_numpy


# Callback for receiving messages
def callback(topic_name, msg, time):
    print("Received: {}".format(msg.data))
    pc = ros_numpy.numpify(msg)
    print(pc)


if __name__ == "__main__":
    # Initialize eCAL
    ecal_core.initialize(sys.argv, "Python Hello World Publisher")

    # Create a subscriber that listenes on the "hello_world_python_topic"
    sub = ProtoSubscriber("ROSVLS128CenterCenterRoof", PointCloud2)

    # Set the Callback
    sub.set_callback(callback)

    # Just don't exit
    while ecal_core.ok():
        time.sleep(0.5)

    # finalize eCAL API
    ecal_core.finalize()
