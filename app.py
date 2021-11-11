import streamlit as st



def main():
    st.set_page_config(page_title = "Criatividade Computacional", layout = "wide")
    st.header("Criatividade Computacional - Mini Projeto")
    st.write("Lucas Florêncio \n Matheus Hopper \n Rodrigo Lima")

    st.header("Galeria")
    intro = "Com o objetivo de produzir obras utilizando modelos gerativos \
             o grupo explorou aspectos da culturais Africanos para gerar imagens \
             e vídeos através de duas abordagens:"
    st.subheader(intro)
    st.write("- Geração de imagens e videos explorando letras de músicas africanas ou com referência a Africa")
    st.write("- Geração de videos através de músicas africanas")
    st.subheader("Geração de imagens e videos através de texto")
    with st.expander("A experiência do processo!"):
        st.write("""
                O processo para geração de um conteúdo que possua caracteristicas
                culturais de uma sociedade exige habilidade e entendimento da mesma.
                As técnicas, cores e formas devem respeitar e remeter a emoção e identidade 
                da cultura escolhida. 
                Um estudo supercial foi feito, afim de capturar os elementos, cores e sons
                presentes de maneira geral no continente Africano.

                https://www.todamateria.com.br/arte-africana/
                https://www.infoescola.com/artes/arte-africana/
                https://www.africancontemporary.com/paintings-pt.htm

                Se para um humano gerar um artefato artistico com caracteriticas culturais
                inerentes a um povo ou pais e necessario uma imersão na cultura que ele almeja representar,
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

    st.subheader("Geração de vídeos através de sons")
    with st.expander("A experiência do processo!"):
        st.write("""
                Durante a pesquisa, tivemos uma sensação próxima do que imaginávamos como processo criativo
                de um artista audiovisual. Lendo sobre a história da cultura musical Africana e, finalmente,
                ouvindo os ritmos e sons mais populares, pudemos sentir essa carga cultural.

                Fontes:
                https://pt.wikipedia.org/wiki/M%C3%BAsica_da_%C3%81frica
                https://viagemeturismo.abril.com.br/materias/15-musicas-africanas-para-embalar-uma-viagem-ao-continente/
                """)
    

    col1,col2 = st.columns(2)
    col1.video("media/VID_CAM_RichardBona_ManyakaBrazil.mp4")
    col2.write("Parametros")
    col2.write("Audio: Richard Bona - Manyaka Brazil")
    col2.write("Origem: Camaroes")
    col2.write("model: Lucid Sonic Dreams")
    col2.write("style: wikiart")
    col2.write("seed: default")

    col1,col2 = st.columns(2)
    col1.video("media/VID_RDC_MbongwanaStar_Malukayi.mp4")
    col2.write("Parametros")
    col2.write("Audio: Mbongwana Star - Malukayi")
    col2.write("Origem: Republica Democratica do Congo")
    col2.write("model: Lucid Sonic Dreams")
    col2.write("style: wikiart")
    col2.write("seed: default")

    col1,col2 = st.columns(2)
    col1.video("media/VID_Default_WikiArt_NIG_Kuti_YellowFever.mp4")
    col2.write("Parametros")
    col2.write("Audio: Kuti - Yellow Fever")
    col2.write("Origem: Nigeria")
    col2.write("model: Lucid Sonic Dreams")
    col2.write("style: wikiart")
    col2.write("seed: default")

    col1,col2 = st.columns(2)
    col1.video("media/VID_Default_WikiArt_MOC_OrqMarrabenta_ElisaGomara.mp4")
    col2.write("Parametros")
    col2.write("Audio: Orquestra Marrabenta - Elisa Gomara")
    col2.write("Origem: Mocambique")
    col2.write("model: Lucid Sonic Dreams")
    col2.write("style: wikiart")
    col2.write("seed: default")

    col1,col2 = st.columns(2)
    col1.video("media/VID_SAF_DieAntwood_FattyBoomBoom.mp4")
    col2.write("Parametros")
    col2.write("Audio: Die Antwood - Fitty Boom Boom")
    col2.write("Origem: Africa do Sul")
    col2.write("model: Lucid Sonic Dreams")
    col2.write("style: wikiart")
    col2.write("seed: default")

    col1,col2 = st.columns(2)
    col1.video("media/VID_SAF_MiriamMakeba_PataPata.mp4")
    col2.write("Parametros")
    col2.write("Audio: Miriam Makeba - PataPata")
    col2.write("Origem: Africa do Sul")
    col2.write("model: Lucid Sonic Dreams")
    col2.write("style: wikiart")
    col2.write("seed: default")

    col1,col2 = st.columns(2)
    col1.video("media/VID_SRL_JankaNabay&BubuGang_Feba.mp4")
    col2.write("Parametros")
    col2.write("Audio: Janka Nabay & Bubu Gang - Feba")
    col2.write("Origem: Serra Leoa")
    col2.write("model: Lucid Sonic Dreams")
    col2.write("style: wikiart")
    col2.write("seed: default")
    
    
if __name__ == '__main__':
    main()    

