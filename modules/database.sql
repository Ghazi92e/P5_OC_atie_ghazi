

CREATE TABLE IF NOT EXISTS `Category`(
  `id`   INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(50) NOT NULL,
  PRIMARY KEY(`id`))
  ENGINE = InnoDB DEFAULT CHARACTER
  SET = utf8;

CREATE TABLE IF NOT EXISTS `User`(
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY(`id`)
);
CREATE TABLE IF NOT EXISTS `Product`(
  `id`   INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(200) NOT NULL,
  `barcode` BIGINT NOT NULL,
  `nutriscore` VARCHAR(1) NOT NULL,
  `link` VARCHAR(200) NOT NULL,
  `stores` VARCHAR(150) NOT NULL,
  `category_id` INT,
  PRIMARY KEY(`id`),
  CONSTRAINT fk_category_product_id
  FOREIGN KEY (`category_id`)
  REFERENCES Category(id)
);
CREATE TABLE IF NOT EXISTS `Subproduct`(
    `subproduct_id` INT NOT NULL,
    `product_id` INT NOT NULL,
    `user_id` INT NOT NULL,
    CONSTRAINT fk_prod_id
    FOREIGN KEY (`product_id`)
    REFERENCES Product(id),
    CONSTRAINT fk_sub_product_id
    FOREIGN KEY (`subproduct_id`)
    REFERENCES Product(id),
    CONSTRAINT fk_user_id
    FOREIGN KEY (`user_id`)
    REFERENCES User(id)
)
ENGINE = InnoDB;