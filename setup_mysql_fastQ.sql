-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS fastq_dev_db;
CREATE USER IF NOT EXISTS 'fastq_dev'@'localhost' IDENTIFIED BY 'fastq_dev_pwd';
GRANT ALL PRIVILEGES ON `fastq_dev_db`.* TO 'fastq_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'fastq_dev'@'localhost';
FLUSH PRIVILEGES;
