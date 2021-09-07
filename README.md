<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="Circuit/autoCentrifuge.png" alt="Project logo"></a>
</p>

<h3 align="center">Automatic Centrifuge</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()


</div>

---


<p align="center"> Automatic Centrifuge
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [RPiClient Installation](#Installation)
- [Circuit](#circuit)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)


## 🧐 About <a name = "about"></a>

This repo contains

- Backend
- RPiClient Software
- Client auto-Installer script
- Detailed instructions

for IoTManagement System.



## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on you raspberry pi.

### Prerequisites

Turn on your Raspberry Pi and execute the following commands

```
- sudo apt update
- sudo apt upgrade
```

## RPiClient Installation <a name = "Installation"></a>


### Auto Installer
To install and Run RPi Client Automatically just run the following command on your Raspberry Pi terminal

- ```curl -sSL  https://raw.githubusercontent.com/Nauman3S/IOTManagementSystem/main/installer.sh  | bash```

After the installer completes the process, note down the MAC Address on the terminal with success message.





## Circuit <a name = "circuit"></a>


### Motor Driver Details

```http
Motor Driver Header Pins(already connected to the Raspberry Pi)
```

| MotorDriverPin | RPi Pin | Description | 
| :--- | :--- | :--- |
| `PWM1` | `GPIO12` | *Already connected via header*  |
| `DIR1` | `GPIO26` | *Already connected via header*  |
| `PWM2` | `GPIO13` | *Already connected via header*  |
| `DIR2` | `GPIO24` | *Already connected via header*  |


```http
Motor Driver Pins for connecting motors
```

| MotorDriverPin | RPi Pin | Description | 
| :--- | :--- | :--- |
| `M1A` | `GPIO12` | *Connect to motor1 terminal A*  |
| `M1B` | `GPIO26` | *Connect to motor1 terminal B*  |
| `VM` | `GPIO13` | *Positive Supply (6V to 24V)*  |
| `GND` | `GPIO24` | *Negative Supply*  |
| `M2A` | `GPIO24` | *Connect to motor2 terminal A*  |
| `M2B` | `GPIO24` | *Connect to motor2 terminal B*  |




### Raspberry Pi Pinout


### Complete Circuit Diagram

Complete Circuit Diagram of Sensor Node
![RPiPinout](Circuit/pinout.png)

## Usage <a name = "usage"></a>

1.  Run installer script on your Raspberry Pi.
2.  Note down the MAC Address given by the installer script at the end.
3.  Add the device with the MAC Address collected in the previous step to the database using addDevice API endpoint mentioned above
4.  Interact with the device with using MAC Address, or interact with all the devices in the system by using `all` in devices parameter of the API.

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - For programming RPi Client
  
<!-- ## Demo Videos <a name = "demo"></a>

- Complete Demo Part 1: https://youtu.be/d15zIwMxJ3w
- - This is a part 1 of complete demo of IoT Management System, showing how to install the Client on Raspberry Pi and run it.
- Complete Demo Part 2: https://youtu.be/kUgdPix0l-g
- - Part 2 of complete demo showing how to interact with all the devices or specific devices in the system using API. -->

## ✍️ Authors <a name = "authors"></a>

- [@Nauman3S](https://github.com/Nauman3S) - Development and Deployment
