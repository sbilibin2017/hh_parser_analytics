CREATE SCHEMA IF NOT EXISTS content;

SET search_path TO content,public;

CREATE TABLE vacancies(
    id integer PRIMARY KEY,
    url text,
    name varchar(256),
    area_name varchar(256),
    published_at timestamp with time zone,
    employer_name varchar(256),
    schedule_name varchar(256),
    salary_from varchar(256),
    salary_to varchar(256),
    requirement text,
    responsibility text
);

