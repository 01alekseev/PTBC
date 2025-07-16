# 🧠 Made for people - PTBC by Ivan Alekseev 2025 - Petoron core (ADC)

Petoron Time Burn Cipher (PTBC)
A promising cipher based on self-destruction of time, complete absence of traces and impossibility of key selection.

How to encrypt any text data? (must have Petoron Time Burn Cipher already installed)

1) Create any .txt file
2) python3 CLI/ptbc_cli.py encrypt <NAME>.txt <NAME>.ptbc --ttl 600 (Here specify any number in seconds - for example 123456789).
3) Specify a PASSWORD (if you lose this password, you will lose the contents of the file forever).

- How to decrypt on any device? (must have Petoron Time Burn Cipher already installed)

1) python3 CLI/ptbc_cli.py decrypt <NAME>.ptbc <NAME>.txt
2) Enter the original PASSWORD (you will never get the contents of <NAME>.ptbc if you enter the wrong password).
3) If you successfully entered the password, you will receive a <NAME>.txt document with the following contents 

*If you specify a time value like --ttl 600 (i.e. 10 minutes), the file cannot be opened after that time, so if it is 601 you will lose access to the information forever, keep this in mind.

Any time values such as:
1 hour --ttl 3600
1 day --ttl 86400
10 years --ttl 315360000 # Well and so on ))

Keep the password separate, not in the same place! 

You can use PTBC to:
Storing Petoron Cube A+B wallets and seed phrases (or any other passwords)
Temporary messages
Personal records

In short, anything :)




...

Can I read an encrypted .ptbc file without a password?
No. But why?

The key is generated from the password via Argon2id
Argon2id = world's best algorithm for brute force protection
___
memory_cost=2^18 - 256MB RAM
parallelism=4
time_cost=3

GPU, ASIC and even quantum system can't handle brute force even in years if password ≥ 12 characters.

It is impossible to get without password :)

...
The key is not stored anywhere
It is created in RAM, via hash_secret_raw()
No key files, metadata, cookies or backups
Password is deleted from memory via .destroy() after execution

No traces. Nothing to intercept ))))

...

The file is encrypted by AES-CFB with a unique IV
Unique IV = every file even with the same password will be encrypted differently
Stream encryption is strong, HMAC protects against modifications

No pattern attack or re-encryption can be used.

...

HMAC-SHA512 protects against spoofing and modification
If you try to spoof the body - decryption will not be performed

HMAC is calculated with a secret key, also from Argon2id.

It cannot be hacked or forged.

...

 TTL is built into ciphertext
Even if someone gets .ptbc, finds the password and decrypts everything - if ttl is expired - decryption is impossible

ttl is checked before HMAC, everything is strictly in order.

Even with password, but after ttl - file is destroyed forever.


___
Welcome!
chmod +x setup_ptbc.sh
./setup_ptbc.sh

---
Licensed under the PTBC Fair Use License by Ivan Alekseev | Petoron

