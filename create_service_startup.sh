
#!/bin/bash


sudo echo "[Unit]
Description=Startup Play
After=multi-user.target

[Service]
WorkingDirectory=/home/mendel/
ExecStart=python3 /home/mendel/coral_test/coral_test.py
Restart = on-failure

[Install]
WantedBy=multi-user.target" > /etc/systemd/system/sedia_2_test.service

sudo chmod 777 /home/mendel/coral_test/coral_test.py

sudo systemctl daemon-reload
sudo systemctl enable sedia_2_test.service
sudo systemctl start sedia_2_test.service
