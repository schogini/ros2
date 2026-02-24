

echo source /opt/ros/humble/setup.bash
echo source /ros2_ws/install/setup.bash
echo rqt_graph
echo rqt --standalone rqt_topic

cat <<EOT
cd /ros2_ws
mkdir -p src
cd src

ros2 pkg create --build-type ament_python temp_sensor_pkg

ros2_ws/
 └── src/
      └── temp_sensor_pkg/

nano /ros2_ws/src/temp_sensor_pkg/temp_sensor_pkg/temperature_node.py

nano /ros2_ws/src/temp_sensor_pkg/setup.py
entry_points={
    'console_scripts': [
        'temperature_node = temp_sensor_pkg.temperature_node:main',
    ],
},


cd /ros2_ws
rm -rf build install log
colcon build
source install/setup.bash


ros2 run temp_sensor_pkg temperature_node


EOT

docker exec -it ros2_gui bash
