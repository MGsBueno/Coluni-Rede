install server 


- Linux CentOS:

Open the cron task list by using the following command:

crontab -e


------------------------------------------------
Note: If you have multiple text editors installed, 
the system prompts you to select an editor to update the cron task list with. 
Use the number in the brackets to choose your preferred option. 
We will be using the default option, Nano.
------------------------------------------------
To run a cron job at every system boot, 
add a string called @reboot to the end of the task list. 
The job defined by this string runs at startup, immediately after Linux reboots.
Use the following syntax when adding a @reboot string:

@reboot [path_of_server.py]

------------------------------------------------
Note: In some cases, the crond service needs to be enabled on boot for the configuration to function.

To check if the crond service is enabled, use:
sudo systemctl status cron.service

To enable this service, use:
sudo systemctl enable cron.service



--------------------------------------------------------------------------------------------------------
Remove a Reboot Command

To do this, open the task list using the crontab -e command. 
Scroll down to the bottom to review the jobs you added.
To remove a task from the list, 
delete the appropriate line from the appropriate string. Press Control + X to exit Nano, 
then Y and Enter to save changes.

