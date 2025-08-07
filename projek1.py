import streamlit as st
import streamlit.components.v1 as components
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import cloudinary
import cloudinary.uploader
import io
import requests



st.title("Pythagoras")

if "coba" not in st.session_state:
    st.session_state.coba=False
if "coba1" not in st.session_state:
    st.session_state.coba1 = False
if "coba2" not in st.session_state:
    st.session_state.coba2 = False
if "coba3" not in st.session_state:
    st.session_state.coba3 = False
if "jawab" not in st.session_state:
    st.session_state.jawab = []
if "skor1" not in st.session_state:
    st.session_state.skor1 = 0
if "jawab1" not in st.session_state:
    st.session_state.jawab1 = []
if "skor2" not in st.session_state:
    st.session_state.skor2 = 0
if "jawab1" not in st.session_state:
    st.session_state.jawab2 = []
if "skor2" not in st.session_state:
    st.session_state.skor3 = 0
if "nama" not in st.session_state:
    st.session_state.nama=""
if "kelas" not in st.session_state:
    st.session_state.kelas=""
if "materi1" not in st.session_state:
    st.session_state.materi1=False
if "materi2" not in st.session_state:
    st.session_state.materi2=False
if "tampilan" not in st.session_state:
    st.session_state.tampilan = True
if "materiU" not in st.session_state:
    st.session_state.materiU = False
if "diskusian" not in st.session_state:
    st.session_state.diskusian = False
if "kumpulanH" not in st.session_state:
    st.session_state.kumpulanH = {'kondisi1':True, 'kondisi2':False, 'kondisi3':False,
                                  'kondisi4':False, 'kondisi5':False, 'kondisi6':False,
                                  'kondisi7':False, 'kondisi8':False, 'kondisi9':False, 'kondisi10':True}
if "prasyaratan" not in st.session_state:
    st.session_state.prasyaratan = False
if "penilaian1" not in st.session_state:
    st.session_state.penilaian1={'jwb1':0,'jwb2':0,'jwb3':0,
                                 'jwb4':0,'jwb5':0,'jwb6':0}
if "nilai1" not in st.session_state:
    st.session_state.nilai1 = 0
if "penilaian2" not in st.session_state:
    st.session_state.penilaian2 = {'jwb1':0,'jwb2':0,'jwb3':0,'jwb4':0}
    

kolom = st.columns(2)
with kolom[0]:
    st.session_state.nama = st.text_input("Masukan Nama")
with kolom[1]:
    st.session_state.kelas = st.text_input("Masukan Kelas")

st.markdown("""
    <style>
        .para{
            font-family:"comic sans ms";
            font-size:20px;
            border:2px solid black;
            border-radius:10px;
            padding:5px;
            margin:10px;
            box-shadow:2px 2px 3px 3px orange;
            background-color:pink;
            color:black;
            text-align:justify;
        }
        .gmb{
            width:200px;
            border:2px solid black;
        }
        #gmb1{
            width:400px;
        }
        #posisi{
            text-align:center;
        }
        #gmb2{
            margin:10px;
        }
        .kelompok{
            font-size:20px;
            font-family:"Brush script mt";
            font-weight:bold;
        }
    </style>
    """,unsafe_allow_html=True)
soal_masalah = {"soal1":{"pert":["Sebuah segitiga siku-siku memiliki panjang alas 6 cm dan tinggi 8 cm. Berapa panjang sisi miringnya?",
                                 "Panjang sisi miring sebuah segitiga adalah 13 cm, dan salah satu sisi lainnya 5 cm. Hitung panjang sisi yang belum diketahui.",
                                 "Diketahui panjang sisi siku-siku adalah 9 cm dan 12 cm. Hitung panjang sisi miring."],
                         "jwb":[10,12,15]},
                "soal2":{"pert":["Seorang siswa mengukur tiang dan menemukan bahwa jarak dari dasar tiang ke ujung bayangan adalah 15 meter, dan tinggi tiang adalah 9 meter. Berapa panjang bayangannya?",
                                 "Diberikan tiga sisi segitiga: 7 cm, 24 cm, dan 25 cm. Apakah segitiga tersebut merupakan segitiga siku-siku? Jelaskan.",
                                 "Sebuah tangga sepanjang 10 m disandarkan ke tembok dan membentuk sudut siku-siku dengan tanah. Jika jarak kaki tangga ke tembok adalah 6 m, berapa tinggi tembok?"],
                         "jwb":[12,1,8]},
                "soal3":{"pert":["Di taman, seorang anak berjalan 5 m ke timur, lalu 12 m ke utara. Jika ia memotong langsung ke titik awal, berapa meter jarak yang ditempuhnya?",
                                 "Sebuah drone terbang vertikal setinggi 80 meter, kemudian bergerak horizontal sejauh 60 meter. Hitung jarak langsung drone dari titik awal penerbangannya.",
                                 "Dalam koordinat kartesius, titik A berada di (2, 3) dan titik B di (8, 11). Hitung jarak antara titik A dan B menggunakan teorema Pythagoras.",
                                 "Sebuah layar proyektor berbentuk persegi panjang memiliki diagonal 100 cm dan lebar 60 cm. Hitung tinggi layar tersebut."],
                         "jwb":[13,100,10,80]},
                }

def tampilkan():
    st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1754526033/Teorema_Pythagoras_midmap_Luvy_clecjb.jpg")

if st.session_state.tampilan:
    tampilkan()
if st.session_state.kumpulanH['kondisi1']:
    if st.sidebar.button("Peta_Konsep"):
        st.session_state.coba2 = False
        st.session_state.coba1 = False
        st.session_state.coba = False
        st.session_state.coba3 = False
        st.session_state.materi1 = False
        st.session_state.materi2 = False
        st.session_state.tampilan = True
        st.session_state.materiU = False
        st.session_state.diskusian = False
        st.session_state.prasyaratan = False
        st.session_state.kumpulanH['kondisi2']=True
        st.rerun()

def sebelum():
    st.write("Mengingat")
    st.markdown("""<div style="font-size:20px; font-weight:bold; color:black; background-color:yellow;
                    padding:5px; width:300px;margin-top:10px; margin-bottom:10px;border-radius:10px">
                    Jenis-Jenis Segitiga
                    </div>""",unsafe_allow_html=True)
    with st.expander("Jenis-jenis Segitiga"):
        st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1754557074/jenis_segitiga_o2zqej.png",width=1000)
    st.write("Segitiga berdasarkan sudut:")
    isi1 = st.radio("1. Ada 1 sudut 90 derajat",("A. Tumpul","B. Siku-siku","C. Lancip"))
    if isi1=="B. Siku-siku":
        st.session_state.penilaian1['jwb1'] = 16
    else:
        st.session_state.penilaian1['jwb1'] = 0
    isi2 = st.radio("2. semua sudut kurang 90 derajat",("A. Tumpul","B. Siku-siku","C. Lancip"))
    if isi2=="C. Lancip":
        st.session_state.penilaian1['jwb2'] = 17
    else:
        st.session_state.penilaian1['jwb2'] = 0
    isi3 = st.radio("3. Ada 1 sudut lebih 90 derajat",("A. Tumpul","B. Siku-siku","C. Lancip"))
    if isi3=="A. Tumpul":
        st.session_state.penilaian1['jwb3'] = 17
    else:
        st.session_state.penilaian1['jwb3'] = 0
    st.write("Segitiga berdasarkan sisi:")
    with st.expander("Segitiga berdasarkan sisi"):
        st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1754558768/segitiga_sisi_uof2uq.png",width=1000)
    isi4 = st.radio("1. Segitiga memiliki semua sisi yang panjangnya sama",("A. sama kaki","B. sama sisi","C. sembarang"))
    if isi4=="B. sama sisi":
        st.session_state.penilaian1['jwb4'] = 16
    else:
        st.session_state.penilaian1['jwb4'] = 0
    isi5 = st.radio("2. Segitiga yang memiliki 2 garis yang sama panjang",("A. sembarang","B. sama sisi","C. sama kaki"))
    if isi5=="C. sama kaki":
        st.session_state.penilaian1['jwb5'] = 17
    else:
        st.session_state.penilaian1['jwb5'] = 0
    isi6 = st.radio("3. Segitiga yang semua sisinya tidak sama panjang",("A. Sembarang","B. sama kaki","C. sama sisi"))
    if isi6=="A. Sembarang":
        st.session_state.penilaian1['jwb6'] = 17
    else:
        st.session_state.penilaian1['jwb6'] = 0
        
    st.session_state.nilai1 =0
    for i in st.session_state.penilaian1:
        st.session_state.nilai1 += st.session_state.penilaian1[i]
    if st.button("segitiga1"):
        st.info(st.session_state.nilai1)

    st.markdown("""<div style="font-size:20px; font-weight:bold; color:black; background-color:yellow;
                    padding:5px; width:500px;margin-top:10px; margin-bottom:10px;border-radius:10px">
                    Mengenal Sisi-sisi Segitiga Siku-Siku (catatan penting)
                    </div>""",unsafe_allow_html=True)
    st.markdown("""
        <div>misalkan:
            <ul>
                <li>Sisi miring (hipotenusa): sisi yang berseberangan dengan sudut siku-siku (paling panjang).</li>
                <li>Dua sisi lainnya disebut sisi tegak dan sisi datar.</li>
            </ul>
        </div>
        """,unsafe_allow_html=True)
    st.markdown("""<div style="font-size:20px; font-weight:bold; color:black; background-color:yellow;
                    padding:5px; width:500px;margin-top:10px; margin-bottom:10px;border-radius:10px">
                    Perpangkatan Kuadat
                    </div>""",unsafe_allow_html=True)
    st.write("Kuadrat")
    st.latex("a^{2}=a\\times{a}")
    st.markdown("Contoh: Berapakah $4^{2}$")
    hasil = st.text_input("Masukan jawaban perpangkatan")
    if hasil:
        if int(hasil)==16:
            st.info("Jawaban Benar")
        else:
            st.error("Jawabanmu Belum tepat")
    st.write("Akar Kuadrat")
    st.latex("\sqrt{b} = b\\;bilangan\\;jika\\;dikuadratkan\\;menghasilkan")
    st.markdown("Contoh: Berapakah $\sqrt{25}$")
    hasil1 = st.text_input("Masukan jawaban akar")
    if hasil1:
        if int(hasil1)==5:
            st.info("Jawaban Benar")
        else:
            st.error("Jawabanmu Belum tepat")
    
    st.subheader("📝 Soal Latihan Prasyarat Pythagoras")
    st.write('🔹 A. Mengenal Segitiga Siku-Siku')
    pilihan1 = st.multiselect("Manakah dari segitiga berikut yang merupakan segitiga siku-siku?",["a. 60°, 60°, 60°","b. 90°, 30°, 60°",
                                                                                                "c. 45°, 45°, 90°","d. 100°, 40°, 40°"])
    if len(pilihan1)==2:
        if set(pilihan1) == set(["b. 90°, 30°, 60°","c. 45°, 45°, 90°"]) :
            st.info("Jawabanmu Benar")
        else:
            st.error("Jawabanmu belum tepat")
    st.write("🔹 B. Perpangkatan")
    st.write("Hitunglah:")
    st.markdown("a. $6^{2}$")
    st.session_state.penilaian2['jwb1']=st.text_input("Jawaban pertama")
    st.markdown("a. $9^{2}$")
    st.session_state.penilaian2['jwb2']=st.text_input("Jawaban kedua")
    st.markdown("a. $\sqrt{49}$")
    st.session_state.penilaian2['jwb3']=st.text_input("Jawaban ketiga")
    st.markdown("a. $\sqrt{121}$")
    st.session_state.penilaian2['jwb4']=st.text_input("Jawaban keempat")

    evaluasi = st.button("Evaluasi")
    if evaluasi:
        skor1 = 0
        for i in st.session_state.penilaian2:
            for j in [36,81,7,11]:
                if int(st.session_state.penilaian2[i])==j:
                    skor1 += 25
        st.info("skor Anda: "+str(skor1))
    
if st.session_state.prasyaratan:
    sebelum()
if st.session_state.kumpulanH['kondisi2']:
    if st.sidebar.button("prasyarat"):
        st.session_state.coba2 = False
        st.session_state.coba1 = False
        st.session_state.coba = False
        st.session_state.coba3 = False
        st.session_state.materi1 = False
        st.session_state.materi2 = False
        st.session_state.tampilan = False
        st.session_state.materiU = False
        st.session_state.diskusian = False
        st.session_state.prasyaratan = True
        st.session_state.kumpulanH['kondisi3']=True
        st.rerun()

def konsep():
    tab = st.tabs(["Definisi dan Rumus","Triple Pythagoras","Segitiga Istimewa"])
    with tab[0]:
        st.markdown("<div class='kelompok'>Teorema Pythagoras</div>", unsafe_allow_html=True)
        st.markdown("""<div style="font-size:20px;"><i><b>Teorema Pythagoras</b></i> adalah salah satu teorema
                    dasar dalam geometri yang berlaku pada segitiga siku-siku.</div>""",unsafe_allow_html=True)
        st.markdown("""<div style="font-size:20px; font-weight:bold; color:black; background-color:yellow;
                    padding:5px; width:300px;margin-top:10px; margin-bottom:10px;border-radius:10px">
                    🔷 Definisi Teorema Pythagoras
                    </div>""",unsafe_allow_html=True)
        st.markdown("""<div style="font-size:20px;">Teorema Pythagoras menyatakan bahwa:</div>""",unsafe_allow_html=True)
        st.markdown("""<div style="font-size:20px; color: black; background-color:white; border-radius:10px; width:600px;
                        margin-bottom:10px;font-weight:bold; padding:10px;text-align:justify">
                    Dalam segitiga siku-siku, kuadrat panjang sisi miring (hipotenusa) sama dengan jumlah
                    kuadrat panjang kedua sisi lainnya.</div>""",unsafe_allow_html=True)
        st.markdown("""<iframe scrolling="no" title="pythagoras pesegi" src="https://www.geogebra.org/material/iframe/id/mcbszmq5/width/1341/height/531/
border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/false/ld/false/sdz/true/ctl
/false" width="687px" height="265px" style="border:0px;"> </iframe>""",unsafe_allow_html=True)
        st.markdown("""<div style="font-size:20px; font-weight:bold; color:black; background-color:yellow;
                    padding:5px; width:300px;margin-top:10px; margin-bottom:10px;border-radius:10px">
                    🔷 Rumus Teorema Pythagoras
                    </div>""",unsafe_allow_html=True)
        st.markdown("""
        <div>misalkan:
            <ul>
                <li>a = panjang sisi tegak,</li>
                <li>b = panjang sisi datar,</li>
                <li>c = panjang sisi miring (hipotenusa),</li>
            </ul>
            maka:
        </div>
        """,unsafe_allow_html=True)
        st.latex("a^2+b^2=c^2")
        st.markdown("""<div style="font-size:20px; font-weight:bold; color:black; background-color:yellow;
                    padding:5px; width:300px;margin-top:10px; margin-bottom:10px;border-radius:10px">
                    🔷 Bentuk Turunan Lain
                    </div>""",unsafe_allow_html=True)
        st.markdown("""
        <div>Jika yang dicari adalah sisi tegak atau sisi datar:
        </div>
        """,unsafe_allow_html=True)
        st.latex("a=\sqrt{c^2-b^2}")
        st.latex("b=\sqrt{c^2-a^2}")
    with tab[1]:
        st.markdown("<div class='kelompok'>Definisi dan Rumus Pythagoras</div>", unsafe_allow_html=True)
        st.markdown("""<iframe scrolling="no" title="Pythagoras Segitiga" src="https://www.geogebra.org/material/iframe/id/uhqmtbn8/width/1341/height/531/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/true/rc/false/ld/false/sdz/true/ctl/false"
width="687px" height="256px" style="border:0px;"> </iframe>""",unsafe_allow_html=True)
        st.markdown("""
        <div>Berikut penjelasan materi tentang Triple Pythagoras secara lengkap dan mudah dipahami:
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""<div style="font-size:20px; font-weight:bold; color:black; background-color:yellow;
                    padding:5px; width:300px;margin-top:10px; margin-bottom:10px;border-radius:10px">
                    🔷 Apa Itu Triple Pythagoras?
                    </div>""",unsafe_allow_html=True)
        st.markdown("""
        <div>Triple Pythagoras (atau Pythagorean Triple) adalah tiga bilangan bulat positif yang memenuhi Teorema Pythagoras, yaitu:
        </div>
        """,unsafe_allow_html=True)
        st.latex("c^2=a^2+b^2")
        st.markdown("""
        <div>Di mana:
            <ul>
                <li>a, b adalah sisi-sisi siku-siku (tegak dan datar),</li>
                <li>c adalah sisi miring (hipotenusa),</li>
                <li>Ketiganya adalah bilangan bulat dan membentuk segitiga siku-siku.</li>
            </ul>
        </div>
        """,unsafe_allow_html=True)
        st.markdown("""<div style="font-size:20px; font-weight:bold; color:black; background-color:yellow;
                    padding:5px; width:400px;margin-top:10px; margin-bottom:10px;border-radius:10px">
                    🔷 Contoh Triple Pythagoras yang Umum
                    </div>""",unsafe_allow_html=True)
        with st.container():
            pilihan1 = st.radio("Jika a=3 dan b=4, maka c = ...",["A.4","B.5","C.7","D.8"])
            jwbn1 = st.button("jawb1")
            if jwbn1:
                if pilihan1=="B.5":
                    st.info("Jawabanmu Benar ✅")
                else:
                    st.error("Jawabanmu kurang tepat ❌")
            pilihan2 = st.radio("Jika a=5 dan c=13, maka b = ...",["A.15","B.17","C.20","D.12"])
            jwbn2 = st.button("jawb2")
            if jwbn2:
                if pilihan2=="D.12":
                    st.info("Jawabanmu Benar ✅")
                else:
                    st.error("Jawabanmu kurang tepat ❌")
            pilihan3 = st.radio("Jika b=5 dan c=41, maka a = ...",["A.5","B.13","C.9","D.17"])
            jwbn3 = st.button("jawb3")
            if jwbn3:
                if pilihan3=="C.9":
                    st.info("Jawabanmu Benar ✅")
                else:
                    st.error("Jawabanmu kurang tepat ❌")
    with tab[2]:
        st.markdown("<div class='kelompok'>Segitiga Istimewa</div>", unsafe_allow_html=True)
        st.markdown("""
            **Segitiga istimewa** dalam konteks teorema Pythagoras di kelas 8 merujuk pada segitiga siku-siku yang memiliki sudut-sudut khusus atau perbandingan
            sisi yang tetap. Dua jenis segitiga siku-siku istimewa yang umum dipelajari adalah segitiga 45° - 45° - 90° dan segitiga 30° - 60° - 90°.
            Selain itu, dikenal juga tripel Pythagoras, yaitu kumpulan tiga bilangan bulat yang memenuhi teorema Pythagoras. 
        """)
        st.image("https://res.cloudinary.com/ikip-siliwangi/image/upload/v1754179521/pythagorais_ozgctq.png", width=400)
        st.markdown("""<div style="font-size:20px; font-weight:bold; color:black; background-color:yellow;
                    padding:5px; width:500px;margin-top:10px; margin-bottom:10px;border-radius:10px">
                     🔷 Segitiga Siku-Siku Sama Kaki (45°-45°-90°)
                     </div>""",unsafe_allow_html=True)
        st.markdown("""
        - Dua sudutnya masing-masing 45 derajat, dan satu sudut siku-siku (90 derajat).
        - Perbandingan sisi-sisinya adalah $1 : 1 : √2$ (sisi yang berhadapan dengan sudut $45°$ : sisi yang berhadapan dengan sudut $45°$ : sisi miring)
        - Contoh: Jika sisi yang berhadapan dengan sudut $45°$ adalah 5, maka sisi miringnya adalah $5√2$. 
        """)
        st.markdown("""<div style="font-size:20px; font-weight:bold; color:black; background-color:yellow;
                    padding:5px; width:500px;margin-top:10px; margin-bottom:10px;border-radius:10px">
                     🔷 Segitiga Siku-Siku dengan Sudut 30°-60°-90°
                     </div>""",unsafe_allow_html=True)
        st.markdown("""
        - Satu sudutnya 30 derajat, satu sudut 60 derajat, dan satu sudut siku-siku (90 derajat).
        - Perbandingan sisi-sisinya adalah $ √3 : 1 : 2$ (sisi terpendek : sisi sedang : sisi miring).
        - Contoh: Jika sisi terpendek (berhadapan dengan sudut 30°) adalah 4, maka sisi yang berhadapan dengan sudut 60° adalah 4√3, dan sisi miringnya adalah 8.  
        """)
        st.markdown("""<div style="font-size:20px; font-weight:bold; color:black; background-color:yellow;
                    padding:5px; width:200px;margin-top:10px; margin-bottom:10px;border-radius:10px">
                     🔷 Contoh
                     </div>""",unsafe_allow_html=True)
        st.markdown("""
        Jika diketahui segitiga siku-siku sama kaki dengan panjang salah satu sisi siku-sikunya $6\;cm$,
        maka panjang sisi miringnya adalah $6√2\;cm$ (karena perbandingannya $1:1:√2$).   
        """)
if st.session_state.materiU:
    konsep()

if st.session_state.kumpulanH['kondisi3']:
    if st.sidebar.button("Materi Phytagoras"):
        st.session_state.coba2 = False
        st.session_state.coba1 = False
        st.session_state.coba = False
        st.session_state.coba3 = False
        st.session_state.materi1 = False
        st.session_state.materi2 = False
        st.session_state.tampilan = False
        st.session_state.materiU = True
        st.session_state.diskusian = False
        st.session_state.prasyaratan = False
        st.session_state.kumpulanH['kondisi4']=True
        st.rerun()
        
def testing():
    st.subheader("🟢Le vel Dasar")
    st.markdown("""<div style="font-family:Arial;font-size:20px">Fokus: Mengidentifikasi sisi miring dan menghitung panjang sisi menggunakan rumus.<div>""",unsafe_allow_html=True)
    st.session_state.jawab = []
    st.session_state.skor1 = 0
    st.write(f'1. {soal_masalah["soal1"]["pert"][0]}')
    st.session_state.jawab.append(st.text_input("Jawab 1: "))
    st.write(f'2. {soal_masalah["soal1"]["pert"][1]}')
    st.session_state.jawab.append(st.text_input("Jawab 2: "))
    st.write(f'3. {soal_masalah["soal1"]["pert"][2]}')
    st.session_state.jawab.append(st.text_input("Jawab 3: "))
    tekan = st.button("Skor1")
    j=-1
    if tekan:
        for i in st.session_state.jawab:
            j+=1
            if int(i)==soal_masalah['soal1']['jwb'][j]:
                st.session_state.skor1 +=10
        st.info(f"Skor: {st.session_state.skor1}")
        url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSettfmqtx3JNQBdC3oGzpoVGA0B8KNO6L-oTrHKzkjuBBGO3A/formResponse"
        data = {
                "entry.958134651":st.session_state.nama,
                "entry.717789674":st.session_state.kelas,
                "entry.304047274": st.session_state.jawab[0],   # Ganti dengan entry ID dari form
                "entry.1139367795": st.session_state.jawab[1],   # Ganti dengan entry ID dari form
                "entry.2128328793": st.session_state.jawab[2],   # Ganti dengan entry ID dari form
                "entry.2014153957": st.session_state.skor1,   # Ganti dengan entry ID dari form
            }
        response = requests.post(url, data=data)
        if response.status_code == 200:
            st.success("Berhasil dikirim!")
        else:
            st.error(f"Gagal mengirim. Status code: {response.status_code}")

    st.subheader("🟡 Level 2: Menengah (Masalah Kontekstual dan Pembalikan Rumus)")
    st.markdown("""<div style="font-family:Arial;font-size:20px">Fokus: Soal cerita dan menentukan apakah segitiga merupakan segitiga siku-siku.<div>""",unsafe_allow_html=True)
    st.session_state.jawab1 = []
    st.session_state.skor2 = 0
    st.write(f'4. {soal_masalah["soal2"]["pert"][0]}')
    st.session_state.jawab1.append(st.text_input("Jawab 4: "))
    st.write(f'5. {soal_masalah["soal2"]["pert"][1]}')
    st.session_state.jawab1.append(st.text_input("Jawab 5: "))
    st.write(f'6. {soal_masalah["soal2"]["pert"][2]}')
    st.session_state.jawab1.append(st.text_input("Jawab 6: "))
    tekan1 = st.button("Skor2")
    j=-1
    if tekan1:
        for i in st.session_state.jawab1:
            j+=1
            if int(i)==soal_masalah['soal2']['jwb'][j]:
                st.session_state.skor2 +=10
        st.info(f"Skor: {st.session_state.skor2}")
        url1 = "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdlx-54LFHJ0sZgDYZZ_VWQQpr3QQuz_ghM8pdHdWzteb940A/formResponse"
        data1 = {
                "entry.1933813413":st.session_state.nama,
                "entry.1551515866":st.session_state.kelas,
                "entry.456414240": st.session_state.jawab1[0],   # Ganti dengan entry ID dari form
                "entry.1404636430": st.session_state.jawab1[1],   # Ganti dengan entry ID dari form
                "entry.2066937479": st.session_state.jawab1[2],   # Ganti dengan entry ID dari form
                "entry.1131645300": st.session_state.skor2,   # Ganti dengan entry ID dari form
            }
        response = requests.post(url1, data=data1)
        if response.status_code == 200:
            st.success("Berhasil dikirim!")
        else:
            st.error(f"Gagal mengirim. Status code: {response.status_code}")
    st.subheader("🔴 Level 3: Tinggi (Aplikasi Kompleks dan Soal Terbalik)")
    st.markdown("""<div style="font-family:Arial;font-size:20px">Fokus: Problem solving, multiple steps, dan integrasi konsep.<div>""",unsafe_allow_html=True)
    st.session_state.jawab2 = []
    st.session_state.skor3 = 0
    st.write(f'7. {soal_masalah["soal3"]["pert"][0]}')
    st.session_state.jawab2.append(st.text_input("Jawab 7: "))
    st.write(f'8. {soal_masalah["soal3"]["pert"][1]}')
    st.session_state.jawab2.append(st.text_input("Jawab 8: "))
    st.write(f'9. {soal_masalah["soal3"]["pert"][2]}')
    st.session_state.jawab2.append(st.text_input("Jawab 9: "))
    st.write(f'10. {soal_masalah["soal3"]["pert"][3]}')
    st.session_state.jawab2.append(st.text_input("Jawab 10: "))
    tekan2 = st.button("Skor3")
    j=-1
    if tekan2:
        for i in st.session_state.jawab2:
            j+=1
            if int(i)==soal_masalah['soal3']['jwb'][j]:
                st.session_state.skor3 +=10
        st.info(f"Skor: {st.session_state.skor3}")
if st.session_state.coba3:
    testing()
if st.session_state.kumpulanH['kondisi4']:
    if st.sidebar.button("Test"):
        st.session_state.coba2 = False
        st.session_state.coba1 = False
        st.session_state.coba = False
        st.session_state.coba3 = True
        st.session_state.materi1 = False
        st.session_state.materi2 = False
        st.session_state.tampilan = False
        st.session_state.materiU = False
        st.session_state.diskusian = False
        st.session_state.prasyaratan = False
        st.session_state.kumpulanH['kondisi5']=True
        st.rerun()
        
def materi_segitiga1():
    st.subheader("Misteri Segitiga Ajaib di Desa Sukamaju")
    st.markdown("""
    <div class="para">
    Selamat datang dalam petualangan matematis yang menarik! Dokumen ini menyajikan lima soal
    cerita bersambung tentang teorema Pythagoras yang dikemas dalam narasi petualangan lima siswa
    di Desa Suka Maju. Cerita ini dirancang untuk meningkatkan kemampuan literasi matematis,
    komunikasi matematis, berpikir kreatif, menganalisis kesalahan data, dan kemampuan representasi
    matematis bagi siswa SMP. Setiap soal disertai dengan materi pendukung dan ilustrasi yang
    membantu pemahaman. Mari ikuti petualangan Rian, Nisa, Andi, Wati, dan Edo dalam mengungkap
    misteri segitiga ajaib!
    </div>
    """,unsafe_allow_html=True)
    st.write("")
    kolom2 = st.columns(3,vertical_alignment="center")
    with kolom2[0]:
        st.image("https://img1.picmix.com/output/stamp/normal/7/7/5/2/2622577_be442.gif")
    with kolom2[1]:
        st.image("https://i.gifer.com/HIHe.gif")
    with kolom2[2]:
        st.image("https://upload.wikimedia.org/wikipedia/commons/8/81/Platonic_Solids_Stereo_1_-_Tetrahedron.gif")
if st.session_state.materi1:
    materi_segitiga1()

if st.session_state.kumpulanH['kondisi5']:
    if st.sidebar.button("Misteri Segitiga"):
        st.session_state.coba2 = False
        st.session_state.coba1 = False
        st.session_state.coba = False
        st.session_state.coba3 = False
        st.session_state.materi1 = True
        st.session_state.materi2 = False
        st.session_state.tampilan = False
        st.session_state.materiU = False
        st.session_state.diskusian = False
        st.session_state.kumpulanH['kondisi6']=True
        st.rerun()

def materi_segitiga2():
    st.subheader("Festival Matematika di Desa Suka Maju")
    st.markdown("""
    <div class="para">
    Desa Suka Maju terkenal dengan Festival Matematika tahunan yang selalu dinanti-nanti
    oleh seluruh penduduk, terutama para pelajar. Festival ini tidak hanya menghadirkan kompetisi
    matematika biasa, tetapi juga dikemas dalam bentuk permainan dan petualangan yang
    menarik, menantang, sekaligus mendidik.
    </div>
    """,unsafe_allow_html=True)
    st.markdown("""
    <div class="para">
    Tahun ini, panitia festival menghadirkan acara spesial bertajuk "Perburuan Harta Karun Segitiga
    Ajaib". Acara ini dirancang untuk menguji pemahaman peserta tentang konsep geometri, khususnya teorema Pythagoras, dalam konteks
    kehidupan nyata. Para peserta akan menghadapi berbagai tantangan matematis yang tersebar di seluruh desa.
    </div>
    """,unsafe_allow_html=True)
    st.markdown("""
    <div class="para">
        <div>
        Tahun ini, panitia festival menghadirkan acara spesial bertajuk "Perburuan Harta Karun Segitiga
        Ajaib". Acara ini dirancang untuk menguji pemahaman peserta tentang konsep geometri, khususnya teorema Pythagoras, dalam konteks
        kehidupan nyata. Para peserta akan menghadapi berbagai tantangan matematis yang tersebar di seluruh desa.
        </div>
        <div id="posisi">
            <img class="gmb" src="https://blue.kumparan.com/image/upload/fl_progressive,fl_lossy,c_fill,f_auto,q_auto:best,w_640/v1614254973/Pythagoras_with_tablet_of_ratios_ix1m0h.jpg"></img>
            <img class="gmb" id="gmb1" src="https://i.pinimg.com/736x/7c/9e/1b/7c9e1bd3de9bc6c1adc86aa57d67700e.jpg"></img>
        </div>
    </div>
    """,unsafe_allow_html=True)
    st.markdown("""
    <div class="para">
       Lima siswa SMP yang bersahabat dekat—Rian, Nisa, Andi, Wati, dan Edo—memutuskan untuk
        membentuk satu tim dalam kompetisi ini. Mereka memiliki kelebihan masing-masing: Rian
        pandai mengukur, Nisa jeli dalam menganalisis data, Andi mahir membuat sketsa, Wati selalu
        berpikir kreatif, dan Edo ahli dalam representasi visual. Dengan kombinasi keahlian yang saling
        melengkapi, mereka siap menghadapi tantangan mencari harta karun tersembunyi dengan
        bantuan teorema Pythagoras.
    </div>
    """,unsafe_allow_html=True)
    col1 = st.columns([1,2])
    with col1[0]:
        st.markdown("""
        <img id="gmb2" class="gmb" src="https://asimtot.wordpress.com/wp-content/uploads/2011/06/bukti-2-teorema-pythagoras.gif"></img>
    """,unsafe_allow_html=True)
    with col1[1]:
        st.write("")
        with st.container(height=200):
            st.markdown("""
            ### Teorema Pythagoras
            **Dalam segitiga siku-siku, berlaku: **  
            $a^2 + b^2 = c^2$
            **Dimana c adalah sisi miring (hipotenusa), sedangkan a dan b adalah sisi-sisi yang membentuk sudut siku-siku (90°)**.
            """)
    col2 = st.columns([2,1])
    with col2[0]:
        st.write("")
        with st.container(height=200):
            st.markdown("""
            ### Aplikasi dalam Kehidupan
            **Teorema Pythagoras banyak digunakan dalam kehidupan sehari-hari,
            seperti mengukur jarak, menentukan posisi,
            konstruksi bangunan, dan navigasi.**.
            """)
    col3 = st.columns([1,2])
    with col3[0]:
        st.write("")
    with col3[1]:
        with st.container(height=200):
            st.markdown("""
                ### Kemampuan Matematis
                **Melalui cerita ini, siswa akan mengembangkan literasi matematis,
                komunikasi, berpikir kreatif, analisis data, dan
                representasi matematis.**.
            """)
if st.session_state.materi2:
    materi_segitiga2()

if st.session_state.kumpulanH['kondisi6']:    
    if st.sidebar.button("Pendahuluan"):
        st.session_state.coba2 = False
        st.session_state.coba1 = False
        st.session_state.coba = False
        st.session_state.coba3 = False
        st.session_state.materi1 = False
        st.session_state.materi2 = True
        st.session_state.tampilan = False
        st.session_state.materiU = False
        st.session_state.diskusian = False
        st.session_state.prasyaratan = False
        st.session_state.kumpulanH['kondisi7']=True
        st.session_state.kumpulanH['kondisi9']=True
        st.rerun()


            
def gambaran():
    # ----------------------
# Konfigurasi Cloudinary
# ----------------------
    cloudinary.config(
        cloud_name="ikip-siliwangi",
        api_key="828299653824342",
        api_secret="x_VT-fDecxYHYyN1Wkk7kjyuU1U"
    )

    st.title("Canvas Gambar ke Cloudinary")
    # --------------------------
    # 1. Buat canvas gambar
    # --------------------------
    st.subheader("Gambar di bawah:")
    canvas_result = st_canvas(
        fill_color="rgba(255, 165, 0, 0.3)",  # Transparansi warna
        stroke_width=3,
        stroke_color="#000000",
        background_color="#ffffff",
        height=300,
        width=400,
        drawing_mode="freedraw",
        key="canvas",
    )

    # --------------------------
    # 2. Upload ke Cloudinary
    # --------------------------
    if canvas_result.image_data is not None:
        st.image(canvas_result.image_data, caption="Hasil Gambar", use_container_width=True)

        if st.button("Upload ke Cloudinary"):
            # Simpan hasil gambar ke buffer
            img = Image.fromarray(canvas_result.image_data.astype("uint8"))
            buf = io.BytesIO()
            img.save(buf, format="PNG")
            buf.seek(0)

            # Upload ke Cloudinary
            result = cloudinary.uploader.upload(buf, folder="gambar_streamlit/",public_id=st.session_state.nama)
            st.success("Berhasil diupload!")
            st.image(result['secure_url'], caption="Link dari Cloudinary")
            st.write("URL:", result['secure_url'])


def persoalan1():
    st.subheader("Awal Petualangan – Mengukur Jarak Dua Pohon")
    st.markdown("""
    <div class="para">
       Pagi yang cerah di Desa Suka Maju. Rian, Nisa, Andi, Wati, dan Edo
       berkumpul di lapangan RT 03 untuk memulai petualangan mereka mencari
       harta karun segitiga ajaib. Mereka telah menerima petunjuk pertama
       dari panitia festival.
    </div>
    """,unsafe_allow_html=True)
    st.markdown("""
    <div class="para">
       Rian, yang memiliki ketelitian dalam mengukur, menemukan dua pohon besar
       di pinggir lapangan. Menurut petunjuk yang diberikan, kedua pohon ini menjadi
       titik awal petualangan mereka. Ia mengukur jarak antara kedua pohon tersebut
       dan mendapati bahwa jaraknya adalah 6 meter.
    </div>
    """,unsafe_allow_html=True)
    st.markdown("""
    <div class="para">
       Di tengah kedua pohon, terpasang sebuah bendera berwarna merah yang menjadi
       titik start perburuan harta karun. Menurut petunjuk selanjutnya, mereka harus
       berjalan tegak lurus dari bendera menuju sungai kecil yang ada di pinggir lapangan.
       Rian mengukur jarak dari bendera ke sungai dan mendapati bahwa jaraknya adalah 8 meter.
    </div>
    """,unsafe_allow_html=True)
    with st.container(height=200):
            st.markdown("""
                ### "Hmm, petunjuk berikutnya mengatakan kita perlu mengetahui jarak terpendek dari pohon ke sungai. Tapi pohon mana? Dan bagaimana cara menghitungnya? tanya Wati bingung.
            """)
    # Sisipkan HTML untuk GeoGebra Applet
    html_code = """
<div id="geogebra-container"></div>

<script src="https://www.geogebra.org/scripts/deployggb.js"></script>
<script>
  var ggbApp = new GGBApplet({
    "appName": "classic",
    "width": 1200,
    "height": 500,
    "material_id": "wmkfatpf",  // Ganti dengan material_id kamu
    "showToolBar": false,
    "showAlgebraInput": false,
    "enableShiftDragZoom": false,
    "enableRightClick": false,
    "enableLabelDrags": false,
    "enableZoomButtons": false,
    "showMenuBar": false,
    "showResetIcon": false
  }, true);

  window.onload = function () {
    ggbApp.inject('geogebra-container');

    // Pastikan objek siap sebelum setCoordSystem
    let attempts = 0;
    const trySetView = setInterval(() => {
      try {
        const app = ggbApp.getAppletObject();
        if (app && typeof app.setCoordSystem === "function") {
          app.setCoordSystem(-5, 35, -5, 20);
          clearInterval(trySetView);
        }
      } catch (e) {}
      if (++attempts > 20) clearInterval(trySetView);
    }, 300);
  };
</script>
"""

    # Tampilkan di Streamlit
    components.html(html_code, height=300)
    st.subheader("Soal")
    st.markdown("""
    <div class="para" style="background-color:cyan;box-shadow:-2px -2px 2px 2px red, 2px 2px 2px 2px green">
       Jika Rian berjalan tegak lurus dari bendera ke sungai sejauh 8 meter,
       berapa jarak terpendek dari masing-masing pohon ke sungai?
       (Gunakan teorema Pythagoras)
    </div>
    """,unsafe_allow_html=True)
    st.subheader("Petunjuk Penyelesaian:")
    st.markdown("""
    <div class="para" style="background-color:yellow;box-shadow:-2px -2px 2px 2px red, 2px 2px 2px 2px green">
       <ol>
           <li>Gambarlah situasi ini dalam bentuk segitiga siku-siku</li>
           <li>Identifikasi sisi-sisi segitiga yang diketahui</li>
           <li>Gunakan teorema Pythagoras untuk menghitung jarak terpendek</li>
           <li>Jelaskan langkah-langkah perhitungan dengan rinci</li>
       </ol>
    </div>
    """,unsafe_allow_html=True)

if st.session_state.coba2:
    persoalan1()
if st.session_state.kumpulanH['kondisi7']:
    if st.sidebar.button("Mencari Harta Karun"):
        st.session_state.coba=False
        st.session_state.coba1=False
        st.session_state.coba2=True
        st.session_state.coba3 = False
        st.session_state.materi1 = False
        st.session_state.materi2 = False
        st.session_state.tampilan = False
        st.session_state.materiU = False
        st.session_state.diskusian = False
        st.session_state.prasyaratan = False
        st.session_state.kumpulanH['kondisi8']=True
        st.session_state.kumpulanH['kondisi9']=True
        st.rerun()

    
def persoalan2():
    st.subheader("Bendera Hilang dan Analisis Data")
    st.markdown("""
    <div class="para">
    Keesokan harinya, kelima sahabat itu kembali ke lapangan untuk
    melanjutkan petualangan mereka. Namun, mereka mendapati bahwa bendera
    merah yang menjadi titik start telah hilang! Nisa, yang memiliki
    kejelian dalam menganalisis data, mencoba mengingat posisi bendera kemarin.
    </div>
    """,unsafe_allow_html=True)
    st.markdown("""
    <div class="para">
    "Tunggu, sepertinya bendera itu tidak tepat berada di tengah kedua pohon,"
    ujar Nisa sambil membuka catatannya. "Menurut pengukuranku kemarin, bendera
    itu berjarak 4 meter dari pohon pertama dan 7 meter dari pohon kedua."
    </div>
    """,unsafe_allow_html=True)
    with st.container(height=200):
        st.markdown("""
                ### "Tunggu, sepertinya bendera itu tidak tepat berada di tengah kedua pohon,"ujar Nisa sambil membuka catatannya. "Menurut pengukuranku kemarin, bendera itu berjarak 4 meter dari pohon pertama dan 7 meter dari pohon kedua."
            """)
    with st.container(height=200):
        st.markdown("""
                ### "Itulah yang aneh," jawab Nisa. "Mari kita analisis apakah data ini masuk akal atau tidak. Jika bendera, pohon pertama, dan pohon kedua membentuk segitiga, apakah segitiga tersebut valid?"
            """)
    st.subheader("Soal")
    st.markdown("""
    <div class="para" style="background-color:cyan;box-shadow:-2px -2px 2px 2px red, 2px 2px 2px 2px green">
       Apakah mungkin posisi bendera sesuai dengan data pengukuran Nisa, yaitu berjarak 4 meter
       dari pohon pertama dan 7 meter dari pohon kedua, sementara jarak antara kedua pohon adalah 6 meter?
       Tunjukkan perhitungan dan analisis untuk membuktikan jawabanmu!
    </div>
    """,unsafe_allow_html=True)
    st.subheader("Petunjuk Penyelesaian:")
    st.markdown("""
    <div class="para" style="background-color:yellow;box-shadow:-2px -2px 2px 2px red, 2px 2px 2px 2px green">
       <ol>
           <li>Gambarlah situasi ini dalam bentuk segitiga siku-siku</li>
           <li>Identifikasi sisi-sisi segitiga yang diketahui</li>
           <li>Gunakan teorema Pythagoras untuk menghitung jarak terpendek</li>
           <li>Jelaskan langkah-langkah perhitungan dengan rinci</li>
       </ol>
    </div>
    """,unsafe_allow_html=True)
if st.session_state.coba1:
    persoalan2()

if st.session_state.kumpulanH['kondisi8']:
    if st.sidebar.button("Bendera Hilang"):
        st.session_state.coba=False
        st.session_state.coba1=True
        st.session_state.coba2=False
        st.session_state.coba3 = False
        st.session_state.materi1 = False
        st.session_state.materi2 = False
        st.session_state.tampilan = False
        st.session_state.materiU = False
        st.session_state.diskusian = False
        st.session_state.prasyaratan = False
        st.session_state.kumpulanH['kondisi9']=True
        st.rerun()

if st.session_state.kumpulanH['kondisi9']:
    if st.sidebar.button("gambar"):
        st.session_state.coba = True
        st.session_state.coba3 = False
        st.session_state.materi1 = False
        st.session_state.materi2 = False
        st.session_state.tampilan = False
        st.session_state.materiU = False
        st.session_state.diskusian = False
        st.session_state.prasyaratan = False
        st.rerun()
if st.session_state.coba:
    gambaran()
    
#Menggunakan firebase
def diskusi1():
    percobaan = st.session_state.nama
    percobaan1 = st.session_state.kelas
    html_text=f"""
    <html>
    <head>
        <style>
            #judul{{
                font-family:broadway;
                font-size:20px;
                color:black;
                background-color:yellow;
                padding:5px;
                width:200px;
                
            }}
            textarea {{
              width: 100%;
              height: 50px;
              padding: 10px;
              font-size: 16px;
              resize: vertical;
              border: 1px solid #ccc;
              border-radius: 5px;
              margin:10px;
            }}
            #tombol{{
                width:150px;
                height:30px;
                padding:2px;
            }}
            #nama, #kelas{{
                display:none;
            }}
            #tampilkan{{
                color:white;
            }}
        </style>
    </head>
    <body>
        <div><input id="nama" type="text" value={percobaan}><input id="kelas" type="text" value={percobaan1}></div>
        <div id='judul'>Ruang Diskusi</div>
        <div><textarea id="myText" placeholder="Ketik sesuatu di sini..."></textarea></div>
        <div>alamat link (gambar): <input id='gambar' type='text'></div>
        <div><input id="tombol" type="button" value="masukan"></div>
        <div id="tampilkan">cova</div>
        
        <script type='module'>
        import {{ initializeApp }} from "https://www.gstatic.com/firebasejs/12.0.0/firebase-app.js";
        import {{ getDatabase, ref, push, onValue, set }} from "https://www.gstatic.com/firebasejs/12.0.0/firebase-database.js";
        const firebaseConfig = {{
            apiKey: "AIzaSyAVdiW32EvNadHCs_fhSSpTeIeqxQq0XRg",
            authDomain: "datacv-4ce08.firebaseapp.com",
            databaseURL: "https://datacv-4ce08-default-rtdb.firebaseio.com",
            projectId: "datacv-4ce08",
            storageBucket: "datacv-4ce08.firebasestorage.app",
            messagingSenderId: "168573025334",
            appId: "1:168573025334:web:e35db4e0d85d24e7acec97",
            measurementId: "G-FEBNQSBXC9"
      }};
        
      // Initialize Firebase
          const app = initializeApp(firebaseConfig);
          const db = getDatabase(app);

        //ketika menekan tombol
        const tombol = document.getElementById("tombol")
        const nama = document.getElementById("nama")
        const kelas = document.getElementById("kelas")
        const disk = document.getElementById("myText")
        const tampilkan = document.getElementById("tampilkan")
        const gambar = document.getElementById("gambar")
        const link = ''
        tombol.addEventListener("click",function(){{
            if (nama) {{
                alert("masukan")
                const questionRef = push(ref(db, "questions1"));
                set(questionRef, {{
                  nama:nama.value,        // Pertanyaan yang dimasukkan
                  kelas:kelas.value, // Timestamp saat ini
                  dsk: disk.value,      // Node kosong untuk jawaban
                  gmbr: gambar.value
                }});
            }};
        }})
        //tampilan otomatis
        onValue(ref(db, 'questions1'), (snapshot) => {{
          const data = snapshot.val();
          let tulisan = ''
          for(let key in data){{
              tulisan += '<div>'+data[key].nama+'_'+data[key].kelas+'</div><div style="background-color:cyan;color:black;margin-bottom:10px">'+data[key].dsk+'</div>'
              if(data[key].gmbr!=''){{
                  tulisan += '<div><iframe src='+data[key].gmbr+'></iframe></div>'
              }}
          }}
          tampilkan.innerHTML = tulisan
        }});

        </script>
    </body>
    </html>
    """
    components.html(html_text, height=1500)
    
if st.session_state.diskusian:
    diskusi1()
if st.session_state.kumpulanH['kondisi10']:
    if st.sidebar.button("Diskusi"):
        st.session_state.coba=False
        st.session_state.coba1=False
        st.session_state.coba2=False
        st.session_state.coba3 = False
        st.session_state.materi1 = False
        st.session_state.materi2 = False
        st.session_state.tampilan = False
        st.session_state.materiU = False
        st.session_state.diskusian = True
        st.session_state.prasyaratan = False
        st.rerun()
