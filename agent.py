import os
import json
from openai import OpenAI
from context_tool import read_context_file
from security_guard import inspect_input_for_injection

# 1. إعداد الاتصال بـ OpenRouter لطلب النماذج اللغوية الكبيرة
client = OpenAI(
    base_url="https://openrouter.ai",
    api_key=os.environ.get("OPENROUTER_API_KEY", "ضع_مفتاح_الـ_API_الخاص_بـ_openrouter_هنا")
)

# 2. تعريف بنية حالة الـ Graph (Graph State) لتتبع البيانات بين العقد
class AgentGraphState:
    def __init__(self, user_query: str):
        self.user_query = user_query
        self.current_node = "START"
        self.next_node = "None"
        self.response = ""
        self.tool_input = ""
        self.is_attack = False

# --- [Node 1: عقدة الفحص الأمني - Security Guard Node] ---
def security_node(state: AgentGraphState) -> AgentGraphState:
    state.current_node = "SECURITY_CHECK"
    is_attack, security_message = inspect_input_for_injection(state.user_query)
    
    if is_attack:
        state.is_attack = True
        state.response = security_message
        state.next_node = "END"
    else:
        state.next_node = "REASONING_NODE"
    return state

# --- [Node 2: عقدة التفكير واتخاذ القرار - Reasoning Node] ---
def reasoning_node(state: AgentGraphState) -> AgentGraphState:
    state.current_node = "REASONING"
    
    system_prompt = (
        "You are 'Madar' running inside a Graph Workflow node. Analyze the query and select a tool.\n"
        "Format response as strict JSON:\n"
        "{\n"
        "  \"tool_to_use\": \"read_context\" or \"send_mcp_alert\" or \"None\",\n"
        "  \"tool_input\": \"description\"\n"
        "}"
    )
    
    try:
        response = client.chat.completions.create(
            model="meta-llama/llama-3-8b-instruct:free",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": state.user_query}
            ],
            temperature=0
        )
        
        raw_content = response.choices.message.content.strip()
        if raw_content.startswith("```json"):
            raw_content = raw_content.replace("```json", "").replace("```", "").strip()
            
        decision = json.loads(raw_content)
        tool_name = decision.get("tool_to_use")
        state.tool_input = decision.get("tool_input")
        
        # التوجيه الشرطي والربط التلقائي للمسار (Conditional Routing / Edges)
        if tool_name == "read_context":
            state.next_node = "RETRIEVAL_NODE"
        elif tool_name == "send_mcp_alert":
            state.next_node = "HUMAN_APPROVAL_NODE"
        else:
            state.response = "💡 رفيق الإنتاجية: أعمل كـ Graph Agent ومستعد لمساعدتك في استرجاع سياق ملفاتك أو إرسال تنبيهات."
            state.next_node = "END"
            
    except Exception as e:
        state.next_node = "RETRIEVAL_NODE" # خطة الطوارئ البديلة للاسترجاع الآمن
    return state

# --- [Node 3: عقدة استرجاع معلومات الذاكرة - Retrieval Node] ---
def retrieval_node(state: AgentGraphState) -> AgentGraphState:
    state.current_node = "RETRIEVAL"
    state.response = read_context_file(state.tool_input)
    state.next_node = "END"
    return state

# 3. محرك المخطط التنفيذي وتشغيل الـ Graph (Graph Execution Engine)
def compile_and_run_graph(query: str):
    state = AgentGraphState(user_query=query)
    
    # محاكاة الانتقال المنظم عبر الـ Nodes & Edges
    state = security_node(state)
    
    if state.next_node == "REASONING_NODE":
        state = reasoning_node(state)
        
        if state.next_node == "RETRIEVAL_NODE":
            state = retrieval_node(state)
            
        elif state.next_node == "HUMAN_APPROVAL_NODE":
            # تعليق المسار وتمرير الطلب للموافقة البشرية في الواجهة
            return "HUMAN_APPROVAL_REQUIRED", state.tool_input
            
    return "SUCCESS", state.response
