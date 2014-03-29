==- NOTICE -==

1. Browser based only. Cannot be run from commandline or with cron.
2. Please respect the 5 seconds interval so as not to hammer the https://a816-healthpsi.nyc.gov site, and don't run this every day

==- USAGE -==

1. Upload files to your server of local environment
2. Make sure cookie.txt and daycarenyc.csv are writable
3. Edit config.inc.php to set the script reload delay (please use a minimum of 5 seconds) and fill in your DB settings
4. Import centers.sql to your database
5. In your browser open daycare.php -> keep it open until you see "ready". It will reload every 5 seconds (or whatever you put in your config) until it has retrieved all the pages.