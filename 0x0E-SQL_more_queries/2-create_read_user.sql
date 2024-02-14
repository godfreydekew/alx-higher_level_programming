-- Creates the database hbtn_0d_2
-- Creates the user user_0d_2
-- Crants user_0d_2 SELECT
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS
        'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON `hbtn_0d_2`.* TO `user_0d_2`@`localhost`;
