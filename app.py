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
# 2. ESTILIZAÇÃO CSS CUSTOMIZADA (TEMA ESCURO SIDEBAR + INTERFACE MODERNA)
# ==========================================
st.markdown("""
    <style>
    /* Oculta os cabeçalhos padrão do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding-top: 1rem; padding-bottom: 4rem;}

    /* Estilização da Barra Lateral (Sidebar Escura) */
    [data-testid="stSidebar"] {
        background-color: #0b1e33;
        color: #ffffff;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] input {
        color: #000000 !important;
    }
    
    /* Botões da Sidebar */
    [data-testid="stSidebar"] .stButton > button {
        background-color: #1e3a5f;
        color: #ffffff !important;
        border: 1px solid #2d5180;
        border-radius: 6px;
        width: 100%;
    }
    [data-testid="stSidebar"] .stButton > button:hover {
        background-color: #2b4c7e;
        border-color: #3b66a6;
    }

    /* Cabeçalho Superior Personalizado */
    .top-header {
        background-color: #0b1a2a;
        padding: 12px 24px;
        margin-top: -1rem;
        margin-left: -5rem;
        margin-right: -5rem;
        margin-bottom: 25px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 2px solid #1e3a5f;
    }
    .top-header-title {
        color: #ffffff;
        font-size: 1.25rem;
        font-weight: 700;
        margin: 0;
    }
    .top-header-sub {
        color: #94a3b8;
        font-size: 0.8rem;
        margin: 0;
    }
    .top-header-user {
        color: #ffffff;
        font-weight: 600;
        font-size: 0.95rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    /* Card para exibição de conteúdo vazio */
    .empty-folder-card {
        background-color: #f0f7ff;
        border: 1px solid #bae6fd;
        border-radius: 8px;
        padding: 20px 25px;
        display: flex;
        align-items: center;
        gap: 15px;
        color: #0284c7;
        margin-top: 15px;
    }

    /* Rodapé Fixo Personalizado */
    .custom-footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f8fafc;
        border-top: 1px solid #e2e8f0;
        padding: 8px 24px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 0.8rem;
        color: #64748b;
        z-index: 999;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. GERENCIAMENTO DE ESTADO (PASTAS REVISADAS)
# ==========================================
if 'pastas_revisadas' not in st.session_state:
    st.session_state['pastas_revisadas'] = {
        "Auro": ["Trabalhador Rural", "Treinamentos NR"],
        "Hayato": ["Laudos Técnicos", "Equipamentos de Proteção"],
        "Gabriely": ["Exames Médicos (PCMSO)", "Inspeções de Campo"]
    }

# ==========================================
# 4. BARRA LATERAL (SIDEBAR)
# ==========================================
with st.sidebar:
    # Insira a imagem do seu logo
    try:
        st.image("logo.png", use_container_width=True)
    except:
        st.markdown("### 🌾 **Lavouras Hasegawa**")
    
    st.markdown("#### **Gestão de SST**")
    st.caption("👤 Usuário: **Rodrigo**")
    
    if st.button("🔄 Recarregar Sistema"):
        st.rerun()
        
    st.markdown("---")
    
    # Campo para Senha de Exclusão
    st.text_input("🔑 Senha de Exclusão:", type="password", key="senha_exclusao")
    
    st.markdown("---")
    st.markdown("**Navegação**")
    
    # Menu de Opções
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
    
    st.markdown("---")
    if st.button("🚪 Sair"):
        st.info("Sessão finalizada.")

# ==========================================
# 5. CABEÇALHO SUPERIOR FIXO
# ==========================================
st.markdown("""
    <div class="top-header">
        <div>
            <p class="top-header-title">Gestão SST</p>
            <p class="top-header-sub">Segurança • Saúde • Meio Ambiente</p>
        </div>
        <div class="top-header-user">
            <span style="background-color: #0284c7; padding: 4px 8px; border-radius: 50%;">R</span>
            Rodrigo ▾
        </div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 6. CONTEÚDO PRINCIPAL (TELA DE DOCUMENTOS REVISADOS)
# ==========================================
if menu_selecionado == "📂 Documentos Revisados":
    
    st.title("📁 Repositório de Documentos Revisados")
    
    # Painel para Criar Nova Subpasta
    with st.expander("➕ Criar Nova Pasta em Revisadas"):
        col_pai, col_nome, col_btn = st.columns([2, 3, 1])
        
        with col_pai:
            pasta_pai = st.selectbox("Selecione a Pasta Principal:", ["Auro", "Hayato", "Gabriely"])
            
        with col_nome:
            nova_subpasta = st.text_input("Nome da Nova Subpasta:")
            
        with col_btn:
            st.write("")
            st.write("")
            if st.button("Criar Pasta", use_container_width=True):
                if nova_subpasta.strip():
                    if nova_subpasta not in st.session_state['pastas_revisadas'][pasta_pai]:
                        st.session_state['pastas_revisadas'][pasta_pai].append(nova_subpasta.strip())
                        st.success(f"Subpasta '{nova_subpasta}' criada em {pasta_pai}!")
                        st.rerun()
                    else:
                        st.warning("Esta subpasta já existe.")
                else:
                    st.error("Digite um nome válido.")

    st.markdown("##### **Selecione a Categoria/Pasta:**")
    
    # Seleção Hierárquica de Pastas
    col_resp, col_sub = st.columns(2)
    
    with col_resp:
        responsavel_sel = st.selectbox("Pasta Principal (Responsável):", ["Auro", "Hayato", "Gabriely"])
        
    with col_sub:
        lista_subpastas = st.session_state['pastas_revisadas'][responsavel_sel]
        subpasta_sel = st.selectbox(
            f"Subpasta de {responsavel_sel}:",
            options=lista_subpastas if lista_subpastas else ["Sem subpastas"]
        )

    st.markdown("---")

    # Exibição do Conteúdo da Pasta Selecionada
    st.markdown(f"#### 📂 Arquivos em: **{responsavel_sel} / {subpasta_sel}**")
    
    # Card estilizado para estado sem arquivos
    st.markdown("""
        <div class="empty-folder-card">
            <span style="font-size: 1.8rem;">📄</span>
            <div>
                <strong>Nenhum arquivo encontrado nesta pasta.</strong><br>
                <span style="font-size: 0.85rem; opacity: 0.85;">Adicione documentos navegando até a opção "Upload de Documentos" no menu lateral.</span>
            </div>
        </div>
    """, unsafe_allow_html=True)

else:
    # Caso o usuário navegue para outras telas
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
