# Phishing Email Analysis Report

## 1. Sample Information
- Report ID: REPORT-005
- Analysis date: 2026-04-06
- Analyst: Gergo Petrovszky
- Sample source: Self-created sanitized training sample
- Original file name: N/A
- Sanitized file name: sample-005-fake-payroll-update.txt

## 2. Executive Summary
This email is a likely phishing message impersonating an HR/payroll service. It attempts to pressure the recipient into clicking a fake payroll verification link and submitting sensitive payroll or banking-related information.

## 3. Sender Analysis
- Display name: HR Payroll Services
- Sender address: payroll@company-payroll-portal.com
- Reply-to address: hr-support@employee-payroll-secure.net
- Domain observations: The sender and reply-to domains are not consistent with a normal internal corporate payroll service and appear designed to sound trustworthy.
- Mismatch observed: Yes

## 4. Subject Analysis
- Subject line: Action required: confirm direct deposit details for upcoming payroll
- Observed urgency: High
- Suspicious wording: Yes
- Brand impersonation signs: Yes, HR/payroll function is being impersonated

## 5. Body Content Analysis
- Main message: The email claims employees must confirm direct deposit details because of a payroll system update.
- Request made to recipient: Click the link and confirm payroll or banking information
- Pressure tactics: Deadline by end of day and warning of delayed salary payment
- Grammar/spelling issues: Minimal
- Social engineering indicators: Trust in HR/payroll process, urgency, fear of payment delay, request for sensitive information

## 6. Link Analysis
- Link present: Yes
- Visible text: https://company.example/payroll
- Actual destination: http://employee-payroll-secure-check.com/login
- Mismatch observed: Yes
- Notes: The visible link appears internal or trusted, but the actual destination points to an unrelated suspicious domain and a login page, suggesting credential harvesting.

## 7. Attachment Analysis
- Attachment present: No
- File name: N/A
- File type: N/A
- Expected or unexpected: N/A
- Notes: No attachment included

## 8. Technical Indicators
- SPF result: Not available in this sanitized sample
- DKIM result: Not available in this sanitized sample
- DMARC result: Not available in this sanitized sample
- Header anomalies: Sender and reply-to are inconsistent with a legitimate internal payroll communication pattern
- Other indicators: Payroll-themed lure, link mismatch, suspicious domain naming, urgency, likely sensitive data harvesting

## 9. Red Flags
- [x] Urgent language
- [x] Threats or consequences
- [x] Credential request
- [x] Payment request
- [x] Suspicious sender domain
- [x] Link mismatch
- [ ] Unexpected attachment
- [x] Impersonation attempt
- [ ] Poor grammar
- [x] Generic greeting

## 10. Verdict
- Final assessment: Likely Phishing
- Confidence level: High
- Reasoning: The email combines HR/payroll impersonation, urgency, fear of salary delay, a suspicious destination domain, and a misleading link intended to collect sensitive information.

## 11. Recommended Action
- Do not click the link
- Do not submit payroll or banking information through the email
- Report the message to the security team
- Verify payroll requests through trusted internal channels
- Block or monitor the suspicious sender/domain if confirmed malicious

## 12. Lessons Learned
- Payroll-related phishing can be highly effective because it targets sensitive and time-critical concerns.
- Fear of delayed salary payment is a strong social engineering tactic.
- HR and payroll impersonation can be used to steal both credentials and banking details.
- A seemingly trusted visible link should always be checked against its actual destination.