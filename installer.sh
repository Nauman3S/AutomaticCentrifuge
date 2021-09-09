#-e option instructs bash to immediately exit if any command [1] has a non-zero exit status
# We do not want users to end up with a partially working install, so we exit the script
# instead of continuing the installation with something broken
set -e

echo "AutomaticCentrifuge Client Installer"

######## VARIABLES #########

# Location for final installation log storage
#installLogLoc=/etc/pihole/install.log


echo "Welcome user"
echo $USER

show_ascii_berry() {
    echo -e "

_________________________   _______    _______         _______
Automatic Centrifuge Installer

    "
}
show_ascii_berry


if [ -d "$HOME/AutomaticCentrifuge" ]
then
    echo "Directory AutomaticCentrifuge exists."
else
    echo "Error: Directory AutomaticCentrifuge does not exists."
    cd $HOME
    git clone \
    https://github.com/Nauman3S/AutomaticCentrifuge;
    cd AutomaticCentrifuge/Firmware
    
fi
if [ -d "$HOME/AutomaticCentrifuge/Firmware/logs" ]
then
    echo "Directory AutomaticCentrifuge/Firmware/logs exists."
else
    echo "Error: Directory AutomaticCentrifuge does not exists."
    mkdir ~/AutomaticCentrifuge/Firmware/logs
fi

File="/etc/rc.local"

if [[ $(grep "(sleep 10; sh /home/pi/AutomaticCentrifuge/Firmware/starter.sh)&" $File) ]] ; then
    echo "Found startup script. Doing nothing."
else
    echo "Not Found. Adding startup script"
    sudo sed -i -e '$i \(sleep 10; sh /home/pi/AutomaticCentrifuge/Firmware/starter.sh)&\n' /etc/rc.local
fi

echo "Installtion Completed, conifgure the camera and restart your raspberry pi."