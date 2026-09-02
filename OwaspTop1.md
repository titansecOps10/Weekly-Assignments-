

Date: September 2, 2026
Type: Hands-on Practical
Tool: Replit + AI + Firefox


📋 Overview

Built a vulnerable task management app using Replit AI, then tested it for IDOR and Stored XSS. Created two accounts, exploited both flaws, and documented everything.

Live Lab:

https://09f5373f-4b0a-4ced-892d-526d65d61a7b-00-2xdr54lwohj5k.worf.replit.dev/api/register

---

🔎 PART 1: IDOR (Broken Access Control)

What I Did:

1. Created two accounts: titansec and victim
2. As victim, created a task and noted its ID (e.g., /edit/2)
3. Switched to titansec and changed the URL from /edit/1 to /edit/2

What Happened:

The app loaded victim's task in titansec's session. I could edit, delete, or change the visibility of a task that didn't belong to me.

Why It Worked:

The app trusted the user-supplied task ID without verifying ownership. No authorization check was performed.

---

💉 PART 2: Stored XSS

What I Did:

1. As titansec, created a task with the title:
   ```html
   <script>alert('XSS')</script>
   ```
2. Marked it as public
3. Viewed the public feed

What Happened:

The alert() popup appeared in my browser. The script executed because the app didn't sanitize user input before rendering it.


🧠 What I Learned

Vulnerability How It Works Impact
IDOR Changing a numeric ID in the URL gives access to another user's data Data leakage, unauthorized modifications
Stored XSS Injecting a script that saves to the database and runs for every viewer Session hijacking, credential theft
