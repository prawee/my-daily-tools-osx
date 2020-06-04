# How to solve could not connect server

## Error

```bash
psql
```

```bash
psql: error: could not connect to server: could not connect to server: No such file or directory
  Is the server running locally and accepting
  connections on Unix domain socket "/tmp/.s.PGSQL.5432"?
```

## Fixed

```bash
sudo mkdir /var/pgsql_socket/
sudo ln -s /private/tmp/.s.PGSQL.5432 /var/pgsql_socket/
```

```bash
brew postgresql-upgrade-database
echo 'export PATH="/usr/local/opt/postgresql@10/bin:$PATH"' >> ~/.zshrc
```

```bash
brew services start postgresql@10 | pg_ctl -D /usr/local/var/postgresql@10 start
```

```bash
/usr/local/opt/postgresql/bin/pg_ctl -D /usr/local/var/postgres -l logfile start
```
