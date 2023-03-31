import mysql.connector

class User:
    def __init__(self, name, id, phone, email, password, gender, avatar, status):
        # 将属性初始化为参数
        self.name = name;
        self.id = id;
        self.phone = phone;
        self.email = email;
        self.password = password;
        self.gender = gender;
        self.avatar = avatar;
        self.status = status;


    # 生成getter和setter方法
    def get_name(self):
        return self.name;

    def set_name(self, name):
        self.name = name;

    def get_id(self):
        return self.id;

    def set_id(self, id):
        self.id = id;

    def get_phone(self):
        return self.phone;

    def set_phone(self, phone):
        self.phone = phone;

    def get_email(self):
        return self.email;

    def set_email(self, email):
        self.email = email;

    def get_password(self):
        return self.password;

    def set_password(self, password):
        self.password = password;

    def get_gender(self):
        return self.gender;

    def set_gender(self,gender):
        self.gender = gender;

    def get_avatar(self):
        return self.avatar;

    def set_avatar(self, avatar):
        self.avatar = avatar;

    def get_status(self):
        return self.status;

    def set_status(self, status):
        self.status = status;


class Message:
    def __init__(self, content, sender, receiver, timestamp):
        #初始化属性
        self.content = content;
        self.sender = sender;
        self.receiver = receiver;
        self.timestamp = timestamp;

    # 生成getter和setter方法
    def get_content(self):
        return self.content;

    def set_content(self, content):
        self.content = content;

    def get_sender(self):
        return self.sender;

    def set_sender(self, sender):
        self.sender = sender;

    def get_receiver(self):
        return self.receiver;

    def set_receiver(self, receiver):
        self.receiver = receiver;

    def get_timestamp(self):
        return self.timestamp;

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp;



class StudyRecord:
    def __init__(self, student_id, course_id, status, study_time):
        #初始化属性
        self.student_id = student_id;
        self.course_id = course_id;
        self.status = status;
        self.study_time = study_time;

    # 生成getter和setter方法
    def get_student_id(self):
        return self.student_id;

    def set_student_id(self, student_id):
        self.student_id = student_id;

    def get_course_id(self):
        return self.course_id;

    def set_course_id(self, course_id):
        self.course_id = course_id;

    def get_status(self):
        return self.status;

    def set_status(self, status):
        self.status = status;

    def get_study_time(self):
        return self.study_time;

    def set_study_time(self, study_time):
        self.study_time = study_time;



class Material:
    def __init__(self, name, description, uploader, upload_time, file_content):
        #初始化属性
        self.name = name;
        self.description = description;
        self.uploader = uploader;
        self.upload_time = upload_time;
        self.file_content = file_content;



    # 生成getter和setter方法
    def get_name(self):
        return self.name;

    def set_name(self, name):
        self.name = name;

    def get_description(self):
        return self.description;

    def set_description(self, description):
        self.description = description;

    def get_uploader(self):
        return self.uploader;

    def set_uploader(self, uploader):
        self.uploader = uploader;

    def get_upload_time(self):
        return self.upload_time;

    def set_upload_time(self, upload_time):
        self.upload_time = upload_time;

    def get_file_content(self):
        return self.file_content;

    def set_file_content(self, file_content):
        self.file_content = file_content;



class Database:
    def __init__(self):
        # 存入本地文件
        self.file = open("database.txt", "w+")

    # 文件的操作 (create, insert, query, update, delete)
    def create(self, table_name, table_content):
        self.file.write(table_name)
        self.file.write(table_content)

    def insert(self, table_name, table_content):
        self.file.write(table_name)
        self.file.write(table_content)

    def query(self, table_name, table_content):
        self.file.write(table_name)
        self.file.write(table_content)

    def update(self, table_name, table_content):
        self.file.write(table_name)
        self.file.write(table_content)

    def delete(self, table_name, table_content):
        self.file.write(table_name)
        self.file.write(table_content)
