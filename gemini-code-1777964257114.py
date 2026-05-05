import streamlit as st
import pandas as pd
from datetime import date

# পেজ কনফিগারেশন
st.set_page_config(page_title="Zara Tech Mart", layout="wide")

# দোকানের তথ্য
SHOP_NAME = "Zara Tech Mart"
ADDRESS = "111/1 New Elephant Road, VIP Shopping Center, Dhaka 1205"
MOBILE = "01788130206, 01968308603"

# হেডার সেকশন
st.markdown(f"<h1 style='text-align: center; color: #d9534f;'>{SHOP_NAME}</h1>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align: center;'>{ADDRESS}<br>মোবাইল: {MOBILE}</p>", unsafe_allow_html=True)
st.write("---")

# ডেটাবেস লোড ফাংশন
def load_data():
    try:
        return pd.read_csv('zara_tech_records.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=["তারিখ", "কাস্টমার নাম", "পণ্যের বিবরণ", "পরিমাণ (টাকা)", "পেমেন্ট স্ট্যাটাস"])

data = load_data()

# সাইডবার মেনু
st.sidebar.title("মেনু")
choice = st.sidebar.radio("কাজ নির্বাচন করুন", ["ড্যাশবোর্ড", "নতুন মেমো/এন্ট্রি", "সব রিপোর্ট"])

if choice == "ড্যাশবোর্ড":
    st.subheader("📊 আজকের ব্যবসার অবস্থা")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("মোট কাস্টমার", len(data))
    with col2:
        total_sales = data["পরিমাণ (টাকা)"].sum() if not data.empty else 0
        st.metric("মোট বিক্রয়", f"{total_sales} টাকা")
    with col3:
        st.metric("তারিখ", str(date.today()))

elif choice == "নতুন মেমো/এন্ট্রি":
    st.subheader("📝 নতুন বিক্রয় বা সার্ভিস এন্ট্রি")
    with st.form("billing_form"):
        cust_name = st.text_input("কাস্টমারের নাম")
        item_details = st.text_area("পণ্য বা সার্ভিসের বিবরণ (যেমন: HP Laptop Repair)")
        amount = st.number_input("টাকার পরিমাণ", min_value=0)
        p_status = st.selectbox("পেমেন্ট স্ট্যাটাস", ["পেইড", "বাকি", "আংশিক"])
        submit = st.form_submit_button("রেকর্ড সেভ করুন")
        
        if submit:
            new_entry = {
                "তারিখ": date.today(),
                "কাস্টমার নাম": cust_name,
                "পণ্যের বিবরণ": item_details,
                "পরিমাণ (টাকা)": amount,
                "পেমেন্ট স্ট্যাটাস": p_status
            }
            data = pd.concat([data, pd.DataFrame([new_entry])], ignore_index=True)
            data.to_csv('zara_tech_records.csv', index=False)
            st.success(f"{cust_name}-এর রেকর্ড সফলভাবে সেভ হয়েছে!")

elif choice == "সব রিপোর্ট":
    st.subheader("📋 সব বিক্রয় ও সার্ভিসের তালিকা")
    if not data.empty:
        st.dataframe(data, use_container_width=True)
        # এক্সেল ফাইল হিসেবে ডাউনলোড
        csv = data.to_csv(index=False).encode('utf-8')
        st.download_button("Excel ফাইল ডাউনলোড করুন", csv, "Zara_Tech_Report.csv", "text/csv")
    else:
        st.info("এখনো কোনো রেকর্ড নেই।")