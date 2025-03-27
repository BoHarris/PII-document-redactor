import re
import hashlib
#Define PII patterns
PII_PATTERNS ={
    "email": r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',
    "phone": r'\b\d{3}[-.]?\d{3}[-.]?\d{4}\b',
    "ssn": r'\b\d{3}-?\d{2}-\d{4}\b',
    "ip": r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'
}

def hash_pii(data):
    return hashlib.sha256(data.encode()).hexdigest()[:10]

def hash_and_replace_pii(doc):
    counts = {key: 0 for key in PII_PATTERNS}
    for pii_type, pattern in PII_PATTERNS.items():
        def replace(match):
            counts[pii_type] +=1
            return f"HASHED - {pii_type.upper()} -- {hash_pii(match.group())}]"
        
        doc = re.sub(pattern, replace, doc)
    return doc, counts