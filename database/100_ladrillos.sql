CREATE TABLE `properties` (
  `property_id` INT NOT NULL AUTO_INCREMENT,
  `name` varchar(50),
  `description` varchar(200),
  `total_quantity _bricks` INT,
  `remaining_bricks` INT,
  PRIMARY KEY (`property_id`)
);

CREATE TABLE `users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `email` varchar(30),
  `password` TEXT(500),
  PRIMARY KEY (`user_id`)
);

CREATE TABLE `shopping_cart` (
  `shopping_cart_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT,
  `total` DECIMAL(25,2),
  PRIMARY KEY (`shopping_cart_id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`)
);

CREATE TABLE `bricks` (
  `brick_id` INT NOT NULL AUTO_INCREMENT,
  `property_id` INT,
  `description` varchar(250),
  PRIMARY KEY (`brick_id`),
  FOREIGN KEY (`property_id`) REFERENCES `properties`(`property_id`)
);

CREATE TABLE `order_detail` (
  `order_detail_id` INT NOT NULL AUTO_INCREMENT,
  `brick_id` INT,
  `shopping_cart_id` INT,
  PRIMARY KEY (`order_detail_id`),
  FOREIGN KEY (`shopping_cart_id`) REFERENCES `shopping_cart`(`shopping_cart_id`),
  FOREIGN KEY (`brick_id`) REFERENCES `bricks`(`property_id`)
);

CREATE TABLE `payment_methods` (
  `payment_method_id` INT NOT NULL AUTO_INCREMENT,
  `name` varchar(50),
  `description` varchar(250),
  PRIMARY KEY (`payment_method_id`)
);

CREATE TABLE `transactions` (
  `transaction_id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT,
  `payment_method_id` INT,
  `total_paid` DECIMAL(25,2),
  PRIMARY KEY (`transaction_id`),
  FOREIGN KEY (`payment_method_id`) REFERENCES `payment_methods`(`payment_method_id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`)
);
