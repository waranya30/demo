import streamlit as st
import pandas as pd 
from sklearn.linear_model  import LinearRegression
import joblib
st.title(':blue[Cars Showroom]')
st.write('เว็บไซต์นี้นำเสนอรถยนต์ในเลทราคาที่ท่านต้องการ')
left, center,right = st.columns(3)
if left:
    add_number = left.number_input(':violet[ราคารถที่ต้องการ]')
if center:
    add_band = center.selectbox(
    ':violet[ยี่ห้อรถยนต์]',
    ('Toyota', 'Honda', 'Ford', 'Benz'))

predictb = left.button('ประเมินราคา')
if predictb:
        if 500000 <= add_number <= 800000:
            df = pd.read_csv('model.csv')
            if add_band:
                data = df[df['Bands'].str.contains(add_band, case=False)]
                st.dataframe(data)
            if add_band =='Toyota':
                st.image('https://s3.amazonaws.com/files.activate.social/user-image-31543935-1557939530-5cdc454a86e3c',width=600,caption='Toyota New Vios 1.5J M/T ราคา 559,000 บาท')
                st.image('https://www.checkraka.com/uploaded/logo/bb/bbf10ed94baaf21f688433c64800b668.jpg',width=600,caption='Toyota B-CAB 4x2 2.4J plus ช่วงล้อสั้น ราคา 569,000 บาท')
                st.image('https://www.checkraka.com/uploaded/gallery/d2/d2e1915f31b895bed89514fc0af5651f.jpg',width=600,caption='Toyota Revo B-CAB 4x4(4WD) ราคา 668,000 บาท')

            if add_band =='Honda':
                st.image('https://www.checkraka.com/uploaded/gallery/78/78af5fa5b4fc0ade8f22639a4e89d619.jpg',width=600,caption='Honda City S ราคา 579,000 บาท')
                st.image('https://img.indianautosblog.com/2019/11/28/2020-honda-city-rs-exterior-11-3eb5.jpg',width=600,caption='Honda City RS ราคา 739,000 บาท')

            if add_band =='Ford':
                st.image('https://www.checkraka.com/uploaded/logo/7e/7e5276ab24636a7af6b5ba4c3fd033d3.png',width=600,caption='Ford Ranger Standard Chassis Cab XL 2.0L Turbo LR 5MT ราคา 564,000 บาท')
                st.image('https://www.checkraka.com/uploaded/_resized/max_400x300/14/1477c621fa6a41815c34a932f7a69e9d.png',width=600,caption='Ford Ranger Open Cab XL 2.0L Turbo LR 5MT ราคา 645,000 บาท')
                st.image('https://www.checkraka.com/uploaded/gallery/27/271e93d6221ee39003cbb2d2fa8aaea8.jpg',width=600,caption='Ford SWB 2.0L Turbo 4x2 6AT ราคา 669,000 บาท')
                st.image('https://images.autofun.co.th/file1/9a1c3177436b499ea9491a888700df70_456x258.jpg',width=600,caption='Ford Ranger Standard Cab XL 2.0L Turbo 4x4 6MT ราคา 707,000 บาท')
            if add_band =='Benz':
                st.write('ยี่ห้อรถยนต์นี้อยู่ในเลทราคาที่สูงขึ้น')

        if add_number >= 810000:
            dt = pd.read_csv('band2.csv')
            if add_band:
                data2 = dt[dt['Bands'].str.contains(add_band, case=False)]
                st.dataframe(data2)
                if add_band =='Toyota':
                    st.image('https://i.ytimg.com/vi/sOak6coPQ1M/maxresdefault.jpg',width=600, caption='Toyota D-CAB 4x4 2.4E ราคา 892,000 บาท')
                    st.image('https://cdn.motor1.com/images/mgl/kk8gB/s3/2015-555325-toyota-corolla-esport-nurburgring-edition-at-2015-bangkok-motor-show1.jpg',width=600, caption='Toyota New Corolla Altis Esport nurburgring edition ราคา 949,000 บาท')
                    st.image('https://cdn.motor1.com/images/mgl/GNAE1/s3/2019-toyota-prius-by-trd.jpg',width=600, caption='Toyota Prius Topoption TRD ราคา 1,399,000 บาท')
                    st.image('https://www.checkraka.com/uploaded/logo/fe/fe8cc66694f16c5bfcf3db6c33ce0f18.jpg',width=600, caption='Toyota Fortuner VA/T 4x4 ราคา 1,629,000 บาท')
                    st.image('https://www.autodeft.com/_uploads/images/2015/Toyota%20Australia/15Camry_03.jpg',width=600, caption='Toyota Camry Esport ราคา 1,639,000 บาท')

                if add_band =='Honda':
                    st.image('https://www.carwizard.co.th/wp-content/uploads/2022/08/001-Honda-BR-V.jpeg',width=600, caption='Honda All-New BR-V EL-Premium Sunlight ราคา 977,000 บาท')
                    st.image('https://www.drivingplace.com/images/NEW%20CARS/HONDA2019_New-Civic-Hatchback-RS/New-Civic-Hatchback-RS-024.jpg',width=600, caption='Honda New Civic Hatcthbaack Turbo RS ราคา 1,229,000 บาท')
                    st.image('https://img.kaidee.com/prd/20221227/367326701/m/7fd8235d-2fbe-47ca-aac5-41877bcbfb62.jpg',width=600, caption='Honda CR-V 2.4 EL(4WD) ราคา 1,579,000 บาท')
                    st.image('https://www.9carthai.com/wp-content/uploads/2021/08/HONDA-ACCORD-eHEV.png',width=600, caption='Honda The Accord e:HEV Tech Turbo ราคา 1,799,000 บาท')

                if add_band =='Ford':
                    st.image('https://www.checkraka.com/uploaded/gallery/9c/9c025247ccd7842657e4a18a8ec9b367.png',width=600, caption='Ford Ranger Double Cab XL+ 2.0L Turbo 6MT ราคา 802,000 บาท')
                    st.image('https://imgcdn.zigwheels.co.th/medium/gallery/exterior/8/3061/ford-ranger-front-angle-low-view-235057.jpg',width=600, caption='Ford SWB 2.0L Bi-turbo 4x4 10AT ราคา 849,000 บาท')
                    st.image('https://www.checkraka.com/uploaded/gallery/c3/c3da29ae816eb113f1890f171ebbd57c.jpg',width=600, caption='Ford Ranger Double Cab XLT 2.0L Turbo HR 6AT ราคา 944,000 บาท')
                    st.image('https://tse3.mm.bing.net/th?id=OIP.773X20qJ5lSFVowOmT-FLQHaEL&pid=Api&P=0',width=600, caption='Ford Ranger Double Cab Wildtrak 2.0L Turbo HR 6AT ราคา 1,064,000 บาท')
                    st.image('https://www.ford.co.th/content/dam/ecomm/Release-3/EN_TH/offer/P703_TH_WILDTRAK_DBL_PantherJ_4x2_HiRide_LuxeYellow.png',width=600, caption='Ford Ranger Double Cab Wildtrak 2.0L Bi-Turbo HR 10AT ราคา 1,174,000 บาท')

                if add_band =='Benz':
                    st.image('https://acroadtrip.blob.core.windows.net/catalogo-imagenes/m/RT_V_cd9fdc1e7be64b888fe73b5c8c0fc8f4.jpg',width=600, caption='Benz Mercedes-Benz A 200 Progressive (1,332 ซีซี) ราคา 1,990,000 บาท')
                    st.image('https://luxina.id/wp-content/uploads/2021/02/asset.MQ4_.0.2x.20200918151815-2048x1151.jpg',width=600, caption='Benz Mercedes-Benz GLA 200 Progressive (1,332 ซีซี) ราคา 2,330,000 บาท')
                    st.image('https://carnetwork.s3.ap-southeast-1.amazonaws.com/file/27288324242a4c68aa0cca3a09e00868.jpg',width=600, caption='Benz Mercedes-Benz E 300 e AMG Dynamic (1,991 ซีซี) ราคา 3,899,000 บาท')
                    st.image('https://www.9carthai.com/wp-content/uploads/2020/01/New-Mercedes-Benz-E-200-Coupe-AMG-Dynamic-1.jpg',width=600, caption='Benz Mercedes-Benz E 200 Coupe AMG Dynamic (1,991 ซีซี) ราคา 4,850,000 บาท')
                    st.image('https://www.autotecnica.org/wp-content/uploads/2016/09/apre10.jpg',width=600, caption='Benz Mercedes-AMG GLC 43 4MATIC Coupe (2,996 ซีซี) ราคา 5,100,000 บาท')
                    st.image('https://images-na.ssl-images-amazon.com/images/I/717X0B8fM2L._AC_SL1280_.jpg',width=600, caption='Benz Mercedes-AMG C 63 S Coupe (3,982 ซีซี) ราคา 10,129,000 บาท')
                    st.image('https://www.fudgenmore.com/wp-content/uploads/INKAS_Mercedes_Benz_G63_04-1.jpg',width=600, caption='Benz Mercedes-AMG G 63 (3,982 ซีซี) ราคา 16,300,000 บาท')
                    st.image('https://s.aolcdn.com/commerce/autodata/images/USD10MBCCM1A021001.jpg',width=600, caption='Benz Mercedes-Maybach S 580 4MATIC Premium (3,982 ซีซี) ราคา 18,300,000 บาท')
def generate_save_data():
    pass
def load_save_data():
    return pd.read_excel('p.xlsx')

def save_model(model):
    joblib.dump(model, 'model.joblib')

def load_model():
    return joblib.load('model.joblib')
def generate_save_data():
    pass

generateb = st.button('generate Automobile')
if generateb:
    st.write('generating "Automobile" ...')
    generate_save_data()
    right.write(' ... done')
loadb = st.button('load Automobile')
if loadb:
    st.write('loading "Automobile"')
    st.write('... done')
    df = pd.read_excel('p.xlsx', index_col=0)
    st.dataframe(df)

trainb = st.button('Predict Automobile')
if trainb:
    st.write('แนวโน้มอุตสาหกรรมยายยนต์ไทยในปี 2566 ...')
    df = pd.read_excel('p.xlsx', index_col=0)
    model = LinearRegression()
    st.write('... done')
    st.dataframe(df)
    st.write("autospinn.com")
    save_model(model)
