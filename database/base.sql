drop table if exists urls;
create table urls (
  id integer primary key autoincrement UNIQUE,
  url text not null UNIQUE
);