/*
SQLyog Ultimate - MySQL GUI v8.21 
MySQL - 5.1.29-rc-community : Database - class_test
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`class_test` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `class_test`;

/*Table structure for table `info` */

DROP TABLE IF EXISTS `info`;

CREATE TABLE `info` (
  `Username` varchar(30) DEFAULT NULL,
  `password` varchar(30) DEFAULT NULL,
  `address` varchar(70) DEFAULT NULL,
  `phone` int(15) DEFAULT NULL,
  `city` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `info` */

insert  into `info`(`Username`,`password`,`address`,`phone`,`city`) values ('Hassan','test123','53 A Johar Town',54879,'Lahore'),('marcin','test1243','Frankfurt',8574554,'Frankfurt'),('Frerick','test675','Siegnstr 56',987654,'Frankfurt'),('Florian','tets453','52 SiegStr',78654677,'Munich');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
