#برنامه مون چیه
#یه تابع بنویسیم برای پیدا کردن کلمه
# بعد فایلو بیاد باز کنه
#تابع رو روش اعمال کنه

def replace(text, word, replaceword):
    wrds = text.split()
    for i in range(len(wrds)):
        if wrds[i] == word:
            wrds[i] = replaceword
    new_text = ' '.join(wrds)
    return new_text

with open('secndfile.txt', 'r') as f:
    content = f.read()
    contentt = replace(content, 'melika', 'dina')
    print(contentt)
