#!/usr/bin/env python3
import weasyprint
import os

def generate_pdf():
    """Generate PDF using weasyprint"""
    html_file = '/home/ubuntu/healthcare/phd_thesis.html'
    pdf_file = '/home/ubuntu/healthcare/Future_Healthcare_AI_PhD_Thesis_Fixed.pdf'
    
    print("Generating PDF with weasyprint...")
    
    # Generate PDF
    weasyprint.HTML(filename=html_file).write_pdf(pdf_file)
    
    # Check file size
    size = os.path.getsize(pdf_file) / (1024 * 1024)
    print(f"✅ PDF generated: {pdf_file}")
    print(f"📄 File size: {size:.1f} MB")

if __name__ == "__main__":
    generate_pdf()
