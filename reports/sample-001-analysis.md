# Phishing Email Analysis Report

## 1. Sample Information
- Report ID: REPORT-001
- Analysis date: 2026-04-06
- Analyst: Gergo Petrovszky
- Sample source: Self-created sanitized training sample
- Original file name: N/A
- Sanitized file name: sample-001-fake-microsoft-password-reset.txt

## 2. Executive Summary
This email is a likely phishing message impersonating Microsoft. It uses urgency, account-related fear, and a misleading link to pressure the recipient into visiting a suspicious domain and potentially entering credentials.

## 3. Sender Analysis
- Display name: Microsoft Account Team
- Sender address: security-update@micr0soft-account.com
- Reply-to address: support@micr0soft-helpdesk.com
- Domain observations: The sender domain uses "micr0soft" with a zero instead of the letter "o", which is a common impersonation tactic.
- Mismatch observed: Yes

## 4. Subject Analysis
- Subject line: Urgent: Your password expires today - action required immediately
- Observed urgency: High
- Suspicious wording: Yes
- Brand impersonation signs: Yes, Microsoft is being impersonated

## 5. Body Content Analysis
- Main message: The email claims unusual activity was detected and the user must verify the account immediately.
- Request made to recipient: Click a link and reset or confirm account credentials
- Pressure tactics: Threat of suspension and time pressure within 2 hours
- Grammar/spelling issues: Minor unnatural phrasing
- Social engineering indicators: Fear, urgency, authority impersonation

## 6. Link Analysis
- Link present: Yes
- Visible text: https://account.microsoft.com/security
- Actual destination: http://micr0soft-account-security-login.com/verify
- Mismatch observed: Yes
- Notes: The visible text suggests a legitimate Microsoft destination, but the actual destination is a suspicious impersonation domain.

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
- Header anomalies: Reply-to differs from sender domain
- Other indicators: Lookalike domain, urgency, impersonation, link mismatch

## 9. Red Flags
- [x] Urgent language
- [x] Threats or consequences
- [x] Credential request
- [ ] Payment request
- [x] Suspicious sender domain
- [x] Link mismatch
- [ ] Unexpected attachment
- [x] Impersonation attempt
- [x] Poor grammar
- [x] Generic greeting

## 10. Verdict
- Final assessment: Likely Phishing
- Confidence level: High
- Reasoning: The message contains multiple strong phishing indicators, including impersonation, a deceptive domain, a mismatched link, urgency, and a request related to account credentials.

## 11. Recommended Action
- Delete
- Report to security team
- Block sender/domain
- Monitor for related phishing attempts using similar branding or domains

## 12. Lessons Learned
- Brand impersonation often uses small spelling changes in domains.
- Visible link text should never be trusted without checking the actual destination.
- Urgency and fear are common phishing tactics.
- Reply-to mismatches can be a strong warning sign.