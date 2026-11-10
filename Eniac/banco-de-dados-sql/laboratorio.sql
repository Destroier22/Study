-- Execute uma vez em um esquema novo de treinamento.
CREATE DATABASE study_sql CHARACTER SET utf8mb4;
USE study_sql;

CREATE TABLE cliente (
    id INT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    email VARCHAR(120) UNIQUE,
    ativo BOOLEAN NOT NULL
);

CREATE TABLE produto (
    id INT PRIMARY KEY,
    nome VARCHAR(80) NOT NULL,
    preco DECIMAL(10,2) NOT NULL CHECK (preco >= 0),
    estoque INT NOT NULL CHECK (estoque >= 0)
);

CREATE TABLE pedido (
    id INT PRIMARY KEY,
    cliente_id INT NOT NULL,
    data_pedido DATE NOT NULL,
    status VARCHAR(20) NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES cliente(id)
);

CREATE TABLE item_pedido (
    pedido_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT NOT NULL CHECK (quantidade > 0),
    preco_unitario DECIMAL(10,2) NOT NULL CHECK (preco_unitario >= 0),
    PRIMARY KEY (pedido_id, produto_id),
    FOREIGN KEY (pedido_id) REFERENCES pedido(id),
    FOREIGN KEY (produto_id) REFERENCES produto(id)
);

INSERT INTO cliente VALUES
    (1,'Ana','ana@example.test',1),
    (2,'Bruno','bruno@example.test',1),
    (3,'Carla','carla@example.test',1),
    (4,'Dora',NULL,0);

INSERT INTO produto VALUES
    (1,'Mouse',60,20), (2,'Teclado',120,15), (3,'Cabo',25,30);

INSERT INTO pedido VALUES
    (101,1,'2026-10-01','aberto'),
    (102,1,'2026-10-03','pago'),
    (103,2,'2026-10-04','pago');

INSERT INTO item_pedido VALUES
    (101,1,1,60), (101,2,1,120), (102,1,2,60), (103,3,2,25);
