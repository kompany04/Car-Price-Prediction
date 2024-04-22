import pandas as pd
import pickle
import streamlit as st


# Load the saved Ridge model
model_filename = r'model_car_price.pkl'
with open(model_filename, 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Define available options
manufacturer_options = ['Maruti', 'Hyundai', 'Datsun', 'Honda', 'Tata', 'Chevrolet',
       'Toyota', 'Jaguar', 'Mercedes-Benz', 'Audi', 'Skoda', 'Jeep',
       'BMW', 'Mahindra', 'Ford', 'Nissan', 'Renault', 'Fiat',
       'Volkswagen', 'Volvo', 'Mitsubishi', 'Land', 'Daewoo', 'MG',
       'Force', 'Isuzu', 'OpelCorsa', 'Ambassador', 'Kia']

model_options = ['800', 'Wagon', 'Verna', 'GO', 'Amaze', 'Alto', 'Xcent', 'Indigo',
       'Creta', 'Celerio', 'Sail', 'Corolla', 'Ciaz', 'Venue', 'Enjoy',
       'XF_2.2', 'New', 'Vitara', 'Audi_other', 'City', 'Tigor', 'Superb',
       'Innova', 'other', 'E-Class', 'i10', 'BMW_other', 'tt', 'Elantra',
       'Scorpio', 'Santro', 'Swift', 'Eeco', 'i20', 'Omni', 'Jeep',
       'Indica', 'EON', 'Etios', 'Tavera', 'EcoSport', 'Civic', 'Rapid',
       'Hyundai_other', 'Terrano', 'Brio', 'S-Class', 'XUV500', 'Duster',
       'Bolero', 'Avventura', 'Jetta', 'V40', 'SX4', 'Micra', 'Xylo',
       'KWID', 'Ertiga', 'Beat', 'Zen', 'Baleno', 'Nano', 'Cruze',
       'Aspire', 'Spark', 'Bolt', 'Quanto', 'XJ_5.0', 'Nexon', 'Vento',
       'Figo', 'Esteem', 'Linea', 'Scala', 'Mahindra_other', 'S-Cross',
       'Ameo', 'Renault', 'Optra', 'Mobilio', 'Zest', 'Fabia', 'Fiesta',
       'Sumo', 'Jazz', 'Tiago', 'Marazzo', 'A-Star', 'Yeti', 'Outlander',
       'Endeavour', 'Polo', 'Ritz', 'Estilo', 'Manza', 'Safari',
       'Fortuner', 'Ford_other', 'KUV_100', 'Accord', 'TUV_300', 'BR-V',
       'Ikon', 'Fiat_other', 'WR-V', 'Laura', 'Jaguar_other', 'GL-Class',
       'Pulse', 'C-Class', 'Gypsy', 'Verito', 'Hexa', 'Venture',
       'Captiva', 'Aveo', 'Thar', 'Octavia', 'Rover_Discovery', 'Lodgy',
       'Grande_Punto', 'Palio', 'M-Class', 'Ignis', 'Sunny', 'Camry',
       'Pajero', 'Xenon', 'Captur', 'Passat', 'Aria', 'CR-V', 'XF_3.0',
       'S-Presso', 'Yaris', 'Fluence', 'Evalia', 'Koleos', 'Harrier',
       'Altroz', 'Kicks', 'Honda_other', 'B_Class', 'Triber', 'Montero',
       'X-Trail', 'XC', 'Classic', 'Grand', 'CrossPolo',
       'Rover_Range_Rover', 'Spacio', 'Winger', 'Ambassador_other', 'GLS',
       'Qualis']

fuel_options = ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric']

seller_options = ['Individual', 'Dealer', 'Trustmark Dealer']

transmission_options = ['Manual', 'Automatic']

owner_options = ['First Owner', 'Second Owner', 'Fourth & Above Owner',
       'Third Owner', 'Test Drive Car']




# Streamlit app
st.title('Car Price Prediction')

# Sidebar for user input
st.sidebar.header('User Input')
user_input = {}
features = [ 'manufacturer', 'model','year', 'km_driven', 'fuel', 'seller_type',
             'transmission', 'owner']

for feature in features:
    if feature == 'manufacturer':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', manufacturer_options)
    elif feature == 'model':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', model_options)
    elif feature == 'year':
        user_input[feature] = st.sidebar.number_input(f'Enter the {feature}:', min_value=1992, max_value=2024, step=1)
    elif feature == 'km_driven':
        user_input[feature] = st.sidebar.number_input(f'Select the {feature}:',min_value=0)
    elif feature == 'fuel':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', fuel_options)
    elif feature == 'seller_type':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', seller_options)
    elif feature == 'transmission':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', transmission_options)
    elif feature == 'owner':
        user_input[feature] = st.sidebar.selectbox(f'Select the {feature}:', owner_options)
    
    else:
        user_input[feature] = st.sidebar.text_input(f'Enter the {feature}:')


print(user_input)
# Add a "Predict" button
if st.sidebar.button('Predict'):
    # Convert user input to a DataFrame
    user_df = pd.DataFrame([user_input.values()], columns=['manufacturer', 'model', 'year', 'km_driven', 'fuel',
       'seller_type', 'transmission', 'owner'])

    print(user_df)

    
    #user_prediction = loaded_model.predict(pd.DataFrame([['santa barbara', 2019, 'jeep', 'cherokee', 'good', 4, 97994, 'clean','automatic', 'fwd', 'SUV', 'black', 'ca', 'gas']],columns=['region', 'year', 'manufacturer', 'model', 'condition','cylinders', 'odometer', 'title_status', 'transmission','drive', 'type', 'paint_color', 'state', 'fuel']))
    user_prediction = loaded_model.predict(user_df)

    # Display the prediction
    st.subheader('Prediction Result')
    formatted_prediction = "₹{:.2f}".format(user_prediction[0])
    st.write(f'The predicted price for the car is: {formatted_prediction}')


