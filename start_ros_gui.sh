
#docker run -it --rm \
#  --name ros2_gui \
#  -e DISPLAY=host.docker.internal:0 \
#  -v $PWD/ros2_ws:/ros2_ws \
#  osrf/ros:humble-desktop \
#  bash

docker run -d \
  --name ros2_gui \
  -e DISPLAY=host.docker.internal:0 \
  -v $PWD/ros2_ws:/ros2_ws \
  osrf/ros:humble-desktop tail -f /dev/null

