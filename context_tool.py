import os

def read_context_file(query: str) -> str:
    """
    أداة استرجاع السياق المحدثة لعرض النص العربي مباشرة بالكامل.
    """
    file_name = "my_context.text"
    
    if not os.path.exists(file_name):
        return f"❌ خطأ: ملف السياق '{file_name}' غير موجود في المجلد الحالي."
        
    try:
        # قراءة الملف بطريقة ثنائية آمنة تمنع أخطاء التشفير نهائياً
        with open(file_name, "rb") as f:
            file_bytes = f.read()
            
        content = file_bytes.decode("utf-8", errors="ignore")
        
        # نعيد محتوى الملف النصي كاملاً ليقرأه المستخدم أو الوكيل بوضوح
        if content.strip():
            return f"📖 **إليك تفاصيل معلوماتك المخزنة في ملف السياق:**\n\n{content}"
        else:
            return "🔍 تم فتح ملفك النصي ولكنه فارغ حالياً، يرجى كتابة مهامك بداخله."
            
    except Exception as e:
        return f"❌ حدث خطأ أثناء معالجة الملف: {str(e)}"
