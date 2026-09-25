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
# 3. ESTILIZAÇÃO CSS CUSTOMIZADA (NATURAL E SEGURA)
# ==========================================
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Customização da Sidebar */
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
# 4. BARRA LATERAL (SIDEBAR)
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
            "📝 Emissão de DDS",
            "👥 Cadastro de Colaboradores",
            "📂 Documentos Revisados",
            "📤 Upload de Documentos",
            "♻️ Restauração (Setor Oculto)"
        ],
        index=1,
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
        
        # Construção da lista de linhas da tabela
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
        
        # HTML completo renderizado com iframe isolado
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
        
        # Exibe a folha formatada usando componente HTML limpo
        components.html(documento_html, height=500, scrolling=True)
        
        # Salva o arquivo no repositório
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

else:
    st.title(menu_selecionado)
    st.info("Módulo em desenvolvimento.")

# ==========================================
# 8. RODAPÉ FIXO
# ==========================================
st.markdown("""
    <div class="custom-footer">
        <span>🛡️ <b>Gestão SST</b> - Lavouras Hasegawa</span>
        <span>Segurança é um valor que se cultiva todos os dias! 🌱</span>
    </div>
""", unsafe_allow_html=True)
