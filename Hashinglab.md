







 Hashing Lab Experiment

**Date:** September 3, 2026  
**Tool:** Replit AI-built hashing lab

https://de64a54f-c6bf-4459-994b-d2014e9d4e7c-00-22sn7sm6nfb9s.worf.replit.dev/

## What I Did

1. Entered `password123` into the lab
2. Compared MD5 and SHA-256 outputs
3. Changed one character to `password124` — hashes changed completely
4. Reviewed the attack surface estimates

---

## What I Learned

| Hash Type | Speed | Risk |
|-----------|-------|------|
| MD5 | 2.3 trillion/sec | ❌ Unsafe |
| SHA-256 | 18.1 billion/sec | ⚠️ Fast |
| scrypt | 112/sec | ✅ Safe |

**Key Takeaway:** Fast hashing is the vulnerability. Slow hashing (with salting) protects passwords.

---

## Reflection

This lab showed me exactly why MD5 is dead for passwords and why algorithms like scrypt and Argon2id exist. If a database leaks, attackers will guess billions of passwords per second unless the hash is slow.

