import os
import shutil
import time
import streamlit as st

# -----------------------------------------------------------------------------
# CONFIGURAÇÃO DA PÁGINA
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Gestão SST",
    page_icon="🛡️",
    layout="wide"
)

# Direcionamento de diretórios/pastas
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REVISADAS_DIR = os.path.join(BASE_DIR, "revisadas")
NAO_REVISADAS_DIR = os.path.join(BASE_DIR, "nao_revisadas")
RASCUNHOS_DIR = os.path.join(BASE_DIR, "rascunhos")
LIXEIRA_DIR = os.path.join(BASE_DIR, ".lixeira")

# Verificação do Logo na pasta
LOGO_PATH = os.path.join(BASE_DIR, "Logo.png")
if not os.path.exists(LOGO_PATH):
    LOGO_PATH = os.path.join(BASE_DIR, "logo.png")

# Garantir criação das pastas principais
os.makedirs(REVISADAS_DIR, exist_ok=True)
os.makedirs(NAO_REVISADAS_DIR, exist_ok=True)
os.makedirs(RASCUNHOS_DIR, exist_ok=True)
os.makedirs(LIXEIRA_DIR, exist_ok=True)

# Pastas padrão dentro de 'revisadas'
PASTAS_PADRAO = [
    "Trabalhador Rural",
    "Encarregado de Campo",
    "Supervisor de Campo",
    "Trabalhador Rural Feminino",
    "Tratorista"
]

for p in PASTAS_PADRAO:
    os.makedirs(os.path.join(REVISADAS_DIR, p), exist_ok=True)

# Função para mover arquivos para a lixeira secreta
def mover_para_lixeira(caminho_origem, nome_arquivo):
    caminho_lixeira = os.path.join(LIXEIRA_DIR, nome_arquivo)
    if os.path.exists(caminho_lixeira):
        base, ext = os.path.splitext(nome_arquivo)
        caminho_lixeira = os.path.join(LIXEIRA_DIR, f"{base}_{int(time.time())}{ext}")
    shutil.move(caminho_origem, caminho_lixeira)

# Estilização CSS ultra-compacta para a sidebar
st.markdown("""
    <style>
    /* Estilo compacto da página principal */
    .block-container {
        padding-top: 1.2rem !important;
        padding-bottom: 0.5rem !important;
    }
    
    /* Compactar a Barra Lateral (Sidebar) para caber o botão SAIR */
    section[data-testid="stSidebar"] .block-container {
        padding-top: 0.8rem !important;
        padding-bottom: 0.8rem !important;
    }
    [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
        gap: 0.25rem !important;
    }
    
    /* Estilo dos cards da página inicial */
    .sst-card {
        background-color: #1a2421;
        border-left: 4px solid #2e7d32;
        padding: 8px 12px;
        border-radius: 6px;
        margin-bottom: 8px;
    }
    .sst-title {
        color: #4caf50;
        font-weight: bold;
        font-size: 0.98rem;
        margin-bottom: 2px;
    }
    .sst-text {
        font-size: 0.84rem;
        line-height: 1.25;
        margin: 0;
        color: #e0e0e0;
    }
    .banner-sst {
        background: linear-gradient(135deg, #1b5e20 0%, #0d3b13 100%);
        color: white;
        padding: 10px 14px;
        border-radius: 8px;
        text-align: center;
        margin-bottom: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.3);
    }
    .banner-sst h2 {
        margin: 0;
        font-size: 1.25rem;
        color: #ffffff;
    }
    .banner-sst p {
        margin: 2px 0 0 0;
        font-size: 0.82rem;
        font-style: italic;
        color: #c8e6c9;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# SISTEMA DE LOGIN COM LOGO COMPACTO
# -----------------------------------------------------------------------------
def checar_senha():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False

    if st.session_state["autenticado"]:
        return True

    col_l1, col_l2, col_l3 = st.columns([1, 1.2, 1])
    with col_l2:
        if os.path.exists(LOGO_PATH):
            st.image(LOGO_PATH, width=150)
        st.subheader("🔒 Acesso Restrito - Gestão SST")
        
        usuario = st.text_input("Usuário")
        senha = st.text_input("Senha", type="password")
        
        if st.button("🚀 Entrar no Sistema", use_container_width=True):
            usuarios_validos = {
                "rodrigo": "123",
                "marcia": "123",
                "admin": "123"
            }
            usuario_limpo = usuario.strip().lower()
            if usuario_limpo in usuarios_validos and usuarios_validos[usuario_limpo] == senha:
                st.session_state["autenticado"] = True
                st.session_state["usuario_atual"] = usuario.capitalize()
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos.")
    return False

if not checar_senha():
    st.stop()

# -----------------------------------------------------------------------------
# BARRA LATERAL (SIDEBAR ULTRA COMPACTA)
# -----------------------------------------------------------------------------
if os.path.exists(LOGO_PATH):
    st.sidebar.image(LOGO_PATH, width=110)

st.sidebar.markdown("**🛡️ Gestão de SST**")
st.sidebar.caption(f"👤 Usuário: **{st.session_state.get('usuario_atual', 'Usuário')}**")

if st.sidebar.button("🔄 Recarregar Sistema", use_container_width=True):
    st.rerun()

senha_exclusao = st.sidebar.text_input("🔑 Senha de Exclusão:", type="password", help="Digite '123' para excluir ou '2083' para o modo gestor.")

pode_excluir = (senha_exclusao == "123" or senha_exclusao == "2083")

opcoes_nav = [
    "🏠 Início & Pontos Fortes SST",
    "📋 Temas Obrigatórios (Rascunho)", 
    "📂 Documentos Não Revisados", 
    "📁 Documentos Revisados", 
    "📤 Upload de Documentos"
]

if senha_exclusao == "2083":
    opcoes_nav.append("♻️ Restauração (Setor Oculto)")

opcao = st.sidebar.radio("Navegação", opcoes_nav)

if st.sidebar.button("🚪 Sair", use_container_width=True):
    st.session_state.clear()
    st.rerun()

# -----------------------------------------------------------------------------
# ABA PAINEL PRINCIPAL & PONTOS FORTES DO SST
# -----------------------------------------------------------------------------
if opcao == "🏠 Início & Pontos Fortes SST":
    st.markdown("""
        <div class="banner-sst">
            <h2>🛡️ Sistema de Gestão e Proteção SST</h2>
            <p>"A Segurança do Trabalho não é apenas um conjunto de regras, é um compromisso com a VIDA e com quem espera por você em casa."</p>
        </div>
    """, unsafe_allow_html=True)

    col_p1, col_p2 = st.columns(2)

    with col_p1:
        st.markdown("""
            <div class="sst-card">
                <div class="sst-title">🛡️ 1. Cultura de Prevenção Ativa</div>
                <div class="sst-text">Antecipação, reconhecimento e eliminação de riscos antes que o acidente ocorra. A prevenção garante a integridade física de todos.</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="sst-card">
                <div class="sst-title">🥽 2. Equipamentos e Proteção (EPI & EPC)</div>
                <div class="sst-text">Fornecimento, orientação e fiscalização do uso correto dos Equipamentos de Proteção Individual e Coletiva (NR-06 e NR-31).</div>
            </div>
        """, unsafe_allow_html=True)

    with col_p2:
        st.markdown("""
            <div class="sst-card">
                <div class="sst-title">📜 3. Conformidade Legal & NRs</div>
                <div class="sst-text">Garantia de total alinhamento com a Legislação Trabalhista (CLT), Normas Regulamentadoras e diretrizes no setor agrícola.</div>
            </div>
        """, unsafe_allow_html=True)

        st.markdown("""
            <div class="sst-card">
                <div class="sst-title">❤️ 4. Valorização da Vida & Respeito</div>
                <div class="sst-text">Direito de recusa diante de risco grave, combate a assédios, incentivo à saúde mental e promoção do bem-estar no trabalho.</div>
            </div>
        """, unsafe_allow_html=True)

    st.info("💡 Utilize o menu lateral para gerenciar documentos, pastas e temas das Ordens de Serviço.")

# -----------------------------------------------------------------------------
# ABA 1: TEMAS OBRIGATÓRIOS (RASCUNHOS PADRONIZADOS)
# -----------------------------------------------------------------------------
elif opcao == "📋 Temas Obrigatórios (Rascunho)":
    st.subheader("📋 Temas Obrigatórios em Todas as Ordens de Serviço")
    st.info("Textos padronizados de SST para cópia e consulta rápida:")

    col1, col2 = st.columns(2)
    with col1:
        with st.expander("1. Descrição da Função & Aviso Legal", expanded=True):
            st.text_area("Aviso Legal:", value="Aviso Legal: As atividades relacionadas não esgotam as atribuições compatíveis com a função, nos termos do Art. 456, Parágrafo Único, da CLT.", height=80)
        with st.expander("2. Noções Gerais de Segurança & Tabagismo", expanded=True):
            st.text_area("Regras de Tabagismo:", value="É proibido o uso de cigarros, cigarrilhas, charutos, cachimbos... (Lei Federal nº 9.294/1996 e Decreto nº 8.262/2014).", height=140)
        with st.expander("3. Uso de Substâncias Psicoativas & Medicamentos"):
            st.text_area("Substâncias Psicoativas:", value="• Tolerância Zero: É terminantemente proibido apresentar-se ao trabalho sob o efeito de bebidas alcoólicas...", height=140)

    with col2:
        with st.expander("4. Vestimenta e EPIs", expanded=True):
            st.text_area("Vestimenta e EPIs:", value="Vestimenta: Proibido o uso de roupas largas, abertas ou adornos...\nEPIs: O uso de Equipamentos de Proteção Individual é obrigatório...", height=120)
        with st.expander("5. Direito de Recusa e Assédios"):
            st.text_area("Direito de Recusa:", value="• Direito de Recusa: Constatadas situações de grave e iminente risco...", height=160)
        with st.expander("6. Dispositivos Eletrônicos"):
            st.text_area("Eletrônicos:", value="Dispositivos Digitais: É expressamente proibida a utilização de celulares, tablets, etc...", height=140)

# -----------------------------------------------------------------------------
# ABA 2: DOCUMENTOS NÃO REVISADOS
# -----------------------------------------------------------------------------
elif opcao == "📂 Documentos Não Revisados":
    st.subheader("📂 Documentos Não Revisados (Pendentes)")
    
    arquivos = [f for f in os.listdir(NAO_REVISADAS_DIR) if f.endswith(('.doc', '.docx'))]
    subpastas_revisadas = [d for d in os.listdir(REVISADAS_DIR) if os.path.isdir(os.path.join(REVISADAS_DIR, d))]

    if not arquivos:
        st.success("🎉 Nenhum documento pendente na pasta de Não Revisados!")
    else:
        for idx, arq in enumerate(arquivos):
            col_nome, col_pasta_dest, col_baixar, col_mover, col_deletar = st.columns([2.5, 2, 1, 1.2, 1])
            col_nome.write(f"📄 **{arq}**")
            
            caminho_origem = os.path.join(NAO_REVISADAS_DIR, arq)
            pasta_alvo = col_pasta_dest.selectbox("Mover para:", options=["(Pasta Raiz)"] + subpastas_revisadas, key=f"sel_pasta_{idx}")

            with open(caminho_origem, "rb") as fp:
                col_baixar.download_button(label="📥 Baixar", data=fp, file_name=arq, mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=f"dl_nr_{idx}")

            if col_mover.button("✅ Mover", key=f"mv_{idx}"):
                caminho_destino = os.path.join(REVISADAS_DIR, arq) if pasta_alvo == "(Pasta Raiz)" else os.path.join(REVISADAS_DIR, pasta_alvo, arq)
                shutil.move(caminho_origem, caminho_destino)
                st.toast("Documento movido com sucesso!", icon="✅")
                st.rerun()

            if col_deletar.button("🗑️ Excluir", key=f"del_{idx}", disabled=not pode_excluir, help="Digite a senha na barra lateral para liberar"):
                mover_para_lixeira(caminho_origem, arq)
                st.toast(f"Documento '{arq}' movido para a lixeira.", icon="🗑️")
                st.rerun()

# -----------------------------------------------------------------------------
# ABA 3: DOCUMENTOS REVISADOS
# -----------------------------------------------------------------------------
elif opcao == "📁 Documentos Revisados":
    st.subheader("📁 Repositório de Documentos Revisados")

    with st.expander("➕ Criar Nova Pasta em Revisadas"):
        nova_pasta_nome = st.text_input("Nome da Nova Pasta:")
        if st.button("Criar Pasta"):
            if nova_pasta_nome.strip():
                caminho_nova_pasta = os.path.join(REVISADAS_DIR, nova_pasta_nome.strip())
                if not os.path.exists(caminho_nova_pasta):
                    os.makedirs(caminho_nova_pasta)
                    st.success("Pasta criada com sucesso!")
                    st.rerun()
                else:
                    st.warning("Já existe uma pasta com esse nome.")
            else:
                st.error("Digite um nome válido.")

    subpastas = [d for d in os.listdir(REVISADAS_DIR) if os.path.isdir(os.path.join(REVISADAS_DIR, d))]
    opcoes_pasta = ["📁 Todas as Pastas / Raiz"] + [f"📂 {sp}" for sp in subpastas]
    pasta_selecionada = st.selectbox("Selecione a Categoria/Pasta:", opcoes_pasta)

    caminho_exibicao = REVISADAS_DIR if pasta_selecionada == "📁 Todas as Pastas / Raiz" else os.path.join(REVISADAS_DIR, pasta_selecionada.replace("📂 ", ""))

    arquivos = [f for f in os.listdir(caminho_exibicao) if f.endswith(('.doc', '.docx'))]

    if not arquivos:
        st.info("Nenhum arquivo encontrado nesta pasta.")
    else:
        for idx, arq in enumerate(arquivos):
            col_nome, col_baixar, col_deletar = st.columns([3, 1, 1])
            col_nome.write(f"📄 **{arq}**")
            
            caminho_completo = os.path.join(caminho_exibicao, arq)
            with open(caminho_completo, "rb") as fp:
                col_baixar.download_button(label="📥 Baixar", data=fp, file_name=arq, mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document", key=f"dl_rev_{idx}")

            if col_deletar.button("🗑️ Excluir", key=f"del_rev_{idx}", disabled=not pode_excluir, help="Digite a senha na barra lateral para liberar"):
                mover_para_lixeira(caminho_completo, arq)
                st.toast("Documento movido para a lixeira.", icon="🗑️")
                st.rerun()

# -----------------------------------------------------------------------------
# ABA 4: UPLOAD DE ARQUIVOS
# -----------------------------------------------------------------------------
elif opcao == "📤 Upload de Documentos":
    st.subheader("📤 Adicionar Novo Documento")
    subpastas_revisadas = [d for d in os.listdir(REVISADAS_DIR) if os.path.isdir(os.path.join(REVISADAS_DIR, d))]
    opcoes_destino = ["Pasta Não Revisadas", "Pasta Rascunhos", "Pasta Revisadas (Raiz)"] + [f"Revisadas / {sp}" for sp in subpastas_revisadas]
    destino = st.selectbox("Selecione a pasta de destino:", opcoes_destino)
    arquivos_enviados = st.file_uploader("Selecione arquivos (.doc, .docx)", type=["doc", "docx"], accept_multiple_files=True)

    if st.button("Salvar Arquivo(s)"):
        if arquivos_enviados:
            if destino == "Pasta Não Revisadas": pasta_destino = NAO_REVISADAS_DIR
            elif destino == "Pasta Rascunhos": pasta_destino = RASCUNHOS_DIR
            elif destino == "Pasta Revisadas (Raiz)": pasta_destino = REVISADAS_DIR
            else: pasta_destino = os.path.join(REVISADAS_DIR, destino.replace("Revisadas / ", ""))

            for arq_uploaded in arquivos_enviados:
                with open(os.path.join(pasta_destino, arq_uploaded.name), "wb") as f:
                    f.write(arq_uploaded.getbuffer())
            st.success("Arquivo(s) salvo(s) com sucesso!")
        else:
            st.error("Selecione um arquivo primeiro.")

# -----------------------------------------------------------------------------
# ABA SECRETA: LIXEIRA (Só aparece se a senha for 2083)
# -----------------------------------------------------------------------------
elif opcao == "♻️ Restauração (Setor Oculto)":
    st.subheader("🕵️ Setor Oculto: Arquivos Excluídos")
    st.warning("Aqui estão os arquivos excluídos. É possível restaurá-los ou destruí-los em definitivo.")
    
    arquivos_lixo = [f for f in os.listdir(LIXEIRA_DIR) if os.path.isfile(os.path.join(LIXEIRA_DIR, f))]
    
    if not arquivos_lixo:
        st.info("A lixeira está vazia. Nenhum arquivo foi apagado ainda.")
    else:
        for idx, arq in enumerate(arquivos_lixo):
            col_nome, col_restaurar, col_destruir = st.columns([3, 1, 1])
            col_nome.write(f"📄 **{arq}**")
            caminho_arquivo = os.path.join(LIXEIRA_DIR, arq)
            
            if col_restaurar.button("🔄 Restaurar", key=f"res_{idx}"):
                caminho_restauracao = os.path.join(NAO_REVISADAS_DIR, arq)
                shutil.move(caminho_arquivo, caminho_restauracao)
                st.toast(f"'{arq}' restaurado!", icon="✅")
                st.rerun()
                
            if col_destruir.button("☠️ Destruir", key=f"des_{idx}"):
                os.remove(caminho_arquivo)
                st.toast(f"'{arq}' apagado definitivamente.", icon="🔥")
                st.rerun()
