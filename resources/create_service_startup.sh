
#!/bin/bash

#da cambiare con servizio utente non root


echo "create folder: /home/mendel/.config/systemd/user
create file your_service_name.service:

example:

[Unit]
Description=Startup Play
After=multi-user.target

[Service]
WorkingDirectory=/home/mendel/
ExecStart=python3 /home/mendel/coral_test/coral_test.py
Restart = on-failure

[Install]
WantedBy=default.target


run these command:

sudo systemctl --user enamble your_service_name
sudo systemctl --user start your_service_name


"





##### OLD --- NOT WORKING --- ##########
<<com
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
com

