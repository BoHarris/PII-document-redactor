🛡️ PII Document Redactor (CLI Tool)
A privacy-focused Python tool that scans documents for Personally Identifiable Information (PII), replaces sensitive values with hashed placeholders, and logs a redaction summary. Built with privacy engineering best practices and modular design (SOLID principles).

🔍 Features
✅ Detects PII (Emails, Phone Numbers, SSNs, IP Addresses)

🔐 Hashes sensitive values using SHA-256

🧠 Tracks number of redacted items by type

📁 CLI interface for quick input/output file processing

🧱 Built for privacy engineers and data compliance analysts

📦 How to Use
Install Python 3.10+

Clone this repo:
```
git clone https://github.com/your-username/PII-document-redactor.git
cd PII-document-redactor
Run the CLI tool:
python cli.py sensitive.txt --output redacted_output.txt
```


✅ Redacted document is saved, and a summary is printed.

🧪 Example Input (sensitive.txt)
```
Alice: alice.johnson@example.com, 555-123-4567
Bob’s SSN: 123-45-6789, IP: 192.168.1.50
```
🔐 Example Output (redacted_output.txt)
```
Alice: HASHED - EMAIL -- 1079ed8c61], HASHED - PHONE -- d36e830822]
Bob’s SSN: HASHED - SSN -- 01a54629ef], IP: HASHED - IP -- 725b4c8929]
```
📊 Console Summary
```
✅ Redacted file saved as: redacted_output.txt
📊 Redaction summary:
  Email: 1
  Phone: 1
  Ssn: 1
  Ip: 1
```
📁 File Structure
PII-document-redactor/
├── redact_document.py   # Core redaction logic
├── cli.py               # CLI runner
├── sensitive.txt        # Example input
├── redacted_output.txt  # Output (auto-generated)

🛠 Tech Stack
Python 3.12
re (Regex)
hashlib (SHA-256)
argparse (Command-line interface)

💬 Notes
This tool is designed as a learning and demo project, but can be extended for real-world use in:
Privacy compliance automation (FTC, GDPR, CCPA)
Internal audits and test data sanitization
Secure document review workflows
