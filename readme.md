

# Introduction
This project contains a set of ROS2 drivers, installation instructions and scripts to collect and extract data for [**3D-OLE**](https://www.hcu-hamburg.de/en/geomatik/harald-sternberg/3d-ole).

This project integrates and manages various sensors to facilitate efficient inspection processes. The primary sensors used are:

- **WitMotion HW T9053-485**
- **RPLIDAR S2**
- **RealSense D345i**

All sensors are connected to an **Intel NUC 13 Pro**.  

<div style="text-align: center;">
  <img title="5G AKI" src="/images/platform.jpg" width="400" height="300">
</div>


## Table of contents
- [Introduction](#introduction)
- [Installation](#installation)
  - [LiDAR (RPLIDAR S2)](#lidar)
    - [Troubleshooting LiDAR](#troubleshooting)
    - [Documentation](#documentation)
    - [Start LiDAR](#starting-the-lidar)
    - [Returned values](#returned-values-by-the-lidar)
  - [IMU (WitMotion HW T9053-485)](#imu)
    - [Documentation](#documentation-imu)
    - [Troubleshooting](#troubleshooting-imu)
    - [Startingthe IMU](#starting-the-imu)
    - [Returned Values](#retuned-values-imu)
  - [Camera (RealSense D435i)](#camera)
    - [Documentation](#documentation-camera)
  - [Laser Scanner](#scancontrol-micro-epsilon)
    - [Documentation](#documentation-scanner)
    - [Starting](#starting-scancontrol)
    - [Returned Values](#retuned-values-profiles)
  - [External Monitor (Asus Zenscreen)](#external-monitor)
- [Quickstart](#quickstart)
  - [Bash scripts](#bash-scripts)
- [Data extraction](#data-extraction)
  - [Setup](#setup-data-extraction)
  - [Python scripts for extraction](#python-script-for-extraction)
  - [Content](#data-content)
  - [Deserialization](#data-deserialization)
- [Next steps](#next-steps)


## Installation
The setup is required to use `WitMotion HW T9053-485`, `RPLIDAR S2`  and `RealSense D345i` with ROS2 and Python on `Ubuntu 22.04` and [ROS2 Humble](https://docs.ros.org/en/humble/index.html).


Note: The workspace is named `ros2_ws`, the LiDAR package `rp_test`, the camera package `my_realsense` and the IMU package `witmotion_imu`.

### LiDAR 
1. Open the terminal and create a package:
```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python rp_test
```

2. Update the setup and config files to include the necessary Python libraries:
  - [package.xml](https://github.com/FjoGeo/ROS_Tutotrial/blob/master/rplidar/rp_test/package.xml)
  - [setup.py](https://github.com/FjoGeo/ROS_Tutotrial/blob/master/rplidar/rp_test/setup.py)
  - [setup.cfg](https://github.com/FjoGeo/ROS_Tutotrial/blob/master/rplidar/rp_test/setup.cfg)

3. Install missing libraries:
```bash
pip install rplidar
pip install pyserial
```

4. Create a publisher and subscriber in `rp_test/rp_test/`
5. Build the Node `colcon build --packages-select rp_test`


#### Troubleshooting
- device not detected: `sudo apt remove brltty` , then unplug and replug it
- grant permission: `sudo chmod 777 /dev/ttyUSB*`
- check the permission: `ls -l /dev/ttyUSB*`


#### Documentation

[ROS2](https://github.com/Slamtec/rplidar_ros/blob/ros2/launch/rplidar_s2_launch.py)

[Python](https://github.com/SkoltechRobotics/rplidar)

[Documentation](http://bucket.download.slamtec.com/ccb3c2fc1e66bb00bd4370e208b670217c8b55fa/LR001_SLAMTEC_rplidar_protocol_v2.1_en.pdf)


#### Starting the LiDAR
This code is for starting a single LiDAR node. Check if the port is correct and open before using it.

```
cd ~/ros2_ws
source install/setup.bash
ros2 run rp_test talker_single
```


####  Returned values by the LiDAR:
* Measured values
    * quality - Quality of the current measurement sample 
    * angle_q6 - The measurement heading angle related to RPLIDAR’s heading. In degree unit, (0°-360°) Stored using fix point numb 
    * distance_q2 - Measured object distance related to RPLIDAR’s rotation center. In millimeter (mm) unit. Represents using fix point. Set to 0 when the measurement is invalid 


### IMU

1. Open the terminal and create a package:
```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python witmotion_imu
```


2. Update the setup and config files to include the necessary Python libraries:
  - [package.xml](https://github.com/FjoGeo/ROS_Tutotrial/blob/master/WitMotion/package.xml)
  - [setup.py](https://github.com/FjoGeo/ROS_Tutotrial/blob/master/WitMotion/setup.py)
  - [setup.cfg](https://github.com/FjoGeo/ROS_Tutotrial/blob/master/WitMotion/setup.cfg)

3. Install missing libraries:
```bash
pip install pyserial
```

4. Create a publisher and subscriber in `~/ros2_ws/src/witmotion_imu/witmotion_imu/`
5. Build the Node `colcon build --packages-select witmotion_imu`


#### Troubleshooting IMU
- device not detected: `sudo apt remove brltty` , then unplug and replug it
- grant permission: `sudo chmod 777 /dev/ttyUSB*`
- check the permission: `ls -l /dev/ttyUSB*`


#### Documentation IMU
[Official github repo](https://github.com/WITMOTION/WitHighModbus_HWT9073485)


#### Starting the IMU
First check ports, then run node.
```
cd ~/ros2_ws
source install/setup.bash
ros2 run witmotion_imu talker
```


#### Retuned Values IMU
- `Acc`: Acceleration - These values measure the acceleration forces in different directions
- `As`: Gyroscope - These values measure the rate of rotation around each axis
- `H`: Magnetometer - These values measure the magnetic field strength in different directions
- `Ang`: Euler Angles - These values describe the orientation of the sensor in space


### Camera

1. Open the terminal and create a package:
```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python my_realsense
```

2. Update the setup and config files to include the necessary Python libraries:
 - [package.xml](https://github.com/FjoGeo/ROS_Tutotrial/blob/master/realsense/my_realsense/package.xml)
  - [setup.cfg](https://github.com/FjoGeo/ROS_Tutotrial/blob/master/realsense/my_realsense/setup.cfg)
  - [setup.py](https://github.com/FjoGeo/ROS_Tutotrial/blob/master/realsense/my_realsense/setup.py)

3. Install missing libraries:
```bash
pip install pyrealsense2
pip install opencv-python
```

4. Install librealsense2:  https://github.com/IntelRealSense/librealsense/blob/master/doc/installation.md#prerequisites


 Clone the librealsense2 repo
```bash
git clone https://github.com/IntelRealSense/librealsense.git
```
Run Intel Realsense permissions script from librealsense2 root directory:

```bash
cd librealsense
./scripts/setup_udev_rules.sh
```

4. Create a publisher and subscriber in `~/ros2_ws/src/my_realsense/my_realsense`
5. Build the Node `colcon build --packages-select my_realsense`


#### Documentation Camera
[doc](https://github.com/IntelRealSense/librealsense/blob/master/doc/distribution_linux.md#installing-the-packages)

[Github](https://github.com/IntelRealSense/realsense-ros?tab=readme-ov-file)

### scanControl (micro-epsilon)
1. Open the terminal and create a package:
```bash
cd ~/ros2_ws/src
ros2 pkg create --build-type ament_python laser_scanner
```
2. Update the setup and config files to include the necessary Python libraries:
  - [package.xml](https://github.com/FjoGeo/ROS2_Pipeline_And_Crane_Inspection/blob/master/scanner_stuff/ROS/package.xml)
  - [setup.py](https://github.com/FjoGeo/ROS2_Pipeline_And_Crane_Inspection/blob/master/scanner_stuff/ROS/setup.py)
  - [setup.cfg](https://github.com/FjoGeo/ROS2_Pipeline_And_Crane_Inspection/blob/master/scanner_stuff/ROS/setup.cfg)

3. Build the linllt libraries

For pain-free usage, the libraries can be built with the [Meson](http://mesonbuild.com) build system. Meson checks for the required dependencies, like aravis, and does all necessary steps to prepare compiling and installing the code on the currently used platform. For compiling and installing [Ninja](https://ninja-build.org) is used.

If Meson is not installed on the host PC, it can be retrieved via the distribuitions package manager, e.g.

```bash
sudo apt install meson
```

or from [source](https://github.com/mesonbuild/meson/releases). Meson dependencies are [Python](http://python.org) (>=3.4) and [Ninja](https://ninja-build.org) (>=1.5).

Before continuing please have a look at the dependencies to guarantee successful compilation.

For each library in the root folder (libmescan/ & libllt/), the following commands have to be executed to fully compile and install linllt. libmescan has to be compiled and installed first.

```bash
meson builddir
cd builddir
ninja
sudo ninja install
```

It might be necessary to call `sudo ldconfig` afterwards, to reload the linker cache.

To use the libraries with Python (>=3.4), the module pylinllt (located in the python_bindings folder) has to be copied to the site-packages of the desired python installation. The module assumes the library in /usr/local/lib.

Aravis has to be compiled from source via the GNU build system:

- [Aravis](https://github.com/AravisProject/aravis/releases) (version 0.8 or newer)

To compile the basic GNU build toolchain and the autotools are necessary. Further aravis dependencies are:

- [libxml2](https://github.com/GNOME/libxml2/releases)
- [glib2](https://github.com/GNOME/glib/releases)

These and the toolchain packages are usually available via the package manager, e.g.

```bash
sudo apt install build-essential autotools-dev automake intltool libtool gtk-doc-tools libxml2-dev libglib2.0-dev
```

Make sure to update and upgrade your repos beforehand. Further information can be found on the [aravis Github page](https://github.com/AravisProject/aravis).


4. Copy the libraries into the ROS directory
- copy the pylinllt librarie to `~/ros2_ws/install/laser_scanner/lib/laser_scanner/`

4. Create a publisher  in `~/ros2_ws/src/laser_scanner/laser_scanner/`
5. Build the Node `colcon build --packages-select laser_scanner`


#### Documentation (scanner)
Documentation can be found [here](https://github.com/FjoGeo/ROS2_Pipeline_And_Crane_Inspection/tree/master/scanner_stuff/scanCONTROL-Linux-SDK-1-0-1/documentation)


#### Starting scanControl
1.  Set IPv4 address of the device to 192.168.100.2
2. Netmask to 255.255.255.0

2. 
```
	sudo ip addr flush dev enp86s0
	sudo ip addr add 192.168.100.1/24 dev enp86s0
```
3. run setup script 
```
    python3 gige_ip_control_mod.py 192.168.100.2 192.168.100.1 -s 255.255.255.0 -g 0.0.0.0 -d enp86s0
```
4. Now you can run ROS nodes or just python scripts
```
cd ~/ros2_ws
source install/setup.bash
ros2 run laser_scanner talker
```

#### Retuned Values (Profiles)
- `Distance`: To get the  distance  (i.e. z value) of a measuring point,  the center of gravity of the 
reflection  detected  by  the  CMOS  sensor  column  is  calculated.  Based  on  a  calibration  table 
this value is converted to a real distance coordinate in the sensor. The value is transmitted as 
16 bit unsigned integer field which has to be scaled by the sensor specific scaling factors.  
 
- `Position`:  The  position  (x  value)  corresponds  to  a  pixel  row  of  the  CMOS  sensor.  For  every 
column  one  position  value  is  detected.  Calibration  to  the  real  position  is  achieved  by  the 
calibration table saved on the sensor. A 16 bit unsigned integer field is transmitted which has 
to be scaled, too. 
 
- `Intensity`:  The  transmitted value  is  the  difference  between  the  detected  intensity  maximum 
and  the  currently  used  threshold.  Intensity  correlates  to  how  much  light  one  pixel  of  the 
matrix has detected while the shutter was open. Prerequisite for detection of a reflection is 
that the intensity is above the threshold. A 10 bit unsigned integer field is transmitted.


### External Monitor
Steps to install the Asus Zenscreen:

Disable Secure Boot in the BIOS, then reboot, and run the following:
```
# Make this directory if it doesn't exist, and cd into it
mkdir -p ~/Downloads/Install_Files/DisplayLink
cd ~/Downloads/Install_Files/DisplayLink

# Download the Ubuntu APT package provided by Synaptics.com, the official 
# makers of DisplayLink
wget https://www.synaptics.com/sites/default/files/Ubuntu/pool/stable/main/all/synaptics-repository-keyring.deb

# Install the DisplayLink APT package keyring
sudo apt install ./synaptics-repository-keyring.deb

# Update your APT package cache
sudo apt update

# Install the DisplayLink driver provided by Synaptics.com, the official source
sudo apt install displaylink-driver

# Reboot. 
# Now it is plug-and-play. Plug in your DisplayLink adapter and it just works.
# It may take up to 5~10 seconds to recognize a monitor. 
```


## QuickStart

Check the ports and the sequence you connect the device to the PC.

- open ports
  - ```sudo chmod 777 /dev/ttyUSB*```
- navigate into ROS2 directory
  - ```cd ~/ros2_ws/```
- source
  - ``` source install/setup.bash ```
- use a launch file
  - ``` cd launch/ ```
  - ``` ros2 launch <launch_file.py> ```
-  launching sensors separately
  - ```cd ~/ros2_ws/```
  - ```ros2 run rp_test talker_single```
  - ```ros2 run my_realsense talker_rgb```
  - ```ros2 run witmotion_imu talker```

  
Using a launch file will record the data in a bag file.


### Bash scripts
To automate the commands above, it is possible to use one of the scripts in the `Bash` directory. 


## Data extraction

### Setup data extraction

To read a recorded bag  with Python you need multiple libraries:

                sudo apt-get install python-is-python3
                pip install pandas
                pip install catkin_pkg

- rclpy: https://index.ros.org/r/rclpy/
  
                sudo apt install python3-sphinx python3-pip
                sudo -H pip3 install sphinx_autodoc_typehints
Source your ROS 2 installation, then:

                mkdir -p rclpy_ws/src
                cd rclpy_ws/src
                git clone https://github.com/ros2/rclpy.git
                cd ..
                colcon build --symlink-install
                
Source workspace and build docs:

                source install/setup.bash
                cd src/rclpy/rclpy/docs
                make html


### Python script for extraction
To extract all RGB images, pointclouds and IMU/Gyroscope data from a recorded bag-file, use the `extract_all.py` file.
Other extraction files are located under the directory `read and display data`.


### Data content

The recorded file consists of 4 tables:

        
            "SELECT name FROM sqlite_master WHERE type='table';"
        

- schema
    - version of ROS and schema
- metadata
    - empty
- topics
    - list of all recorded topics, type, serialization format and info
- messages
    - contains the serialized data, the topic and the time frame

### Data deserialization

To deserialize the data you need to start rclpy and create a connection to the database.


## Next steps
- Simple installation
- Visual Odometry
- camera calibration
- sensor synchronization

