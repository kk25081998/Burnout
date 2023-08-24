-- MySQL dump 10.16  Distrib 10.1.48-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: db
-- ------------------------------------------------------
-- Server version	10.1.48-MariaDB-0+deb9u2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alembic_version`
--

DROP TABLE IF EXISTS `alembic_version`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alembic_version` (
  `version_num` varchar(12) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alembic_version`
--

LOCK TABLES `alembic_version` WRITE;
/*!40000 ALTER TABLE `alembic_version` DISABLE KEYS */;
INSERT INTO `alembic_version` VALUES ('3a02e95825b5');
/*!40000 ALTER TABLE `alembic_version` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `company`
--

DROP TABLE IF EXISTS `company`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `company` (
  `id` tinyint(4) DEFAULT NULL,
  `name` varchar(11) DEFAULT NULL,
  `description` varchar(69) DEFAULT NULL,
  `size` mediumint(9) DEFAULT NULL,
  `frequency` varchar(7) DEFAULT NULL,
  `image` varchar(14) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `company`
--

LOCK TABLES `company` WRITE;
/*!40000 ALTER TABLE `company` DISABLE KEYS */;
INSERT INTO `company` VALUES (1,'TechPros','Leading provider of innovative tech solutions',1200,'',''),(2,'BioHealth','BioHealth is at the forefront of medical biotechnology',750,'',''),(3,'EcoBuild','Eco-friendly construction and architectural solutions',890,'',''),(4,'FinTrust','A trustworthy partner for all your financial needs',1450,'',''),(5,'FoodJoy','Delivering joy through quality food products',670,'',''),(6,'FitLife','Promoting healthier lifestyles through high-quality fitness equipment',920,'',''),(7,'AutoRapid','Providing rapid solutions in the automobile industry',1100,'',''),(8,'StyleSphere','Your ultimate destination for fashion and lifestyle products',980,'',''),(9,'EduBright','A platform to enlighten young minds with quality education',123012,'1_month','company-9.jpg'),(10,'GreenPower','Contributing to a greener future with renewable energy solutions',1420,'1_month','company-10.png');
/*!40000 ALTER TABLE `company` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feedback`
--

DROP TABLE IF EXISTS `feedback`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `feedback` (
  `id` tinyint(4) DEFAULT NULL,
  `company_id` tinyint(4) DEFAULT NULL,
  `date_submitted` varchar(10) DEFAULT NULL,
  `description` varchar(21) DEFAULT NULL,
  `status` varchar(8) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feedback`
--

LOCK TABLES `feedback` WRITE;
/*!40000 ALTER TABLE `feedback` DISABLE KEYS */;
INSERT INTO `feedback` VALUES (1,10,'','Feedback from User 12','Reviewed'),(2,10,'','Feedback from User 13','Reviewed'),(3,10,'','Feedback from User 14','Reviewed'),(4,10,'','Feedback from User 15','Reviewed'),(5,10,'','Feedback from User 16','Reviewed'),(6,10,'','Feedback from User 17','Pending'),(7,10,'','Feedback from User 18','Pending'),(8,10,'','Feedback from User 19','Pending'),(9,10,'','Feedback from User 20','Pending'),(10,10,'','Feedback from User 21','Pending'),(11,10,'','Feedback from User 22','Pending'),(12,10,'','Feedback from User 23','Pending'),(13,10,'','Feedback from User 24','Pending'),(14,10,'','Feedback from User 25','Pending'),(15,10,'','Feedback from User 26','Pending'),(16,10,'','Feedback from User 27','Pending'),(17,10,'','Feedback from User 28','Pending'),(18,10,'','Feedback from User 29','Pending'),(19,10,'','Feedback from User 30','Pending'),(20,10,'','Feedback from User 31','Pending'),(21,9,'','Feedback from User 32','Pending'),(22,9,'','Feedback from User 33','Pending'),(23,9,'','Feedback from User 34','Pending'),(24,9,'','Feedback from User 35','Pending'),(25,9,'','Feedback from User 36','Pending'),(26,9,'','Feedback from User 37','Pending'),(27,9,'','Feedback from User 38','Pending'),(28,9,'','Feedback from User 39','Pending'),(29,9,'','Feedback from User 40','Pending'),(30,9,'','Feedback from User 41','Pending'),(31,9,'','Feedback from User 42','Pending'),(32,9,'','Feedback from User 43','Pending'),(33,9,'','Feedback from User 44','Pending'),(34,9,'','Feedback from User 45','Pending'),(35,9,'','Feedback from User 46','Pending'),(36,9,'','Feedback from User 47','Reviewed'),(37,9,'','Feedback from User 48','Reviewed'),(38,9,'','Feedback from User 49','Reviewed'),(39,9,'','Feedback from User 50','Reviewed'),(40,9,'','Feedback from User 51','Reviewed'),(41,9,'2023-08-23','Test1','Pending'),(42,9,'2023-08-23','test1','Pending'),(43,9,'2023-08-23','Test23','Pending'),(44,9,'2023-08-23','Test2','Pending'),(45,9,'2023-08-23','Test2','Pending'),(46,9,'2023-08-23','Test2','Pending'),(47,9,'2023-08-23','Test223','Pending'),(48,9,'2023-08-23','Test223','Pending'),(49,9,'2023-08-23','Test223','Pending'),(50,9,'2023-08-23','Test22334242342','Pending'),(51,9,'2023-08-23','Test22334242342','Pending'),(52,9,'2023-08-23','jkhgfcjhg','Pending'),(53,9,'2023-08-23','jkhgfcjhg','Pending'),(54,9,'2023-08-23','Testasfasdfasdf','Pending'),(55,9,'2023-08-23','Adcasfasdfasdfas','Pending'),(56,9,'2023-08-23','adsfasdfasdfasdfaf','Pending');
/*!40000 ALTER TABLE `feedback` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `permission`
--

DROP TABLE IF EXISTS `permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `permission` (
  `id` tinyint(4) DEFAULT NULL,
  `name` varchar(8) DEFAULT NULL,
  `description` varchar(17) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `permission`
--

LOCK TABLES `permission` WRITE;
/*!40000 ALTER TABLE `permission` DISABLE KEYS */;
INSERT INTO `permission` VALUES (1,'read','Can read data'),(2,'write','Can write data'),(3,'delete','Can delete data'),(4,'view_all','Can view all data');
/*!40000 ALTER TABLE `permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resources`
--

DROP TABLE IF EXISTS `resources`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `resources` (
  `id` tinyint(4) DEFAULT NULL,
  `category` varchar(23) DEFAULT NULL,
  `title` varchar(37) DEFAULT NULL,
  `description` varchar(143) DEFAULT NULL,
  `link` text,
  `date_added` varchar(0) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resources`
--

LOCK TABLES `resources` WRITE;
/*!40000 ALTER TABLE `resources` DISABLE KEYS */;
INSERT INTO `resources` VALUES (1,'Evaluate Your Options','Harvard Business Review (HBR) Article','\"How to Tell Your Boss You\'re Burned Out\" - This article provides insights on approaching and communicating with your supervisor about burnout.','https://hbr.org/2021/01/how-to-tell-your-boss-youre-burned-out',''),(2,'Evaluate Your Options','Sproutsocial','Gain insights on addressing burnout in the workplace and how to communicate your feelings effectively.','https://sproutsocial.com/insights/talking-to-your-boss-about-burnout/',''),(3,'Evaluate Your Options','The Muse','\"A Realistic Plan for Telling Your Boss That You\'re Burnt Out\" - A step-by-step guide to discussing burnout and seeking personal time.','https://www.themuse.com/advice/a-realistic-plan-for-telling-your-boss-that-youre-burnt-out-and-need-personal-time',''),(4,'Seek Support','7 Cups','7 Cups offers a platform where you can connect with trained listeners for free counseling and support.','https://www.7cups.com/',''),(5,'Seek Support','Talkspace','Online therapy with professional therapists to help you navigate personal challenges.','https://www.talkspace.com/',''),(6,'Seek Support','Peer Recovery Alliance','Promotes peer support in mental health, connecting individuals with others who have had similar experiences.','https://www.peerrecoveryalliance.org/',''),(7,'Seek Support','ADAA','Resources on understanding anxiety and depression, finding treatment, and connecting with a supportive community.','https://adaa.org/',''),(8,'Try a Relaxing Activity','Headspace','Headspace offers guided meditations designed to reduce stress, improve sleep, and enhance focus.','https://www.headspace.com/',''),(9,'Try a Relaxing Activity','Do Yoga With Me','Free and premium yoga videos for practitioners of all levels.','https://www.doyogawithme.com/',''),(10,'Try a Relaxing Activity','Tai Chi for Health Institute','Resources, classes, and information about Tai Chi for stress reduction and overall health.','https://taichiforhealthinstitute.org/',''),(11,'Try a Relaxing Activity','Calm','Meditation and sleep app designed to reduce stress and improve overall well-being.','https://www.calm.com/',''),(12,'Try a Relaxing Activity','10% Happier','Practical meditation techniques suitable for beginners and experienced meditators alike.','https://www.tenpercent.com/',''),(13,'Exercise','Peloton','Peloton offers at home guided workouts with use of minimal equipment. Helps you to take your attention off work.','https://www.onepeloton.com',''),(14,'Exercise','Caliber','Free strength training platform, allowing you to work on your muscles with the comfort of your home.','https://pages.caliberstrong.com/app/?_branch_match_id=1219740800959854574&utm_source=pillar4&utm_campaign=1_SI_best-free-workout-apps_F_FT_AP_RU&utm_medium=partner&_branch_referrer=H4sIAAAAAAAAA8soKSkottLXT07MyUxKLdJLLCjQy8nMy9YvyMzJSSwy0Q32BADTaRw3IwAAAA%3D%3D',''),(15,'Exercise','My Fitness Pal','Track your exercises and food intake in a single platform to keep yourself in the optimum shape','https://www.myfitnesspal.com',''),(16,'Exercise','Nike Training Club','Optimal workout companion offering quick workouts for all body types','https://www.nike.com/ntc-app?cp=66334508171_search_-nike%20training%20club-g-19789573190-148378492202-e-c---650700845426-aud-1114682402147:kwd-300268666982-9067609&gclid=Cj0KCQjwoeemBhCfARIsADR2QCu_yeUHW6fOm1tuziu6rShAOJtGNPiVS9F4zUIXCGs8V9bOEz0gsBkaAh6hEALw_wcB&gclsrc=aw.ds',''),(17,'Sleep','Article by Forbes','An article by Forbes that elaborates on the importance of sleep in our lives.','https://www.forbes.com/sites/forbesbusinesscouncil/2023/04/13/employee-burnout-recovery-and-prevention/?sh=2f2bde844073',''),(18,'Sleep','ShutEye','Sleep tracking platform that helps you track the quality of your sleep.','https://shuteye.ai',''),(19,'Sleep','Oura Ring','Oura ring is a minimal device that helps you track your sleep and other vitals.','https://ouraring.com/?g_acctid=553-919-5922&g_adgroupid=139082356777&g_adid=621632875186&g_adtype=search&g_campaign=sem_prosp_alwayson_nb_allgeo_en_broad_sleep&g_campaignid=18324137946&g_keyword=sleep%20tracking&g_keywordid=kwd-298756685196&g_network=g&utm_campaign=sem_prosp_alwayson_nb_allgeo_en_broad_sleep&utm_medium=cpc&utm_source=google&utm_source=google_search&gclid=Cj0KCQjwoeemBhCfARIsADR2QCt8MB9s3LDVN_6dAF6CrI1yjelFbxPPistyx2SDmrYZTqoS0sRbqfIaAulqEALw_wcB',''),(20,'Mindfulness','Headspace','Headspace offers guided meditations designed to reduce stress, improve sleep, and enhance focus.','https://www.headspace.com',''),(21,'Mindfulness','Mindfulness Masterclass','Take an exceptional Masterclass by Jon Kabat-Zinn talking about mindfulness and meditation and its impact on the body.','https://www.masterclass.com/classes/jon-kabat-zinn-teaches-mindfulness-and-meditation?campaignid=18815197582&adgroupid=146742775841&adid=660277727679&utm_term=learn%20mindfulness%20online&utm_campaign=%5BMC%5D+%7C+Search+%7C+NonBrand+%7C+Wellness+%7C+USA+%7C+EN+%7C+tROAS+%7C+EG&utm_source=adwords&utm_medium=ppc&hsa_acc=9801000675&hsa_cam=18815197582&hsa_grp=146742775841&hsa_ad=660277727679&hsa_src=g&hsa_tgt=kwd-296044441582&hsa_kw=learn%20mindfulness%20online&hsa_mt=b&hsa_net=adwords&hsa_ver=3&gclid=Cj0KCQjwoeemBhCfARIsADR2QCv5lf244bQ1AiGY5QjE7xUj9ton3r9rStJG7YBUAAlpCcqJu5ATcdMaAri_EALw_wcB',''),(22,'Mindfulness','Article on Mindfulness','The awareness that emerges through paying attention, on purpose, and nonjudgmentally to the unfolding of experience moment by moment.','https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4776732/',''),(23,'Mindfulness','InsightTimer','InsightTimer offers different talks on the impact of Mindfulness and how one can incorporate it into their life.','https://insighttimer.com','');
/*!40000 ALTER TABLE `resources` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `results` (
  `id` smallint(6) DEFAULT NULL,
  `testDate` varchar(0) DEFAULT NULL,
  `scoreA` tinyint(4) DEFAULT NULL,
  `scoreB` tinyint(4) DEFAULT NULL,
  `scoreC` tinyint(4) DEFAULT NULL,
  `user_id` varchar(2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` VALUES (2,'',32,23,35,'11'),(3,'',14,23,17,'11'),(4,'',23,39,12,'11'),(5,'',41,39,27,'11'),(6,'',17,33,21,'11'),(7,'',42,39,41,'11'),(8,'',16,4,7,'11'),(9,'',30,3,33,'11'),(10,'',25,32,23,'11'),(11,'',12,1,29,'11'),(12,'',0,3,40,'11'),(13,'',21,35,25,'11'),(14,'',1,6,20,'11'),(15,'',42,42,0,'11'),(16,'',0,11,24,''),(17,'',17,25,41,''),(18,'',31,5,23,''),(19,'',24,26,8,''),(20,'',20,25,31,''),(21,'',9,42,33,''),(22,'',37,34,44,''),(23,'',9,29,14,''),(24,'',11,16,43,''),(25,'',30,5,12,''),(26,'',13,23,5,''),(27,'',23,5,2,''),(28,'',11,27,45,'13'),(29,'',40,23,29,'13'),(30,'',27,3,7,'13'),(31,'',1,42,28,'13'),(32,'',39,21,45,'13'),(33,'',37,3,32,'13'),(34,'',27,32,1,'13'),(35,'',41,23,7,'13'),(36,'',12,22,40,'13'),(37,'',3,8,26,'13'),(38,'',9,41,33,'13'),(39,'',40,39,37,'13'),(40,'',19,21,35,'14'),(41,'',24,19,12,'14'),(42,'',5,36,2,'14'),(43,'',8,4,23,'14'),(44,'',26,7,40,'14'),(45,'',36,29,24,'14'),(46,'',25,40,28,'14'),(47,'',11,25,3,'14'),(48,'',34,7,26,'14'),(49,'',2,27,11,'14'),(50,'',8,37,25,'14'),(51,'',4,34,20,'14'),(52,'',1,23,10,'15'),(53,'',9,19,30,'15'),(54,'',18,11,9,'15'),(55,'',7,10,6,'15'),(56,'',0,31,45,'15'),(57,'',7,14,42,'15'),(58,'',31,21,5,'15'),(59,'',19,28,20,'15'),(60,'',24,14,26,'15'),(61,'',27,21,22,'15'),(62,'',6,13,25,'15'),(63,'',29,4,47,'15'),(64,'',34,24,11,'16'),(65,'',42,14,28,'16'),(66,'',26,17,42,'16'),(67,'',10,19,43,'16'),(68,'',22,6,32,'16'),(69,'',37,4,30,'16'),(70,'',37,15,8,'16'),(71,'',18,34,4,'16'),(72,'',36,39,35,'16'),(73,'',39,14,0,'16'),(74,'',14,27,3,'16'),(75,'',24,16,14,'16'),(76,'',37,38,47,'17'),(77,'',33,34,40,'17'),(78,'',11,13,21,'17'),(79,'',35,7,3,'17'),(80,'',11,8,4,'17'),(81,'',17,13,46,'17'),(82,'',12,30,22,'17'),(83,'',10,11,28,'17'),(84,'',26,10,48,'17'),(85,'',8,27,9,'17'),(86,'',25,6,28,'17'),(87,'',18,39,26,'17'),(88,'',10,17,18,'18'),(89,'',2,6,33,'18'),(90,'',41,2,23,'18'),(91,'',31,28,36,'18'),(92,'',5,28,18,'18'),(93,'',33,14,11,'18'),(94,'',30,17,37,'18'),(95,'',15,26,10,'18'),(96,'',31,18,19,'18'),(97,'',36,22,24,'18'),(98,'',16,30,35,'18'),(99,'',0,31,43,'18'),(100,'',8,42,15,'19'),(101,'',4,14,10,'19'),(102,'',36,38,44,'19'),(103,'',33,35,33,'19'),(104,'',1,16,11,'19'),(105,'',38,25,34,'19'),(106,'',14,32,31,'19'),(107,'',11,5,37,'19'),(108,'',13,16,18,'19'),(109,'',31,6,34,'19'),(110,'',6,2,4,'19'),(111,'',10,11,24,'19'),(112,'',30,5,33,'20'),(113,'',24,23,18,'20'),(114,'',25,4,38,'20'),(115,'',33,21,48,'20'),(116,'',39,18,7,'20'),(117,'',24,0,48,'20'),(118,'',14,29,30,'20'),(119,'',40,7,25,'20'),(120,'',40,29,48,'20'),(121,'',13,13,46,'20'),(122,'',36,4,15,'20'),(123,'',14,5,10,'20'),(124,'',4,20,24,''),(125,'',22,24,30,''),(126,'',14,39,27,''),(127,'',39,29,4,''),(128,'',2,27,36,''),(129,'',38,23,11,''),(130,'',21,31,2,''),(131,'',9,18,9,''),(132,'',37,6,35,''),(133,'',1,37,26,''),(134,'',41,14,44,''),(135,'',39,3,29,''),(136,'',31,9,26,'22'),(137,'',37,40,45,'22'),(138,'',33,4,12,'22'),(139,'',13,17,26,'22'),(140,'',35,15,37,'22'),(141,'',32,12,29,'22'),(142,'',38,17,42,'22'),(143,'',17,37,29,'22'),(144,'',7,4,27,'22'),(145,'',39,18,35,'22'),(146,'',30,19,9,'22'),(147,'',24,31,12,'22'),(148,'',30,6,13,'23'),(149,'',21,24,4,'23'),(150,'',34,33,28,'23'),(151,'',6,38,48,'23'),(152,'',30,23,11,'23'),(153,'',36,11,35,'23'),(154,'',1,12,35,'23'),(155,'',21,34,4,'23'),(156,'',6,21,47,'23'),(157,'',22,0,12,'23'),(158,'',26,26,39,'23'),(159,'',37,18,27,'23'),(160,'',19,29,16,'24'),(161,'',16,29,13,'24'),(162,'',30,16,24,'24'),(163,'',39,22,27,'24'),(164,'',4,38,6,'24'),(165,'',6,30,35,'24'),(166,'',9,2,47,'24'),(167,'',1,26,28,'24'),(168,'',31,12,26,'24'),(169,'',1,18,1,'24'),(170,'',4,34,47,'24'),(171,'',37,30,31,'24'),(172,'',14,36,9,'25'),(173,'',18,41,48,'25'),(174,'',40,18,31,'25'),(175,'',7,19,14,'25'),(176,'',25,27,40,'25'),(177,'',23,17,44,'25'),(178,'',12,0,42,'25'),(179,'',29,16,2,'25'),(180,'',3,41,36,'25'),(181,'',7,15,42,'25'),(182,'',32,21,34,'25'),(183,'',2,19,19,'25'),(184,'',17,18,40,'26'),(185,'',39,7,48,'26'),(186,'',26,24,1,'26'),(187,'',29,1,24,'26'),(188,'',21,3,27,'26'),(189,'',9,0,42,'26'),(190,'',21,29,26,'26'),(191,'',4,5,12,'26'),(192,'',28,17,39,'26'),(193,'',3,33,28,'26'),(194,'',42,16,31,'26'),(195,'',11,42,38,'26'),(196,'',7,21,9,'27'),(197,'',32,11,43,'27'),(198,'',20,14,48,'27'),(199,'',5,15,44,'27'),(200,'',20,36,3,'27'),(201,'',22,25,31,'27'),(202,'',35,27,31,'27'),(203,'',7,10,22,'27'),(204,'',33,17,42,'27'),(205,'',26,18,34,'27'),(206,'',7,34,42,'27'),(207,'',38,13,44,'27'),(208,'',14,35,42,'28'),(209,'',1,28,32,'28'),(210,'',5,35,40,'28'),(211,'',17,27,34,'28'),(212,'',11,20,14,'28'),(213,'',32,29,9,'28'),(214,'',35,21,31,'28'),(215,'',6,4,30,'28'),(216,'',7,29,35,'28'),(217,'',14,11,33,'28'),(218,'',6,38,15,'28'),(219,'',2,25,4,'28'),(220,'',29,42,0,'29'),(221,'',10,12,11,'29'),(222,'',11,8,5,'29'),(223,'',4,40,11,'29'),(224,'',38,40,13,'29'),(225,'',0,18,4,'29'),(226,'',28,22,43,'29'),(227,'',6,30,18,'29'),(228,'',23,32,38,'29'),(229,'',13,37,6,'29'),(230,'',6,2,20,'29'),(231,'',8,22,37,'29'),(232,'',42,1,40,'30'),(233,'',1,2,36,'30'),(234,'',19,35,21,'30'),(235,'',39,5,46,'30'),(236,'',41,32,20,'30'),(237,'',26,20,39,'30'),(238,'',24,4,33,'30'),(239,'',12,6,43,'30'),(240,'',38,4,32,'30'),(241,'',36,28,44,'30'),(242,'',16,2,23,'30'),(243,'',12,17,32,'30'),(244,'',12,19,5,'31'),(245,'',35,22,18,'31'),(246,'',26,21,38,'31'),(247,'',35,26,13,'31'),(248,'',4,21,47,'31'),(249,'',41,6,42,'31'),(250,'',24,18,8,'31'),(251,'',13,40,22,'31'),(252,'',12,30,44,'31'),(253,'',24,9,35,'31'),(254,'',28,31,34,'31'),(255,'',29,40,12,'31'),(256,'',16,18,25,'32'),(257,'',4,22,32,'32'),(258,'',31,14,25,'32'),(259,'',21,41,11,'32'),(260,'',40,29,1,'32'),(261,'',8,3,11,'32'),(262,'',41,39,11,'32'),(263,'',0,40,28,'32'),(264,'',12,10,6,'32'),(265,'',0,30,26,'32'),(266,'',1,33,44,'32'),(267,'',40,6,35,'32'),(268,'',27,33,38,'33'),(269,'',20,28,43,'33'),(270,'',10,22,33,'33'),(271,'',36,23,47,'33'),(272,'',23,22,32,'33'),(273,'',27,9,11,'33'),(274,'',35,26,17,'33'),(275,'',31,8,32,'33'),(276,'',0,29,47,'33'),(277,'',12,22,11,'33'),(278,'',21,22,38,'33'),(279,'',9,20,10,'33'),(280,'',32,34,29,'34'),(281,'',28,10,18,'34'),(282,'',7,38,7,'34'),(283,'',21,41,1,'34'),(284,'',41,8,48,'34'),(285,'',13,27,6,'34'),(286,'',17,27,15,'34'),(287,'',3,14,5,'34'),(288,'',16,0,15,'34'),(289,'',21,4,43,'34'),(290,'',21,10,31,'34'),(291,'',18,18,22,'34'),(292,'',1,24,7,'35'),(293,'',30,11,42,'35'),(294,'',6,33,1,'35'),(295,'',26,23,37,'35'),(296,'',40,26,18,'35'),(297,'',27,40,8,'35'),(298,'',25,16,9,'35'),(299,'',19,24,5,'35'),(300,'',39,31,35,'35'),(301,'',4,14,47,'35'),(302,'',13,7,38,'35'),(303,'',31,0,22,'35'),(304,'',22,20,20,'36'),(305,'',34,5,47,'36'),(306,'',42,23,38,'36'),(307,'',22,36,14,'36'),(308,'',2,39,34,'36'),(309,'',25,34,20,'36'),(310,'',3,34,42,'36'),(311,'',41,28,6,'36'),(312,'',21,0,2,'36'),(313,'',23,1,11,'36'),(314,'',42,30,30,'36'),(315,'',38,1,35,'36'),(316,'',36,4,40,'37'),(317,'',3,5,37,'37'),(318,'',40,23,24,'37'),(319,'',33,14,1,'37'),(320,'',2,25,25,'37'),(321,'',20,4,3,'37'),(322,'',31,1,43,'37'),(323,'',13,29,29,'37'),(324,'',39,12,21,'37'),(325,'',1,39,24,'37'),(326,'',39,33,37,'37'),(327,'',30,10,37,'37'),(328,'',22,30,28,'38'),(329,'',2,25,8,'38'),(330,'',37,2,12,'38'),(331,'',10,21,41,'38'),(332,'',15,21,0,'38'),(333,'',9,4,21,'38'),(334,'',6,4,30,'38'),(335,'',39,10,13,'38'),(336,'',13,17,10,'38'),(337,'',30,4,4,'38'),(338,'',31,8,35,'38'),(339,'',28,28,27,'38'),(340,'',23,20,2,'39'),(341,'',24,25,25,'39'),(342,'',29,2,22,'39'),(343,'',31,38,23,'39'),(344,'',40,19,44,'39'),(345,'',11,0,48,'39'),(346,'',24,37,23,'39'),(347,'',7,2,41,'39'),(348,'',15,38,25,'39'),(349,'',14,22,5,'39'),(350,'',16,10,37,'39'),(351,'',4,41,14,'39'),(352,'',29,10,4,'40'),(353,'',13,10,9,'40'),(354,'',28,25,34,'40'),(355,'',15,12,12,'40'),(356,'',20,38,15,'40'),(357,'',8,10,39,'40'),(358,'',25,4,3,'40'),(359,'',8,21,27,'40'),(360,'',39,3,28,'40'),(361,'',8,33,3,'40'),(362,'',20,4,6,'40'),(363,'',8,15,18,'40'),(364,'',3,7,47,'41'),(365,'',14,33,6,'41'),(366,'',35,27,6,'41'),(367,'',42,11,30,'41'),(368,'',31,41,12,'41'),(369,'',16,6,31,'41'),(370,'',14,18,35,'41'),(371,'',26,40,19,'41'),(372,'',0,34,13,'41'),(373,'',38,21,29,'41'),(374,'',14,5,24,'41'),(375,'',35,17,24,'41'),(376,'',4,14,28,'42'),(377,'',19,13,2,'42'),(378,'',38,7,16,'42'),(379,'',39,22,44,'42'),(380,'',37,4,37,'42'),(381,'',13,17,33,'42'),(382,'',34,20,20,'42'),(383,'',22,2,16,'42'),(384,'',29,18,15,'42'),(385,'',41,28,21,'42'),(386,'',8,17,5,'42'),(387,'',1,34,40,'42'),(388,'',11,2,33,'43'),(389,'',4,12,47,'43'),(390,'',5,3,9,'43'),(391,'',22,20,37,'43'),(392,'',27,15,44,'43'),(393,'',35,35,38,'43'),(394,'',26,25,35,'43'),(395,'',8,18,23,'43'),(396,'',22,25,45,'43'),(397,'',27,22,32,'43'),(398,'',40,10,12,'43'),(399,'',29,4,42,'43'),(400,'',41,11,43,'44'),(401,'',16,14,39,'44'),(402,'',9,39,10,'44'),(403,'',8,36,43,'44'),(404,'',28,18,45,'44'),(405,'',18,21,23,'44'),(406,'',9,7,9,'44'),(407,'',9,33,2,'44'),(408,'',3,40,6,'44'),(409,'',35,33,32,'44'),(410,'',22,11,4,'44'),(411,'',15,7,7,'44'),(412,'',15,9,38,'45'),(413,'',33,23,29,'45'),(414,'',33,10,0,'45'),(415,'',23,11,17,'45'),(416,'',29,26,32,'45'),(417,'',23,31,37,'45'),(418,'',14,6,1,'45'),(419,'',32,32,6,'45'),(420,'',42,26,24,'45'),(421,'',8,29,18,'45'),(422,'',12,14,0,'45'),(423,'',2,15,14,'45'),(424,'',31,28,6,'46'),(425,'',3,0,25,'46'),(426,'',19,39,43,'46'),(427,'',29,20,4,'46'),(428,'',30,36,13,'46'),(429,'',20,42,19,'46'),(430,'',29,4,10,'46'),(431,'',1,0,15,'46'),(432,'',14,15,34,'46'),(433,'',30,7,39,'46'),(434,'',16,42,7,'46'),(435,'',20,14,4,'46'),(436,'',34,29,30,'47'),(437,'',27,32,44,'47'),(438,'',19,41,43,'47'),(439,'',14,23,26,'47'),(440,'',16,19,38,'47'),(441,'',36,42,41,'47'),(442,'',20,10,24,'47'),(443,'',21,25,38,'47'),(444,'',5,21,42,'47'),(445,'',41,13,2,'47'),(446,'',20,26,9,'47'),(447,'',5,37,13,'47'),(448,'',17,29,14,'48'),(449,'',1,31,22,'48'),(450,'',16,5,7,'48'),(451,'',17,22,13,'48'),(452,'',31,1,3,'48'),(453,'',21,30,29,'48'),(454,'',7,35,31,'48'),(455,'',26,0,27,'48'),(456,'',17,33,14,'48'),(457,'',19,19,20,'48'),(458,'',42,22,36,'48'),(459,'',29,30,25,'48'),(460,'',12,32,31,'49'),(461,'',31,23,1,'49'),(462,'',30,28,45,'49'),(463,'',24,40,42,'49'),(464,'',33,40,19,'49'),(465,'',6,19,11,'49'),(466,'',40,40,19,'49'),(467,'',13,42,31,'49'),(468,'',15,14,25,'49'),(469,'',35,21,11,'49'),(470,'',32,12,14,'49'),(471,'',30,8,44,'49'),(472,'',12,16,15,'50'),(473,'',32,13,36,'50'),(474,'',34,39,16,'50'),(475,'',2,7,22,'50'),(476,'',26,10,9,'50'),(477,'',26,25,9,'50'),(478,'',6,14,44,'50'),(479,'',25,1,14,'50'),(480,'',34,42,36,'50'),(481,'',13,26,43,'50'),(482,'',8,26,11,'50'),(483,'',35,38,0,'50'),(484,'',26,26,48,'51'),(485,'',4,29,17,'51'),(486,'',33,0,41,'51'),(487,'',2,24,32,'51'),(488,'',26,30,28,'51'),(489,'',5,38,6,'51'),(490,'',41,36,14,'51'),(491,'',10,21,0,'51'),(492,'',26,5,40,'51'),(493,'',42,37,26,'51'),(494,'',32,17,24,'51'),(495,'',8,3,35,'51');
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` tinyint(4) DEFAULT NULL,
  `name` varchar(9) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (2,'Admin'),(3,'HR'),(4,'Manager'),(1,'SuperUser'),(5,'User');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role_permissions`
--

DROP TABLE IF EXISTS `role_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role_permissions` (
  `role_id` tinyint(4) DEFAULT NULL,
  `permission_id` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role_permissions`
--

LOCK TABLES `role_permissions` WRITE;
/*!40000 ALTER TABLE `role_permissions` DISABLE KEYS */;
INSERT INTO `role_permissions` VALUES (1,4),(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(5,1);
/*!40000 ALTER TABLE `role_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` tinyint(4) DEFAULT NULL,
  `email` varchar(23) DEFAULT NULL,
  `password_hash` varchar(102) DEFAULT NULL,
  `firstname` varchar(12) DEFAULT NULL,
  `lastname` varchar(11) DEFAULT NULL,
  `image` varchar(24) DEFAULT NULL,
  `date_of_birth` varchar(19) DEFAULT NULL,
  `companyId` tinyint(4) DEFAULT NULL,
  `manager_id` varchar(2) DEFAULT NULL,
  `first_login` tinyint(4) DEFAULT NULL,
  `role_id` varchar(1) DEFAULT NULL,
  `department` varchar(5) DEFAULT NULL,
  `title` varchar(13) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'harsh.gupta@test.com','pbkdf2:sha256:600000$BB0QUr4jP0nhlVyW$abb1320700b803887783938aac710a9bd5ce6af4891aaa7128f27f62ff4b7570','Harsh','Gupta','','1999-10-28 00:00:00',2,'3',1,'','',''),(2,'kartik.khosa@test.com','pbkdf2:sha256:600000$utVHRGDIOKgfn4Fq$093046141d5aaab665df8b3c62d04f14f737a556ede07c12ff15f294ba75170d','Kartik','Khosa','','1999-05-20 00:00:00',1,'4',1,'','',''),(3,'joh.doe@gmail.com','pbkdf2:sha256:600000$9z09z0S5A85Eibe4$4d9e7d6e480484ac8955d2130c5c6302574a56b046d431ece7cbead8b2b671f1','John','Doe','','1995-12-12 00:00:00',2,'6',1,'','',''),(4,'jane.austen@yahoo.com','pbkdf2:sha256:600000$h2jz4a9YJCztr5Pl$b72824e762277f47014432727bafcbe25b942c7a740104d098f1bec4d2c11065','Jane','Austen','','1990-10-02 00:00:00',2,'5',1,'','',''),(5,'leo.messi@outlook.com','pbkdf2:sha256:600000$YFk0EDRjnnH48nvi$043cccd1c18a7cfac0503f1d35c51ed03e746a75d2e96a27f149b2c3af9cf869','Lionel','Messi','','1985-07-22',2,'0',0,'','',''),(6,'rafael.nadal@gmail.com','pbkdf2:sha256:600000$pMXSvtxmaM8Lpedz$20be72896bb332ecb98509a5064c49338c85a12d25ac62d3ed9797f3b987c8f5','Rafael','Nadal','','1980-01-05 00:00:00',2,'2',1,'','',''),(7,'lewis.goat@test.com','pbkdf2:sha256:600000$y2uCeTgHKSwhi0vP$2c91fc65096c3fc88217a771d4e72f571b6ce0ad6dc94c1d023b43246839dc20','Lewis','Hamilton','','1980-04-04 00:00:00',2,'9',1,'','',''),(8,'sergio.perez@mexico.com','pbkdf2:sha256:600000$6aN30tVdMHleQHgs$a2e74320787706ffc8ce3d1cab37dffb7a7736dacaf110007562cf0e1968f9ad','Sergio','Perez','','1980-02-03 00:00:00',2,'1',1,'','',''),(9,'taylor.swift@test.com','pbkdf2:sha256:600000$QZZ6Kn9uJOeVxDuO$24b531926ac6fb36e973f7cd88fd1a10ea0513f6bdffa33dd55a122f28288347','Taylor','Swift','','1990-05-05 00:00:00',2,'2',1,'','',''),(10,'selenagomez123@test.com','pbkdf2:sha256:600000$DTAO4f4yXYYCpvFq$3a97b4b125233f76d54e0377b81e93138163c8f4ac4028a8016bd6322fb1f05d','Selena','Gomez','','1990-06-18 00:00:00',2,'1',1,'','',''),(11,'test@gmail.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','Kartik','Khosa','testgmail.com-11.jpg','1998-08-25',1,'0',0,'','',''),(13,'admin2@example.com','pbkdf2:sha256:600000$lAvEkoRAPaVieWr5$0702ce4436e041298dbbfcb02097c2cd57e6bb3a53002b3719ce27f9e979b681','Admin 222321','User 222321','','2023-08-14',10,'',0,'2','Test','Test'),(14,'admin3@example.com','pbkdf2:sha256:600000$yuJmMeKTlAnwf8x0$8269ce0c4d347621dcdd6f53bda6462f5dcb98c339fee964c4db87bf4c2cbe18','Admin 3','User','','2023-08-22',10,'',0,'2','Test','Test'),(15,'admin4@example.com','pbkdf2:sha256:600000$W4iHU4F0OzwALBx9$6be25296b2a2bba04f4a955d113bcea5e9183078ffd96bb6d511ae3fe8867416','Admin 4','User','','',10,'',0,'2','',''),(16,'admin5@example.com','pbkdf2:sha256:600000$c5IVNtghhgwsLguZ$a577857756dc2bed432b6226610190635c8598a693c9283dc5c1ed6d69f0c54f','Admin 5','User','','',10,'',0,'2','',''),(17,'hr1@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','HR 1','User','','',10,'',1,'3','',''),(18,'hr2@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','HR 2','User','','',10,'',1,'3','',''),(19,'hr3@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','HR 3','User','','',10,'',1,'3','',''),(20,'hr4@example.com','pbkdf2:sha256:600000$ClfHpXlhVmTQfd1O$f617bfde3737c9a84f4ce91ee1c04ada9830c8dc3fedc76bb98238f21c368fdd','HR 4','User','','',10,'',0,'3','',''),(22,'manager1@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','Manager 1','User','','',10,'',1,'4','',''),(23,'manager2@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','Manager 2','User','','',10,'',1,'4','',''),(24,'manager3@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','Manager 3','User','','',10,'',1,'4','',''),(25,'manager4@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','Manager 4','User','','',10,'',1,'4','',''),(26,'manager5@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','Manager 5','User','','',10,'0',1,'4','',''),(27,'user1@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 13','User 13','','2023-08-21',10,'',1,'5','Test','Test'),(28,'user2@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 2','User','','',10,'26',1,'5','',''),(29,'user3@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 3','User','','',10,'26',1,'5','',''),(30,'user4@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 4','User','','',10,'26',1,'5','',''),(31,'user5@example.com','pbkdf2:sha256:600000$2BckqZCjbCFQESy6$0d6ec3e9125973ef1bf4b1182e3a468f5a1a9e53168bfd07c4bdfc627496063c','User 5','User','','',10,'26',0,'5','',''),(32,'admin32@example.com','pbkdf2:sha256:600000$zimRSNevDj63GmIi$3796f90ec049d727d82fcc142c1f5cca03e455ba64546e3d3464935fdb2ef23d','Admin 1','User','','1981-05-19',9,'',0,'2','Tech','Admin Title1'),(33,'admin33@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','Admin 2','User','','1980-03-18',9,'',1,'2','Sales','Admin Title'),(34,'hr34@example.com','pbkdf2:sha256:600000$dIcReJZJfgSnCWDv$9557200ebdeae1fb147852ae0fc6103299e0bcd77441cc3c84e263de97c302d1','HR 1','User','','1986-05-25',9,'',0,'3','Tech','HR Title'),(35,'hr35@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','HR 2','User','','1988-07-23',9,'',1,'3','Tech','HR Title'),(36,'manager36@example.com','pbkdf2:sha256:600000$JLtxKwep3HVbdeTc$b7f112278b62f0c46292a98b0f6271bc686cd2c0ddf5c3f540430d5a945ffeb3','Manager 1','User','','1988-05-11',9,'',0,'4','Tech','Manager Title'),(37,'manager37@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','Manager 2','User','','1980-04-29',9,'',1,'4','Tech','Manager Title'),(38,'manager38@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','Manager 3','User','','1989-01-18',9,'',1,'4','Sales','Manager Title'),(39,'user39@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 1','User','','1983-03-21',9,'38',1,'5','Sales','User Title'),(40,'user40@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 2','User','','1989-09-11',9,'38',1,'5','Tech','User Title'),(41,'user41@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 3','User','','1986-06-29',9,'36',1,'5','Sales','User Title'),(42,'user42@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 4','User','','1987-04-14',9,'38',1,'5','Sales','User Title'),(43,'user43@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 5','User','','1985-07-17',9,'38',1,'5','Sales','User Title'),(44,'user44@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 6','User','','1985-05-15',9,'37',1,'5','Sales','User Title'),(45,'user45@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 7','User','','1985-07-28',9,'37',1,'5','Tech','User Title'),(46,'user46@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 8','User','','1985-01-13',9,'38',1,'5','Sales','User Title'),(47,'user47@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 9','User','','1982-01-14',9,'38',1,'5','Tech','User Title'),(48,'user48@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 10','User','','1989-08-25',9,'37',1,'5','Sales','User Title'),(49,'user49@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 11','User','','1987-02-25',9,'37',1,'5','Sales','User Title'),(50,'user50@example.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','User 12','User','','1989-06-14',9,'37',1,'5','Tech','User Title'),(51,'user51@example.com','pbkdf2:sha256:600000$brRkQj5MuWJJ3Lvc$6e81927d479ab9586c1e14503ee79a57348e4ca8b003a36eb2ca7e9131859661','User 13','User','user51example.com-51.jpg','1981-02-10',9,'36',0,'5','Sales','User Title');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-29 11:52:10
