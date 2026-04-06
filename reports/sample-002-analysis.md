# Phishing Email Analysis Report

## 1. Sample Information
- Report ID: REPORT-002
- Analysis date: 2026-04-06
- Analyst: Gergo Petrovszky
- Sample source: Self-created sanitized training sample
- Original file name: N/A
- Sanitized file name: sample-002-fake-invoice-attachment.txt

## 2. Executive Summary
This email is a likely phishing message using a fake overdue invoice theme. It attempts to pressure the recipient into opening a suspicious attachment disguised as a PDF document.

## 3. Sender Analysis
- Display name: Billing Department
- Sender address: invoices@fastpay-billing.net
- Reply-to address: accounts@fastpay-secure.net
- Domain observations: The sender and reply-to domains differ, which may indicate impersonation or redirection of responses.
- Mismatch observed: Yes

## 4. Subject Analysis
- Subject line: Invoice INV-2026-0416 overdue - immediate review required
- Observed urgency: High
- Suspicious wording: Yes
- Brand impersonation signs: Possible, but not tied to a well-known brand in this sample

## 5. Body Content Analysis
- Main message: The email claims an invoice is overdue and requests immediate attention.
- Request made to recipient: Open the attachment and review the invoice
- Pressure tactics: Threat of late charges and service interruption
- Grammar/spelling issues: Minimal
- Social engineering indicators: Financial pressure, urgency, and implied consequences

## 6. Link Analysis
- Link present: No
- Visible text: N/A
- Actual destination: N/A
- Mismatch observed: No
- Notes: No link included in this sample

## 7. Attachment Analysis
- Attachment present: Yes
- File name: Invoice_INV-2026-0416.pdf.html
- File type: HTML file disguised as a PDF-like document
- Expected or unexpected: Unexpected and suspicious
- Notes: Double-extension style naming can be used to trick users into believing the file is a safe document.

## 8. Technical Indicators
- SPF result: Not available in this sanitized sample
- DKIM result: Not available in this sanitized sample
- DMARC result: Not available in this sanitized sample
- Header anomalies: Reply-to differs from sender domain
- Other indicators: Suspicious attachment naming, urgency, payment theme

## 9. Red Flags
- [x] Urgent language
- [x] Threats or consequences
- [ ] Credential request
- [x] Payment request
- [x] Suspicious sender domain
- [ ] Link mismatch
- [x] Unexpected attachment
- [ ] Impersonation attempt
- [ ] Poor grammar
- [x] Generic greeting

## 10. Verdict
- Final assessment: Likely Phishing
- Confidence level: High
- Reasoning: The message uses a common invoice lure, creates financial urgency, includes a mismatched reply-to address, and contains a suspicious attachment with a misleading file name.

## 11. Recommended Action
- Do not open the attachment
- Quarantine the message
- Report to security team
- Block sender/domain if confirmed malicious
- Warn finance users about invoice-themed phishing

## 12. Lessons Learned
- Invoice-themed phishing often targets finance or administrative users.
- Attachments with misleading double extensions are high risk.
- Urgent payment language is a common social engineering tactic.
- Reply-to mismatches can signal malicious intent.