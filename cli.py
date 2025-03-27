import argparse
from redact_document import hash_and_replace_pii

def open_and_read_doc(doc):
    with open(doc, encoding="utf-8") as f:
        read_data = f.read()
        
        return read_data
    
if __name__ =="__main__":
    parser = argparse.ArgumentParser(description="Redact PII from a document.")
    parser.add_argument("input_file", help="Path to the file you want to redact.")
    parser.add_argument("--output", help="Output file name", default="redacted_output.txt")
    args = parser.parse_args()
    
    original = open_and_read_doc(args.input_file)
    redacted, counts = hash_and_replace_pii(original)
    
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(redacted)
        
        print(f"Redacted file saved as: {args.output}")
        print("Redacted Summary: ")
        for pii_type, count in counts.items():
            print(f"{pii_type.title()}: {count}")