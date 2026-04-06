# Phishing Email Analysis Report

## 1. Sample Information
- Report ID: REPORT-004
- Analysis date: 2026-04-06
- Analyst: Gergo Petrovszky
- Sample source: Self-created sanitized training sample
- Original file name: N/A
- Sanitized file name: sample-004-fake-cloud-document-share.txt

## 2. Executive Summary
This email is a likely phishing message impersonating a cloud document sharing service. It attempts to lure the recipient into clicking a fake access link that likely leads to credential harvesting.

## 3. Sender Analysis
- Display name: OneDrive Notifications
- Sender address: documents@onedrive-share-access.com
- Reply-to address: no-reply@onedrive-secure-files.net
- Domain observations: The sender and reply-to domains are not official Microsoft or OneDrive domains and appear crafted to imitate a trusted cloud service.
- Mismatch observed: Yes

## 4. Subject Analysis
- Subject line: [External] A document has been shared with you securely
- Observed urgency: Medium to High
- Suspicious wording: Mildly suspicious
- Brand impersonation signs: Yes, OneDrive is being impersonated

## 5. Body Content Analysis
- Main message: The email claims that a document has been shared and needs review.
- Request made to recipient: Click the link and access the shared document
- Pressure tactics: Suggests access may expire if the recipient does not act promptly
- Grammar/spelling issues: Minimal
- Social engineering indicators: Trust in a known service, curiosity, urgency, and login-based lure

## 6. Link Analysis
- Link present: Yes
- Visible text: https://onedrive.live.com/
- Actual destination: http://onedrive-secure-document-access.com/login
- Mismatch observed: Yes
- Notes: The visible text appears legitimate, but the actual destination points to a suspicious impersonation domain and a login page, which strongly suggests credential harvesting intent.

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
- Header anomalies: Sender identity and reply-to domain are inconsistent with legitimate OneDrive delivery patterns
- Other indicators: Brand impersonation, link mismatch, suspicious domain naming, urgency

## 9. Red Flags
- [x] Urgent language
- [ ] Threats or consequences
- [x] Credential request
- [ ] Payment request
- [x] Suspicious sender domain
- [x] Link mismatch
- [ ] Unexpected attachment
- [x] Impersonation attempt
- [ ] Poor grammar
- [x] Generic greeting

## 10. Verdict
- Final assessment: Likely Phishing
- Confidence level: High
- Reasoning: The message impersonates a trusted cloud service, uses a misleading link, and likely attempts to steal credentials through a fake login page.

## 11. Recommended Action
- Do not click the link
- Report the message to the security team
- Block the sender/domain if confirmed malicious
- Warn users about fake cloud-sharing notifications
- Monitor for similar login-themed phishing attempts

## 12. Lessons Learned
- Cloud document sharing notifications are effective phishing lures because they look routine and familiar.
- Visible link text should always be compared with the actual destination.
- Impersonation domains often sound believable but are still not official service domains.
- Credential harvesting emails may appear cleaner and less aggressive than attachment-based phishing.