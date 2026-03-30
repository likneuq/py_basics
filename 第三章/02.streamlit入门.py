import streamlit as st

# 设置页面的配置项
st.set_page_config(
    page_title="Streamlit入门",
    page_icon="🧊",
    # 布局
    layout="wide",
    # 控制的是侧边栏的状态
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("Streamlit 入门演示")
st.header("Streamlit 一级标题")
st.subheader("Streamlit 二级标题")

# 段落文字
st.write("布偶猫，猫中名副其实的“小仙女”与“温柔巨人”。这个品种诞生于20世纪60年代的美国，以其惊艳的外表和极为甜美的性格，赢得了无数爱猫人士的倾心。")
st.write("布偶猫最令人过目不忘的，是其丝绒般顺滑的中长型被毛和独特的重点色图案。它们拥有如海水般清澈湛蓝的湛蓝双眸，仿佛盛满了一汪清泉。身体主要部分为浅色，而在面部、耳朵、四肢和尾巴这些“重点”区域，则呈现出海豹色、蓝色、巧克力色等深邃而优雅的色块，对比鲜明，宛如自带妆容。")
st.write("然而，比外貌更迷人的是它们的性格。布偶猫以温顺、对人极度友善而闻名。它们非常享受与主人的亲密互动，当你抱起它时，它会完全放松身体，柔软得像一块精美的布娃娃，这也是其名字的由来。它们不是孤高的猫，反而会像忠诚的小狗一样跟在你脚边，用温柔的声音表达依赖。布偶猫聪明、忍耐力强，是非常理想的家庭伴侣猫。若你向往一份毫无保留的温柔陪伴，布偶猫定会是你生活中最甜美的那抹色彩。")

# 图片
# st.image("./resources/cat.jpg")
st.image("resources/cat.jpg")

# 音频
st.audio("resources/news.mp3")

# 视频
st.video("resources/news.mp4")

# Logo
st.logo("resources/logo.png")

# 表格
student_data = {
    "姓名": ["王林", "李慕婉", "贝洛", "莫厉海", "石萧"],
    "学号": ["20260001", "20260002", "20260003", "20260004", "20260005"],
    "语文": [98, 90, 59, 29, 80],
    "数学": [88, 78, 65, 70, 39],
    "英语": [99, 89, 87, 59, 62],
    "总分": [285, 257, 211, 158, 181]
}
st.table(student_data)

# 输入框
name = st.text_input("请输入姓名")
st.write(f"您输入的姓名为: {name}")

# 密码输入框
password = st.text_input("请输入密码", type="password")
st.write(f"您输入的密码为: {password}")

# 单选按钮
gender = st.radio("请输入您的性别", ["男", "女", "未知"], index=2)
st.write(f"您的性别为: {gender}")