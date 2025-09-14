#!/usr/bin/env python3
"""
Generate AWS Healthcare AI Architecture Diagram and Convert Thesis to PDF
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, ConnectionPatch
import numpy as np
import subprocess
import os

def create_aws_architecture_diagram():
    """Create comprehensive AWS Healthcare AI Architecture Diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Color scheme
    aws_orange = '#FF9900'
    aws_blue = '#232F3E'
    light_blue = '#E8F4FD'
    light_green = '#E8F5E8'
    light_orange = '#FFF4E6'
    
    # Title
    ax.text(8, 11.5, 'AWS Cloud Architecture for Healthcare AI', 
            fontsize=20, fontweight='bold', ha='center')
    ax.text(8, 11, 'Real-time Patient Monitoring and AI-Powered Clinical Decision Support', 
            fontsize=14, ha='center', style='italic')
    
    # Data Sources Layer
    ax.add_patch(FancyBboxPatch((0.5, 9), 15, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor=light_blue, 
                                edgecolor=aws_blue, linewidth=2))
    ax.text(8, 10, 'Data Sources Layer', fontsize=14, fontweight='bold', ha='center')
    
    # Data sources
    sources = ['EHR Systems', 'Medical Devices', 'Wearables', 'Lab Systems', 'Imaging']
    for i, source in enumerate(sources):
        x = 1.5 + i * 2.8
        ax.add_patch(FancyBboxPatch((x, 9.2), 2.5, 0.6, 
                                    boxstyle="round,pad=0.05", 
                                    facecolor='white', 
                                    edgecolor=aws_blue))
        ax.text(x + 1.25, 9.5, source, fontsize=10, ha='center')
    
    # Data Ingestion Layer
    ax.add_patch(FancyBboxPatch((0.5, 7), 15, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor=light_green, 
                                edgecolor=aws_blue, linewidth=2))
    ax.text(8, 8, 'Data Ingestion & Streaming Layer', fontsize=14, fontweight='bold', ha='center')
    
    # AWS Ingestion Services
    ingestion_services = [
        ('Kinesis Data Streams', 2, 7.5),
        ('API Gateway', 5, 7.5),
        ('IoT Core', 8, 7.5),
        ('Direct Connect', 11, 7.5),
        ('S3 Transfer', 14, 7.5)
    ]
    
    for service, x, y in ingestion_services:
        ax.add_patch(FancyBboxPatch((x-0.8, y-0.3), 1.6, 0.6, 
                                    boxstyle="round,pad=0.05", 
                                    facecolor=aws_orange, 
                                    edgecolor=aws_blue))
        ax.text(x, y, service, fontsize=9, ha='center', color='white', fontweight='bold')
    
    # Processing Layer
    ax.add_patch(FancyBboxPatch((0.5, 5), 15, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor=light_orange, 
                                edgecolor=aws_blue, linewidth=2))
    ax.text(8, 6, 'Real-time Processing & Analytics Layer', fontsize=14, fontweight='bold', ha='center')
    
    # Processing Services
    processing_services = [
        ('Lambda Functions', 2, 5.5),
        ('Kinesis Analytics', 5, 5.5),
        ('EMR Clusters', 8, 5.5),
        ('Glue ETL', 11, 5.5),
        ('Step Functions', 14, 5.5)
    ]
    
    for service, x, y in processing_services:
        ax.add_patch(FancyBboxPatch((x-0.8, y-0.3), 1.6, 0.6, 
                                    boxstyle="round,pad=0.05", 
                                    facecolor=aws_orange, 
                                    edgecolor=aws_blue))
        ax.text(x, y, service, fontsize=9, ha='center', color='white', fontweight='bold')
    
    # AI/ML Layer
    ax.add_patch(FancyBboxPatch((0.5, 3), 15, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#F0E6FF', 
                                edgecolor=aws_blue, linewidth=2))
    ax.text(8, 4, 'AI/ML Services Layer', fontsize=14, fontweight='bold', ha='center')
    
    # ML Services
    ml_services = [
        ('SageMaker', 2, 3.5),
        ('Comprehend Medical', 5, 3.5),
        ('Textract', 8, 3.5),
        ('Rekognition', 11, 3.5),
        ('Bedrock', 14, 3.5)
    ]
    
    for service, x, y in ml_services:
        ax.add_patch(FancyBboxPatch((x-0.8, y-0.3), 1.6, 0.6, 
                                    boxstyle="round,pad=0.05", 
                                    facecolor='#8A2BE2', 
                                    edgecolor=aws_blue))
        ax.text(x, y, service, fontsize=9, ha='center', color='white', fontweight='bold')
    
    # Storage Layer
    ax.add_patch(FancyBboxPatch((0.5, 1), 15, 1.5, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#FFE6E6', 
                                edgecolor=aws_blue, linewidth=2))
    ax.text(8, 2, 'Data Storage & Management Layer', fontsize=14, fontweight='bold', ha='center')
    
    # Storage Services
    storage_services = [
        ('S3 Buckets', 2, 1.5),
        ('RDS/Aurora', 5, 1.5),
        ('DynamoDB', 8, 1.5),
        ('Redshift', 11, 1.5),
        ('ElastiCache', 14, 1.5)
    ]
    
    for service, x, y in storage_services:
        ax.add_patch(FancyBboxPatch((x-0.8, y-0.3), 1.6, 0.6, 
                                    boxstyle="round,pad=0.05", 
                                    facecolor='#DC143C', 
                                    edgecolor=aws_blue))
        ax.text(x, y, service, fontsize=9, ha='center', color='white', fontweight='bold')
    
    # Add arrows showing data flow
    arrow_props = dict(arrowstyle='->', lw=2, color=aws_blue)
    
    # Vertical arrows between layers
    for x in [2, 5, 8, 11, 14]:
        ax.annotate('', xy=(x, 8.8), xytext=(x, 9.2), arrowprops=arrow_props)
        ax.annotate('', xy=(x, 6.8), xytext=(x, 7.2), arrowprops=arrow_props)
        ax.annotate('', xy=(x, 4.8), xytext=(x, 5.2), arrowprops=arrow_props)
        ax.annotate('', xy=(x, 2.8), xytext=(x, 3.2), arrowprops=arrow_props)
    
    # Add security and compliance annotations
    ax.add_patch(FancyBboxPatch((0.2, 0.2), 4, 0.6, 
                                boxstyle="round,pad=0.05", 
                                facecolor='#FFD700', 
                                edgecolor=aws_blue))
    ax.text(2.2, 0.5, 'Security: IAM, KMS, VPC, CloudTrail', 
            fontsize=10, ha='center', fontweight='bold')
    
    ax.add_patch(FancyBboxPatch((11.8, 0.2), 4, 0.6, 
                                boxstyle="round,pad=0.05", 
                                facecolor='#FFD700', 
                                edgecolor=aws_blue))
    ax.text(13.8, 0.5, 'Compliance: HIPAA, SOC 2, ISO 27001', 
            fontsize=10, ha='center', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/healthcare/aws_architecture_diagram.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def create_real_time_use_case_diagram():
    """Create real-time use case flow diagram"""
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(7, 9.5, 'Real-time Healthcare AI Use Case: Cardiac Monitoring', 
            fontsize=18, fontweight='bold', ha='center')
    ax.text(7, 9, 'Continuous Patient Monitoring with AI-Powered Early Warning System', 
            fontsize=12, ha='center', style='italic')
    
    # Patient monitoring device
    ax.add_patch(FancyBboxPatch((1, 7.5), 2.5, 1, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#E8F4FD', 
                                edgecolor='#232F3E', linewidth=2))
    ax.text(2.25, 8, 'Cardiac Monitor\n(ECG, Vitals)', fontsize=10, ha='center', fontweight='bold')
    
    # Data streaming
    ax.add_patch(FancyBboxPatch((5, 7.5), 2.5, 1, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#FF9900', 
                                edgecolor='#232F3E', linewidth=2))
    ax.text(6.25, 8, 'Kinesis Data\nStreams', fontsize=10, ha='center', color='white', fontweight='bold')
    
    # Lambda processing
    ax.add_patch(FancyBboxPatch((9, 7.5), 2.5, 1, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#FF9900', 
                                edgecolor='#232F3E', linewidth=2))
    ax.text(10.25, 8, 'Lambda Function\n(Real-time Processing)', fontsize=10, ha='center', color='white', fontweight='bold')
    
    # AI Model
    ax.add_patch(FancyBboxPatch((5, 5.5), 4, 1, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#8A2BE2', 
                                edgecolor='#232F3E', linewidth=2))
    ax.text(7, 6, 'SageMaker Endpoint\nCardiac Risk Prediction Model', fontsize=11, ha='center', color='white', fontweight='bold')
    
    # Decision logic
    ax.add_patch(FancyBboxPatch((1, 3.5), 3, 1, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#32CD32', 
                                edgecolor='#232F3E', linewidth=2))
    ax.text(2.5, 4, 'Risk Assessment\nNormal: < 0.3\nElevated: 0.3-0.7\nCritical: > 0.7', 
            fontsize=9, ha='center', fontweight='bold')
    
    # Alert system
    ax.add_patch(FancyBboxPatch((6, 3.5), 3, 1, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#DC143C', 
                                edgecolor='#232F3E', linewidth=2))
    ax.text(7.5, 4, 'SNS Alerts\nNurse Station\nPhysician Mobile', 
            fontsize=10, ha='center', color='white', fontweight='bold')
    
    # Data storage
    ax.add_patch(FancyBboxPatch((10.5, 3.5), 3, 1, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#FF9900', 
                                edgecolor='#232F3E', linewidth=2))
    ax.text(12, 4, 'DynamoDB\nPatient History\nTrend Analysis', 
            fontsize=10, ha='center', color='white', fontweight='bold')
    
    # Clinical response
    ax.add_patch(FancyBboxPatch((4, 1.5), 6, 1, 
                                boxstyle="round,pad=0.1", 
                                facecolor='#FFD700', 
                                edgecolor='#232F3E', linewidth=2))
    ax.text(7, 2, 'Clinical Response\nImmediate Intervention • Medication Adjustment • Specialist Consultation', 
            fontsize=10, ha='center', fontweight='bold')
    
    # Add arrows
    arrow_props = dict(arrowstyle='->', lw=2, color='#232F3E')
    
    # Horizontal flow
    ax.annotate('', xy=(4.8, 8), xytext=(3.7, 8), arrowprops=arrow_props)
    ax.annotate('', xy=(8.8, 8), xytext=(7.7, 8), arrowprops=arrow_props)
    
    # To AI model
    ax.annotate('', xy=(7, 6.5), xytext=(10.25, 7.5), arrowprops=arrow_props)
    
    # From AI model
    ax.annotate('', xy=(2.5, 4.5), xytext=(6, 5.5), arrowprops=arrow_props)
    ax.annotate('', xy=(7.5, 4.5), xytext=(7.5, 5.5), arrowprops=arrow_props)
    ax.annotate('', xy=(12, 4.5), xytext=(8, 5.5), arrowprops=arrow_props)
    
    # To clinical response
    ax.annotate('', xy=(7, 2.5), xytext=(7.5, 3.5), arrowprops=arrow_props)
    
    # Add timing annotations
    ax.text(3.5, 8.5, '< 100ms', fontsize=8, ha='center', style='italic', color='red')
    ax.text(7.5, 8.5, '< 200ms', fontsize=8, ha='center', style='italic', color='red')
    ax.text(8.5, 6.8, '< 300ms', fontsize=8, ha='center', style='italic', color='red')
    ax.text(5, 3, '< 500ms\nTotal Latency', fontsize=9, ha='center', style='italic', 
            color='red', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/healthcare/real_time_use_case.png', 
                dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()

def convert_html_to_pdf():
    """Convert HTML thesis to PDF using wkhtmltopdf"""
    try:
        # Check if wkhtmltopdf is installed
        subprocess.run(['which', 'wkhtmltopdf'], check=True, capture_output=True)
    except subprocess.CalledProcessError:
        print("Installing wkhtmltopdf...")
        subprocess.run(['sudo', 'apt-get', 'update'], check=True)
        subprocess.run(['sudo', 'apt-get', 'install', '-y', 'wkhtmltopdf'], check=True)
    
    # Convert HTML to PDF
    input_file = '/home/ubuntu/healthcare/phd_thesis.html'
    output_file = '/home/ubuntu/healthcare/Future_Healthcare_AI_PhD_Thesis.pdf'
    
    cmd = [
        'wkhtmltopdf',
        '--page-size', 'A4',
        '--margin-top', '0.75in',
        '--margin-right', '0.75in',
        '--margin-bottom', '0.75in',
        '--margin-left', '0.75in',
        '--encoding', 'UTF-8',
        '--print-media-type',
        '--enable-local-file-access',
        input_file,
        output_file
    ]
    
    print("Converting HTML to PDF...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print(f"✅ PDF thesis generated successfully: {output_file}")
        # Get file size
        size = os.path.getsize(output_file) / (1024 * 1024)  # MB
        print(f"📄 File size: {size:.1f} MB")
    else:
        print(f"❌ Error generating PDF: {result.stderr}")

def main():
    """Main function to generate all diagrams and PDF"""
    print("🏥 Generating AWS Healthcare AI Architecture Diagram...")
    create_aws_architecture_diagram()
    print("✅ AWS Architecture diagram created")
    
    print("⚡ Generating Real-time Use Case Diagram...")
    create_real_time_use_case_diagram()
    print("✅ Real-time use case diagram created")
    
    print("📚 Converting thesis to PDF...")
    convert_html_to_pdf()
    
    print("\n🎉 PhD Thesis Generation Complete!")
    print("📁 Generated files:")
    print("   • phd_thesis.html - Complete thesis in HTML format")
    print("   • Future_Healthcare_AI_PhD_Thesis.pdf - Final PDF thesis")
    print("   • aws_architecture_diagram.png - AWS architecture diagram")
    print("   • real_time_use_case.png - Real-time use case flow")

if __name__ == "__main__":
    main()
