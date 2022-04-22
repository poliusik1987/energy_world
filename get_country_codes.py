from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n

def get_country_code(country_name):
         for code, name in COUNTRIES.items():
                  if name == country_name:
                           return code
                  elif country_name == 'Slovak Republic':
                           return 'sk'
                  elif country_name == 'Aruba':
                           return 'ae'
                  elif country_name == 'Bolivia':
                           return 'bo'
                  elif country_name == 'Cabo Verde':
                           return 'cv'
                  elif country_name == 'Congo, Dem. Rep.':
                           return 'cd'
                  elif country_name == 'Congo, Rep.':
                           return 'cg'
                  elif country_name == 'Dominica':
                           return 'do'
                  elif country_name == 'Egypt, Arab Rep.':
                           return 'eg'
                  elif country_name == 'Eswatini':
                           return 'sz'
                  elif country_name == 'Gambia, The':
                           return 'gm'
                  elif country_name == 'Hong Kong SAR, China':
                           return 'hk'
                  elif country_name == 'Iran, Islamic Rep.':
                           return 'ir'
                  elif country_name == "Korea, Dem. People's Rep.":
                           return 'kp'
                  elif country_name == 'Korea, Rep.':
                           return 'kr'
                  elif country_name == 'Kosovo':
                           return 'mk'
                  elif country_name == 'Kyrgyz Republic':
                           return 'kg'
                  elif country_name == 'Lao PDR':
                           return 'la'
                  elif country_name == 'Libya':
                           return 'ly'
                  elif country_name == 'Macao SAR, China':
                           return 'mo'
                  elif country_name == 'Moldova':
                           return 'md'
                  elif country_name == 'South Sudan':
                           return 'sd'
                  elif country_name == 'Tanzania':
                           return 'tz'
                  elif country_name == 'Venezuela, RB':
                           return 've'
                  elif country_name == 'Vietnam':
                           return 'vn'
                  elif country_name == 'West Bank and Gaza':
                           return 'il'
                  elif country_name == 'Yemen, Rep.':
                           return 'ye'
                  elif country_name == 'Sub-Saharan Africa':
                           return 'eh'
                  elif country_name == 'Latin America & Caribbean':
                           return 'gf'
                  elif country_name == 'South Asia':
                           return 'tw'
                  
                           
                  
         return None



