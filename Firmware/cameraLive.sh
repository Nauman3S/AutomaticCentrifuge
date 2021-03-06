sleep 10
# export DISPLAY=:0
# xset s off
# xset -dpms 
# xset s noblank

(cvlc v4l2:///dev/video0:chroma=h264
                       :input-slave=alsa://hw:1,0
                       :live-caching=2500
--sout '#transcode{
                     deinterlace,
                     vcodec=mpgv,
                     acodec=mpga,
                     ab=128,
                     channels=2,
                     samplerate=44100,
                     threads=4,
                     audio-sync=1,
                     fps=60}
       :standard{
                     access=http,
                     mux=ts,
                     mime=video/ts,
                     dst=0.0.0.0:8099}'

 >/home/pi/AutomaticCentrifuge/Firmware/logs/liveCamLogs.txt 2>&1)&

sleep 10

#(DISPLAY=:0 sudo -u pi chromium-browser http://localhost:8099 >/home/pi/AutomaticCentrifuge/Firmware/logs/browserLogs.txt 2>&1 )&
(chromium-browser --no-sandbox http://localhost:8099 >/home/pi/AutomaticCentrifuge/Firmware/logs/browserLogs.txt 2>&1 )&

