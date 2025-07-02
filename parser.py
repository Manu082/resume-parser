import docx
from pdfminer.high_level import extract_text

class ResumeParser:
    def parse_pdf(self, filepath):
        return extract_text(filepath)
    
    def parse_docx(self, filepath):
        doc = docx.Document(filepath)
        return '\n'.join([p.text for p in doc.paragraphs])

    def parse_resume(self, filepath):
        if filepath.lower().endswith('.pdf'):
            return self.parse_pdf(filepath)
        elif filepath.lower().endswith('.docx'):
            return self.parse_docx(filepath)
        else:
            raise ValueError("Unsupported file type")

