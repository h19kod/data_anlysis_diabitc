"""
Generate Roadmap Excel File - Simple Version
"""

import pandas as pd

# Data
roadmap_data = {
    'المرحلة': [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 8, 8],
    'الميزة': [
        'JWT Authentication', 'Rate Limiting', 'Input Validation', 'API Keys',
        'Prometheus Metrics', 'Grafana Dashboard', 'Sentry Integration', 'Structured Logging',
        'PostgreSQL Setup', 'SQLAlchemy Models', 'Migrations', 'Redis Cache', 'Data Migration',
        'MLflow Setup', 'Model Registry', 'Experiment Tracking', 'A/B Testing', 'Drift Detection', 'Model Retraining',
        'AWS EC2', 'AWS RDS', 'AWS S3', 'Kubernetes', 'Helm Charts', 'Terraform', 'CI/CD Pipeline', 'Load Balancer',
        'React Setup', 'UI Components', 'Dashboard Page', 'Prediction Page', 'API Integration', 'Authentication', 'Mobile Responsive', 'Flutter App',
        'Integration Tests', 'E2E Tests', 'Load Testing', 'Security Scanning', 'Code Coverage', 'Performance Testing',
        'Sphinx Docs', 'API Reference', 'User Guide', 'Developer Guide', 'Video Tutorials', 'Architecture Diagrams'
    ],
    'الأولوية': ['عالية', 'عالية', 'عالية', 'متوسطة', 'عالية', 'عالية', 'عالية', 'متوسطة', 'عالية', 'عالية', 'عالية', 'متوسطة', 'عالية', 'عالية', 'متوسطة', 'متوسطة', 'متوسطة', 'متوسطة', 'عالية', 'عالية', 'عالية', 'متوسطة', 'عالية', 'متوسطة', 'متوسطة', 'عالية', 'متوسطة', 'متوسطة', 'متوسطة', 'متوسطة', 'متوسطة', 'متوسطة', 'عالية', 'متوسطة', 'منخفضة', 'عالية', 'متوسطة', 'متوسطة', 'عالية', 'عالية', 'متوسطة', 'متوسطة', 'متوسطة', 'متوسطة', 'متوسطة', 'منخفضة', 'متوسطة'],
    'الحالة': ['جاهز', 'جاهز', 'جاهز', 'قيد التنفيذ', 'جاهز', 'جاهز', 'جاهز', 'قيد التنفيذ', 'قيد التنفيذ', 'قيد التنفيذ', 'قيد التنفيذ', 'قيد التنفيذ', 'قيد التنفيذ', 'قيد التنفيذ', 'قيد التنفيذ', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'مخطط', 'جاهز', 'مخطط', 'مخطط', 'جاهز', 'قيد التنفيذ', 'مخطط', 'قيد التنفيذ', 'جاهز', 'مخطط', 'قيد التنفيذ', 'جاهز', 'مخطط', 'مخطط', 'مخطط', 'مخطط'],
    'التقدير (أيام)': [2, 1, 1, 1, 2, 1, 1, 1, 3, 2, 2, 2, 2, 3, 2, 2, 3, 2, 2, 5, 5, 5, 5, 3, 3, 3, 2, 2, 3, 3, 3, 3, 2, 3, 15, 3, 3, 2, 2, 2, 2, 2, 1, 2, 2, 5, 2],
    'التبعيات': ['API موجود', 'API موجود', '-', 'API موجود', 'Config YAML', '-', '-', '-', 'Docker', 'PostgreSQL', 'SQLAlchemy', 'Docker', 'PostgreSQL', 'PostgreSQL', 'MLflow', 'MLflow', 'Model Registry', 'MLflow', 'MLflow', 'Docker', 'EC2', 'EC2', 'AWS', 'AWS', 'AWS', 'AWS', 'K8s', 'API', 'React', 'React', 'React', 'API', 'Frontend', 'Frontend', 'API', 'Tests', 'Frontend', 'K8s', 'CI/CD', 'Tests', 'CI/CD', '-', 'FastAPI', '-', '-', '-', '-'],
    'الوصف': [
        'حماية API بـ JWT tokens', 'منع الإساءة (100 request/min)', 'Pydantic strict validation', 'مفاتيح API للتطبيقات الخارجية',
        'قياس الأداء', 'لوحة مراقبة', 'تتبع الأخطاء', 'JSON format logs',
        'بدلاً من Excel', 'ORM models', 'Alembic migrations', 'تسريع الاستجابة', 'نقل البيانات من Excel',
        'Tracking server', 'إدارة النماذج', 'تتبع التجارب', 'اختبار النماذج', 'كشف تغير البيانات', 'إعادة التدريب التلقائي',
        'Virtual servers', 'PostgreSQL managed', 'Storage', 'Orchestration', 'Package management', 'Infrastructure as Code', 'GitHub Actions → AWS', 'ALB',
        'Create React App', 'Material-UI / Tailwind', 'لوحة المعلومات', 'صفحة التنبؤ', 'Axios + React Query', 'Login / Register', 'CSS Media Queries', 'تطبيق موبايل',
        'pytest + testcontainers', 'Playwright', 'Locust', 'Snyk', '90%+ target', 'k6',
        'RST format', 'Auto-generated', 'Step-by-step', 'Contributing', 'شرح فيديو', 'C4 Model'
    ]
}

def create_excel_roadmap():
    """Create Excel roadmap with multiple sheets"""
    
    # Create DataFrame
    df = pd.DataFrame(roadmap_data)
    
    # Create Excel writer
    output_path = "ROADMAP.xlsx"
    
    with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
        # Sheet 1: Detailed Plan
        df.to_excel(writer, sheet_name='الخطة التفصيلية', index=False)
        
        # Sheet 2: Phase Summary
        phase_summary = df.groupby('المرحلة').agg({
            'الميزة': 'count',
            'التقدير (أيام)': 'sum'
        }).reset_index()
        phase_summary.columns = ['المرحلة', 'عدد الميزات', 'إجمالي الأيام']
        phase_summary.to_excel(writer, sheet_name='ملخص المراحل', index=False)
        
        # Sheet 3: By Priority
        priority_summary = df.groupby('الأولوية').agg({
            'الميزة': 'count',
            'التقدير (أيام)': 'sum'
        }).reset_index()
        priority_summary.columns = ['الأولوية', 'عدد الميزات', 'إجمالي الأيام']
        priority_summary.to_excel(writer, sheet_name='حسب الأولوية', index=False)
        
        # Sheet 4: By Status
        status_summary = df.groupby('الحالة').agg({
            'الميزة': 'count',
            'التقدير (أيام)': 'sum'
        }).reset_index()
        status_summary.columns = ['الحالة', 'عدد الميزات', 'إجمالي الأيام']
        status_summary.to_excel(writer, sheet_name='حسب الحالة', index=False)
    
    # Statistics
    total_features = len(df)
    total_days = df['التقدير (أيام)'].sum()
    ready_count = len(df[df['الحالة'] == 'جاهز'])
    in_progress_count = len(df[df['الحالة'] == 'قيد التنفيذ'])
    planned_count = len(df[df['الحالة'] == 'مخطط'])
    
    print("="*60)
    print("✅ تم إنشاء ملف ROADMAP.xlsx بنجاح!")
    print("="*60)
    print(f"📊 إجمالي الميزات: {total_features}")
    print(f"⏱️ إجمالي الأيام: {total_days} يوم ({total_days/30:.1f} شهر)")
    print(f"✅ جاهز: {ready_count}")
    print(f"🔄 قيد التنفيذ: {in_progress_count}")
    print(f"📋 مخطط: {planned_count}")
    print(f"📁 الملف: {output_path}")
    print("="*60)
    print("\n📑 الأوراق في الملف:")
    print("   1. الخطة التفصيلية")
    print("   2. ملخص المراحل")
    print("   3. حسب الأولوية")
    print("   4. حسب الحالة")
    print("="*60)

if __name__ == "__main__":
    try:
        create_excel_roadmap()
    except ImportError as e:
        print("⚠️ يرجى تثبيت المكتبات المطلوبة:")
        print("   pip install pandas openpyxl")
        print(f"\nخطأ: {e}")
