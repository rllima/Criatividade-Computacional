import streamlit as st



def main():
    st.set_page_config(page_title = "Criatividade Computacional", layout = "wide")
    st.header("Criatividade Computacional - Mini Projeto")
    st.write("Lucas Florencio \n Matheus Hopper \n Rodrigo Lima")

    st.header("Galeria")
    intro = "Com o objetivo de produzir obras utilizando modelos gerativos \
             o grupo explorou aspectos da culturais Africanos para gerar imagens \
             e videos atraves de duas abordagens:"
    st.subheader(intro)
    st.write("- Geracao de imagens e videos explorando letras de musicas africanas ou com referencia a Africa")
    st.write("- Geracao de videos atraves de musicas africanas")
    st.subheader("Geracao de imagens e videos atraves de texto")
    with st.expander("A experiencia do processo!"):
        st.write("""
                O processo para geracao de um conteudo que possua caracteristicas
                culturais de uma sociedade exige habilidade e entendimento da mesma.
                As tecnicas, cores e formas devem respeitar e remeter a emocao e identidade 
                da cultura escolhida. 
                Um estudo supercial foi feito, afim de capturar os elementos, cores e sons
                presentes de maneirar geral no continente Africano.

                https://www.todamateria.com.br/arte-africana/
                https://www.infoescola.com/artes/arte-africana/
                https://www.africancontemporary.com/paintings-pt.htm

                Se para um humano gerar um artefato artistico com caracteriticas culturais
                inerentes a um povo, ou pais e necessario um certo senso e conhecimento historico,
                poderia um processo de gerativo (ML,IA) gerar tais artefatos (imagens) atraves de textos e sons?

                SIM! O processo consegue capturar aspectos presentes em outras obras, e o mais importante,
                consegue muitas vezes causar aquela sensacao de "Uma imagem vale mais que mil palavras"
                
                
                
                
        """)
    st.write("As obras geradas aqui utilizam o notebook: https://colab.research.google.com/drive/1ZAus_gn2RhTZWzOWUpPERNC0Q8OhZRTZ#scrollTo=JX56bq4rEKIp")
    
    col1,col2,col3 = st.columns(3)
    col1.image("media/t1.png")
    col2.video("media/t1.mp4")
    col3.write("Parametros")
    col3.write("texts: Africa dances in raggae \n model: vqgan_imagenet_f16_16384 \n seed: 42 \n max_interations: 200")

    col1,col2,col3 = st.columns(3)
    col1.image("media/t2.png")
    col2.video("media/t3.mp4")
    col3.write("Parametros")
    col3.write("texts: Mother Africa cradle of culture")
    col3.write("model: vqgan_imagenet_f16_16384")
    col3.write("seed: 42")
    col3.write("seed: 500")

    col1,col2,col3 = st.columns(3)
    col1.image("media/t3.png")
    col2.video("media/t3.mp4")
    col3.write("Parametros")
    col3.write("texts: I put the brazier on the floor | sing the slave his song ")
    col3.write("model: vqgan_imagenet_f16_16384")
    col3.write("seed: 42")
    col3.write("seed: 500")
    col3.write("Link para musica de onde foram extraidos versos: https://www.letras.mus.br/nacao-kariri/986357/")

    col1,col2,col3 = st.columns(3)
    col1.image("media/t4.png")
    col2.video("media/t4.mp4")
    col3.write("Parametros")
    col3.write("texts: Those so big lands as long as the sea with its few palm trees")
    col3.write("model: vqgan_imagenet_f16_16384")
    col3.write("seed: 42")
    col3.write("seed: 400")
    col3.write("Link para musica de onde foram extraidos versos: https://www.letras.mus.br/nacao-kariri/986357/")

    col1,col2,col3 = st.columns(3)
    col1.image("media/t5.png")
    col2.video("media/t7.mp4")
    col3.write("Parametros")
    col3.write("texts: Those so big lands as long as the sea with its few palm trees")
    col3.write("model: vqgan_imagenet_f16_16384")
    col3.write("seed: 2")
    col3.write("seed: 400")
    col3.write("Link para musica de onde foram extraidos versos: https://www.letras.mus.br/nacao-kariri/986357/")

    col1,col2,col3 = st.columns(3)
    col1.image("media/t6.png")
    col2.video("media/t8.mp4")
    col3.write("Parametros")
    col3.write("texts: Inflation fever | freedom fever | Yellow fever")
    col3.write("model: vqgan_imagenet_f16_16384")
    col3.write("seed: 2")
    col3.write("seed: 450")
    
    
if __name__ == '__main__':
    main()    

