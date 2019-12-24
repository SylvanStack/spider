SHOW DATABASES; -- 显示数据库


DROP DATABASE IF EXISTS db_yanxuan;
CREATE DATABASE db_yanxuan;# 创建数据库

SHOW TABLES FROM db_yanxuan; # 查看数据库中的表

drop table if exists db_yanxuan.category;
CREATE TABLE db_yanxuan.category
(
    id              INT(11)                     NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '自增主键',
    superCategoryId VARCHAR(255)                NULL COMMENT '父级目录Id',
    name            VARCHAR(255) COMMENT '目录名称',
    category_url    VARCHAR(255) COMMENT '标签链接',
    groupId         VARCHAR(255) COMMENT '分组Id' null,
    level           VARCHAR(500) COMMENT '排序层次',
    showIndex       VARCHAR(255) COMMENT '显示索引',
    iconUrl         VARCHAR(255) COMMENT '图标url',
    frontNameIcon   VARCHAR(255) COMMENT '字体名称图片',
    frontName       VARCHAR(255) COMMENT '名字',
    frontDesc       VARCHAR(255) COMMENT '描述',
    bannerUrl       VARCHAR(255) COMMENT '广告链接',
    createTime      TIMESTAMP COMMENT '数据创建时间'     default now(),
    updateTime      TIMESTAMP COMMENT '数据最后一次更新时间' default now()
);

truncate table db_yanxuan.category;

select *
from db_yanxuan.category;



# alter table db_school.student
#   add constraint
#     student_fk_departmentId
#     foreign key (departmentId)
#       references db_school.department (id)