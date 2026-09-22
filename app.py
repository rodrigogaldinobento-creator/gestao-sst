import streamlit as st

# ==========================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Gestão SST - Lavouras Hasegawa",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. ESTILIZAÇÃO CSS CUSTOMIZADA (LAYOUT AZUL ESCURO & COMPACTO)
# ==========================================
st.markdown("""
    <style>
    /* Oculta elementos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Reduz espaçamentos do topo para caber tudo na tela */
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 2rem !important;
    }

    /* Estilização da Barra Lateral (Sidebar Escura Compacta) */
    [data-testid="stSidebar"] {
        background-color: #0d1b2a;
        color: #ffffff;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] .block-container {
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }
    
    /* Ajuste nos campos e botões da Sidebar */
    [data-testid="stSidebar"] input {
        color: #000000 !important;
        height: 35px;
    }
    [data-testid="stSidebar"] .stButton > button {
        background-color: #1b3a4b;
        color: #ffffff !important;
        border: 1px solid #274c5e;
        border-radius: 6px;
        width: 100%;
        padding: 4px 10px;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: #274c5e;
    }

    /* Reduz o espaçamento dos itens do Radio na Sidebar */
    [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
        font-size: 0.9rem;
        margin-bottom: 2px;
    }
    
    /* Cabeçalho Superior Fixo */
    .top-header {
        background-color: #0b1a2a;
        padding: 10px 20px;
        margin-top: -0.5rem;
        margin-left: -5rem;
        margin-right: -5rem;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 2px solid #1e3a5f;
    }
    .top-header-title {
        color: #ffffff;
        font-size: 1.15rem;
        font-weight: 700;
        margin: 0;
    }
    .top-header-sub {
        color: #94a3b8;
        font-size: 0.78rem;
        margin: 0;
    }
    .top-header-user {
        color: #ffffff;
        font-weight: 600;
        font-size: 0.9rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Card para pasta sem arquivos */
    .empty-folder-card {
        background-color: #f0f7ff;
        border: 1px solid #bae6fd;
        border-radius: 8px;
        padding: 18px 22px;
        display: flex;
        align-items: center;
        gap: 12px;
        color: #0284c7;
        margin-top: 15px;
    }

    /* Rodapé Fixo */
    .custom-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f8fafc;
        border-top: 1px solid #e2e8f0;
        padding: 6px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.75rem;
        color: #64748b;
        z-index: 999;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. GERENCIAMENTO DE ESTADO (PASTAS VAZIAS)
# ==========================================
if 'pastas_revisadas' not in st.session_state:
    st.session_state['pastas_revisadas'] = {
        "Auro": [],
        "Hayato": [],
        "Gabriely": []
    }

# ==========================================
# 4. BARRA LATERAL (SIDEBAR COMPACTA)
# ==========================================
with st.sidebar:
    st.markdown("### 🌾 Lavouras Hasegawa")
    st.markdown("**Gestão de SST**")
    st.caption("👤 Usuário: **Rodrigo**")
    
    if st.button("🔄 Recarregar Sistema"):
        st.rerun()
        
    st.text_input("🔑 Senha de Exclusão:", type="password", key="senha_exclusao")
    
    st.markdown("**Navegação**")
    
    menu_selecionado = st.radio(
        "Navegação",
        options=[
            "🏠 Início & Pontos Fortes SST",
            "📋 Temas Obrigatórios (Rascunho)",
            "📁 Documentos Não Revisados",
            "📂 Documentos Revisados",
            "📤 Upload de Documentos",
            "♻️ Restauração (Setor Oculto)"
        ],
        index=3, # Padrão: Documentos Revisados
        label_visibility="collapsed"
    )
    
    if st.button("🚪 Sair"):
        st.info("Sessão finalizada.")

# ==========================================
# 5. CABEÇALHO SUPERIOR
# ==========================================
st.markdown("""
    <div class="top-header">
        <div>
            <p class="top-header-title">Gestão SST</p>
            <p class="top-header-sub">Segurança • Saúde • Meio Ambiente</p>
        </div>
        <div class="top-header-user">
            <span style="background-color: #0284c7; color: white; padding: 2px 7px; border-radius: 50%; font-size: 0.8rem;">R</span>
            Rodrigo ▾
        </div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 6. CONTEÚDO PRINCIPAL
# ==========================================
if menu_selecionado == "📂 Documentos Revisados":
    
    st.title("📁 Repositório de Documentos Revisados")
    
    # Form para Criar Nova Subpasta
    with st.expander("➕ Criar Nova Pasta em Revisadas"):
        col_pai, col_nome, col_btn = st.columns([2, 3, 1])
        
        with col_pai:
            pasta_pai = st.selectbox("Pasta Principal (Responsável):", ["Auro", "Hayato", "Gabriely"])
            
        with col_nome:
            nova_subpasta = st.text_input("Nome da Nova Pasta:")
            
        with col_btn:
            st.write("")
            st.write("")
            if st.button("Criar Pasta", use_container_width=True):
                if nova_subpasta.strip():
                    if nova_subpasta not in st.session_state['pastas_revisadas'][pasta_pai]:
                        st.session_state['pastas_revisadas'][pasta_pai].append(nova_subpasta.strip())
                        st.success(f"Pasta '{nova_subpasta}' criada em {pasta_pai}!")
                        st.rerun()
                    else:
                        st.warning("Esta pasta já existe.")
                else:
                    st.error("Digite um nome válido.")

    st.markdown("##### **Selecione a Categoria/Pasta:**")
    
    # Seleção de Pastas
    col_resp, col_sub = st.columns(2)
    
    with col_resp:
        responsavel_sel = st.selectbox("Pasta Principal (Responsável):", ["Auro", "Hayato", "Gabriely"])
        
    with col_sub:
        lista_subpastas = st.session_state['pastas_revisadas'][responsavel_sel]
        if lista_subpastas:
            subpasta_sel = st.selectbox(f"Subpasta de {responsavel_sel}:", options=lista_subpastas)
        else:
            subpasta_sel = None
            st.selectbox(f"Subpasta de {responsavel_sel}:", options=["Nenhuma pasta criada"], disabled=True)

    st.markdown("---")

    # Exibição do Conteúdo da Pasta
    if subpasta_sel:
        st.markdown(f"#### 📂 Arquivos em: **{responsavel_sel} / {subpasta_sel}**")
    else:
        st.markdown(f"#### 📂 Arquivos em: **{responsavel_sel}**")
    
    # Card para estado sem arquivos
    st.markdown("""
        <div class="empty-folder-card">
            <span style="font-size: 1.5rem;">📄</span>
            <div>
                <strong>Nenhum arquivo encontrado nesta pasta.</strong><br>
                <span style="font-size: 0.85rem; opacity: 0.85;">Adicione documentos navegando até a opção "Upload de Documentos" no menu lateral.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

else:
    st.title(menu_selecionado)
    st.info("Módulo em desenvolvimento ou selecione 'Documentos Revisados' no menu lateral.")

# ==========================================
# 7. RODAPÉ FIXO
# ==========================================
st.markdown("""
    <div class="custom-footer">
        <span>🛡️ <b>Gestão SST</b> - Lavouras Hasegawa</span>
        <span>Segurança é um valor que se cultiva todos os dias! 🌱</span>
    </div>
""", unsafe_allow_html=True)
