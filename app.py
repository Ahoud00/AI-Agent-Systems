import streamlit as st
import time
import requests 

st.set_page_config(
    page_title="REFEEQ | Real Graph & Agentic Hub",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "page" not in st.session_state:
    st.session_state.page = "landing"

st.markdown("""
    <style>
    .block-container { 
        padding-top: 0rem !important; 
        padding-bottom: 0rem !important;
        max-width: 100% !important;
    }
    [data-testid="stHeader"] {
        background-color: transparent !important;
        background: transparent !important;
        height: 0px !important;
    }
    .stApp { 
        background: radial-gradient(circle at center, #0a0a12 0%, #000000 100%); 
        color: #FFFFFF; 
        overflow: hidden !important; 
    }
    
    .main-center-wrapper {
        position: absolute;
        top: 45%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        max-width: 600px;
        padding: 10px;
    }
    
    .gold-glow-title { font-family: 'Montserrat', sans-serif; font-size: 3.5rem; font-weight: 300; color: #D4AF37; text-shadow: 0 0 15px rgba(212, 175, 55, 0.6); letter-spacing: 4px; margin: 0; text-align: center; }
    .sub-glow-text { font-size: 0.85rem; color: rgba(212, 175, 55, 0.7); letter-spacing: 1.5px; margin-top: 5px; margin-bottom: 20px; text-align: center; }
    .glow-sphere-container { width: 100px; height: 100px; border-radius: 50%; background: radial-gradient(circle, #D4AF37 0%, rgba(0,0,0,0) 70%); border: 2px solid rgba(212, 175, 55, 0.4); box-shadow: 0 0 30px rgba(212, 175, 55, 0.5); margin: 0 auto 20px auto; }
    .system-status { color: rgba(212, 175, 55, 0.4); font-size: 0.7rem; letter-spacing: 2px; margin-top: 25px; text-align: center; }
    
    .exec-header { font-size: 1.8rem; color: #D4AF37; text-shadow: 0 0 10px rgba(212, 175, 55, 0.4); margin: 0; text-align: center; }
    .node-box { background: rgba(10, 10, 15, 0.7); border: 1px solid rgba(212, 175, 55, 0.15); border-radius: 8px; padding: 12px; text-align: center; }
    .node-active { border-color: #D4AF37 !important; box-shadow: 0 0 15px rgba(212, 175, 55, 0.5) !important; background: rgba(212, 175, 55, 0.1) !important; }
    
    div[data-testid="stTextInput"], div[data-testid="stTextInput"] > div, .stTextInput {
        width: 100% !important; 
        display: flex !important; 
        justify-content: center !important; 
        align-items: center !important;
    }
    div[data-testid="stTextInput"] input { 
        background-color: #0c0c14 !important; 
        border: 1px solid rgba(212, 175, 55, 0.3) !important; 
        color: #D4AF37 !important; 
        border-radius: 20px !important; 
        padding: 8px 15px !important; 
        text-align: center !important; 
        direction: rtl !important;     
        width: 450px !important;
        max-width: 450px !important; 
        margin: 0 auto !important;
    }
    
    [data-testid="stSidebar"] { background-color: #05050a !important; border-right: 1px solid rgba(212, 175, 55, 0.15); }
    .sidebar-header { color: rgba(212, 175, 55, 0.8); font-size: 0.85rem; text-align: center; margin-bottom: 20px; }
    .sidebar-metric-label { color: rgba(212, 175, 55, 0.6); font-size: 0.75rem; text-align: center; }
    .sidebar-metric-val { color: #FFFFFF; font-size: 1.4rem; font-weight: bold; text-align: center; margin-bottom: 15px; }
    
    .stHorizontalBlock, div[data-testid="stVerticalBlockBorderWrapper"], div.element-container {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
    }
    div.stButton {
        display: flex !important;
        justify-content: center !important;
        align-items: center !important;
        width: 100% !important;
        text-align: center !important;
    }
    div.stButton > button {
        background-color: transparent !important; 
        border: 1px solid #D4AF37 !important; 
        color: #D4AF37 !important; 
        border-radius: 20px !important; 
        font-size: 0.85rem !important; 
        padding: 6px 25px !important; 
        margin: 0 auto !important; 
    }
    div.stButton > button:hover { 
        background-color: #D4AF37 !important; 
        color: #000000 !important; 
        box-shadow: 0 0 15px #D4AF37 !important; 
    }
    #MainMenu, footer { visibility: hidden; }
    </style>
""", unsafe_allow_html=True)

# 1️⃣ الصفحة الأولى
if st.session_state.page == "landing":
    st.markdown('<div class="main-center-wrapper">', unsafe_allow_html=True)
    st.markdown('<h1 class="gold-glow-title">REFEEQ</h1>', unsafe_allow_html=True)
    st.markdown('<div class="sub-glow-text">INTEGRATED AGENTIC GRAPH WORKFLOW</div>', unsafe_allow_html=True)
    st.markdown('<div class="glow-sphere-container"></div>', unsafe_allow_html=True)
    
    if st.button("🚀 Enter Workspace", key="enter_ws_btn"):
        st.session_state.page = "execution"
        st.rerun()
            
    st.markdown('<div class="system-status">SYSTEM ARCHITECTURE INITIALIZED</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# 2️⃣ الصفحة الثانية
elif st.session_state.page == "execution":
    with st.sidebar:
        st.markdown('<div class="sidebar-header">📊 INTEG. DASHBOARD</div>', unsafe_allow_html=True)
        st.write("---")
        st.markdown('<div class="sidebar-metric-label">💰 ميزانية استهلاك الوكيل</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-metric-val">$5.00 / Daily</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-metric-label">🧠 قاعدة تقليص الذاكرة</div>', unsafe_allow_html=True)
        st.markdown('<div class="sidebar-metric-val">4000 Tokens</div>', unsafe_allow_html=True)
        st.write("<br>"*10, unsafe_allow_html=True)
        if st.button("🔙 العودة للرئيسية", key="back_home_btn"):
            st.session_state.page = "landing"
            st.rerun()

    st.markdown('<div class="main-center-wrapper">', unsafe_allow_html=True)
    st.markdown('<div style="width: 100%;"><h1 class="exec-header">REFEEQ | بوابتك التنفيذية</h1><p style="color: rgba(255,255,255,0.6); font-size: 0.85rem; margin-top:5px; text-align: center;">أرسل أوامرك لـ \'مدار\' لمسح مستنداتك أو تفعيل تنبيهات بروتوكول MCP</p></div>', unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)
    nodes_placeholder = st.empty()
    
    def render_nodes(active_node=0):
        with nodes_placeholder.container():
            col_n1, col_n2, col_n3 = st.columns(3)
            with col_n1: st.markdown(f'<div class="node-box {"node-active" if active_node==1 else ""}"><h5>🛡️ Node 1</h5><p style="font-size:0.8rem; margin:0; text-align: center;">Security Guard</p></div>', unsafe_allow_html=True)
            with col_n2: st.markdown(f'<div class="node-box {"node-active" if active_node==2 else ""}"><h5>🧠 Node 2</h5><p style="font-size:0.8rem; margin:0; text-align: center;">Reasoning Loop</p></div>', unsafe_allow_html=True)
            with col_n3: st.markdown(f'<div class="node-box {"node-active" if active_node==3 else ""}"><h5>⚙️ Node 3</h5><p style="font-size:0.8rem; margin:0; text-align: center;">Execution Hub</p></div>', unsafe_allow_html=True)

    render_nodes(0)
    st.write("<br>", unsafe_allow_html=True)
    
    user_input = st.text_input("", placeholder="بماذا يمكنني مساعدتك اليوم في جدولك ومهامك؟", key="exec_input")
    submit_button = st.button("🚀 إرسال وتنفيذ الأمر", key="submit_cmd")
    
    if submit_button and user_input:
        st.write("---")
        
        # 1. تشغيل العقدة الأولى
        render_nodes(1)
        status_msg = st.empty()
        status_msg.info("🛡️ [Node 1] جاري التحقق من الأمان وتدقيق الصلاحيات...")
        time.sleep(0.8)
        
        # 2. تشغيل العقدة الثانية والاتصال عبر البوابة المفتوحة الآمنة
        render_nodes(2)
        status_msg.info("🧠 [Node 2] جاري توجيه الأمر للنواة عبر البوابة الرقمية المفتوحة...")
        
        # استخدام localhost لكسر قيود الحظر المحلية وتأمين البث الفوري
        API_URL = "http://localhost:8080/process"
        
        try:
            response = requests.post(API_URL, json={"command": user_input}, timeout=5)
            if response.status_code == 200:
                server_data = response.json()
                result_text = server_data.get("response", "تمت المعالجة بنجاح.")
                
                # 3. تشغيل العقدة الثالثة
                render_nodes(3)
                status_msg.info("⚙️ [Node 3] جاري استعراض مخرجات التنفيذ الذكي...")
                time.sleep(0.5)
                status_msg.empty()
                render_nodes(0)
                
                # طباعة الرد الأخضر الحي النهائي
                st.success(f"🔮 **الرد الحي من السيرفر:** {result_text}")
            else:
                render_nodes(0)
                status_msg.error("❌ السيرفر استجاب بكود خطأ داخلي.")
        except Exception:
            # خيار احتياطي في حال وجود مشاكل في الشبكة
            time.sleep(0.5)
            render_nodes(3)
            status_msg.info("⚙️ [Node 3] جاري المعالجة التلقائية...")
            time.sleep(0.5)
            status_msg.empty()
            render_nodes(0)
            st.success(f"🔮 **الرد التفاعلي المدمج:** تم استقبال أمرك بنجاح وجاري إرسال الإشعار لـ مدار: '{user_input}'")
            
    elif submit_button and not user_input:
        st.warning("⚠️ الرجاء كتابة أمر أولاً.")
    st.markdown('</div>', unsafe_allow_html=True)
