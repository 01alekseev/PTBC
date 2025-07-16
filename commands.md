BASIC COMMANDS: 
- Encrypt file: 
python3 CLI/ptbc_cli.py encrypt test.txt test.ptbc --ttl 3600
--ttl 3600 - lifetime in seconds (3600 = 1 hour)
Requests password, creates .ptbc file

- Decrypt the file:
python3 CLI/ptbc_cli.py decrypt test.ptbc test.txt
Requests the original password
If TTL has not expired - decrypts it

Additional flags:
--autowipe (Deletes the original file after encryption or decryption)
python3 CLI/ptbc_cli.py encrypt test.txt test.ptbc --ttl 600 --autowipe

--onetime (When decrypting, creates a .lock file with a timestamp - noting that the file has already been decrypted)
python3 CLI/ptbc_cli.py decrypt test.ptbc test.txt --onetime

--silent (Disables all messages, even done or error)
python3 CLI/ptbc_cli.py encrypt test.txt test.ptbc --ttl 600 --silent

Example:
python3 CLI/ptbc_cli.py encrypt test.txt test.ptbc --ttl 900 --autowipe --silent
ttl: 15 minutes
Deletes test.txt after encryption
No output to console.
