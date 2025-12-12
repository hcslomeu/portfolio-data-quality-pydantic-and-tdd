CREATE TABLE products_bronze (
    id_prod SERIAL PRIMARY KEY,
    name_prod VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    price FLOAT NOT NULL,
    category VARCHAR(255) NOT NULL,
);