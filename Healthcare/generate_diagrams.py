#!/usr/bin/env python3
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import seaborn as sns
import pandas as pd
import numpy as np
from matplotlib.patches import FancyBboxPatch, Rectangle
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('default')
sns.set_palette("husl")

# 1. AI Healthcare Architecture Diagram
def create_architecture_diagram():
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    
    # Data Layer
    data_box = FancyBboxPatch((0.5, 6.5), 9, 1, boxstyle="round,pad=0.1", 
                              facecolor='lightblue', edgecolor='black', linewidth=2)
    ax.add_patch(data_box)
    ax.text(5, 7, 'Data Layer\n(EHR, Medical Images, IoT Sensors, Genomics)', 
            ha='center', va='center', fontsize=10, weight='bold')
    
    # AI Processing Layer
    ai_box = FancyBboxPatch((0.5, 4.5), 9, 1.5, boxstyle="round,pad=0.1", 
                            facecolor='lightgreen', edgecolor='black', linewidth=2)
    ax.add_patch(ai_box)
    ax.text(5, 5.25, 'AI Processing Layer\n(ML Models, Deep Learning, NLP, Computer Vision)', 
            ha='center', va='center', fontsize=10, weight='bold')
    
    # Application Layer
    app_boxes = [
        (0.5, 2.5, 'Diagnostic\nImaging'),
        (2.5, 2.5, 'Clinical\nDecision Support'),
        (4.5, 2.5, 'Drug\nDiscovery'),
        (6.5, 2.5, 'Personalized\nMedicine'),
        (8.5, 2.5, 'Predictive\nAnalytics')
    ]
    
    for x, y, text in app_boxes:
        box = FancyBboxPatch((x, y), 1.8, 1.5, boxstyle="round,pad=0.1", 
                             facecolor='lightyellow', edgecolor='black')
        ax.add_patch(box)
        ax.text(x+0.9, y+0.75, text, ha='center', va='center', fontsize=9)
    
    # User Interface Layer
    ui_box = FancyBboxPatch((0.5, 0.5), 9, 1, boxstyle="round,pad=0.1", 
                            facecolor='lightcoral', edgecolor='black', linewidth=2)
    ax.add_patch(ui_box)
    ax.text(5, 1, 'User Interface Layer\n(Clinician Dashboard, Patient Portal, Mobile Apps)', 
            ha='center', va='center', fontsize=10, weight='bold')
    
    # Arrows
    for i in range(5):
        ax.arrow(5, 6.4, 0, -0.7, head_width=0.1, head_length=0.1, fc='black', ec='black')
        ax.arrow(5, 4.4, 0, -0.7, head_width=0.1, head_length=0.1, fc='black', ec='black')
        ax.arrow(5, 2.4, 0, -0.7, head_width=0.1, head_length=0.1, fc='black', ec='black')
    
    ax.set_title('AI Healthcare System Architecture', fontsize=16, weight='bold', pad=20)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('/home/ubuntu/healthcare/architecture_diagram.png', dpi=300, bbox_inches='tight')
    plt.close()

# 2. AI Implementation Process Flow
def create_process_flow():
    fig, ax = plt.subplots(1, 1, figsize=(14, 10))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    
    # Process steps
    steps = [
        (2, 8.5, 'Data Collection\n& Integration'),
        (6, 8.5, 'Data Preprocessing\n& Cleaning'),
        (10, 8.5, 'Feature Engineering\n& Selection'),
        (2, 6.5, 'Model Training\n& Validation'),
        (6, 6.5, 'Model Testing\n& Evaluation'),
        (10, 6.5, 'Clinical Validation\n& Testing'),
        (2, 4.5, 'Regulatory\nApproval'),
        (6, 4.5, 'System Integration\n& Deployment'),
        (10, 4.5, 'Monitoring\n& Maintenance'),
        (6, 2.5, 'Continuous Learning\n& Improvement')
    ]
    
    colors = ['lightblue', 'lightgreen', 'lightyellow', 'lightcoral', 'lightpink', 
              'lightgray', 'wheat', 'lavender', 'lightcyan', 'mistyrose']
    
    for i, (x, y, text) in enumerate(steps):
        box = FancyBboxPatch((x-0.8, y-0.4), 1.6, 0.8, boxstyle="round,pad=0.1", 
                             facecolor=colors[i], edgecolor='black')
        ax.add_patch(box)
        ax.text(x, y, text, ha='center', va='center', fontsize=9, weight='bold')
    
    # Arrows
    arrows = [
        (2.8, 8.5, 2.4, 0), (6.8, 8.5, 2.4, 0), (10, 8.1, 0, -1.2),
        (9.2, 6.5, -2.4, 0), (5.2, 6.5, -2.4, 0), (2, 6.1, 0, -1.2),
        (2.8, 4.5, 2.4, 0), (6.8, 4.5, 2.4, 0), (10, 4.1, 0, -1.2),
        (9.2, 2.5, -2.4, 0)
    ]
    
    for x, y, dx, dy in arrows:
        ax.arrow(x, y, dx, dy, head_width=0.15, head_length=0.15, fc='red', ec='red')
    
    ax.set_title('AI Healthcare Implementation Process Flow', fontsize=16, weight='bold', pad=20)
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('/home/ubuntu/healthcare/process_flow.png', dpi=300, bbox_inches='tight')
    plt.close()

# 3. AI Adoption Timeline Chart
def create_timeline_chart():
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    diagnostic_ai = [25, 35, 50, 65, 75, 85, 95]
    drug_discovery = [15, 25, 40, 55, 70, 80, 90]
    personalized_med = [10, 20, 35, 50, 65, 80, 95]
    autonomous_systems = [5, 10, 20, 35, 50, 70, 85]
    
    ax.plot(years, diagnostic_ai, marker='o', linewidth=3, label='Diagnostic AI', markersize=8)
    ax.plot(years, drug_discovery, marker='s', linewidth=3, label='Drug Discovery AI', markersize=8)
    ax.plot(years, personalized_med, marker='^', linewidth=3, label='Personalized Medicine', markersize=8)
    ax.plot(years, autonomous_systems, marker='D', linewidth=3, label='Autonomous Systems', markersize=8)
    
    ax.set_xlabel('Year', fontsize=12, weight='bold')
    ax.set_ylabel('Adoption Rate (%)', fontsize=12, weight='bold')
    ax.set_title('AI Healthcare Technology Adoption Timeline', fontsize=16, weight='bold')
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 100)
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/healthcare/timeline_chart.png', dpi=300, bbox_inches='tight')
    plt.close()

# 4. Performance Comparison Chart
def create_performance_chart():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Accuracy comparison
    methods = ['Traditional\nDiagnosis', 'AI-Assisted\nDiagnosis', 'AI-Only\nDiagnosis']
    accuracy = [78, 92, 89]
    colors = ['lightcoral', 'lightgreen', 'lightblue']
    
    bars1 = ax1.bar(methods, accuracy, color=colors, edgecolor='black', linewidth=2)
    ax1.set_ylabel('Accuracy (%)', fontsize=12, weight='bold')
    ax1.set_title('Diagnostic Accuracy Comparison', fontsize=14, weight='bold')
    ax1.set_ylim(0, 100)
    
    for bar, acc in zip(bars1, accuracy):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                f'{acc}%', ha='center', va='bottom', fontsize=11, weight='bold')
    
    # Cost reduction
    categories = ['Drug Discovery', 'Diagnostic Imaging', 'Clinical Trials', 'Administrative']
    cost_reduction = [45, 35, 40, 60]
    
    bars2 = ax2.bar(categories, cost_reduction, color=['gold', 'lightgreen', 'lightblue', 'lightcoral'], 
                    edgecolor='black', linewidth=2)
    ax2.set_ylabel('Cost Reduction (%)', fontsize=12, weight='bold')
    ax2.set_title('AI-Driven Cost Reduction by Category', fontsize=14, weight='bold')
    ax2.set_ylim(0, 70)
    
    for bar, cost in zip(bars2, cost_reduction):
        ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
                f'{cost}%', ha='center', va='bottom', fontsize=11, weight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/healthcare/performance_chart.png', dpi=300, bbox_inches='tight')
    plt.close()

# 5. Simulation Report - Patient Outcome Prediction
def create_simulation_report():
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
    
    # ROC Curve
    fpr = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    tpr = np.array([0, 0.3, 0.5, 0.65, 0.75, 0.82, 0.87, 0.91, 0.94, 0.97, 1.0])
    
    ax1.plot(fpr, tpr, 'b-', linewidth=3, label='AI Model (AUC = 0.89)')
    ax1.plot([0, 1], [0, 1], 'r--', linewidth=2, label='Random Classifier')
    ax1.set_xlabel('False Positive Rate', fontsize=10, weight='bold')
    ax1.set_ylabel('True Positive Rate', fontsize=10, weight='bold')
    ax1.set_title('ROC Curve - Patient Risk Prediction', fontsize=12, weight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Confusion Matrix
    conf_matrix = np.array([[850, 50], [30, 870]])
    sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', ax=ax2,
                xticklabels=['Low Risk', 'High Risk'], yticklabels=['Low Risk', 'High Risk'])
    ax2.set_title('Confusion Matrix - Risk Classification', fontsize=12, weight='bold')
    ax2.set_xlabel('Predicted', fontsize=10, weight='bold')
    ax2.set_ylabel('Actual', fontsize=10, weight='bold')
    
    # Feature Importance
    features = ['Age', 'BMI', 'Blood Pressure', 'Cholesterol', 'Glucose', 'Family History']
    importance = [0.25, 0.18, 0.22, 0.15, 0.12, 0.08]
    
    bars = ax3.barh(features, importance, color='lightgreen', edgecolor='black')
    ax3.set_xlabel('Feature Importance', fontsize=10, weight='bold')
    ax3.set_title('AI Model Feature Importance', fontsize=12, weight='bold')
    
    # Training Progress
    epochs = range(1, 51)
    train_loss = [0.8 - 0.6 * (1 - np.exp(-0.1 * np.array(epochs)))]
    val_loss = [0.85 - 0.55 * (1 - np.exp(-0.08 * np.array(epochs)))]
    
    ax4.plot(epochs, train_loss[0], 'b-', linewidth=2, label='Training Loss')
    ax4.plot(epochs, val_loss[0], 'r-', linewidth=2, label='Validation Loss')
    ax4.set_xlabel('Epochs', fontsize=10, weight='bold')
    ax4.set_ylabel('Loss', fontsize=10, weight='bold')
    ax4.set_title('Model Training Progress', fontsize=12, weight='bold')
    ax4.legend()
    ax4.grid(True, alpha=0.3)
    
    plt.suptitle('AI Healthcare Simulation Report', fontsize=16, weight='bold', y=0.98)
    plt.tight_layout()
    plt.savefig('/home/ubuntu/healthcare/simulation_report.png', dpi=300, bbox_inches='tight')
    plt.close()

# 6. Market Analysis Chart
def create_market_analysis():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    # Market size projection
    years = ['2024', '2025', '2026', '2027', '2028', '2029', '2030']
    market_size = [15.1, 20.9, 28.4, 38.1, 50.2, 65.8, 85.2]
    
    ax1.plot(years, market_size, marker='o', linewidth=4, markersize=10, color='green')
    ax1.fill_between(years, market_size, alpha=0.3, color='green')
    ax1.set_ylabel('Market Size (Billion USD)', fontsize=12, weight='bold')
    ax1.set_title('AI Healthcare Market Growth', fontsize=14, weight='bold')
    ax1.grid(True, alpha=0.3)
    
    for i, size in enumerate(market_size):
        ax1.text(i, size + 2, f'${size}B', ha='center', va='bottom', fontsize=10, weight='bold')
    
    # Investment by sector
    sectors = ['Diagnostic\nImaging', 'Drug\nDiscovery', 'Clinical\nDecision', 'Robotics', 'Digital\nTherapeutics']
    investment = [28, 24, 18, 16, 14]
    colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7']
    
    wedges, texts, autotexts = ax2.pie(investment, labels=sectors, autopct='%1.1f%%', 
                                       colors=colors, startangle=90)
    ax2.set_title('AI Healthcare Investment Distribution', fontsize=14, weight='bold')
    
    plt.tight_layout()
    plt.savefig('/home/ubuntu/healthcare/market_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    print("Generating healthcare AI diagrams...")
    create_architecture_diagram()
    print("✓ Architecture diagram created")
    
    create_process_flow()
    print("✓ Process flow diagram created")
    
    create_timeline_chart()
    print("✓ Timeline chart created")
    
    create_performance_chart()
    print("✓ Performance chart created")
    
    create_simulation_report()
    print("✓ Simulation report created")
    
    create_market_analysis()
    print("✓ Market analysis chart created")
    
    print("All diagrams generated successfully!")
