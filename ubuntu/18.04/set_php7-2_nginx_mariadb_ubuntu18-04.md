/***** set server for yii2 in ubuntu 18.04 (nginx, php7.2, mariadb) ******/

1. หลังจากที่ติดตั้ง ubuntu เสร็จ
    ~~~bat
    apt install net-tools
    apt update
    apt upgrate
    ~~~
2. ติดตั้ง nginx
    ~~~bat
    apt install nginx
    ~~~
    ทดสอบ nginx โดยการเปิด browser -> localhost หรือ 127.0.0.1

    part default สำหรับแสดงผล
    ~~~bat
    /var/www/html
    ~~~
    

3. ติดตั้ง mariadb
    ~~~bat
    apt install mariadb-server
    ~~~

    ตั้งค่า password
    ~~~bat
    mysql_secure_installation

    Enter current password for root(enter for none): Enter    
    
    Change the root password? [Y/n]: Y
    
    New password: password

    Re-enter new password: password
    
    Remove anonymous user? [Y/n]: Y
    
    Disallow root login remotely? [Y/n]: Y
    
    Remove test database and access now? [Y/n]: Y
 
    Reload privilege tables now? [Y/n]: Y
    ~~~

    login to database
    ~~~bat
    mysql -u root -p
    password: password
    ~~~
    
    สร้าง database
    ~~~bat
    create database dbname;
    ~~~
    
    แสดงรายการ database และ table
    ~~~bat
    show databases;
    show tables;
    ~~~
    
    ถ้าต้องการเปลี่ยน password mariadb
    ~~~bat
    use mysql;
    UPDATE user SET plugin = ’’ WHERE user=’root’;
    FLUSH PRIVILEGES;
    exit;
    service mysqld restart
    ~~~

4. ติดตั้ง extensions เบื้องต้นสำหรับ php7.2
    ~~~bat
    apt install php7.2-fpm
    apt install php7.2-mbstring
    apt install php7.2-xml
    ~~~
    
   ในกรณีที่ ubuntu ยังไม่ได้ติดตั้ง zip และ unzip #ต้องติดตั้งเพราะจะทำให้ไม่สารมารถ composer install ได้
    ~~~bat
    apt install zip unzip
    ~~~
    
5. ติดตั้ง project
    เข้าไปยัง part ที่ใช้สำหรับแสดงผลเว็บ
    ~~~bat
    cd /var/www
    ~~~
    ใช้คำสั่ง
    ~~~bat
    git clone <url>
    
    cd <projectname>
    
    sudo php init
    ~~~
    
    ตั้งค่าเชื่อมต่อกับ database
    ~~~bat
    nano /var/www/pov-website/common/config/main-local.php
    ~~~
    
    file main-local.php
   ~~~bat
   	'class' => 'yii\db\Connection',
       		 'dsn' => 'mysql:host=127.0.0.1;dbname=pov',
       		 'username' => 'root',
       		 'password' => 'password',
       		 'charset' => 'utf8',
    ~~~
6. ตั้งค่า part ตำแหน่งที่แสดงผลเว็บ
    ~~~bat
    cd /etc/nginx/sites-enable/
    
    nano default
    ~~~
    
    file default
   ~~~bat
   	 server{
   		 listen 80 default_server;
   	     	listen [::]:80 default_server;

   		 root /var/www/pov-website;

   			 charset utf-8;
   			 client_max_body_size 128M;

   		 index index.php index.html index.htm index.nginx-debian.html;

   			 server_name localhost;

   		 location / {
           	 
           			}

   		 location ~ \.php$ {
           			 fastcgi_pass unix:/run/php/php7.2-fpm.sock;
           			 fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
           			 include fastcgi_params;
   		   		 }
   		 location ~ /\.ht {
           			 deny all;
   			 }

   	 }
    ~~~    
    
    restart nginx
    ~~~bat
    nginx -s reload
    nginx -s reopen
    ~~~
    
    ทดสอบการทำงานร่วมกับของ php กับ nginx
    ~~~bat
    cd /var/www/pov-website/
    
    nano info.php
    ~~~
    
    file info.php
    ~~~bat
   	 <?php
   		 phpinfo();	 
    ~~~


    run info.php
    เปิด browser -> localhost/info.php  หรือ ip ของ server/info.php #ถ้าเปิด info.php ได้แสดงว่าสามารถใช้งาน php ร่วมกับ nginx ได้แล้ว

7. ติดตั้ง extensions เพิ่มเติมสำหรับใช้งานกับ yii2
    เช็ค requirements ของ yii2 #ติดตั้งตาม extension ที่ยังไม่ได้ติดตั้ง
    เปิด browser -> localhost/requirements.php
    เช่น  
    ~~~bat
    apt install php7.2-intl
    apt install php7.2-sqlite
    apt install php7.2-mysql
    apt install php7.2-gd
    ~~~
    เป็นต้น

8. ติดตั้ง composer ใน project
    เข้าไปที่ part ของ project
    ~~~bat
    cd /var/www/pov-web-site
    ~~~
    
    สร้างโฟล์เดอร์ vendor และแก้ไขการอนุญาตให้สามารถ เขียน อ่าน ลบ ดู โฟล์เดเอร์ vendor ไฟล์ composer.json และ composer.lock
   ~~~bat
	 sudo mkdir vendor
   	 
   	 sudo chmod -R 777 vendor
   	 sudo chmod -R 777 composer.json
   	 sudo chmod -R 777 composer.lock    
   ~~~	 
   ~~~bat
    composer install
   ~~~
9. migrate database
    เข้าไปที่ part ของ project
    ~~~bat
    cd /var/www/pov-web-site
    ~~~
    
    migrate database
    ~~~bat
    ./yii migrate
    ~~~
    
    ทดสอบ run project โดยการเปิด browser -> localhost/frontend/web

(เพิ่มเติม)
กรณีที่ต้องการอัพโหลไฟล์ได้มากกว่า 2M 
     แก้ไขไฟล์ php.ini ของโฟลเดอร์ fpm และ cli โดยใช้คำสั่ง 
   ~~~bat
     nano /etc/php7.2/fpm/php.ini
   ~~~
   แก้ไขให้เป็นดังนี้
   ~~~bat
     upload_max_filesize = 20M
     post_max_size = 20M  
   ~~~  
   ~~~bat   
     nano /etc/php7.2/cli/php.ini
   ~~~
   แก้ไขให้เป็นดังนี้
   ~~~bat
     upload_max_filesize = 20M
     post_max_size = 20M  
   ~~~
   แก้ไขไฟล์ nginx.conf โดยใช้คำสั่ง
   ~~~bat
     nano /etc/nginx/nginx.conf
   ~~~
   เพิ่มคำสั่งเข้าไปในส่วนของ http {} ดังนี้
   ~~~bat
   Http {
	client max_body_size 20m;
     }
   ~~~
   Restart php-fpm และ nginx ด้วยคำสั่ง
   ~~~bat
     Service php7.2-fpm restart && service nginx restart
   ~~~

