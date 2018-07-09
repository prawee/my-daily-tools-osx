/***** set server for yii2 in ubuntu 18.04 (nginx, php7.2, mariadb) ******/

1. ËÅÑ§¨Ò¡·ÕèµÔ´µÑé§ ubuntu àÊÃç¨
    /*** ãªé¤ÓÊÑè§ ***/
    ~~~bash
    apt install net-tools
    apt update
    apt upgrate
    ~~~

2. µÔ´µÑé§ nginx
    /*** ãªé¤ÓÊÑè§ ***/
    apt install nginx
    
    /*** ·´ÊÍº nginx ***/
    à»Ô´ browser -> localhost ËÃ×Í 127.0.0.1

    /*** part default ÊÓËÃÑºáÊ´§¼Å ***/
    /var/www/html

    

3. µÔ´µÑé§ mariadb
    /*** ãªé¤ÓÊÑè§ ***/
    apt install mariadb-server


    /*** µÑé§¤èÒ password ***/
    mysql_secure_installation

    Enter current password for root(enter for none): Enter    
    
    Change the root password? [Y/n]: Y
    
    New password: password

    Re-enter new password: password
    
    Remove anonymous user? [Y/n]: Y
    
    Disallow root login remotely? [Y/n]: Y
    
    Remove test database and access now? [Y/n]: Y
 
    Reload privilege tables now? [Y/n]: Y


    /***login to database***/
    mysql -u root -p
    password: password

    /*** ÊÃéÒ§ database ***/
    create database dbname;

    /*** áÊ´§ÃÒÂ¡ÒÃ database áÅÐ table ***/
    show databases;
    show tables;

    /*** ¶éÒµéÍ§¡ÒÃà»ÅÕèÂ¹ password mariadb ***/    
    use mysql;
    UPDATE user SET plugin = ’’ WHERE user=’root’;
    FLUSH PRIVILEGES;
    exit;
    service mysqld restart

4. µÔ´µÑé§ extensions àº×éÍ§µé¹ÊÓËÃÑº php7.2
    /*** ãªé¤ÓÊÑè§ ***/    
    apt install php7.2-fpm
    apt install php7.2-mbstring
    apt install php7.2-xml

    /*** ã¹¡Ã³Õ·Õè ubuntu ÂÑ§äÁèä´éµÔ´µÑé§ zip áÅÐ unzip #µéÍ§µÔ´µÑé§à¾ÃÒÐ¨Ð·ÓãËéäÁèÊÒÃÁÒÃ¶ composer install ä´é ***/
    apt install zip unzip

5. µÔ´µÑé§ project
    /*** à¢éÒä»ÂÑ§ part ·ÕèãªéÊÓËÃÑºáÊ´§¼ÅàÇçº ***/
    cd /var/www
    
    /*** ãªé¤ÓÊÑè§ ***/
    git clone <url>
    
    cd projectname
    
    sudo php init

    /*** µÑé§¤èÒàª×èÍÁµèÍ¡Ñº database ***/
    nano /var/www/pov-website/common/config/main-local.php
    /***file main-local.php***/
   	 'class' => 'yii\db\Connection',
       		 'dsn' => 'mysql:host=127.0.0.1;dbname=pov',
       		 'username' => 'root',
       		 'password' => 'password',
       		 'charset' => 'utf8',
    /***end file***/

6. µÑé§¤èÒ part µÓáË¹è§·ÕèáÊ´§¼ÅàÇçº
    cd /etc/nginx/sites-enable/
    nano default
    
    /****file default****/
   	 
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
    
    /*****end file*****/

    nginx -s reload
    nginx -s reopen

    /*** ·´ÊÍº¡ÒÃ·Ó§Ò¹ÃèÇÁ¡Ñº¢Í§ php ¡Ñº nginx ***/
    
    cd /var/www/pov-website/

    nano info.php

    /*****file info.php*****/
   	 <?php
   		 phpinfo();
   		 
    /*****end file*****/


  		 /***run info.php***/
    à»Ô´ browser -> localhost/info.php  ËÃ×Í ip ¢Í§ server/info.php #¶éÒà»Ô´ info.php ä´éáÊ´§ÇèÒÊÒÁÒÃ¶ãªé§Ò¹ php ÃèÇÁ¡Ñº nginx ä´éáÅéÇ

7. µÔ´µÑé§ extensions à¾ÔèÁàµÔÁÊÓËÃÑºãªé§Ò¹¡Ñº yii2
    àªç¤ requirements ¢Í§ yii2 #µÔ´µÑé§µÒÁ extension ·ÕèÂÑ§äÁèä´éµÔ´µÑé§
    à»Ô´ browser -> localhost/requirements.php
    àªè¹    apt install php7.2-intl
   	 apt install php7.2-sqlite
   	 apt install php7.2-mysql
   	 apt install php7.2-gd
    à»ç¹µé¹

8. µÔ´µÑé§ composer ã¹ project
    /*** à¢éÒä»·Õè part ¢Í§ project ***/
    cd /var/www/pov-web-site
    
    /*** ÊÃéÒ§â¿Åìà´ÍÃì vendor áÅÐá¡éä¢¡ÒÃÍ¹Ø­ÒµãËéÊÒÁÒÃ¶ à¢ÕÂ¹ ÍèÒ¹ Åº ´Ù â¿Åìà´àÍÃì vendor ä¿Åì composer.json áÅÐ composer.lock ***/
   	 sudo mkdir vendor
   	 
   	 sudo chmod -R 777 vendor
   	 sudo chmod -R 777 composer.json
   	 sudo chmod -R 777 composer.lock    
   		 
    
    composer install

9. migrate database
    /*** à¢éÒä»·Õè part ¢Í§ project *///
    cd /var/www/pov-web-site

    /*** migrate database ***/
    ./yii migrate

    /*** ·´ÊÍº run project ***/
    à»Ô´ browser -> localhost/frontend/web



/********* ¡Ã³Õ·ÕèµéÍ§¡ÒÃÍÑ¾âËÅä¿Åìä´éÁÒ¡¡ÇèÒ 2M *********/
     /*** á¡éä¢ä¿Åì php.ini ¢Í§â¿Åà´ÍÃì fpm áÅÐ cli â´Âãªé¤ÓÊÑè§ ***/     
     nano /etc/php7.2/fpm/php.ini
     /*** á¡éä¢ãËéà»ç¹´Ñ§¹Õé ***/
     upload_max_filesize = 20M
     post_max_size = 20M  
     
     nano /etc/php7.2/cli/php.ini
     /*** á¡éä¢ãËéà»ç¹´Ñ§¹Õé ***/
     upload_max_filesize = 20M
     post_max_size = 20M  
     
     /*** á¡éä¢ä¿Åì nginx.conf â´Âãªé¤ÓÊÑè§ ***/
     nano /etc/nginx/nginx.conf
     /*** à¾ÔèÁ¤ÓÊÑè§à¢éÒä»ã¹ÊèÇ¹¢Í§ http {} ´Ñ§¹Õé ***/
     Http {
	client max_body_size 20m;
     }

     /*** Restart php-fpm áÅÐ nginx ´éÇÂ¤ÓÊÑè§ ***/
     Service php7.2-fpm restart && service nginx restart


