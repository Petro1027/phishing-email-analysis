# Analyst Decision Tree

## Purpose
This document provides a simple decision-support flow for reviewing suspicious emails in a safe and repeatable way.

## Decision Tree

### Step 1 - Is the sender recognizable and expected?
- If yes, continue reviewing the message carefully.
- If no, increase suspicion and continue to Step 2.

### Step 2 - Does the sender domain look legitimate?
- If yes, continue to Step 3.
- If no, mark this as a red flag and continue to Step 3.

### Step 3 - Is there a reply-to mismatch?
- If yes, mark this as a red flag and continue.
- If no, continue.

### Step 4 - Does the subject or message create urgency, fear, or pressure?
- If yes, mark this as a red flag and continue.
- If no, continue.

### Step 5 - Does the email request one of the following?
- credentials
- payment
- opening an attachment
- clicking a login link
- secrecy
- bypassing normal verification

If yes, mark each applicable red flag and continue to Step 6.

### Step 6 - Are there links in the message?
- If yes, compare visible text with the real destination.
- If there is a mismatch, mark this as a red flag.
- If no, continue to Step 7.

### Step 7 - Are there attachments?
- If yes, inspect the file name and extension carefully.
- If the file type is unexpected or misleading, mark this as a red flag.
- If no, continue to Step 8.

### Step 8 - Are there signs of impersonation?
Examples:
- trusted brand imitation
- executive authority language
- finance or IT team impersonation
- lookalike domains

If yes, mark this as a red flag and continue to Step 9.

### Step 9 - Can the request be verified safely through another trusted channel?
- If yes, do not trust the email alone. Verify independently.
- If no, treat the email with elevated caution.

### Step 10 - Final Assessment
Use the number and strength of red flags to assign one of these outcomes:
- Likely Benign
- Suspicious
- Likely Phishing

## Quick Interpretation Guide
- One weak indicator alone may not be enough for a phishing verdict.
- Multiple aligned indicators greatly increase confidence.
- Urgency plus impersonation plus a risky request is a strong phishing pattern.
- BEC emails may have no link and no attachment, but still be malicious.

## Safe Handling Reminder
Do not click suspicious links, open suspicious attachments, or interact with attacker-controlled infrastructure on the host machine.