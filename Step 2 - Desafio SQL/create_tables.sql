-- MySQL Script generated by MySQL Workbench
-- Mon Feb 26 19:20:08 2024

CREATE SCHEMA IF NOT EXISTS MercadoLivre;

-- -----------------------------------------------------
-- Table MercadoLivre.clientes
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS MercadoLivre.clientes (
  id_cliente INT NOT NULL ,
  nome_cliente VARCHAR(30) NULL,
  sobrenome_cliente VARCHAR(45) NULL,
  sexo_cliente VARCHAR(3) NULL,
  endereco_cliente VARCHAR(45) NULL,
  data_nasc DATE NULL,
  telefone_cliente VARCHAR(13) NULL,
  email_cliente VARCHAR(45) NULL,
  PRIMARY KEY (id_cliente));

-- -----------------------------------------------------
-- Table MercadoLivre.pedido
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS MercadoLivre.pedido (
  id_pedido INT NOT NULL,
  id_cliente INT NULL,
  id_produto INT NULL,
  qtd_itens INT NULL,
  data_pedido DATE NULL,
  status_pedido VARCHAR(20) NULL,
  valor_total DECIMAL NULL,
  PRIMARY KEY (id_pedido));



-- -----------------------------------------------------
-- Table MercadoLivre.categorias
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS MercadoLivre.categorias (
  id_categoria INT NOT NULL,
  titulo_categoria VARCHAR(45) NULL,
  descricao_categoria VARCHAR(100) NULL,
  id_ref_categoria INT NULL,
  PRIMARY KEY (id_categoria));


-- -----------------------------------------------------
-- Table MercadoLivre.produto
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS MercadoLivre.produto (
  id_produto INT NOT NULL,
  id_categoria INT NULL,
  id_cliente INT NULL,
  titulo_produto VARCHAR(45) NULL,
  descricao_produto VARCHAR(45) NULL,
  preco_produto DECIMAL NULL,
  data_cancelamento DATE NULL,
  PRIMARY KEY (id_produto));

