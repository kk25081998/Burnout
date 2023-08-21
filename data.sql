BEGIN;

DROP TABLE IF EXISTS results CASCADE;
DROP TABLE IF EXISTS "user" CASCADE;
DROP TABLE IF EXISTS role CASCADE;
DROP TABLE IF EXISTS company CASCADE;

CREATE TABLE company (
	id SERIAL PRIMARY KEY, 
	name VARCHAR(64) NOT NULL, 
	description VARCHAR(128), 
	size INTEGER
);

INSERT INTO company (id, name, description, size) VALUES
(1,'TechPros','Leading provider of innovative tech solutions',1200),
(2,'BioHealth','BioHealth is at the forefront of medical biotechnology',750),
(3,'EcoBuild','Eco-friendly construction and architectural solutions',890),
(4,'FinTrust','A trustworthy partner for all your financial needs',1450),
(5,'FoodJoy','Delivering joy through quality food products',670),
(6,'FitLife','Promoting healthier lifestyles through high-quality fitness equipment',920),
(7,'AutoRapid','Providing rapid solutions in the automobile industry',1100),
(8,'StyleSphere','Your ultimate destination for fashion and lifestyle products',980),
(9,'EduBright','A platform to enlighten young minds with quality education',1230),
(10,'GreenPower','Contributing to a greener future with renewable energy solutions',1420);

CREATE TABLE role (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    email VARCHAR(120),
    password_hash VARCHAR(128),
    firstname VARCHAR(64) NOT NULL,
    lastname VARCHAR(64) NOT NULL,
    image VARCHAR(128),
    date_of_birth DATE,
    companyId INTEGER REFERENCES company (id),
    manager_id INTEGER REFERENCES "user" (id),
    first_login BOOLEAN DEFAULT TRUE,
    role_id INTEGER REFERENCES role (id)
);

INSERT INTO "user" (id, email, password_hash, firstname, lastname, image, date_of_birth, companyId, manager_id, first_login, role_id) VALUES
(1,'harsh.gupta@test.com','pbkdf2:sha256:600000$BB0QUr4jP0nhlVyW$abb1320700b803887783938aac710a9bd5ce6af4891aaa7128f27f62ff4b7570','Harsh','Gupta',NULL,'1999-10-28',2,3,TRUE,NULL),
(2,'kartik.khosa@test.com','pbkdf2:sha256:600000$utVHRGDIOKgfn4Fq$093046141d5aaab665df8b3c62d04f14f737a556ede07c12ff15f294ba75170d','Kartik','Khosa',NULL,'1999-05-20',2,4,TRUE,NULL),
(3,'joh.doe@gmail.com','pbkdf2:sha256:600000$9z09z0S5A85Eibe4$4d9e7d6e480484ac8955d2130c5c6302574a56b046d431ece7cbead8b2b671f1','John','Doe',NULL,'1995-12-12',2,6,TRUE,NULL),
(4,'jane.austen@yahoo.com','pbkdf2:sha256:600000$h2jz4a9YJCztr5Pl$b72824e762277f47014432727bafcbe25b942c7a740104d098f1bec4d2c11065','Jane','Austen',NULL,'1990-10-02',2,5,TRUE,NULL),
(5,'leo.messi@outlook.com','pbkdf2:sha256:600000$YFk0EDRjnnH48nvi$043cccd1c18a7cfac0503f1d35c51ed03e746a75d2e96a27f149b2c3af9cf869','Lionel','Messi',NULL,'1985-07-22',2,NULL,TRUE,NULL),
(6,'rafael.nadal@gmail.com','pbkdf2:sha256:600000$pMXSvtxmaM8Lpedz$20be72896bb332ecb98509a5064c49338c85a12d25ac62d3ed9797f3b987c8f5','Rafael','Nadal',NULL,'1980-01-05',2,2,TRUE,NULL),
(7,'lewis.goat@test.com','pbkdf2:sha256:600000$y2uCeTgHKSwhi0vP$2c91fc65096c3fc88217a771d4e72f571b6ce0ad6dc94c1d023b43246839dc20','Lewis','Hamilton',NULL,'1980-04-04',2,9,TRUE,NULL),
(8,'sergio.perez@mexico.com','pbkdf2:sha256:600000$NLKjzZmTr5vnTFS8$57e0d853759d4ab07bb8083b65bb3d378cf232f442bd66cc362e81665bbd0ea5','Sergio','Perez',NULL,'1995-03-12',2,8,TRUE,NULL),
(9,'freddy.mercury@test.com','pbkdf2:sha256:600000$CqO12X8e8mOihpET$4f5a8e06559516a7ecf1f65dbec3785b135ad116f79ad51aa2b7705952875c5b','Freddie','Mercury',NULL,'1960-02-05',2,10,TRUE,NULL),
(10,'lady.gaga@pop.com','pbkdf2:sha256:600000$X57qzZiTr5vnTqP8$5e0d853759d5ab07bb8083b65bb3d378cf232f442bd66cc362e81665bbd0er9d','Lady','Gaga',NULL,'1985-11-25',2,1,TRUE,NULL);

CREATE TABLE results (
	id SERIAL PRIMARY KEY, 
	"testDate" DATE NOT NULL, 
	"scoreA" INTEGER NOT NULL, 
	"scoreB" INTEGER NOT NULL, 
	"scoreC" INTEGER NOT NULL, 
	user_id INTEGER REFERENCES "user" (id)
);

INSERT INTO results (id, "testDate", "scoreA", "scoreB", "scoreC", user_id) VALUES
(2,'2023-07-14',32,23,35,1),
(3,'2023-06-19',28,21,31,2),
(4,'2023-07-11',33,28,36,3),
(5,'2023-07-15',34,30,38,4),
(6,'2023-06-22',35,27,37,5),
(7,'2023-06-29',32,23,33,6),
(8,'2023-07-01',31,22,32,7),
(9,'2023-07-08',36,29,40,8),
(10,'2023-07-03',37,31,39,9),
(11,'2023-06-30',33,27,37,10);

COMMIT;


INSERT INTO "user" VALUES(
    11,                                -- ID
    'test@gmail.com',                  -- Email
    'pbkdf2:sha256:600000$LiIiJi5YaNTb1TrJ$50f9d06e88d476d7c74c2767a2ac6650a9140f24233bbe73a0c17659210b841f', -- Password Hash
    'Kartik',                          -- First Name
    'Khosa',                           -- Last Name
    'testgmail.com-11.jpg',            -- Image
    '1998-08-25',                      -- Date of Birth
    1,                                 -- companyId
    2,                                 -- manager_id
    False,                                 -- first_login
    NULL                               -- role_id
);
