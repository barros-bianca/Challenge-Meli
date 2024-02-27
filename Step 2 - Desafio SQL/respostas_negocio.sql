-- 1. Listar los usuarios que cumplan años el día de hoy cuya cantidad de ventas realizadas en enero 2020 sea superior a 1500.

SELECT c.nome_cliente, c.sobrenome_cliente
FROM MercadoLivre.clientes c
JOIN MercadoLivre.pedido p ON c.id_cliente = p.id_cliente
WHERE DAY(c.data_nasc) = DAY(CURRENT_DATE()) AND MONTH(c.data_nasc) = MONTH(CURRENT_DATE())
AND YEAR(p.data_pedido) = 2020 AND MONTH(p.data_pedido) = 1
GROUP BY c.nome_cliente, c.sobrenome_cliente 
HAVING COUNT(p.id_pedido) > 1500;

--2. Por cada mes del 2020, se solicita el top 5 de usuarios que más vendieron($) en la categoría Celulares. Se requiere el mes y año de análisis, nombre y apellido del vendedor, cantidad de ventas realizadas, cantidad de productos vendidos y el monto total transaccionado.
SELECT YEAR(p.data_pedido) AS ano, MONTH(p.data_pedido) AS mes,
       c.nome_cliente, c.sobrenome_cliente,
       COUNT(p.id_pedido) AS quantidade_vendas,
       SUM(pro.preco_produto) AS valor_total_vendas
FROM MercadoLivre.pedido p
JOIN MercadoLivre.clientes c ON p.id_cliente = c.id_cliente
JOIN MercadoLivre.produto pro ON p.id_produto = pro.id_produto
JOIN MercadoLivre.categorias cat ON pro.id_categoria = cat.id_categoria
WHERE YEAR(p.data_pedido) = 2020 AND cat.titulo_categoria = 'Celulares'
GROUP BY YEAR(p.data_pedido), MONTH(p.data_pedido), c.nome_cliente, c.sobrenome_cliente
ORDER BY YEAR(p.data_pedido), MONTH(p.data_pedido), valor_total_vendas DESC
LIMIT 5;

--3. Se solicita poblar una nueva tabla con el precio y estado de los Ítems a fin del día. Tener en cuenta que debe ser reprocesable. Vale resaltar que en la tabla Item, vamos a tener únicamente el último estado informado por la PK definida. (Se puede resolver a través de StoredProcedure)
-- Criar a tabela ItemStatusDiario
CREATE TABLE IF NOT EXISTS MercadoLivre.ItemStatusDiario (
  id_item INT NOT NULL,
  id_pedido INT NOT NULL,
  id_produto INT NOT NULL,
  preco DECIMAL(10, 2) NULL,
  status VARCHAR(20) NULL,
  data_registro DATE NOT NULL,
  PRIMARY KEY (id_item)
);

-- Criar a Stored Procedure para preencher a tabela
DELIMITER //
CREATE PROCEDURE PreencherItemStatusDiario()
BEGIN
  INSERT INTO MercadoLivre.ItemStatusDiario (id_pedido, id_produto, preco, status, data_registro)
  SELECT p.id_pedido, p.id_produto, pro.preco_produto, p.status_pedido, CURDATE() AS data_registro
  FROM MercadoLivre.pedido p
  JOIN MercadoLivre.produto pro ON p.id_produto = pro.id_produto;
END//
DELIMITER ;

-- Chamar a Stored Procedure para preencher a tabela
CALL PreencherItemStatusDiario();