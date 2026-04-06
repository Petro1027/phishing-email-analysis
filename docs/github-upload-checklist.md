# GitHub Upload Checklist

## Purpose
This checklist is used before pushing updates to the public repository to reduce the risk of uploading sensitive or unsafe content.

## Safe to Upload
- [ ] Sanitized training samples only
- [ ] Self-written analysis reports
- [ ] Methodology and checklist documents
- [ ] Glossary and supporting documentation
- [ ] Changelog and portfolio summary files
- [ ] Fictional domains, names, and email addresses only
- [ ] Safe text-based training examples only

## Do Not Upload
- [ ] Real mailbox exports
- [ ] Real `.eml`, `.msg`, `.pst`, or `.ost` files unless fully safe and intentionally excluded from public upload
- [ ] Personal email addresses
- [ ] Company-internal email addresses
- [ ] Real employee names
- [ ] Real customer names
- [ ] Real banking information
- [ ] Real payment information
- [ ] Authentication tokens or secrets
- [ ] Harmful attachments or payloads
- [ ] Live phishing URLs
- [ ] Screenshots showing sensitive data

## Repository Hygiene
- [ ] Check `.gitignore` before pushing
- [ ] Confirm `.idea/` is not being uploaded
- [ ] Confirm no temporary files are included
- [ ] Confirm no local exports are included
- [ ] Confirm only intended files appear in `git status`

## Content Review
- [ ] Samples are clearly marked as sanitized
- [ ] Reports are consistent with the sample content
- [ ] Documentation matches the current repository state
- [ ] README reflects the actual completed cases
- [ ] No exaggerated claims are present

## Final Verification
Before each push:
1. Run `git status`
2. Review changed files carefully
3. Open sensitive-looking files before committing
4. Make sure no real data is present
5. Commit and push only after verification

## Reminder
If there is any doubt about whether a file is safe to publish, do not upload it.