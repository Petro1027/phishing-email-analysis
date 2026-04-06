# Case Index

## Purpose
This file provides a quick overview of all phishing analysis cases included in this repository.

## Cases

### CASE-001
- Sample: `samples/sanitized/sample-001-fake-microsoft-password-reset.txt`
- Report: `reports/sample-001-analysis.md`
- Category: Credential phishing
- Theme: Fake Microsoft password reset
- Main red flags:
    - lookalike domain
    - reply-to mismatch
    - urgent language
    - link mismatch
    - credential-related request
- Verdict: Likely Phishing

### CASE-002
- Sample: `samples/sanitized/sample-002-fake-invoice-attachment.txt`
- Report: `reports/sample-002-analysis.md`
- Category: Attachment phishing
- Theme: Fake overdue invoice
- Main red flags:
    - urgent payment language
    - suspicious attachment
    - double extension
    - reply-to mismatch
- Verdict: Likely Phishing

### CASE-003
- Sample: `samples/sanitized/sample-003-bec-ceo-payment-request.txt`
- Report: `reports/sample-003-analysis.md`
- Category: Business Email Compromise (BEC)
- Theme: Executive payment request
- Main red flags:
    - authority impersonation
    - secrecy
    - urgent action
    - anti-verification language
    - payment-related setup
- Verdict: Likely Phishing / BEC

## Coverage Summary
Current phishing themes covered in the repository:
- credential phishing
- invoice/payment phishing
- business email compromise

## Notes
All samples in this repository are sanitized training examples created for safe educational and portfolio use.