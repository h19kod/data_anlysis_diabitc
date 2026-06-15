import pandas as pd
from faker import Faker
import random

# إعداد المكتبة لإنشاء بيانات باللغة العربية
fake = Faker('ar_AA')

# دالة لإنشاء البيانات
def generate_diabetes_data(num_records=1000):
    data = []
    for _ in range(num_records):
        data.append({
            'الاسم': fake.name(),
            'العمر': random.randint(18, 90),
            'العنوان': fake.address().replace('\n', ', '),
            'مستوى الجلوكوز': random.randint(70, 200),
            'ضغط الدم': random.randint(80, 160),
            'مؤشر كتلة الجسم (BMI)': round(random.uniform(18.5, 40.0), 1),
            'مصاب بالسكري': random.choice(['نعم', 'لا'])
        })
    return pd.DataFrame(data)

# إنشاء 1000 سجل
df = generate_diabetes_data(1000)

# حفظ الملف بصيغة إكسل
df.to_excel('diabetes_patients_data.xlsx', index=False)
print("تم إنشاء ملف 'diabetes_patients_data.xlsx' بنجاح!")
