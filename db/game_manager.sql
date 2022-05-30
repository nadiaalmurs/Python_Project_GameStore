PRAGMA FOREIGN_KEYS = ON;

DROP TABLE IF EXISTS games;
DROP TABLE IF EXISTS developers;

CREATE TABLE developers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    shipping_price INT,
    shipping_time INT
);

CREATE TABLE games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR,
    genre VARCHAR,
    description TEXT,
    stock_quantity INTEGER,
    buying_price INTEGER,
    selling_price INTEGER,
    mark_up INTEGER,
    developer_id INTEGER NOT NULL,
        FOREIGN KEY (developer_id)
            REFERENCES developers(id)
);