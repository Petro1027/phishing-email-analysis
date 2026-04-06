# Red Flags Comparison Table

## Purpose
This table compares the main phishing indicators across the current sample cases in this repository.

| Case ID   | Theme                              | Urgency | Impersonation | Link Mismatch | Suspicious Attachment | Reply-To Mismatch | Payment Theme | Credential Theme | Secrecy | Anti-Verification |
|-----------|------------------------------------|---------|---------------|---------------|-----------------------|-------------------|---------------|------------------|---------|-------------------|
| CASE-001  | Fake Microsoft password reset      | Yes     | Yes           | Yes           | No                    | Yes               | No            | Yes              | No      | No                |
| CASE-002  | Fake overdue invoice               | Yes     | No            | No            | Yes                   | Yes               | Yes           | No               | No      | No                |
| CASE-003  | BEC executive payment request      | Yes     | Yes           | No            | No                    | Yes               | Yes           | No               | Yes     | Yes               |

## Observations
- Urgency appears in all current cases.
- Reply-to mismatch appears in all current cases.
- Credential theft is most visible in CASE-001.
- Attachment risk is the key technical lure in CASE-002.
- Secrecy and anti-verification behavior are strongest in CASE-003.

## Analyst Use
This table can help quickly compare phishing patterns and identify which indicators are most associated with each scenario type.