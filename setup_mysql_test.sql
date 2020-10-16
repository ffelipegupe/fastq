-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS fastq_test_db;
CREATE USER IF NOT EXISTS 'fastq_test'@'localhost' IDENTIFIED BY 'fastq_test_pwd';
GRANT ALL PRIVILEGES ON `fastq_test_db`.* TO 'fastq_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'fastq_test'@'localhost';
FLUSH PRIVILEGES;
