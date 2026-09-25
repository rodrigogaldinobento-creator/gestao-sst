import streamlit as st
import streamlit.components.v1 as components
import datetime

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
# 2. INICIALIZAÇÃO DE ESTADOS (SESSÃO)
# ==========================================
if 'pastas_revisadas' not in st.session_state:
    st.session_state['pastas_revisadas'] = {
        "Auro": {},
        "Hayato": {},
        "Gabriely": {}
    }

if 'colaboradores' not in st.session_state:
    st.session_state['colaboradores'] = [
        {"nome": "Rodrigo Galdino Bento", "funcao": "Técnico em Segurança do Trabalho (TST)", "setor": "EQUIPE PLANTIO DE BATATAS"},
        {"nome": "Márcia Bueno Machado", "funcao": "Auxiliar Administrativo / SST", "setor": "EQUIPE PLANTIO DE BATATAS"},
        {"nome": "Adenir De Matos Machado", "funcao": "Chefe de Pátio", "setor": "EQUIPE PLANTIO DE BATATAS"},
        {"nome": "Alex de Jesus Daum", "funcao": "Tratorista", "setor": "EQUIPE PLANTIO DE BATATAS"},
        {"nome": "Alessandro Pires Ribeiro", "funcao": "Trab. Rural Masc.", "setor": "EQUIPE PLANTIO DE BATATAS"}
    ]

# ==========================================
# 3. ESTILIZAÇÃO CSS CUSTOMIZADA
# ==========================================
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Botão de abrir/fechar a barra lateral */
    [data-testid="stSidebarCollapsedControl"] {
        display: block !important;
        visibility: visible !important;
        color: #ffffff !important;
        background-color: #0d1b2a !important;
        border-radius: 4px;
        z-index: 999999 !important;
    }

    /* Estilização da Sidebar Escura */
    [data-testid="stSidebar"] {
        background-color: #0d1b2a !important;
    }
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    [data-testid="stSidebar"] input {
        color: #000000 !important;
    }
    [data-testid="stSidebar"] .stButton > button {
        background-color: #1b3a4b;
        color: #ffffff !important;
        border: 1px solid #274c5e;
        border-radius: 6px;
        width: 100%;
    }

    /* Cabeçalho Superior Fixo */
    .top-header {
        background-color: #0b1a2a;
        padding: 10px 20px;
        margin-top: -1rem;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 2px solid #1e3a5f;
    }
    .top-header-title { color: #ffffff; font-size: 1.15rem; font-weight: 700; margin: 0; }
    .top-header-sub { color: #94a3b8; font-size: 0.78rem; margin: 0; }
    .top-header-user { color: #ffffff; font-weight: 600; font-size: 0.9rem; display: flex; align-items: center; gap: 8px; }

    /* Rodapé Fixo */
    .custom-footer {
        position: fixed; bottom: 0; left: 0; width: 100%;
        background-color: #f8fafc; border-top: 1px solid #e2e8f0;
        padding: 6px 20px; display: flex; justify-content: space-between;
        font-size: 0.75rem; color: #64748b; z-index: 999;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 4. BARRA LATERAL (SIDEBAR COM LOGO DEDICADO)
# ==========================================
with st.sidebar:
    # Tenta carregar o logótipo oficial cadastrado no GitHub (Logo.png)
    try:
        st.image("Logo.png", use_container_width=True)
    except:
        st.markdown("### 🌾 **Lavouras Hasegawa**")
        
    st.markdown("#### **Gestão de SST**")
    st.caption("👤 Usuário: **Rodrigo**")
    
    if st.button("🔄 Recarregar Sistema"):
        st.rerun()
        
    st.text_input("🔑 Senha de Exclusão:", type="password", key="senha_exclusao")
    st.markdown("**Navegação**")
    
    menu_selecionado = st.radio(
        "Navegação",
        options=[
            "🏠 Início & Pontos Fortes SST",
            "📝 Emissão de DDS",
            "👥 Cadastro de Colaboradores",
            "📂 Documentos Revisados",
            "📤 Upload de Documentos",
            "♻️ Restauração (Setor Oculto)"
        ],
        index=2,
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
# 6. MÓDULO: EMISSÃO DE DDS
# ==========================================
if menu_selecionado == "📝 Emissão de DDS":
    st.title("📝 Gerador de DDS (Registro de Treinamento)")
    
    opcoes_setor = ["EQUIPE PLANTIO DE BATATAS", "EQUIPE DE COLHEITA", "ADMINISTRATIVO", "MECANIZAÇÃO"]
    
    with st.form("form_dds"):
        st.subheader("1. Informações do Treinamento")
        col_d1, col_d2, col_d3 = st.columns(3)
        
        with col_d1:
            setor = st.selectbox("Setor / Equipe:", opcoes_setor)
            instrutor = st.text_input("Instrutor(es):", value="Rodrigo Galdino Bento - TST")
            
        with col_d2:
            data_dds = st.date_input("Data do Treinamento:", datetime.date.today())
            carga_horaria = st.text_input("Carga Horária:", value="15 min")
            
        with col_d3:
            responsavel_salvar = st.selectbox("Salvar na pasta de:", ["Auro", "Hayato", "Gabriely"])
        
        assuntos = st.text_area(
            "Assuntos Abordados:",
            value="CUIDADOS E PROCEDIMENTOS CORRETOS DURANTE O PLANTIO; USO CORRETO DE EPIS, ATENÇÃO DURANTE ATIVIDADES PLANTIO E MANUTENÇÕES, CUIDADOS COM USO DE AGROTÓXICOS.",
            height=80
        )
        
        st.markdown("---")
        st.subheader("2. Filtro de Colaboradores por Função")
        
        funcoes_disponiveis = list(set([c["funcao"] for c in st.session_state['colaboradores']]))
        funcoes_selecionadas = st.multiselect("Filtrar por Função(ões):", options=funcoes_disponiveis, default=funcoes_disponiveis)
        
        colabs_filtrados = [c for c in st.session_state['colaboradores'] if c["funcao"] in funcoes_selecionadas]
        
        st.markdown("##### **Lista de Presença:**")
        
        presencas = {}
        cols_pres = st.columns(2)
        for idx, colab in enumerate(colabs_filtrados):
            col = cols_pres[idx % 2]
            presencas[colab["nome"]] = col.checkbox(
                f"{colab['nome']} - *{colab['funcao']}*", 
                value=True, 
                key=f"pres_{idx}"
            )
            
        gerar_btn = st.form_submit_button("📄 Gerar e Imprimir Registro de DDS")

    if gerar_btn:
        st.markdown("---")
        st.success("DDS gerado com sucesso!")
        
        linhas_tabela = ""
        for colab in colabs_filtrados:
            if presencas.get(colab["nome"]):
                linhas_tabela += f"""
                <tr>
                    <td style="border: 1px solid #000; padding: 6px;">{colab['nome']}</td>
                    <td style="border: 1px solid #000; padding: 6px;">{colab['funcao']}</td>
                    <td style="border: 1px solid #000; padding: 6px; text-align: center; color: #888;">___________________</td>
                </tr>
                """
        
        documento_html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                body {{ font-family: Arial, sans-serif; background-color: #fff; margin: 0; padding: 10px; }}
                .paper {{ border: 2px solid #000; padding: 15px; background: #fff; }}
                table {{ width: 100%; border-collapse: collapse; margin-top: 10px; font-size: 13px; }}
                th, td {{ border: 1px solid #000; padding: 6px; text-align: left; }}
                .header-tbl td {{ text-align: center; font-weight: bold; }}
            </style>
        </head>
        <body>
            <div class="paper">
                <table class="header-tbl">
                    <tr>
                        <td style="width: 25%;">LAVOURAS HASEGAWA</td>
                        <td style="width: 50%;">REGISTRO DE TREINAMENTO PADRÃO<br><small>TIPO DE TREINAMENTO: DDS</small></td>
                        <td style="width: 25%;">SEGURANÇA DO TRABALHO</td>
                    </tr>
                </table>
                
                <table>
                    <tr>
                        <td colspan="3"><b>ASSUNTOS ABORDADOS:</b> {assuntos}</td>
                        <td><b>SETOR:</b> {setor}</td>
                    </tr>
                    <tr>
                        <td style="width: 40%;"><b>INSTRUTOR(ES):</b> {instrutor}</td>
                        <td style="width: 20%;"><b>DATA:</b> {data_dds.strftime('%d/%m/%Y')}</td>
                        <td colspan="2" style="width: 40%;"><b>CARGA HORÁRIA:</b> {carga_horaria}</td>
                    </tr>
                </table>

                <table>
                    <thead>
                        <tr style="background-color: #f2f2f2;">
                            <th style="width: 45%;">Nome do Colaborador</th>
                            <th style="width: 35%;">Função</th>
                            <th style="width: 20%;">Assinatura</th>
                        </tr>
                    </thead>
                    <tbody>
                        {linhas_tabela}
                    </tbody>
                </table>
            </div>
        </body>
        </html>
        """
        
        components.html(documento_html, height=500, scrolling=True)
        
        nome_doc = f"DDS_{data_dds.strftime('%Y%m%d')}_{setor.replace(' ', '_')}.pdf"
        if "DDS_Emitidos" not in st.session_state['pastas_revisadas'][responsavel_salvar]:
            st.session_state['pastas_revisadas'][responsavel_salvar]["DDS_Emitidos"] = []
            
        st.session_state['pastas_revisadas'][responsavel_salvar]["DDS_Emitidos"].append({
            "nome": nome_doc,
            "tamanho": 1024
        })
        st.info(f"💾 Documento gravado automaticamente na pasta: **{responsavel_salvar} / DDS_Emitidos**")

# ==========================================
# 7. MÓDULO: CADASTRO DE COLABORADORES
# ==========================================
elif menu_selecionado == "👥 Cadastro de Colaboradores":
    st.title("👥 Cadastro Base de Funcionários")
    
    with st.expander("➕ Cadastrar Novo Colaborador"):
        c1, c2, c3 = st.columns(3)
        with c1:
            novo_nome = st.text_input("Nome do Colaborador:")
        with c2:
            nova_funcao = st.text_input("Função / Cargo:")
        with c3:
            novo_setor = st.selectbox("Setor:", ["EQUIPE PLANTIO DE BATATAS", "EQUIPE DE COLHEITA", "ADMINISTRATIVO", "MECANIZAÇÃO"])
            
        if st.button("Cadastrar Funcionário"):
            if novo_nome and nova_funcao:
                st.session_state['colaboradores'].append({
                    "nome": novo_nome,
                    "funcao": nova_funcao,
                    "setor": novo_setor
                })
                st.success(f"Colaborador {novo_nome} cadastrado com sucesso!")
                st.rerun()

    st.markdown("##### **Colaboradores Cadastrados:**")
    st.dataframe(st.session_state['colaboradores'], use_container_width=True)

# ==========================================
# 8. MÓDULO: DOCUMENTOS REVISADOS
# ==========================================
elif menu_selecionado == "📂 Documentos Revisados":
    st.title("📁 Repositório de Documentos Revisados")
    
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

    if subpasta_sel:
        st.markdown(f"#### 📂 Arquivos em: **{responsavel_sel} / {subpasta_sel}**")
        arquivos = st.session_state['pastas_revisadas'][responsavel_sel][subpasta_sel]
        
        if arquivos:
            for arq in arquivos:
                st.markdown(f"📄 **{arq['nome']}**")
        else:
            st.info("Nenhum arquivo encontrado nesta pasta.")
    else:
        st.info(f"Crie uma pasta em '{responsavel_sel}' para começar a enviar e visualizar documentos.")

# ==========================================
# 9. MÓDULO: UPLOAD DE DOCUMENTOS
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
# 10. RODAPÉ FIXO
# ==========================================
st.markdown("""
    <div class="custom-footer">
        <span>🛡️ <b>Gestão SST</b> - Lavouras Hasegawa</span>
        <span>Segurança é um valor que se cultiva todos os dias! 🌱</span>
    </div>
""", unsafe_allow_html=True)
