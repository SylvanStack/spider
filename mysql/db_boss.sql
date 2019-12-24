SHOW DATABASES ; -- 显示数据库

DROP DATABASE IF EXISTS  db_boss;
CREATE DATABASE db_boss;# 创建数据库

SHOW TABLES FROM db_boss; # 查看数据库中的表

CREATE TABLE db_boss.job_info
(
    id           INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT '自增主键',
    title        VARCHAR(255) COMMENT '工作名称',
    company      VARCHAR(255) COMMENT '招聘公司',
    salary       VARCHAR(255) COMMENT '工资',
    url          VARCHAR(500) COMMENT '工作详细链接',
    work_addr    VARCHAR(255) COMMENT '工作地点',
    industry     VARCHAR(255) COMMENT '行业',
    company_size VARCHAR(255) COMMENT '公司规模',
    recruiter    VARCHAR(255) COMMENT '招聘人',
    publish_date VARCHAR(255) COMMENT '发布时间'
);

select * from db_boss.job_info;

# alter table db_school.student
#   add constraint
#     student_fk_departmentId
#     foreign key (departmentId)
#       references db_school.department (id)