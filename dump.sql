PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE company (
	id INTEGER NOT NULL, 
	name VARCHAR(64) NOT NULL, 
	description VARCHAR(128), 
	size INTEGER, 
	PRIMARY KEY (id)
);
INSERT INTO company VALUES(1,'TechPros','Leading provider of innovative tech solutions',1200);
INSERT INTO company VALUES(2,'BioHealth','BioHealth is at the forefront of medical biotechnology',750);
INSERT INTO company VALUES(3,'EcoBuild','Eco-friendly construction and architectural solutions',890);
INSERT INTO company VALUES(4,'FinTrust','A trustworthy partner for all your financial needs',1450);
INSERT INTO company VALUES(5,'FoodJoy','Delivering joy through quality food products',670);
INSERT INTO company VALUES(6,'FitLife','Promoting healthier lifestyles through high-quality fitness equipment',920);
INSERT INTO company VALUES(7,'AutoRapid','Providing rapid solutions in the automobile industry',1100);
INSERT INTO company VALUES(8,'StyleSphere','Your ultimate destination for fashion and lifestyle products',980);
INSERT INTO company VALUES(9,'EduBright','A platform to enlighten young minds with quality education',1230);
INSERT INTO company VALUES(10,'GreenPower','Contributing to a greener future with renewable energy solutions',1420);
CREATE TABLE results (
	id INTEGER NOT NULL, 
	"testDate" DATE NOT NULL, 
	"scoreA" INTEGER NOT NULL, 
	"scoreB" INTEGER NOT NULL, 
	"scoreC" INTEGER NOT NULL, 
	user_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES user (id)
);
INSERT INTO results VALUES(2,'2023-07-14',32,23,35,11);
INSERT INTO results VALUES(3,'2023-06-14',14,23,17,11);
INSERT INTO results VALUES(4,'2023-05-14',23,39,12,11);
INSERT INTO results VALUES(5,'2023-04-14',41,39,27,11);
INSERT INTO results VALUES(6,'2023-03-14',17,33,21,11);
INSERT INTO results VALUES(7,'2023-02-14',42,39,41,11);
INSERT INTO results VALUES(8,'2023-01-14',16,4,7,11);
INSERT INTO results VALUES(9,'2022-12-14',30,3,33,11);
INSERT INTO results VALUES(10,'2022-11-14',25,32,23,11);
INSERT INTO results VALUES(11,'2022-10-14',12,1,29,11);
INSERT INTO results VALUES(12,'2022-09-14',0,3,40,11);
INSERT INTO results VALUES(13,'2022-08-14',21,35,25,11);
INSERT INTO results VALUES(14,'2022-07-14',1,6,20,11);
INSERT INTO results VALUES(15,'2023-08-17',42,42,0,11);
CREATE TABLE role (
    id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);
CREATE TABLE IF NOT EXISTS "user" (
    id INTEGER NOT NULL PRIMARY KEY,
    email VARCHAR(120),
    password_hash VARCHAR(128),
    firstname VARCHAR(64) NOT NULL,
    lastname VARCHAR(64) NOT NULL,
    image VARCHAR(128),
    date_of_birth VARCHAR(64),
    companyId INTEGER,
    manager_id INTEGER,
    first_login BOOLEAN DEFAULT TRUE,
    role_id INTEGER,
    FOREIGN KEY(companyId) REFERENCES company (id),
    FOREIGN KEY(manager_id) REFERENCES user (id),
    FOREIGN KEY(role_id) REFERENCES role (id)
);
INSERT INTO user VALUES(1,'harsh.gupta@test.com','pbkdf2:sha256:600000$BB0QUr4jP0nhlVyW$abb1320700b803887783938aac710a9bd5ce6af4891aaa7128f27f62ff4b7570','Harsh','Gupta',NULL,'1999-10-28 00:00:00',2,3,1,NULL);
INSERT INTO user VALUES(2,'kartik.khosa@test.com','pbkdf2:sha256:600000$utVHRGDIOKgfn4Fq$093046141d5aaab665df8b3c62d04f14f737a556ede07c12ff15f294ba75170d','Kartik','Khosa',NULL,'1999-05-20 00:00:00',2,4,1,NULL);
INSERT INTO user VALUES(3,'joh.doe@gmail.com','pbkdf2:sha256:600000$9z09z0S5A85Eibe4$4d9e7d6e480484ac8955d2130c5c6302574a56b046d431ece7cbead8b2b671f1','John','Doe',NULL,'1995-12-12 00:00:00',2,6,1,NULL);
INSERT INTO user VALUES(4,'jane.austen@yahoo.com','pbkdf2:sha256:600000$h2jz4a9YJCztr5Pl$b72824e762277f47014432727bafcbe25b942c7a740104d098f1bec4d2c11065','Jane','Austen',NULL,'1990-10-02 00:00:00',2,5,1,NULL);
INSERT INTO user VALUES(5,'leo.messi@outlook.com','pbkdf2:sha256:600000$YFk0EDRjnnH48nvi$043cccd1c18a7cfac0503f1d35c51ed03e746a75d2e96a27f149b2c3af9cf869','Lionel','Messi',NULL,'1985-07-22',2,0,0,NULL);
INSERT INTO user VALUES(6,'rafael.nadal@gmail.com','pbkdf2:sha256:600000$pMXSvtxmaM8Lpedz$20be72896bb332ecb98509a5064c49338c85a12d25ac62d3ed9797f3b987c8f5','Rafael','Nadal',NULL,'1980-01-05 00:00:00',2,2,1,NULL);
INSERT INTO user VALUES(7,'lewis.goat@test.com','pbkdf2:sha256:600000$y2uCeTgHKSwhi0vP$2c91fc65096c3fc88217a771d4e72f571b6ce0ad6dc94c1d023b43246839dc20','Lewis','Hamilton',NULL,'1980-04-04 00:00:00',2,9,1,NULL);
INSERT INTO user VALUES(8,'sergio.perez@mexico.com','pbkdf2:sha256:600000$6aN30tVdMHleQHgs$a2e74320787706ffc8ce3d1cab37dffb7a7736dacaf110007562cf0e1968f9ad','Sergio','Perez',NULL,'1980-02-03 00:00:00',2,1,1,NULL);
INSERT INTO user VALUES(9,'taylor.swift@test.com','pbkdf2:sha256:600000$QZZ6Kn9uJOeVxDuO$24b531926ac6fb36e973f7cd88fd1a10ea0513f6bdffa33dd55a122f28288347','Taylor','Swift',NULL,'1990-05-05 00:00:00',2,2,1,NULL);
INSERT INTO user VALUES(10,'selenagomez123@test.com','pbkdf2:sha256:600000$DTAO4f4yXYYCpvFq$3a97b4b125233f76d54e0377b81e93138163c8f4ac4028a8016bd6322fb1f05d','Selena','Gomez',NULL,'1990-06-18 00:00:00',2,1,1,NULL);
INSERT INTO user VALUES(11,'test@gmail.com','pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f','Kartik','Khosa','testgmail.com-11.jpg','1998-08-25',1,0,0,NULL);
COMMIT;



