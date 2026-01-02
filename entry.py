import streamlit as st
import pandas as pd

# ページ設定：若手向けにモダンなレイアウト
st.set_page_config(page_title="RE-PRO BOOTCAMP | 採用特設", layout="wide")

# カスタムCSS：IT企業のような洗練されたデザイン
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        font-weight: bold;
        font-size: 16px;
    }
    .skill-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🛡️ REAL ESTATE PROFESSIONAL BOOTCAMP")
st.subheader("「勘と根性」の時代は終わった。データで勝つコンサルタントへ。")

# 採用コンセプト
st.info("このアプリは、あなたが弊社で『1年以内にプロ』になるための育成工程を可視化したものです。")

tab1, tab2, tab3 = st.tabs(["🔥 成長シミュレーション", "📊 習得スキル体系", "✉️ エントリー"])

# --- TAB 1: 成長シミュレーション ---
with tab1:
    st.markdown("### 📅 入社1年目のリアルな航海図")
    phase = st.select_slider(
        "現在のフェーズを選択",
        options=["入社直後", "3ヶ月目", "半年後", "1年後"],
        key="growth_slider"
    )
    
    col1, col2 = st.columns([2, 1])
    
    if phase == "入社直後":
        with col1:
            st.markdown("#### 📖 基礎：徹底した「言語化」研修")
            st.write("まずは先輩の商談に全て同行。現場で何が起きているか、弊社の『標準ロードマップ』を見ながら答え合わせをします。")
            st.markdown("""
            * **メインミッション**: 物件の「履歴」を読み解く（登記簿・公図の解読）
            * **サポート体制**: 全商談の録音・ログを振り返り、先輩からフィードバック
            """)
        with col2:
            st.metric(label="リーガル知識", value="Lv.10", delta="START")
            st.metric(label="交渉力", value="Lv.5", delta="START")

    elif phase == "3ヶ月目":
        with col1:
            st.markdown("#### 🔍 調査：不動産の『真実』を見抜く")
            st.write("役所調査や現地調査を一人で担当。表面上の綺麗さではなく、法令や埋設管など『プロにしか見えないリスク』を特定します。")
            st.markdown("""
            * **メインミッション**: 完璧な『物件調査報告書』の作成
            * **プロの技**: 境界標の有無から、隣人との関係性までをプロファイリング
            """)
        with col2:
            st.metric(label="調査スキル", value="Lv.45", delta="+35")
            st.metric(label="分析力", value="Lv.30", delta="+25")

    elif phase == "半年後":
        with col1:
            st.markdown("#### 🤝 受託：顧客のパートナーへ")
            st.write("いよいよ媒介契約（売却依頼）を一人で獲得するフェーズ。データに基づいた『根拠ある査定』を武器に戦います。")
            st.markdown("""
            * **メインミッション**: 初めての媒介契約獲得
            * **武器**: 自社開発のマーケット分析ツールと価格交渉ロジック
            """)
        with col2:
            st.metric(label="プレゼン力", value="Lv.65", delta="+35")
            st.metric(label="受託スキル", value="Lv.50", delta="+50")

    elif phase == "1年後":
        with col1:
            st.markdown("#### 🏆 完結：1億円以上の資産を動かす")
            st.write("決済・引渡しを完遂。顧客から『あなたに頼んでよかった』と言われる感動を味わい、プロとして独り立ちします。")
            st.markdown("""
            * **メインミッション**: 年間成約目標の達成
            * **次のステップ**: チームリーダーとして後輩の育成・マネジメントへ
            """)
        with col2:
            st.metric(label="年収イメージ", value="600万〜", delta="Top 10%")
            st.metric(label="顧客満足度", value="98%", delta="High")

# --- TAB 2: 習得スキル体系 ---
with tab2:
    st.markdown("### 🏆 弊社で手に入る「一生モノ」のスキル")
    
    
    s_col1, s_col2, s_col3 = st.columns(3)
    with s_col1:
        st.markdown('<div class="skill-card"><b>🏛️ 法務・鑑定</b><br>建築基準法や都市計画法を読み解き、土地の真の価値を鑑定する力。</div>', unsafe_allow_html=True)
    with s_col2:
        st.markdown('<div class="skill-card"><b>💰 金融・税務</b><br>住宅ローン控除や相続税対策など、FP級の資産設計アドバイス力。</div>', unsafe_allow_html=True)
    with s_col3:
        st.markdown('<div class="skill-card"><b>交渉心理学</b><br>Win-Winの合意点を見極める、一生モノのコミュニケーション能力。</div>', unsafe_allow_html=True)

# --- TAB 3: エントリー ---
with tab3:
    st.markdown("### 🚀 未来のプロフェッショナルへ")
    st.write("私たちは、単に家を売る人を求めているのではありません。")
    st.write("顧客の人生の岐路に立ち、プロとして最高の選択肢を提示できる。そんな仲間を探しています。")
    
    with st.form("entry_form"):
        name = st.text_input("氏名（またはニックネーム）")
        email = st.text_input("メールアドレス")
        message = st.text_area("あなたがこのロードマップで一番興味を持った工程は？")
        submitted = st.form_submit_button("カジュアル面談を申し込む")
        if submitted:
            st.success(f"{name}さん、エントリーありがとうございます。後ほど担当者よりご連絡いたします。")

st.divider()
st.caption("© 2024 Your Professional Real Estate Team. すべての教育工程を言語化し、あなたの挑戦を支えます。")