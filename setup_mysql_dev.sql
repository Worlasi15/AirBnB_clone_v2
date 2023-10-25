/*script to do the following:
  creates an AIRBNB_dev Database if not found
  create hbnb user and a password if not found
  grant privileges and access*/

-- Create the hbnb_dev_db database if not in existence
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

--Create the hbnb user with a password if not in existence
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

--Grant all hbnb_dev_db privileges to hbnb_dev
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

--Grant SELECT privileges on performance_schema to hbnb_dev
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

FLUSH PRIVILEGES;
