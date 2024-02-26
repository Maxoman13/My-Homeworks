"Шаг 1"
CREATE TABLE MarvelCharacters (
    page_id INTEGER,
    name TEXT,
    urlslug TEXT,
    identify TEXT,
    ALIGN TEXT,
    EYE TEXT,
    HAIR TEXT,
    SEX TEXT,
    GSM TEXT,
    ALIVE TEXT,
    APPEARANCES INTEGER,
    FIRST_APPEARANCE TEXT,
    Year INTEGER
);

"Шаг 2"

CREATE TABLE MarvelCharacters_new (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page_id INTEGER,
    name TEXT,
    urlslug TEXT,
    identify TEXT,
    ALIGN TEXT,
    EYE TEXT,
    HAIR TEXT,
    SEX TEXT,
    GSM TEXT,
    ALIVE TEXT,
    APPEARANCES INTEGER,
    FIRST_APPEARANCE TEXT,
    Year INTEGER
);

"Шаг 3"

INSERT INTO MarvelCharacters_new (page_id, name, urlslug, identify, ALIGN, EYE, HAIR, SEX, GSM, ALIVE, APPEARANCES,
FIRST_APPEARANCE, YEAR)
SELECT page_id, name, urlslug, identify, ALIGN, EYE, HAIR, SEX, GSM, ALIVE, APPEARANCES, FIRST_APPEARANCE, YEAR
FROM MarvelCharacters

DROP TABLE MarvelCharacters

"Шаг 4"

ALTER TABLE MarvelCharacters_new RENAME TO MarvelCharacters

"Шаг 5"

CREATE TABLE Sex (
    sex_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE EyeColor (
    eye_id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT UNIQUE
);

CREATE TABLE HairColor (
    hair_id INTEGER PRIMARY KEY AUTOINCREMENT,
    color TEXT UNIQUE
);

CREATE TABLE Alignment (
    align_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE
);

CREATE TABLE LivingStatus (
    status_id INTEGER PRIMARY KEY AUTOINCREMENT,
    status TEXT UNIQUE
);

CREATE TABLE Identity (
    identity_id INTEGER PRIMARY KEY AUTOINCREMENT,
    identity TEXT UNIQUE
);

"Шаг 6"

INSERT INTO Sex (name)
SELECT DISTINCT SEX FROM MarvelCharacters;

INSERT INTO EyeColor (color)
SELECT DISTINCT EYE FROM MarvelCharacters;

INSERT INTO HairColor (color)
SELECT DISTINCT HAIR FROM MarvelCharacters;

INSERT INTO Alignment (name)
SELECT DISTINCT ALIGN FROM MarvelCharacters;

INSERT INTO LivingStatus (status)
SELECT DISTINCT ALIVE FROM MarvelCharacters;

INSERT INTO Identity (identity)
SELECT DISTINCT identify FROM MarvelCharacters;

"Шаг 7"

CREATE TABLE MarvelCharacters_New (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    page_id INTEGER,
    name TEXT,
    urlslug TEXT,
    identity_id TEXT,
    align_id TEXT,
    eye_id TEXT,
    hair_id TEXT,
    sex_id TEXT,
    status_id TEXT,
    APPEARANCES INTEGER,
    FIRST_APPEARANCE TEXT,
    Year INTEGER,
    FOREIGN KEY (identify_id) REFERENCES Identity(identity_id)
    FOREIGN KEY (align_id) REFERENCES Alignment(align_id)
    FOREIGN KEY (eye_id) REFERENCES EyeColor(eye_id)
    FOREIGN KEY (hair_id) REFERENCES HairColor(hair_id)
    FOREIGN KEY (sex_id) REFERENCES Sex(sex_id)
    FOREIGN KEY (status_id) REFERENCES LivingStatus(status_id)
);

"Шаг 8"

INSERT INTO MarvelCharacters_New (page_id, name, urlslug, identity_id, align_id, eye_id, hair_id, sex_id, status_id,
APPEARANCES, FIRST_APPEARANCE, YEAR)
SELECT mc.page_id, mc.name, mc.urlslug, id.identity_id, al.align_id, ec.eye_id, hr.hair_id, sx.sex_id,
av.status_id, mc.APPEARANCES, mc.FIRST_APPEARANCE, mc.YEAR
FROM MarvelCharacters mc
JOIN Identity id ON mc.identify = id.identity or (mc.identify is Null and id.identity is Null)
JOIN Alignment al ON mc.ALIGN = al.name or (mc.ALIGN is Null and al.name is Null)
JOIN EyeColor ec ON mc.EYE = ec.color or (mc.EYE is Null and ec.color is Null)
JOIN HairColor hr ON mc.HAIR = hr.color or (mc.HAIR is Null and hr.color is Null)
JOIN Sex sx ON mc.SEX = sx.name or (mc.SEX is Null and sx.name is Null)
JOIN LivingStatus av ON mc.ALIVE = av.status or (mc.ALIVE is Null and av.status is Null)

"Шаг 9 и 10"

DROP TABLE MarvelCharacters

ALTER TABLE MarvelCharacters_New RENAME TO MarvelCharacters