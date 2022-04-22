import csv
import pycountry
from pygal.maps.world import World
from pygal.style import LightColorizedStyle, RotateStyle
from get_country_codes import get_country_code
from pygal.maps.world import COUNTRIES
from pygal_maps_world import i18n

with open('data_bank.csv') as f:
         reader = csv.reader(f)
         header_row = next(reader)

         """отображение индексов в файле"""
         #for index, rows in enumerate(header_row):
                  #print(index, rows)

         dict_from_csv = {rows[2]:rows[4] for rows in reader}
         """отображение словаря"""
         #print(dict_from_csv)

energy_value = {}
for name, value in dict_from_csv.items():
       """проверка наименования страны и значения"""
       #print( name + ': ' +  value)
       country_name = name
       code = get_country_code(country_name)
       if code:
              energy_value[code] = int(float(value))
              #print(code + ": " + str(int(float(value))))
       #else:
              #print('ERROR - ' + country_name) 
#print(energy_value)проверка работоспособности словаря   

cc_value_1, cc_value_2, cc_value_3, cc_value_4, cc_value_5, cc_value_6 = {}, {}, {}, {}, {}, {}
for cc, value in energy_value.items():
       if 0 < value < 10:
              cc_value_1[cc] = value
       elif 20 < value < 30:
              cc_value_2[cc] = value
       elif 40 < value < 50:
              cc_value_3[cc] = value
       elif 60 < value < 70:
              cc_value_4[cc] = value
       elif 80 < value < 90:
              cc_value_5[cc] = value
       else:
              cc_value_6[cc] = value
              



wm_style = RotateStyle('#056197', base_style=LightColorizedStyle)                 
wm = World(style = wm_style)
wm.title = 'World energy in 2009, by Country'
wm.add('0-10', cc_value_1)
wm.add('20-30', cc_value_2)
wm.add('40-50', cc_value_3)
wm.add('60-70', cc_value_4)
wm.add('80-90', cc_value_5)
wm.add('100', cc_value_6)
wm.render_to_file('world_energy_in_2009.svg')

                

         
         
                  
         
         
