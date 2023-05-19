Incident report for 404 error / Site Outage
Summary
On October 12th, 2017 at  around midnight the server access  of a FinTech company went down resulting in 404 errors for anyone trying to access their  website or payment app. Background on the server being based on a LAMP stack.
Timeline
00:00 BST - 404 error for anyone trying to access the website or app
00:15 BST - Ensuring Apache and MySQL are up and running.
00:17 BST - The website/app was not loading properly which on background investigation, it was revealed that the server was working properly as well as the database.
00:19 BST - After a quick restart of the Apache the server returned a status of 200 and OK while trying to curl the website.
00:20 BST - Reviewing error logs to check where the error might be coming from.
00:23 BST - Check /log/var to see that the Apache server was being initially shut down. The error logs for PHP were not found.
00:25 BST - Checking php.ini settings revealed all error logging had been turned off. Turning the error logging on.
00:30 BST - Restarting the apache server and going to the error log to check what is being logged into the php error logs.
00:36 BST - in reviewing the error logs for php, it was  revealed a mistyped file name which was resulting in incorrect loading and premature closing of apache.
00:38 BST - Fixing the file name and restarting Apache server.
00:40 BST - Server is now running normally and the website and app is now loading properly.
Root Cause and Resolution
The issue was from a wrong file name that was referred to in the wp-settings.php file. The error was raised when trying to curl the server, wherein the server responded with 404 errors. By checking the error logs it was found that no error log file was being created for the php errors and reading the default error log for apache did not result in any much information regarding the closing on the server. Once understood that the errors for php logs were not being directed anywhere the engineers chose to review the error log setting for the php in the php.ini file and found that all error logging was turned off. Once turned on, the error logging the apache server was restarted to check if any errors were being registered in the log. As suspected, the php log showed that a file with a .php extension was not found in the wp-settings.php file. This was clearly a misspelt error that resulted in the error to site access. As this was one server that the error was found in, this error might have been replicated in other servers as well. An easy fix by changing the file extension by puppet would result in the fix being made to other servers as well. A quick deployment of the puppet code replaced all misspelt file extensions with the right one and restarting of the server resulted in proper loading of the site and server.
Corrective and Preventive Measures
All servers and sites should have error logging turned on to easily identify errors if anything goes wrong.
All servers and sites should be tested locally before deploying on a multi-server setup; this will result in correcting errors before going live resulting in less fixing time if the site goes down.
