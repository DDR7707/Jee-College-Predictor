import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore")


mains = pd.read_csv("Mains_2020.csv")
adv = pd.read_csv("Non_Prep_Adv_2020.csv")
prep = pd.read_csv("Preperatory_2020.csv")


college_sorter = ['Indian Institute of Technology Madras' ,
                  'Indian Institute of Technology Delhi' ,
                  'Indian Institute of Technology Bombay' ,
                  'Indian Institute of Technology Kanpur' ,                  
                  'Indian Institute of Technology Kharagpur' ,
                  'Indian Institute of Technology Roorkee' ,
                  'Indian Institute of Technology Guwahati' ,
                  'Jawaharlal Nehru University, Delhi' , 
                  'University of Hyderabad' ,
                  'Indian Institute of Technology Hyderabad' , 
                  'National Institute of Technology, Tiruchirappalli' ,
                  'Indian Institute of Technology Indore' ,
                  'Indian Institute of Technology (BHU) Varanasi' ,
                  'Indian Institute of Technology (ISM) Dhanbad' ,
                  'National Institute of Technology Karnataka, Surathkal' ,
                  'National Institute of Technology, Rourkela' ,
                  'National Institute of Technology, Warangal' ,
                  'Indian Institute of Engineering Science and Technology, Shibpur' ,
                  'Indian Institute of Technology Bhubaneswar' ,
                  'National Institute of Technology Calicut' ,
                  'Indian Institute of Technology Gandhinagar' , 
                  'Indian Institute of Technology Ropar' ,                  
                  'Indian Institute of Technology Patna' , 
                  'Visvesvaraya National Institute of Technology, Nagpur' ,
                  'Indian Institute of Technology Mandi' ,
                  'School of Engineering, Tezpur University, Napaam, Tezpur' ,
                  'Malaviya National Institute of Technology Jaipur' ,
                  'Birla Institute of Technology, Mesra, Ranchi' ,
                  'National Institute of Technology, Kurukshetra' ,
                  'National Institute of Technology, Silchar' ,
                  'National Institute of Technology Durgapur' ,
                  'Motilal Nehru National Institute of Technology Allahabad' ,
                  'Dr. B R Ambedkar National Institute of Technology, Jalandhar' , 
                  'Indian Institute of Technology Jodhpur' , 
                  'Sardar Vallabhbhai National Institute of Technology, Surat' ,
                  'National Institute of Technology Meghalaya' ,
                  'Maulana Azad National Institute of Technology Bhopal' ,
                  'Indian Institute of Information Technology Guwahati' ,
                  'National Institute of Technology Raipur' ,
                  'Punjab Engineering College, Chandigarh' ,
                  'National Institute of Technology Agartala' ,
                  'National Institute of Technology Goa' ,
                  'National Institute of Technology, Jamshedpur' ,
                  'Pt. Dwarka Prasad Mishra Indian Institute of Information Technology, Design & Manufacture Jabalpur' ,
                  'National Institute of Technology Patna' ,
                  'National Institute of Technology Hamirpur' ,
                  'Indian Institute of Technology Tirupati',
                  'Indian Institute of Technology Palakkad' , 
                  'Indian Institute of Technology Bhilai' , 
                  'Indian Institute of Technology Goa' , 
                  'Indian Institute of Technology Jammu' , 
                  'Indian Institute of Technology Dharwad' , 
                  'Atal Bihari Vajpayee Indian Institute of Information Technology & Management Gwalior' ,
                  'Indian Institute of Information Technology, Allahabad' ,
                  'Pondicherry Engineering College, Puducherry' ,
                  'National Institute of Technology Puducherry' ,
                  'National Institute of Technology, Manipur' ,
                  'Indian Institute of Information Technology, Design & Manufacturing, Kancheepuram' ,
                  'National Institute of Technology Arunachal Pradesh' ,
                  'National Institute of Technology, Srinagar' ,
                  'National Institute of Technology Delhi' , 'National Institute of Technology, Mizoram' ,
                  'National Institute of Technology Nagaland' ,
                  'National Institute of Technology Sikkim' ,
                  'National Institute of Technology, Uttarakhand' ,
                  'National Institute of Technology, Andhra Pradesh' ,
                  'Indian Institute of Information Technology (IIIT) Pune' ,
                  'Indian Institute of Information Technology (IIIT)Kota, Rajasthan' ,
                  'Indian Institute of Information Technology (IIIT), Sri City, Chittoor' ,
                  'Indian Institute of Information Technology(IIIT), Vadodara, Gujrat' ,
                  'Indian Institute of Information Technology, Vadodara International Campus Diu (IIITVICD)',
                  'Indian Institute of Information Technology (IIIT) Nagpur' ,
                  'Indian Institute of Information Technology(IIIT) Kalyani, West Bengal' ,
                  'Indian Institute of Information Technology Lucknow' ,
                  'Indian Institute of Information Technology(IIIT) Dharwad' ,
                  'Indian Institute of Information Technology Bhagalpur' , 
                  'Indian Institute of Information Technology Bhopal' ,
                  'Indian Institute of Information Technology(IIIT) Kottayam' , 
                  'Indian Institute of Information Technology (IIIT) Ranchi' ,
                  'Indian Institute of Information Technology Surat' ,
                  'Indian Institute of Information Technology Manipur' ,
                  'Indian Institute of Information Technology Design & Manufacturing Kurnool, Andhra Pradesh' ,
                  'Indian Institute of Information Technology Srirangam, Tiruchirappalli' ,
                  'Indian Institute of Information Technology(IIIT) Kilohrad, Sonepat, Haryana' ,
                  'Indian Institute of Information Technology, Agartala' ,
                  'Indian institute of information technology, Raichur, Karnataka' ,
                  'Indian Institute of Information Technology(IIIT) Una, Himachal Pradesh' ,
                  'Assam University, Silchar' ,
                  'Gurukula Kangri Vishwavidyalaya, Haridwar' ,
                  'Indian Institute of Carpet Technology, Bhadohi' ,
                  'Institute of Infrastructure, Technology, Research and Management-Ahmedabad' ,
                  'Institute of Technology, Guru Ghasidas Vishwavidyalaya (A Central University), Bilaspur, (C.G.)' ,
                  'J.K. Institute of Applied Physics & Technology, Department of Electronics & Communication, University of Allahabad- Allahabad' ,
                  'National Institute of Electronics and Information Technology, Aurangabad (Maharashtra)' ,
                  'National Institute of Foundry & Forge Technology, Hatia, Ranchi' ,
                  'Sant Longowal Institute of Engineering and Technology' ,
                  'Mizoram University, Aizawl' ,
                  'School of Planning & Architecture, Bhopal' ,
                  'School of Planning & Architecture, New Delhi' ,
                  'School of Planning & Architecture: Vijayawada' ,
                  'Shri Mata Vaishno Devi University, Katra, Jammu & Kashmir' ,
                  'HNB Garhwal University Srinagar (Garhwal)' ,
                  'International Institute of Information Technology, Naya Raipur' ,
                  'International Institute of Information Technology, Bhubaneswar' ,
                  'Central institute of Technology Kokrajar, Assam' ,
                  'Ghani Khan Choudhary Institute of Engineering and Technology, Malda, West Bengal' ,
                  'Central University of Rajasthan, Rajasthan' ,
                  'National Institute of Food Technology Entrepreneurship and Management, Sonepat, Haryana' ,
                  'lndian Institute of Food Processing Technology, Thanjavur, Tamil Naidu.' ,
                  'North Eastern Regional Institute of Science and Technology, Nirjuli-791109 (Itanagar),Arunachal Pradesh']


cat = str(input("Enter your category : "))
gender = str(input("Enter your gender : "))
state = str(input("Enter your state : "))
adv_rank = int(input("Enter your Advanced Rank : "))
mains_rank = int(input("Enter your Mains Rank : "))
prep_bool = int(input("Looking for preperatory Colleges (1 / 0) : "))


def only_adv(adv , prep , adv_rank , cat , gender , prepare = 0):
    
    if prepare :
        final = prep.loc[(prep["Seat Type"] == cat) & (prep["Gender"] == gender) & (prep["Closing Rank"] >= adv_rank)] 
        
    else:
        final = adv.loc[(adv["Seat Type"] == cat) & (adv["Gender"] == gender) & (adv["Closing Rank"] >= adv_rank)]
        
    final["Institute"] = final["Institute"].astype("category")
    final["Institute"].cat.set_categories(college_sorter, inplace=True)
    final = final.sort_values(by = ["Institute"])
    final.reset_index(drop = True , inplace = True) 

    final = final[["Institute" , "Academic Program Name" , "Opening Rank" , "Closing Rank" , "State"]].values.tolist()   
    
    return final


def only_mains(mains , mains_rank , cat , gender , state):
    
        final_hs = mains.loc[(mains["Seat Type"] == cat) & (mains["Gender"] == gender) & (mains["Closing Rank"] >= mains_rank) & (mains["State"] == state) & (mains["Quota"].isin(["HS" , "JK" , "GO" , "LA"]))]
        final_ai = mains.loc[(mains["Seat Type"] == cat) & (mains["Gender"] == gender) & (mains["Closing Rank"] >= mains_rank) & (mains["Quota"].isin(["AI"]))]  
        final_os = mains.loc[(mains["Seat Type"] == cat) & (mains["Gender"] == gender) & (mains["Closing Rank"] >= mains_rank) & (mains["State"] != state) & (mains["Quota"].isin(["OS"]))]  
        
        final = pd.concat([final_hs , final_ai , final_os])
        
        final["Institute"] = final["Institute"].astype("category")
        final["Institute"].cat.set_categories(college_sorter, inplace=True)
        final = final.sort_values(by = ["Institute"])
        final.reset_index(drop = True , inplace = True) 

        final = final[["Institute" , "Academic Program Name" , "Opening Rank" , "Closing Rank" , "State"]].values.tolist()
        
        return final


def adv_mains(adv , mains , adv_rank , mains_rank , cat , gender , state):
    final_adv = adv.loc[(adv["Seat Type"] == cat) & (adv["Gender"] == gender) & (adv["Closing Rank"] >= adv_rank)].sort_values(by = ["Institute"] , ascending = [college_sorter]).reset_index(drop = True)
    
    final_hs = mains.loc[(mains["Seat Type"] == cat) & (mains["Gender"] == gender) & (mains["Closing Rank"] >= mains_rank) & (mains["State"] == state) & (mains["Quota"].isin(["HS" , "JK" , "GO" , "LA"]))]
    final_ai = mains.loc[(mains["Seat Type"] == cat) & (mains["Gender"] == gender) & (mains["Closing Rank"] >= mains_rank) & (mains["Quota"].isin(["AI"]))]  
    final_os = mains.loc[(mains["Seat Type"] == cat) & (mains["Gender"] == gender) & (mains["Closing Rank"] >= mains_rank) & (mains["State"] != state) & (mains["Quota"].isin(["OS"]))]  
    
    final = pd.concat([final_adv , final_hs , final_ai , final_os])
    
    final["Institute"] = final["Institute"].astype("category")
    final["Institute"].cat.set_categories(college_sorter, inplace=True)
    final = final.sort_values(by = ["Institute"])
    final.reset_index(drop = True , inplace = True) 
    
    final = final[["Institute" , "Academic Program Name" , "Opening Rank" , "Closing Rank" , "State"]].values.tolist()

    return final


