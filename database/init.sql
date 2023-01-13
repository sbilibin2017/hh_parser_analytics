CREATE SCHEMA IF NOT EXISTS content;

SET search_path TO content,public;

CREATE TABLE vacancies(
    id integer PRIMARY KEY,
    url TEXT,
    name VARCHAR(256),
    area_name VARCHAR(256),
    published_at TIMESTAMP WITH TIME ZONE,
    employer_name VARCHAR(256),
    schedule_name VARCHAR(256),
    salary_from VARCHAR(256),
    salary_to VARCHAR(256),
    requirement TEXT,
    responsibility TEXT
);

