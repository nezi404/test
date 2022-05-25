DROP TABLE IF EXISTS entradas;
create table entradas(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo STRING NOT NULL,
    texto STRING NOT NULL,
    criado_em DATETIME DEFAULT NOW
    )