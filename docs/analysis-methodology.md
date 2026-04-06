# Phishing Email Analysis Methodology

## Purpose

This document describes the safe and repeatable process used in this repository
to analyze suspicious or phishing-like emails in a legal home-lab environment.

## Safety Principles

The analysis process in this project follows these rules:

- do not interact with malicious links
- do not open suspicious attachments on the host machine
- do not use real personal or corporate email data
- do not publish sensitive information
- sanitize all samples before sharing publicly

## Analysis Goals

The goal of each analysis is to identify indicators that suggest whether an
email is likely phishing, suspicious, or benign.

## Standard Workflow

### 1. Sample Collection

A sample is added only if it is safe and legal to store and review.
Possible sources:

- self-created training samples
- publicly shared phishing examples
- redacted educational examples

### 2. Sanitization

Before publishing, remove or replace:

- personal names
- email addresses
- phone numbers
- account numbers
- company-specific internal references
- tracking links or unique tokens

Sanitized files are stored in:

- `samples/sanitized/`

### 3. Content Review

The email body is reviewed for:

- urgency
- threats or pressure
- unusual requests
- credential harvesting attempts
- payment or invoice fraud themes
- grammar or language anomalies
- impersonation indicators

### 4. Header and Sender Review

If available, review:

- sender display name
- sender email address
- reply-to mismatch
- suspicious domains
- spoofing indicators
- authentication results if present

### 5. Link and Attachment Review

Review only in a safe way:

- do not click suspicious links directly
- inspect visible link text versus real destination
- note suspicious file extensions
- identify unexpected attachments

### 6. Verdict

Each sample should receive one of these outcomes:

- Likely Phishing
- Suspicious
- Likely Benign

### 7. Documentation

Every analyzed sample should have a written report in the `reports/` folder.

## Notes

This repository is for educational and portfolio purposes only.