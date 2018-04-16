

USE `communitydb`;
# 清空所有数据
# 解除外键约束
SET FOREIGN_KEY_CHECKS=0;
TRUNCATE TABLE `user`;
TRUNCATE TABLE `message`;

INSERT INTO `communitydb`.`user` (`openid`, `name`, `phone`, `sex`, `grade`, `major`) VALUES ('oT3Go5VYmQsFhUco-RkCC6666667', 'Mary', '13566668888', '1', '2018', '1');
INSERT INTO `communitydb`.`user` (`openid`, `name`, `phone`, `sex`, `grade`, `major`) VALUES ('oT3Go5VYmQsFhUco-RkCC6666668', 'Tom', '13566668889', '0', '2017', '2');
INSERT INTO `communitydb`.`user` (`openid`, `name`, `phone`, `sex`, `grade`, `major`) VALUES ('oT3Go5VYmQsFhUco-RkCC6666669', 'Cat', '13566668880', '0', '2019', '3');
INSERT INTO `communitydb`.`user` (`openid`, `name`, `phone`, `sex`, `grade`, `major`) VALUES ('oT3Go5VYmQsFhUco-RkCCnFzdY5g', 'Leon', '13528824048', '0', '2020', '1');

INSERT INTO `communitydb`.`message` (`messageId`, `content`, `readed`, `sendtime`, `user_openid`) VALUES ('1', 'hello', '0', '20180413', 'oT3Go5VYmQsFhUco-RkCCnFzdY5g');
INSERT INTO `communitydb`.`message` (`messageId`, `content`, `readed`, `sendtime`, `user_openid`) VALUES ('2', 'hi', '0', '20180414', 'oT3Go5VYmQsFhUco-RkCCnFzdY5g');
INSERT INTO `communitydb`.`message` (`messageId`, `content`, `readed`, `sendtime`, `user_openid`) VALUES ('3', 'haha', '0', '20180415', 'oT3Go5VYmQsFhUco-RkCCnFzdY5g');


SET FOREIGN_KEY_CHECKS=1;