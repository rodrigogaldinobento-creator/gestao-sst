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

# Inicializar o repositório de pastas e arquivos no session_state
if 'pastas_revisadas' not in st.session_state:
    st.session_state['pastas_revisadas'] = {
        "Auro": {},
        "Hayato": {},
        "Gabriely": {}
    }

# ==========================================
# 2. ESTILIZAÇÃO CSS CUSTOMIZADA (SIDEBAR FIXA E VISÍVEL)
# ==========================================
st.markdown("""
    <style>
    /* Esconde elementos padrões do Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* FORÇA A SIDEBAR A FICAR VISÍVEL E FIXA */
    [data-testid="stSidebar"] {
        display: block !important;
        visibility: visible !important;
        background-color: #0d1b2a !important;
        min-width: 280px !important;
        max-width: 280px !important;
    }
    
    /* Garante visibilidade do texto dentro da sidebar */
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Esconde apenas o botão de fechar a sidebar para mantê-la travada */
    [data-testid="stSidebarCollapseButton"] {
        display: none !important;
    }
    
    .block-container {
        padding-top: 0.5rem !important;
        padding-bottom: 2rem !important;
    }

    /* Estilização de inputs e botões da sidebar */
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

    /* Cards Informativos */
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
# 3. BARRA LATERAL (SIDEBAR FIXA E COMPACTA)
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
# 4. CABEÇALHO SUPERIOR
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
# 5. MÓDULO: DOCUMENTOS REVISADOS
# ==========================================
if menu_selecionado == "📂 Documentos Revisados":
    
    st.title("📁 Repositório de Documentos Revisados")
    
    # Criar Nova Subpasta
    with st.expander("➕ Criar Nova Pasta em Revisadas"):
        col_pai, col_nome, col_btn = st.columns([2, 3, 1])
        
        with col_pai:
            pasta_pai = st.selectbox("Pasta Principal (Responsável):", ["Auro", "Hayato", "Gabriely"], key="pai_criar")
            
        with col_nome:
            nova_subpasta = st.text_input("Nome da Nova Pasta:")
            
        with col_btn:
            st.write("")
            st.write("")
            if st.button("Criar Pasta", use_container_width=True):
                nome_limpo = nova_subpasta.strip()
                if nome_limpo:
                    if nome_limpo not in st.session_state['pastas_revisadas'][pasta_pai]:
                        st.session_state['pastas_revisadas'][pasta_pai][nome_limpo] = []
                        st.success(f"Pasta '{nome_limpo}' criada em {pasta_pai}!")
                        st.rerun()
                    else:
                        st.warning("Esta pasta já existe.")
                else:
                    st.error("Digite um nome válido.")

    st.markdown("##### **Selecione a Categoria/Pasta:**")
    
    # Seleção de Pastas
    col_resp, col_sub = st.columns(2)
    
    with col_resp:
        responsavel_sel = st.selectbox("Pasta Principal (Responsável):", ["Auro", "Hayato", "Gabriely"], key="resp_ver")
        
    with col_sub:
        subpastas_existentes = list(st.session_state['pastas_revisadas'][responsavel_sel].keys())
        if subpastas_existentes:
            subpasta_sel = st.selectbox(f"Subpasta de {responsavel_sel}:", options=subpastas_existentes)
        else:
            subpasta_sel = None
            st.selectbox(f"Subpasta de {responsavel_sel}:", options=["Nenhuma pasta criada"], disabled=True)

    st.markdown("---")

    # Exibição de Conteúdo e Arquivos
    if subpasta_sel:
        st.markdown(f"#### 📂 Arquivos em: **{responsavel_sel} / {subpasta_sel}**")
        arquivos = st.session_state['pastas_revisadas'][responsavel_sel][subpasta_sel]
        
        if arquivos:
            for arq in arquivos:
                st.markdown(f"📄 **{arq['nome']}** _({arq['tamanho']} bytes)_")
        else:
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
        st.info(f"Crie uma pasta em '{responsavel_sel}' para começar a enviar e visualizar documentos.")

# ==========================================
# 6. MÓDULO: UPLOAD DE DOCUMENTOS
# ==========================================
elif menu_selecionado == "📤 Upload de Documentos":
    st.title("📤 Envio de Documentos")
    
    col_u1, col_u2 = st.columns(2)
    
    with col_u1:
        resp_upload = st.selectbox("Selecione o Responsável:", ["Auro", "Hayato", "Gabriely"], key="upload_resp")
        
    with col_u2:
        subpastas_upload = list(st.session_state['pastas_revisadas'][resp_upload].keys())
        if subpastas_upload:
            sub_upload = st.selectbox(f"Selecione a Pasta de Destino:", options=subpastas_upload, key="upload_sub")
        else:
            sub_upload = None
            st.selectbox("Selecione a Pasta de Destino:", options=["Nenhuma pasta cadastrada"], disabled=True)
            st.warning(f"Crie primeiro uma pasta dentro de '{resp_upload}' para enviar arquivos.")

    if sub_upload:
        uploaded_files = st.file_uploader(
            f"Escolha os arquivos para anexar em {resp_upload} / {sub_upload}:",
            accept_multiple_files=True
        )
        
        if uploaded_files:
            if st.button("Confirmar e Salvar Documentos"):
                for file in uploaded_files:
                    dados_arquivo = {"nome": file.name, "tamanho": file.size}
                    st.session_state['pastas_revisadas'][resp_upload][sub_upload].append(dados_arquivo)
                st.success(f"{len(uploaded_files)} arquivo(s) enviado(s) com sucesso para {resp_upload} / {sub_upload}!")

else:
    st.title(menu_selecionado)
    st.info("Módulo em desenvolvimento.")

# ==========================================
# 7. RODAPÉ FIXO
# ==========================================
st.markdown("""
    <div class="custom-footer">
        <span>🛡️ <b>Gestão SST</b> - Lavouras Hasegawa</span>
        <span>Segurança é um valor que se cultiva todos os dias! 🌱</span>
    </div>
""", unsafe_allow_html=True)
