"""
Script to generate PDF/HTML report from analysis
"""
import pandas as pd
from datetime import datetime
import os


def generate_html_report(data_path, output_path):
    """Generate HTML report"""
    df = pd.read_excel(data_path)
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Diabetes Analysis Report</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 40px; }}
            h1 {{ color: #1f77b4; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
            th {{ background-color: #1f77b4; color: white; }}
            .stats {{ background-color: #f0f0f0; padding: 20px; margin: 20px 0; }}
        </style>
    </head>
    <body>
        <h1>Diabetes Analysis Report</h1>
        <p>Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        
        <div class="stats">
            <h2>Summary Statistics</h2>
            <p>Total Patients: {len(df)}</p>
            <p>Diabetes Cases: {df['diabetes'].sum()}</p>
            <p>Diabetes Rate: {df['diabetes'].mean():.1%}</p>
        </div>
        
        <h2>Data Sample</h2>
        {df.head(10).to_html(index=False)}
        
        <h2>Statistical Summary</h2>
        {df.describe().to_html()}
    </body>
    </html>
    """
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"Report generated: {output_path}")


if __name__ == "__main__":
    generate_html_report(
        'diabetes_patients_data.xlsx',
        'reports/diabetes_report.html'
    )
