import os
import datetime
import jdatetime

def file_info(input_file, output_file):
  
    with open(input_file, 'r') as f:
        content = f.read()

  
    char_count = len(content)
    word_count = len(content.split())

    created_timestamp = os.path.getctime(input_file)
    created_datetime = datetime.datetime.fromtimestamp(created_timestamp)
    shamsi_datetime = jdatetime.datetime.fromgregorian(datetime=created_datetime)

 
    report = (
        f"نام فایل: {input_file}\n"
        f"تعداد کاراکترها: {char_count}\n"
        f"تعداد کلمات: {word_count}\n"
        f"تاریخ ایجاد (میلادی): {created_datetime.strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"تاریخ ایجاد (شمسی): {shamsi_datetime.strftime('%Y/%m/%d %H:%M:%S')}\n"
    )

 th open(output_file, 'w') as f:
        f.write(report)

    print(f"✅ اطلاعات با موفقیت در '{output_file}' ذخیره شد.")


file_info("scndfile.txt", "info_report.txt")

