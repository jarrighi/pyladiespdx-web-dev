CREATE TABLE locations (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  address VARCHAR(50),
  capacity INT
);

CREATE TABLE events (
  id INT PRIMARY KEY,
  title VARCHAR(50),
  description TEXT,
  time TIMESTAMP,
  location INT references locations(id)
);

CREATE TABLE people (
  id INT PRIMARY KEY,
  firstname VARCHAR(50),
  lastname VARCHAR(50),
  email VARCHAR(50)
);

CREATE TABLE rsvps (
event INT references events(id),
person INT references people(id)
);