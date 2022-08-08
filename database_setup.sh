#! /bin/bash


PGPASSWORD="K0becab0" psql -U "postgres" -h "127.0.0.1" -d "azure" -c "
CREATE TABLE PLATFORM(
PlatformID SERIAL PRIMARY KEY,
PlatformName VARCHAR(30),
HyperlinkPath VARCHAR(150),
Active BOOLEAN DEFAULT TRUE
);

CREATE TABLE COURSE(
CourseId SERIAL PRIMARY KEY, 
CourseName VARCHAR(30),
PlatformID integer REFERENCES PLATFORM,
Duration TIME,
CreationDate DATE DEFAULT CURRENT_DATE,
Active BOOLEAN DEFAULT TRUE
);

CREATE TABLE USERS(
UserID SERIAL PRIMARY KEY,
EmployerNumber INT,
CreationDate DATE DEFAULT CURRENT_DATE,
Username VARCHAR(30),
Password VARCHAR(30),
Level INT,
Active BOOLEAN DEFAULT TRUE
);

CREATE TABLE CERTID(
CertificationID SERIAL PRIMARY KEY,
UserID integer REFERENCES USERS NOT NULL,
CourseID integer REFERENCES COURSE NOT NULL,
CompletionDuration TIME ,
CompletionDate DATE DEFAULT CURRENT_DATE,
Active BOOLEAN DEFAULT TRUE
);


CREATE TABLE REVIEW(
UserID integer REFERENCES USERS NOT NULL,
CourseID integer REFERENCES COURSE NOT NULL,
Feedback VARCHAR(255),
LikeDislike BOOLEAN,
RankingScore INT CHECK (RankingScore > 0 AND RankingScore < 6),
Active BOOLEAN DEFAULT TRUE
);

CREATE TABLE ONGTRAIN(
TrainingID SERIAL PRIMARY KEY,
UserID integer REFERENCES USERS NOT NULL,
CourseID integer REFERENCES COURSE NOT NULL,
Status VARCHAR(30),
CompletionPercentage INT,
StartDate DATE DEFAULT CURRENT_DATE,
FinishDate DATE DEFAULT CURRENT_DATE,
LastUpdated DATE DEFAULT CURRENT_DATE,
Active BOOLEAN DEFAULT TRUE
);

CREATE TABLE PHOTO(
CourseID integer REFERENCES COURSE,
PlatformID integer REFERENCES PLATFORM,
ImageObject BYTEA,
Active BOOLEAN DEFAULT TRUE
);

CREATE TABLE TAGS(
TagID SERIAL PRIMARY KEY,
TName VARCHAR(30),
Active BOOLEAN DEFAULT TRUE
);


CREATE TABLE TAGCOURSE(
TagID integer REFERENCES TAGS,
CourseID integer REFERENCES COURSE,
Active BOOLEAN DEFAULT TRUE
);
"

python -c 'import azure; azure.generate_all()'


exit
