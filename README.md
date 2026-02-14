# Secure Coding Review – CodeAlpha Internship

## 📌 Project Overview
This project demonstrates the difference between insecure and secure coding practices using a simple Python login system.

The goal of this task is to identify security vulnerabilities and improve the code using better security practices.

---

## ❌ Insecure Version (insecure_login.py)

### Issues Identified:
- Password is stored in plain text.
- Credentials are hardcoded inside the program.
- Anyone who accesses the code can see the password.
- No encryption or protection mechanism.

### Security Risk:
This approach is unsafe for real-world applications and can lead to password exposure.

---

## ✅ Secure Version (secure_login.py)

### Improvements Made:
- Password is hashed using SHA-256.
- Plain text password is not directly compared.
- Basic improvement in protecting sensitive data.

---

## 🔍 Key Learning Outcomes
- Importance of secure coding practices.
- Risks of hardcoding credentials.
- Role of hashing in protecting passwords.
- Basic understanding of improving application security.

---

## 🏁 Conclusion
Secure coding is essential to protect user data and prevent security vulnerabilities.
Developers must avoid storing passwords in plain text and always implement proper security mechanisms.
