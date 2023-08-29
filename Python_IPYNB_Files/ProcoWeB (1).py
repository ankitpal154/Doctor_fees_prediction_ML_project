from flask import Flask,request,render_template


import numpy as np
import pickle  
import pandas as pd



model = pickle.load(open('website/lr_model.pkl','rb'))


unique_location = ['AECS Layout',
 'Akshaya nagar',
 'Alaknanda',
 'Anand Niketan',
 'Anand Vihar',
 'Andheri',
 'Andheri East',
 'Andheri West',
 'Ansari Nagar',
 'Arekere',
 'Ashok Vihar',
 'Ashok Vihar Phase 1',
 'Ashoknagar',
 'Avalahalli',
 'Azadpur',
 'BEL Layout',
 'BTM Layout',
 'BTM Layout 1st Stage',
 'BTM Layout 2nd Stage',
 'Bagalur',
 'Bali Nagar',
 'Banashankari',
 'Banashankari 1st Stage',
 'Banashankari 2nd Stage',
 'Banashankari 3rd Stage',
 'Banaswadi',
 'Bandra',
 'Bandra East',
 'Bandra West',
 'Bannerghatta Road',
 'Basavanagudi',
 'Basaveshwaranagar',
 'Begur',
 'Belathur',
 'Bellandur',
 'Bhandup',
 'Bhandup West',
 'Bhattarahalli',
 'Bhogal',
 'Bilekahalli',
 'Bommanahalli',
 'Bommasandra',
 'Borivali',
 'Borivali East',
 'Borivali West',
 'Brigade Road',
 'Burari',
 'CR Park',
 'CV Raman Nagar',
 'Chamarajpet',
 'Chanakyapuri',
 'Chandivali',
 'Chandra Layout',
 'Charni Road',
 'Chattarpur',
 'Chembur',
 'Chembur East',
 'Chembur West',
 'Chinchpokli',
 'Chira Bazaar',
 'Chirag Delhi',
 'Chitra Vihar',
 'Churchgate',
 'Colaba',
 'Connaught Place',
 'Cuffe Parade',
 'Cumballa Hill',
 'DLF Newtown',
 'DN Nagar',
 'Dadar',
 'Dadar East',
 'Dadar West',
 'Dahisar',
 'Dahisar East',
 'Dahisar West',
 'Dasarahalli',
 'Dashrath Puri',
 'Defence Colony',
 'Delhi',
 'Dilshad Garden',
 'Doddakammanahalli',
 'Domlur',
 'Dongri',
 'Durga Puri',
 'Dwarka',
 'Dwarka Sector 11',
 'Dwarka Sector 12',
 'Dwarka Sector 13',
 'Dwarka Sector 17',
 'Dwarka Sector 19',
 'Dwarka Sector 22',
 'Dwarka Sector 23',
 'Dwarka Sector 3',
 'Dwarka Sector 6',
 'Dwarka Sector 7',
 'Dwarka Sector 8',
 'Dwarka Sector 9',
 'East Of Kailash',
 'Electronics City',
 'Elphinstone Road',
 'Fort',
 'Frazer Town',
 'Ghatkopar',
 'Ghatkopar East',
 'Ghatkopar West',
 'Ghitorni',
 'Girgaon',
 'Goregaon',
 'Goregaon East',
 'Goregaon West',
 'Govandi',
 'Grant Road',
 'Greater Kailash',
 'Greater Kailash Part 1',
 'Greater Kailash Part 2',
 'Green Park',
 'Gubbalala',
 'Gujranwala Town',
 'Gulabi Bagh',
 'Gunjur',
 'HAL 2nd Stage',
 'HAL 3rd Stage',
 'HBR Layout',
 'HRBR Layout',
 'HSR Layout',
 'Hanumanthnagar',
 'Hari Nagar',
 'Harlur',
 'Harsh Vihar',
 'Hauz Khas',
 'Hebbal',
 'Hebbal Kempapura',
 'Hegde Nagar',
 'Hennur',
 'Hongasandra',
 'Hoodi',
 'Horamavu',
 'Hosur Road',
 'Hulimavu',
 'IP Extension',
 'Indiranagar',
 'JB Nagar',
 'JP Nagar',
 'JP Nagar 1 Phase',
 'JP Nagar 2 Phase',
 'JP Nagar 3 Phase',
 'JP Nagar 4 Phase',
 'JP Nagar 5 Phase',
 'JP Nagar 6 Phase',
 'JP Nagar 7 Phase',
 'JP Nagar 8 Phase',
 'JP Nagar 9 Phase',
 'Jacob Circle',
 'Jagriti Enclave',
 'Jakkur',
 'Jalahalli',
 'Janakpuri',
 'Jangpura',
 'Jasola',
 'Jayanagar',
 'Jayanagar 2 Block',
 'Jayanagar 3 Block',
 'Jayanagar 4 Block',
 'Jayanagar 5 Block',
 'Jayanagar 7 Block',
 'Jayanagar 8 Block',
 'Jayanagar 9 Block',
 'Jeevanbhimanagar',
 'Jhandewalan',
 'Jogeshwari',
 'Jogeshwari East',
 'Jogeshwari West',
 'Juhu',
 'KR Puram',
 'Kadugodi',
 'Kaggadasapura',
 'Kailash Colony',
 'Kalina',
 'Kalkaji',
 'Kalyan Nagar',
 'Kalyan Vihar',
 'Kamla Nagar',
 'Kammana Halli',
 'Kanakpura Road',
 'Kandivali',
 'Kandivali East',
 'Kandivali West',
 'Kanjurmarg',
 'Kapashera',
 'Karkardooma',
 'Karol Bagh',
 'Kasavanahalli',
 'Kasturi nagar',
 'Katwaria Sarai',
 'Kemps Corner',
 'Kengeri',
 'Khanpur',
 'Khar West',
 'Khetwadi',
 'Kilokri',
 'Kingsway Camp',
 'Kirti Nagar',
 'Kodichikkanahalli',
 'Konanakunte',
 'Koramangala',
 'Koramangala 1 Block',
 'Koramangala 4 Block',
 'Koramangala 5 Block',
 'Koramangala 6 Block',
 'Koramangala 7 Block',
 'Koramangala 8 Block',
 'Kothanur',
 'Krishna Nagar',
 'Kudlu',
 'Kumara Park West',
 'Kumaraswamy Layout',
 'Kundalahalli',
 'Kurla',
 'Kurla East',
 'Kurla West',
 'Lajpat Nagar',
 'Lajpat Nagar 4',
 'Lal baug',
 'Lamington Road',
 'Langford Road',
 'Laxmi Nagar',
 'Lingarajapuram',
 'Lokhandwala',
 'Lower Parel',
 'Madangir',
 'Madhu Vihar',
 'Magrath Road',
 'Mahadevapura',
 'Mahalakshmi Layout',
 'Maharani Bagh',
 'Mahavir Enclave',
 'Mahim',
 'Malabar Hill',
 'Malad',
 'Malad East',
 'Malad West',
 'Malleshpalya',
 'Malleswaram',
 'Malviya Nagar',
 'Marathahalli',
 'Marine Lines',
 'Marol',
 'Mathikere - BEL',
 'Matunga',
 'Matunga East',
 'Matunga West',
 'Mayur Vihar',
 'Mayur Vihar Ph-I',
 'Mayur Vihar Ph-II',
 'Mayur Vihar Ph-III',
 'Mazgaon',
 'Meera Bagh',
 'Mehrauli',
 'Millers Road',
 'Mira Bhayandar',
 'Mira Road',
 'Mira-Bhayandar Road',
 'Model Town 1',
 'Model Town 2',
 'Model Town 3',
 'Moti Nagar',
 'Mukherjee Nagar',
 'Mulund',
 'Mulund East',
 'Mulund West',
 'Mumbai Central',
 'Munirka',
 'Munnekollal',
 'Murugeshpalya',
 'Nagarbhavi',
 'Nagarbhavi 2nd Stage',
 'Nagasandra',
 'Nagawara',
 'Nagpada',
 'Nana Chowk',
 'Nandini Layout',
 'Nangloi',
 'Naraina',
 'Naraina Vihar',
 'Neb Sarai',
 'Nehru Place',
 'Nelamangala',
 'New BEL Road',
 'New Friends Colony',
 'New Rajendra Nagar',
 'New Thippasandra',
 'Nirman Vihar',
 'Nizamuddin East',
 'Okhla',
 'Okhla Industrial Estate',
 'Old Airport Road',
 'Old Rajendra Nagar',
 'Opera House',
 'Oshiwara',
 'Padmanabhanagar',
 'Panathur',
 'Panchsheel Enclave',
 'Panchsheel Park',
 'Pandav Nagar',
 'Parel',
 'Paschim Puri',
 'Paschim Vihar',
 'Patel Nagar',
 'Patel Nagar East',
 'Patel Nagar West',
 'Patparganj',
 'Peddar Road',
 'Pitampura',
 'Powai',
 'Prabhadevi',
 'Prashant Vihar',
 'Preet Vihar',
 'Pulikeshi Nagar',
 'Punjabi Bagh',
 'Pusa Road',
 'RK Puram',
 'RMV 2nd Stage',
 'RT Nagar',
 'Rajajinagar',
 'Rajarajeshwarinagar',
 'Rajouri Garden',
 'Ramamurthy Nagar',
 'Ramesh Nagar',
 'Rana Pratap Bagh',
 'Richmond Town',
 'Rohini',
 'Rohini Sector 11',
 'Rohini Sector 15',
 'Rohini Sector 16',
 'Rohini Sector 18',
 'Rohini Sector 22',
 'Rohini Sector 24',
 'Rohini Sector 3',
 'Rohini Sector 4',
 'Rohini Sector 5',
 'Rohini Sector 6',
 'Rohini Sector 7',
 'Rohini Sector 8',
 'Rohini Sector 9',
 'Sadashivanagar',
 'Safdarjung Development Area',
 'Safdarjung Enclave',
 'Sahakaranagar',
 'Saket',
 'Sakinaka',
 'Sampangiramnagar',
 'Sanjay Nagar',
 'Santacruz East',
 'Santacruz West',
 'Sarita Vihar',
 'Sarjapur Road',
 'Sarvodaya Enclave',
 'Seegehalli',
 'Seshadripuram',
 'Shahdara',
 'Shakti Nagar',
 'Shalimar Bagh',
 'Shastri Nagar',
 'Sheikh Sarai',
 'Shivaji Nagar',
 'Shivalik',
 'Siddapura',
 'Singasandra',
 'Sion',
 'Sion East',
 'Sion West',
 'Siri Fort Road',
 'South Extension 1',
 'South Extension 2',
 'Subhash Nagar',
 'Sukhdev Vihar',
 'Surajmal Vihar',
 'T Dasarahalli',
 'Tagore Garden',
 'Tardeo',
 'Thanisandra',
 'Tilak Nagar',
 'Tri Nagar',
 'Turner Road',
 'Uday Park',
 'Ulsoor',
 'Umerkhadi',
 'Upparahalli',
 'Uttam Nagar',
 'Uttarahalli',
 'VV Puram',
 'Varthur',
 'Vasant Kunj',
 'Vasant Vihar',
 'Vasanthnagar',
 'Vasundhra Enclave',
 'Versova',
 'Vidyaranyapura',
 'Vidyavihar',
 'Vijayanagar',
 'Vikas Puri',
 'Vikhroli',
 'Vikhroli East',
 'Vikhroli West',
 'Vileparle East',
 'Vileparle West',
 'Vinayaka Nagar',
 'Vishnu Garden',
 'Vishwas Nagar',
 'Viveknagar',
 'Wadala',
 'Walkeshwar',
 'West Of Chord Road',
 'Whitefield',
 'Wilson Garden',
 'Worli',
 'Yelachenahalli',
 'Yelahanka',
 'Yelahanka New Town',
 'Yelenahalli',
 'Yeshwanthpur',
 'Yojana Vihar',
 'Zakir Nagar']

unique_degrees = [
    'MSc',
 'PGD',
 'MS',
 'FDSRCS',
 'BDS',
 'DDVL',
 'BAMS',
 'MNAMS',
 'PGDCC',
 'DFFP',
 'BNYS',
 'DDPHN',
 'DPMDB',
 'MFGDP',
 'FCPS',
 'DNHE',
 'PGDE',
 'FFDRCSI',
 'DNB',
 'DHMS',
 'FRANZCP',
 'MRCP',
 'DDV',
 'DDHN',
 'DTCD',
 'FNB',
 'DMD',
 'Diplomate',
 'DICOI',
 'OBG',
 'BSc',
 'FRACP',
 'FAM',
 'FAICO',
 'DCH',
 'FCCM',
 'MBBS',
 'MRCOGUK',
 'FICOI',
 'MDS',
 'DM',
 'DVD',
 'FICOG',
 'MRCS',
 'MScBSc',
 'FMC',
 'FICS',
 'FRCPCH',
 'FRCP',
 'MD',
 'MRCPCH',
 'DOMS',
 'MPH',
 'FRCS',
 'DPM',
 'Diploma',
 'DMDB',
 'FACC',
 'NDDY',
 'DO',
 'MCh',
 'DGO',
 'BHMS',
 'FRCOG',
 'FCCP',
 'PhD'
]

unique_speciality = ['Bariatric',
 'Cardiologist',
 'Dentist',
 'Dermatologist',
 'Dietitian',
 'Gastroenterologist',
 'Gynecologist',
 'Infertility Specialist',
 'Neurologist',
 'Neurosurgeon',
 'Ophthalmologist',
 'Orthopedist',
 'Pediatrician',
 'Physiotherapist',
 'Psychiatrist',
 'Pulmonologist',
 'Rheumatologists',
 'Urologist']

unique_cities = ['Bangalore','Delhi','Mumbai']

def prepare_input(Year_of_experience, dp_score, npv, degree, speciality, location, city):
    
    # Create a dictionary to map cities to binary values
    degree_mapping = {}
    for i, c in enumerate(unique_degrees):
        degree_binary = [0] * len(unique_degrees)
        degree_binary[i] = 1
        degree_mapping[c] = degree_binary
        
    speciality_mapping = {}
    for i, c in enumerate(unique_speciality):
        speciality_binary = [0] * len(unique_speciality)
        speciality_binary[i] = 1
        speciality_mapping[c] = speciality_binary
        
    location_mapping = {}
    for i, c in enumerate(unique_location):
        location_binary = [0] * len(unique_location)
        location_binary[i] = 1
        location_mapping[c] = location_binary
    
    city_mapping = {}
    for i, c in enumerate(unique_cities):
        city_binary = [0] * len(unique_cities)
        city_binary[i] = 1
        city_mapping[c] = city_binary


    if degree in degree_mapping:
        degree_binary = degree_mapping[degree]
        
    if speciality in speciality_mapping:
        speciality_binary = speciality_mapping[speciality]
        
    if location in location_mapping:
        location_binary = location_mapping[location]
        
    if city in city_mapping:
        city_binary = city_mapping[city]

    # Return the input values in the desired numerical form
    return [Year_of_experience, dp_score, npv] + degree_binary + speciality_binary + location_binary+city_binary

#create  flask app
app=Flask(__name__)
#routs
@app.route('/')
def index():
    return render_template("index2.html")


@app.route('/predict',methods=['POST'])
def predict():
    Speciality=""
    Degree=""
    YrEx=0
    Location=""
    City=""
    DP=0
    NVP=0
    try:
        Speciality = request.form['Speciality']
    except:
        pass    
    try:
        Degree = request.form['Degree']
    except:
        pass    
    try:
        YrEx = float(request.form['YrEx'])
    except:
        pass 
    try:
        Location = request.form['Location']
    except:
        pass
    try:    
        City = request.form['City']
    except:
        pass
    try:
        DP = float(request.form['DP'])
    except:
        pass
    try:
        NVP = float(request.form['NPV'])
    except:
        pass    
    
    print(Speciality, Degree, YrEx, Location, City, DP,NVP,sep="\n")
    #prepare_input(Year_of_experience, dp_score, npv, degree, speciality, location, city):
    prepare_input(YrEx,DP,NVP,Degree,Speciality,Location,City)

    #features = np.array([Speciality, Degree, YrEx, Location, City, DP,NVP]).reshape(1, -1)
    prediction = model.predict([prepare_input(YrEx,DP,NVP,Degree,Speciality,Location,City)])
    
    return render_template('index2.html', Fees=int(prediction))

#python main

if __name__=="__main__":
    app.run(debug=True)



