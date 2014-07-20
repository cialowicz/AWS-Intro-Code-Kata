CREATE TABLE `errors` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `date` DATE,
  `time` TIME,
  `type` VARCHAR(64),
  `task` VARCHAR(256),
  `class` VARCHAR(256),
  `message` VARCHAR(2048),
  PRIMARY KEY  (`id`)
);
