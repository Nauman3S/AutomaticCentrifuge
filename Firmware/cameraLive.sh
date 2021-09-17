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

sleep 2

(chromium-browser http://0.0.0.0:8099 >/home/pi/AutomaticCentrifuge/Firmware/logs/browserLogs.txt 2>&1)&