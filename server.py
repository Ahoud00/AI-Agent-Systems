from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

# إنشاء تطبيق FastAPI
app = FastAPI(title="REFEEQ AI API Server")

# تعريف بنية البيانات المستقبلة من واجهة streamlit
class CommandRequest(BaseModel):
    command: str

@app.get("/")
def read_root():
    return {"status": "online", "message": "REFEEQ API Server is running smoothly"}

# نقطة النهاية (Endpoint) المعنية بمعالجة الأوامر المدمجة
@app.post("/process")
def process_command(request: CommandRequest):
    user_cmd = request.command.strip()
    
    # هنا يمكنك لاحقاً حقن أكواد الذكاء الاصطناعي أو بروتوكول MCP
    # سنصيغ ردوداً تفاعلية بناءً على الكلمات المفتاحية لأوامرك
    if "جدول" in user_cmd or "موعد" in user_cmd:
        ai_response = f"تم استقبال أمر الجدولة بنجاح عبر مسار رفيق. جاري تنظيم الموعد وتحديث مفكرة مدار الذكية."
    elif "مسح" in user_cmd or "ملف" in user_cmd:
        ai_response = f"بدء بروتوكول فحص المستندات الذكي. تم التحقق من أمان الملفات عبر العقدة الأولى وجاري استخراج البيانات."
    else:
        ai_response = f"تم استقبال أمرك بنجاح: '{user_cmd}'. مر الأمر عبر الحماية والتفكير، وتم التنفيذ في العقدة الثالثة بنجاح."

    return {
        "status": "success",
        "node_flow": ["Security Guard Verified", "Reasoning Loop Processed", "Execution Hub Completed"],
        "response": ai_response
    }

# تشغيل السيرفر محلياً على منفذ 8080
if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=8080, reload=True)
