from bs4 import BeautifulSoup
import csv

data = """

							<thead class="thead-sticky">
								<tr>
									<th class="country"></th>
									<th class="year" title="2022">2022</th>
								</tr>
							</thead>
							<tbody>
								<tr class="country">
									<th>Afghanistan (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="AFGt: Total">Total</span></td>
									<td class="proper">44.63</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="AFGr101: Central (Kabul, Wardak, Kapisa, Logar, Parwan, Panjsher)">Central (Kabul, Wardak, Kapisa, Logar, Parwan, Panjsher)</span></td>
									<td class="proper">48.41</td>
								</tr>
								<tr>
									<td class="region"><span title="AFGr102: Central Highlands (Bamyan, Daikundi)">Central Highlands (Bamyan, Daikundi)</span></td>
									<td class="proper">44.13</td>
								</tr>
								<tr>
									<td class="region"><span title="AFGr103: East (Nangarhar, Kunar, Laghman, Nooristan)">East (Nangarhar, Kunar, Laghman, Nooristan)</span></td>
									<td class="proper">54.37</td>
								</tr>
								<tr>
									<td class="region"><span title="AFGr104: North (Samangan, Sar-e-Pul, Balkh, Jawzjan, Faryab)">North (Samangan, Sar-e-Pul, Balkh, Jawzjan, Faryab)</span></td>
									<td class="proper">50.11</td>
								</tr>
								<tr>
									<td class="region"><span title="AFGr105: North East (Baghlan, Takhar, Badakhshan, Kunduz)">North East (Baghlan, Takhar, Badakhshan, Kunduz)</span></td>
									<td class="proper">55.74</td>
								</tr>
								<tr>
									<td class="region"><span title="AFGr106: South (Uruzgan, Helmand, Zabul, Nimroz, Kandahar)">South (Uruzgan, Helmand, Zabul, Nimroz, Kandahar)</span></td>
									<td class="proper">24.27</td>
								</tr>
								<tr>
									<td class="region"><span title="AFGr107: South East (Ghazni, Paktya, Paktika, Khost)">South East (Ghazni, Paktya, Paktika, Khost)</span></td>
									<td class="proper">44.48</td>
								</tr>
								<tr>
									<td class="region"><span title="AFGr108: West (Ghor, Herat, Badghis, Farah)">West (Ghor, Herat, Badghis, Farah)</span></td>
									<td class="proper">35.56</td>
								</tr>
								<tr class="country">
									<th>Albania (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ALBt: Total">Total</span></td>
									<td class="proper">66.58</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ALBr201:  Berat"> Berat</span></td>
									<td class="proper">63.27</td>
								</tr>
								<tr>
									<td class="region"><span title="ALBr202:  Diber"> Diber</span></td>
									<td class="proper">68.60</td>
								</tr>
								<tr>
									<td class="region"><span title="ALBr203:  Durres"> Durres</span></td>
									<td class="proper">69.76</td>
								</tr>
								<tr>
									<td class="region"><span title="ALBr204:  Elbasan"> Elbasan</span></td>
									<td class="proper">64.69</td>
								</tr>
								<tr>
									<td class="region"><span title="ALBr205:  Fier"> Fier</span></td>
									<td class="proper">65.79</td>
								</tr>
								<tr>
									<td class="region"><span title="ALBr206:  Gjirokaster"> Gjirokaster</span></td>
									<td class="proper">65.01</td>
								</tr>
								<tr>
									<td class="region"><span title="ALBr207:  Korce"> Korce</span></td>
									<td class="proper">64.33</td>
								</tr>
								<tr>
									<td class="region"><span title="ALBr208:  Kukes"> Kukes</span></td>
									<td class="proper">68.92</td>
								</tr>
								<tr>
									<td class="region"><span title="ALBr209:  Lezhe"> Lezhe</span></td>
									<td class="proper">65.68</td>
								</tr>
								<tr>
									<td class="region"><span title="ALBr210:  Shkoder"> Shkoder</span></td>
									<td class="proper">67.42</td>
								</tr>
								<tr>
									<td class="region"><span title="ALBr211:  Tirana"> Tirana</span></td>
									<td class="proper">66.69</td>
								</tr>
								<tr>
									<td class="region"><span title="ALBr212:  Vlore"> Vlore</span></td>
									<td class="proper">68.85</td>
								</tr>
								<tr class="country">
									<th>Algeria (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="DZAt: Total">Total</span></td>
									<td class="proper">43.01</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="DZAr104: Hauts Plateaux Centre (Djelfa, Laghouat, MSila)">Hauts Plateaux Centre (Djelfa, Laghouat, MSila)</span></td>
									<td class="proper">35.15</td>
								</tr>
								<tr>
									<td class="region"><span title="DZAr105: Hauts Plateaux Est (Setif, Batna, Khenchela, Bordj Bou Arreridj, Oum El Bouaghi, Tebessa)">Hauts Plateaux Est (Setif, Batna, Khenchela, Bordj Bou Arreridj, Oum El Bouaghi, Tebessa)</span></td>
									<td class="proper">45.62</td>
								</tr>
								<tr>
									<td class="region"><span title="DZAr106: Hauts Plateaux Ouest (Tiaret, Saida, Tissemsilt, Naama, El Bayadh)">Hauts Plateaux Ouest (Tiaret, Saida, Tissemsilt, Naama, El Bayadh)</span></td>
									<td class="proper">33.54</td>
								</tr>
								<tr>
									<td class="region"><span title="DZAr101: Nord Centre (Alger, Blida, Boumerdes, Tipaza, Bouira, Medea, Tizi-Ouzou, Bejaia, Chlef, Ain Defla)">Nord Centre (Alger, Blida, Boumerdes, Tipaza, Bouira, Medea, Tizi-Ouzou, Bejaia, Chlef, Ain Defla)</span></td>
									<td class="proper">56.02</td>
								</tr>
								<tr>
									<td class="region"><span title="DZAr102: Nord Est (Annaba, Constantine, Skikda, Jijel, Mila, Souk Ahras, El Tarf, Guelma)">Nord Est (Annaba, Constantine, Skikda, Jijel, Mila, Souk Ahras, El Tarf, Guelma)</span></td>
									<td class="proper">59.14</td>
								</tr>
								<tr>
									<td class="region"><span title="DZAr103: Nord Ouest (Oran, Tlemcen, Mostaganem, Ain Temouchent, Relizane, Sidi Bel Abbes, Mascara)">Nord Ouest (Oran, Tlemcen, Mostaganem, Ain Temouchent, Relizane, Sidi Bel Abbes, Mascara)</span></td>
									<td class="proper">53.14</td>
								</tr>
								<tr>
									<td class="region"><span title="DZAr107: Sud (Bechar, Tindouf, Adrar, Ghardaia, Biskra, El Oued, Ouargla, Tamanrasset,Illizi)">Sud (Bechar, Tindouf, Adrar, Ghardaia, Biskra, El Oued, Ouargla, Tamanrasset,Illizi)</span></td>
									<td class="proper">18.42</td>
								</tr>
								<tr class="country">
									<th>Andorra (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ANDt: Total">Total</span></td>
									<td class="proper">68.45</td>
								</tr>
								<tr class="country">
									<th>Angola (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="AGOt: Total">Total</span></td>
									<td class="proper">63.84</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="AGOr218:  Bengo"> Bengo</span></td>
									<td class="proper">77.35</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr209:  Benguela"> Benguela</span></td>
									<td class="proper">66.28</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr211:  Bie"> Bie</span></td>
									<td class="proper">58.75</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr201:  Cabinda"> Cabinda</span></td>
									<td class="proper">84.47</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr216:  Cunene"> Cunene</span></td>
									<td class="proper">34.45</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr210:  Huambo"> Huambo</span></td>
									<td class="proper">59.87</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr215:  Huila"> Huila</span></td>
									<td class="proper">43.51</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr213:  Kuando Kubango"> Kuando Kubango</span></td>
									<td class="proper">48.99</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr205:  Kuanza Norte"> Kuanza Norte</span></td>
									<td class="proper">76.96</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr206:  Kuanza Sul"> Kuanza Sul</span></td>
									<td class="proper">71.92</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr204:  Luanda"> Luanda</span></td>
									<td class="proper">76.70</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr208:  Lunda Norte"> Lunda Norte</span></td>
									<td class="proper">61.88</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr217:  Lunda Sul"> Lunda Sul</span></td>
									<td class="proper">61.12</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr207:  Malange"> Malange</span></td>
									<td class="proper">63.66</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr212:  Moxico"> Moxico</span></td>
									<td class="proper">58.75</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr214:  Namibe"> Namibe</span></td>
									<td class="proper">51.75</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr203:  Uige"> Uige</span></td>
									<td class="proper">72.80</td>
								</tr>
								<tr>
									<td class="region"><span title="AGOr202:  Zaire"> Zaire</span></td>
									<td class="proper">79.84</td>
								</tr>
								<tr class="country">
									<th>Antigua and Barbuda (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ATGt: Total">Total</span></td>
									<td class="proper">78.56</td>
								</tr>
								<tr class="country">
									<th>Argentina (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ARGt: Total">Total</span></td>
									<td class="proper">52.77</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ARGr104: Cuyo">Cuyo</span></td>
									<td class="proper">43.51</td>
								</tr>
								<tr>
									<td class="region"><span title="ARGr101: Gran Buenos Aires">Gran Buenos Aires</span></td>
									<td class="proper">62.43</td>
								</tr>
								<tr>
									<td class="region"><span title="ARGr103: NEA">NEA</span></td>
									<td class="proper">60.22</td>
								</tr>
								<tr>
									<td class="region"><span title="ARGr102: NOA">NOA</span></td>
									<td class="proper">43.33</td>
								</tr>
								<tr>
									<td class="region"><span title="ARGr105: Pampeana">Pampeana</span></td>
									<td class="proper">54.87</td>
								</tr>
								<tr>
									<td class="region"><span title="ARGr106: Patagonia">Patagonia</span></td>
									<td class="proper">52.30</td>
								</tr>
								<tr class="country">
									<th>Armenia (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ARMt: Total">Total</span></td>
									<td class="proper">62.41</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ARMr101: Aragatsotn">Aragatsotn</span></td>
									<td class="proper">58.75</td>
								</tr>
								<tr>
									<td class="region"><span title="ARMr102: Ararat">Ararat</span></td>
									<td class="proper">53.10</td>
								</tr>
								<tr>
									<td class="region"><span title="ARMr103: Armavir">Armavir</span></td>
									<td class="proper">49.87</td>
								</tr>
								<tr>
									<td class="region"><span title="ARMr104: Gegharkunik">Gegharkunik</span></td>
									<td class="proper">73.06</td>
								</tr>
								<tr>
									<td class="region"><span title="ARMr106: Kotayk">Kotayk</span></td>
									<td class="proper">64.90</td>
								</tr>
								<tr>
									<td class="region"><span title="ARMr105: Lori">Lori</span></td>
									<td class="proper">71.72</td>
								</tr>
								<tr>
									<td class="region"><span title="ARMr107: Shirak">Shirak</span></td>
									<td class="proper">67.47</td>
								</tr>
								<tr>
									<td class="region"><span title="ARMr108: Syunik">Syunik</span></td>
									<td class="proper">66.03</td>
								</tr>
								<tr>
									<td class="region"><span title="ARMr110: Tavush">Tavush</span></td>
									<td class="proper">69.97</td>
								</tr>
								<tr>
									<td class="region"><span title="ARMr109: Vayots Dzor">Vayots Dzor</span></td>
									<td class="proper">60.73</td>
								</tr>
								<tr>
									<td class="region"><span title="ARMr111: Yerevan">Yerevan</span></td>
									<td class="proper">50.89</td>
								</tr>
								<tr class="country">
									<th>Australia (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="AUSt: Total">Total</span></td>
									<td class="proper">60.95</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="AUSr109: Ashmore and Cartier Islands, Coral Sea Islands Territory">Ashmore and Cartier Islands, Coral Sea Islands Territory</span></td>
									<td class="proper">75.16</td>
								</tr>
								<tr>
									<td class="region"><span title="AUSr108: Australian Capital Territory">Australian Capital Territory</span></td>
									<td class="proper">78.29</td>
								</tr>
								<tr>
									<td class="region"><span title="AUSr101: New South Wales">New South Wales</span></td>
									<td class="proper">63.38</td>
								</tr>
								<tr>
									<td class="region"><span title="AUSr107: Northern Territory">Northern Territory</span></td>
									<td class="proper">39.24</td>
								</tr>
								<tr>
									<td class="region"><span title="AUSr103: Queensland">Queensland</span></td>
									<td class="proper">52.60</td>
								</tr>
								<tr>
									<td class="region"><span title="AUSr104: South Australia">South Australia</span></td>
									<td class="proper">48.27</td>
								</tr>
								<tr>
									<td class="region"><span title="AUSr106: Tasmania">Tasmania</span></td>
									<td class="proper">78.38</td>
								</tr>
								<tr>
									<td class="region"><span title="AUSr102: Victoria">Victoria</span></td>
									<td class="proper">72.24</td>
								</tr>
								<tr>
									<td class="region"><span title="AUSr105: Western Australia">Western Australia</span></td>
									<td class="proper">41.03</td>
								</tr>
								<tr class="country">
									<th>Austria (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="AUTt: Total">Total</span></td>
									<td class="proper">71.70</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="AUTr101: Burgenland">Burgenland</span></td>
									<td class="proper">66.68</td>
								</tr>
								<tr>
									<td class="region"><span title="AUTr104: Karnten">Karnten</span></td>
									<td class="proper">73.06</td>
								</tr>
								<tr>
									<td class="region"><span title="AUTr102: Niederosterreich">Niederosterreich</span></td>
									<td class="proper">69.89</td>
								</tr>
								<tr>
									<td class="region"><span title="AUTr106: Oberosterreich">Oberosterreich</span></td>
									<td class="proper">73.87</td>
								</tr>
								<tr>
									<td class="region"><span title="AUTr107: Salzburg">Salzburg</span></td>
									<td class="proper">75.27</td>
								</tr>
								<tr>
									<td class="region"><span title="AUTr105: Steiermark">Steiermark</span></td>
									<td class="proper">73.68</td>
								</tr>
								<tr>
									<td class="region"><span title="AUTr108: Tirol">Tirol</span></td>
									<td class="proper">73.65</td>
								</tr>
								<tr>
									<td class="region"><span title="AUTr109: Vorarlberg">Vorarlberg</span></td>
									<td class="proper">73.79</td>
								</tr>
								<tr>
									<td class="region"><span title="AUTr103: Wien">Wien</span></td>
									<td class="proper">65.45</td>
								</tr>
							
								<tr class="country">
									<th>Azerbaijan (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="AZEt: Total">Total</span></td>
									<td class="proper">64.33</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="AZEr102: Absheron">Absheron</span></td>
									<td class="proper">63.36</td>
								</tr>
								<tr>
									<td class="region"><span title="AZEr107: Aran">Aran</span></td>
									<td class="proper">58.12</td>
								</tr>
								<tr>
									<td class="region"><span title="AZEr101: Baku">Baku</span></td>
									<td class="proper">71.47</td>
								</tr>
								<tr>
									<td class="region"><span title="AZEr109: Dakhlik Shirvan">Dakhlik Shirvan</span></td>
									<td class="proper">62.38</td>
								</tr>
								<tr>
									<td class="region"><span title="AZEr111: East Zangezur">East Zangezur</span></td>
									<td class="proper">70.39</td>
								</tr>
								<tr>
									<td class="region"><span title="AZEr103: Ganja Gazakh">Ganja Gazakh</span></td>
									<td class="proper">63.62</td>
								</tr>
								<tr>
									<td class="region"><span title="AZEr106: Guba Khachmaz">Guba Khachmaz</span></td>
									<td class="proper">71.36</td>
								</tr>
								<tr>
									<td class="region"><span title="AZEr105: Lankaran">Lankaran</span></td>
									<td class="proper">73.22</td>
								</tr>
								<tr>
									<td class="region"><span title="AZEr110: Nakhchivan">Nakhchivan</span></td>
									<td class="proper">48.25</td>
								</tr>
								<tr>
									<td class="region"><span title="AZEr104: Shaki Zaqatala">Shaki Zaqatala</span></td>
									<td class="proper">59.73</td>
								</tr>
								<tr>
									<td class="region"><span title="AZEr108: Yukhari Karabakh">Yukhari Karabakh</span></td>
									<td class="proper">65.67</td>
								</tr>
								<tr class="country">
									<th>Bahamas, The (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BHSt: Total">Total</span></td>
									<td class="proper">77.07</td>
								</tr>
								<tr class="country">
									<th>Bahrain (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BHRt: Total">Total</span></td>
									<td class="proper">68.78</td>
								</tr>
								<tr class="country">
									<th>Bangladesh (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BGDt: Total">Total</span></td>
									<td class="proper">78.36</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BGDr214:  Bagerhat, Khulna, Satkhira"> Bagerhat, Khulna, Satkhira</span></td>
									<td class="proper">78.60</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr204:  Bandarban, Cox s Bazar"> Bandarban, Cox s Bazar</span></td>
									<td class="proper">76.01</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr202:  Barguna, Bhola, Patuakhali"> Barguna, Bhola, Patuakhali</span></td>
									<td class="proper">78.86</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr201:  Barisal, Jhalokati, Pirojpur"> Barisal, Jhalokati, Pirojpur</span></td>
									<td class="proper">78.60</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr219:  Bogra, Gaibandha, Jaypurhat"> Bogra, Gaibandha, Jaypurhat</span></td>
									<td class="proper">79.71</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr207:  Brahmanbaria, Chandpur, Comilla"> Brahmanbaria, Chandpur, Comilla</span></td>
									<td class="proper">77.28</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr203:  Chittagong"> Chittagong</span></td>
									<td class="proper">77.69</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr216:  Chuadanga, Jhenaidah, Kushtia, Meherpur"> Chuadanga, Jhenaidah, Kushtia, Meherpur</span></td>
									<td class="proper">77.56</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr208:  Dhaka"> Dhaka</span></td>
									<td class="proper">78.16</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr220:  Dinajpur, Nilphamari, Panchagarh, Thakurgaon"> Dinajpur, Nilphamari, Panchagarh, Thakurgaon</span></td>
									<td class="proper">78.45</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr212:  Faridpur, Manikganj, Rajbari"> Faridpur, Manikganj, Rajbari</span></td>
									<td class="proper">78.57</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr206:  Feni, Lakshmipur, Noakhali"> Feni, Lakshmipur, Noakhali</span></td>
									<td class="proper">77.17</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr209:  Gazipur, Narayanganj, Narsingdi"> Gazipur, Narayanganj, Narsingdi</span></td>
									<td class="proper">77.72</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr213:  Gopalganj, Madaripur, Munshiganj, Shariatpur"> Gopalganj, Madaripur, Munshiganj, Shariatpur</span></td>
									<td class="proper">78.70</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr223:  Habiganj, Sunamganj"> Habiganj, Sunamganj</span></td>
									<td class="proper">79.58</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr210:  Jamalpur, Sherpur, Tangail"> Jamalpur, Sherpur, Tangail</span></td>
									<td class="proper">79.79</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr215:  Jessore, Magura, Narail"> Jessore, Magura, Narail</span></td>
									<td class="proper">77.63</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr205:  Khagrachhari, Rangamati (Chattagram)"> Khagrachhari, Rangamati (Chattagram)</span></td>
									<td class="proper">77.43</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr211:  Kishoreganj, Mymensingh, Netrakona"> Kishoreganj, Mymensingh, Netrakona</span></td>
									<td class="proper">79.65</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr221:  Kurigram, Lalmonirhat, Rangpur"> Kurigram, Lalmonirhat, Rangpur</span></td>
									<td class="proper">79.59</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr222:  Maulvibazar, Sylhet"> Maulvibazar, Sylhet</span></td>
									<td class="proper">79.68</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr217:  Naogaon, Nawabganj, Rajshahi"> Naogaon, Nawabganj, Rajshahi</span></td>
									<td class="proper">77.36</td>
								</tr>
								<tr>
									<td class="region"><span title="BGDr218:  Natore, Pabna, Sirajganj"> Natore, Pabna, Sirajganj</span></td>
									<td class="proper">78.60</td>
								</tr>
								<tr class="country">
									<th>Barbados (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BRBt: Total">Total</span></td>
									<td class="proper">79.29</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BRBr102: Christ Church and St. Philip">Christ Church and St. Philip</span></td>
									<td class="proper">79.33</td>
								</tr>
								<tr>
									<td class="region"><span title="BRBr101: St Michael">St Michael</span></td>
									<td class="proper">79.32</td>
								</tr>
								<tr>
									<td class="region"><span title="BRBr103: St. James, St. George, and St. Thomas">St. James, St. George, and St. Thomas</span></td>
									<td class="proper">79.27</td>
								</tr>
								<tr>
									<td class="region"><span title="BRBr104: St. Lucy, St. Peter, St. Andrew, St. Joseph, and St. John">St. Lucy, St. Peter, St. Andrew, St. Joseph, and St. John</span></td>
									<td class="proper">79.26</td>
								</tr>
								<tr class="country">
									<th>Belarus (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BLRt: Total">Total</span></td>
									<td class="proper">74.69</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BLRr101: Brest region">Brest region</span></td>
									<td class="proper">73.22</td>
								</tr>
								<tr>
									<td class="region"><span title="BLRr103: Gomel region">Gomel region</span></td>
									<td class="proper">73.08</td>
								</tr>
								<tr>
									<td class="region"><span title="BLRr104: Grodno region">Grodno region</span></td>
									<td class="proper">75.50</td>
								</tr>
								<tr>
									<td class="region"><span title="BLRr105: Minsk region">Minsk region</span></td>
									<td class="proper">75.60</td>
								</tr>
								<tr>
									<td class="region"><span title="BLRr106: Mogilev region">Mogilev region</span></td>
									<td class="proper">75.34</td>
								</tr>
								<tr>
									<td class="region"><span title="BLRr102: Vitebsk region">Vitebsk region</span></td>
									<td class="proper">75.40</td>
								</tr>
								<tr class="country">
									<th>Belgium (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BELt: Total">Total</span></td>
									<td class="proper">73.19</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BELr101: Bruxelles - Brussel">Bruxelles - Brussel</span></td>
									<td class="proper">72.61</td>
								</tr>
								<tr>
									<td class="region"><span title="BELr102: Prov. Antwerpen">Prov. Antwerpen</span></td>
									<td class="proper">72.31</td>
								</tr>
								<tr>
									<td class="region"><span title="BELr107: Prov. Brabant Wallon">Prov. Brabant Wallon</span></td>
									<td class="proper">72.53</td>
								</tr>
								<tr>
									<td class="region"><span title="BELr108: Prov. Hainaut">Prov. Hainaut</span></td>
									<td class="proper">73.61</td>
								</tr>
								<tr>
									<td class="region"><span title="BELr109: Prov. Liege">Prov. Liege</span></td>
									<td class="proper">73.29</td>
								</tr>
								<tr>
									<td class="region"><span title="BELr103: Prov. Limburg">Prov. Limburg</span></td>
									<td class="proper">70.83</td>
								</tr>
								<tr>
									<td class="region"><span title="BELr110: Prov. Luxembourg">Prov. Luxembourg</span></td>
									<td class="proper">74.23</td>
								</tr>
								<tr>
									<td class="region"><span title="BELr111: Prov. Namur">Prov. Namur</span></td>
									<td class="proper">73.48</td>
								</tr>
								<tr>
									<td class="region"><span title="BELr104: Prov. Oost-Vlaanderen">Prov. Oost-Vlaanderen</span></td>
									<td class="proper">73.44</td>
								</tr>
								<tr>
									<td class="region"><span title="BELr106: Prov. West-Vlaanderen">Prov. West-Vlaanderen</span></td>
									<td class="proper">75.57</td>
								</tr>
								<tr class="country">
									<th>Belize (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BLZt: Total">Total</span></td>
									<td class="proper">82.39</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BLZr102: Belize">Belize</span></td>
									<td class="proper">83.13</td>
								</tr>
								<tr>
									<td class="region"><span title="BLZr103: Cayo">Cayo</span></td>
									<td class="proper">82.00</td>
								</tr>
								<tr>
									<td class="region"><span title="BLZr101: Corozal, Orange Walk">Corozal, Orange Walk</span></td>
									<td class="proper">80.70</td>
								</tr>
								<tr>
									<td class="region"><span title="BLZr104: Stann Creek, Toledo">Stann Creek, Toledo</span></td>
									<td class="proper">83.74</td>
								</tr>
								<tr class="country">
									<th>Benin (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BENt: Total">Total</span></td>
									<td class="proper">66.90</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BENr101: Atacora (incl Donga)">Atacora (incl Donga)</span></td>
									<td class="proper">51.62</td>
								</tr>
								<tr>
									<td class="region"><span title="BENr102: Atlantique (incl Littoral (Cotonou))">Atlantique (incl Littoral (Cotonou))</span></td>
									<td class="proper">80.53</td>
								</tr>
								<tr>
									<td class="region"><span title="BENr103: Borgou (incl Alibori)">Borgou (incl Alibori)</span></td>
									<td class="proper">47.83</td>
								</tr>
								<tr>
									<td class="region"><span title="BENr104: Mono (incl Couffo)">Mono (incl Couffo)</span></td>
									<td class="proper">77.75</td>
								</tr>
								<tr>
									<td class="region"><span title="BENr105: Queme (incl Plateau)">Queme (incl Plateau)</span></td>
									<td class="proper">76.32</td>
								</tr>
								<tr>
									<td class="region"><span title="BENr106: Zou (incl Collines)">Zou (incl Collines)</span></td>
									<td class="proper">67.35</td>
								</tr>
								<tr class="country">
									<th>Bhutan (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BTNt: Total">Total</span></td>
									<td class="proper">82.71</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BTNr101: Bumthang">Bumthang</span></td>
									<td class="proper">83.93</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr102: Chukha">Chukha</span></td>
									<td class="proper">82.37</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr103: Dagana">Dagana</span></td>
									<td class="proper">84.09</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr104: Gasa">Gasa</span></td>
									<td class="proper">78.54</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr105: Haa">Haa</span></td>
									<td class="proper">81.68</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr106: Lhuntse">Lhuntse</span></td>
									<td class="proper">84.52</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr107: Mongar">Mongar</span></td>
									<td class="proper">84.43</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr108: Paro">Paro</span></td>
									<td class="proper">79.49</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr109: Pemagatshel">Pemagatshel</span></td>
									<td class="proper">80.69</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr110: Punakha">Punakha</span></td>
									<td class="proper">81.52</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr111: Samdrup jongkhar">Samdrup jongkhar</span></td>
									<td class="proper">82.89</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr112: Samtse">Samtse</span></td>
									<td class="proper">80.12</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr113: Sarpang">Sarpang</span></td>
									<td class="proper">83.03</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr114: Thimphu">Thimphu</span></td>
									<td class="proper">79.77</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr115: Trashigang">Trashigang</span></td>
									<td class="proper">85.35</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr116: Trashiyangtse">Trashiyangtse</span></td>
									<td class="proper">82.90</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr117: Trongsa">Trongsa</span></td>
									<td class="proper">85.97</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr118: Tsirang">Tsirang</span></td>
									<td class="proper">85.38</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr119: Wangdi">Wangdi</span></td>
									<td class="proper">84.71</td>
								</tr>
								<tr>
									<td class="region"><span title="BTNr120: Zhemgang">Zhemgang</span></td>
									<td class="proper">82.90</td>
								</tr>
								<tr class="country">
									<th>Bolivia (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BOLt: Total">Total</span></td>
									<td class="proper">57.70</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BOLr108: Beni">Beni</span></td>
									<td class="proper">73.84</td>
								</tr>
								<tr>
									<td class="region"><span title="BOLr101: Chuquisaca">Chuquisaca</span></td>
									<td class="proper">72.08</td>
								</tr>
								<tr>
									<td class="region"><span title="BOLr103: Cochabamba">Cochabamba</span></td>
									<td class="proper">57.99</td>
								</tr>
								<tr>
									<td class="region"><span title="BOLr102: La Paz">La Paz</span></td>
									<td class="proper">66.14</td>
								</tr>
								<tr>
									<td class="region"><span title="BOLr104: Oruro">Oruro</span></td>
									<td class="proper">23.94</td>
								</tr>
								<tr>
									<td class="region"><span title="BOLr109: Pando">Pando</span></td>
									<td class="proper">77.91</td>
								</tr>
								<tr>
									<td class="region"><span title="BOLr105: Potosi">Potosi</span></td>
									<td class="proper">25.58</td>
								</tr>
								<tr>
									<td class="region"><span title="BOLr107: Santa Cruz">Santa Cruz</span></td>
									<td class="proper">65.68</td>
								</tr>
								<tr>
									<td class="region"><span title="BOLr106: Tarija">Tarija</span></td>
									<td class="proper">56.11</td>
								</tr>
								<tr class="country">
									<th>Bosnia and Herzegovina (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BIHt: Total">Total</span></td>
									<td class="proper">70.10</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BIHr103: Central Bosnia">Central Bosnia</span></td>
									<td class="proper">70.83</td>
								</tr>
								<tr>
									<td class="region"><span title="BIHr102: Northern Bosnia">Northern Bosnia</span></td>
									<td class="proper">70.91</td>
								</tr>
								<tr>
									<td class="region"><span title="BIHr105: Republica Srpska">Republica Srpska</span></td>
									<td class="proper">69.60</td>
								</tr>
								<tr>
									<td class="region"><span title="BIHr101: Western Bosnia">Western Bosnia</span></td>
									<td class="proper">71.35</td>
								</tr>
								<tr>
									<td class="region"><span title="BIHr104: Western herzegovina">Western herzegovina</span></td>
									<td class="proper">67.79</td>
								</tr>
								<tr class="country">
									<th>Botswana (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BWAt: Total">Total</span></td>
									<td class="proper">47.31</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BWAr101: Central">Central</span></td>
									<td class="proper">49.44</td>
								</tr>
								<tr>
									<td class="region"><span title="BWAr110: Chobe">Chobe</span></td>
									<td class="proper">49.49</td>
								</tr>
								<tr>
									<td class="region"><span title="BWAr102: Ghanzi">Ghanzi</span></td>
									<td class="proper">42.95</td>
								</tr>
								<tr>
									<td class="region"><span title="BWAr103: Kgalagadi">Kgalagadi</span></td>
									<td class="proper">39.26</td>
								</tr>
								<tr>
									<td class="region"><span title="BWAr104: Kgatleng">Kgatleng</span></td>
									<td class="proper">49.60</td>
								</tr>
								<tr>
									<td class="region"><span title="BWAr105: Kweneng">Kweneng</span></td>
									<td class="proper">47.80</td>
								</tr>
								<tr>
									<td class="region"><span title="BWAr106: North-East">North-East</span></td>
									<td class="proper">50.04</td>
								</tr>
								<tr>
									<td class="region"><span title="BWAr107: North-West, Ngamiland">North-West, Ngamiland</span></td>
									<td class="proper">45.48</td>
								</tr>
								<tr>
									<td class="region"><span title="BWAr108: South-East">South-East</span></td>
									<td class="proper">51.17</td>
								</tr>
								<tr>
									<td class="region"><span title="BWAr109: Southern">Southern</span></td>
									<td class="proper">47.85</td>
								</tr>
								<tr class="country">
									<th>Brazil (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BRAt: Total">Total</span></td>
									<td class="proper">71.75</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BRAr102: Acre">Acre</span></td>
									<td class="proper">80.58</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr114: Alagoas">Alagoas</span></td>
									<td class="proper">76.61</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr106: Amapa">Amapa</span></td>
									<td class="proper">82.67</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr103: Amazonas">Amazonas</span></td>
									<td class="proper">82.98</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr116: Bahia">Bahia</span></td>
									<td class="proper">67.45</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr110: Ceara">Ceara</span></td>
									<td class="proper">67.49</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr127: Distrito Federal">Distrito Federal</span></td>
									<td class="proper">60.67</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr118: Espirito Santo">Espirito Santo</span></td>
									<td class="proper">74.58</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr126: Goias">Goias</span></td>
									<td class="proper">60.56</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr108: Maranhao">Maranhao</span></td>
									<td class="proper">71.85</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr125: Mato Grosso">Mato Grosso</span></td>
									<td class="proper">67.76</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr124: Mato Grosso do Sul">Mato Grosso do Sul</span></td>
									<td class="proper">63.08</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr117: Minas Gerais">Minas Gerais</span></td>
									<td class="proper">65.06</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr105: Para">Para</span></td>
									<td class="proper">78.70</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr112: Paraiba">Paraiba</span></td>
									<td class="proper">68.74</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr121: Parana">Parana</span></td>
									<td class="proper">73.99</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr113: Pernambuco">Pernambuco</span></td>
									<td class="proper">69.79</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr109: Piaui">Piaui</span></td>
									<td class="proper">61.10</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr119: Rio de Janeiro">Rio de Janeiro</span></td>
									<td class="proper">76.62</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr111: Rio Grande do Norte">Rio Grande do Norte</span></td>
									<td class="proper">68.99</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr123: Rio Grande do Sul">Rio Grande do Sul</span></td>
									<td class="proper">72.89</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr101: Rondonia">Rondonia</span></td>
									<td class="proper">75.52</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr104: Roraima">Roraima</span></td>
									<td class="proper">81.64</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr122: Santa Catarina">Santa Catarina</span></td>
									<td class="proper">78.60</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr120: Sao Paulo">Sao Paulo</span></td>
									<td class="proper">67.93</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr115: Sergipe">Sergipe</span></td>
									<td class="proper">76.41</td>
								</tr>
								<tr>
									<td class="region"><span title="BRAr107: Tocantins">Tocantins</span></td>
									<td class="proper">65.04</td>
								</tr>
								<tr class="country">
									<th>Brunei Darussalam (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BRNt: Total">Total</span></td>
									<td class="proper">86.58</td>
								</tr>
								<tr class="country">
									<th>Bulgaria (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BGRt: Total">Total</span></td>
									<td class="proper">66.51</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BGRr102: Severen tsentralen">Severen tsentralen</span></td>
									<td class="proper">64.77</td>
								</tr>
								<tr>
									<td class="region"><span title="BGRr103: Severoiztochen">Severoiztochen</span></td>
									<td class="proper">67.63</td>
								</tr>
								<tr>
									<td class="region"><span title="BGRr101: Severozapaden">Severozapaden</span></td>
									<td class="proper">64.30</td>
								</tr>
								<tr>
									<td class="region"><span title="BGRr104: Yugoiztochen">Yugoiztochen</span></td>
									<td class="proper">67.90</td>
								</tr>
								<tr>
									<td class="region"><span title="BGRr105: Yugozapaden">Yugozapaden</span></td>
									<td class="proper">68.68</td>
								</tr>
								<tr>
									<td class="region"><span title="BGRr106: Yuzhen tsentralen">Yuzhen tsentralen</span></td>
									<td class="proper">65.81</td>
								</tr>
								<tr class="country">
									<th>Burkina Faso (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BFAt: Total">Total</span></td>
									<td class="proper">42.30</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BFAr101: Boucle de Mouhoun">Boucle de Mouhoun</span></td>
									<td class="proper">42.72</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr102: Cascades">Cascades</span></td>
									<td class="proper">53.15</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr103: Centre (incl Ouagadougou)">Centre (incl Ouagadougou)</span></td>
									<td class="proper">41.14</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr104: Centre-Est">Centre-Est</span></td>
									<td class="proper">42.75</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr105: Centre-Nord">Centre-Nord</span></td>
									<td class="proper">36.10</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr106: Centre-Ouest">Centre-Ouest</span></td>
									<td class="proper">45.28</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr107: Centre-Sud">Centre-Sud</span></td>
									<td class="proper">44.68</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr108: Est">Est</span></td>
									<td class="proper">38.83</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr109: Hauts Bassins">Hauts Bassins</span></td>
									<td class="proper">48.41</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr110: Nord">Nord</span></td>
									<td class="proper">37.80</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr111: Plateau Central">Plateau Central</span></td>
									<td class="proper">40.20</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr112: Sahel">Sahel</span></td>
									<td class="proper">28.68</td>
								</tr>
								<tr>
									<td class="region"><span title="BFAr113: Sud-Ouest">Sud-Ouest</span></td>
									<td class="proper">50.15</td>
								</tr>
								<tr class="country">
									<th>Burundi (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="BDIt: Total">Total</span></td>
									<td class="proper">68.65</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="BDIr104: West (Bubanza, Buja Rural, Cibitoke, Mairie de Bujumbura)">West (Bubanza, Buja Rural, Cibitoke, Mairie de Bujumbura)</span></td>
									<td class="proper">68.14</td>
								</tr>
								<tr>
									<td class="region"><span title="BDIr103: East (Cankuzo, Rutana, Ruyigi )">East (Cankuzo, Rutana, Ruyigi )</span></td>
									<td class="proper">66.56</td>
								</tr>
								<tr>
									<td class="region"><span title="BDIr105: Middle (Gitega, Karuzi, Muramvya, Mwaro)">Middle (Gitega, Karuzi, Muramvya, Mwaro)</span></td>
									<td class="proper">67.19</td>
								</tr>
								<tr>
									<td class="region"><span title="BDIr101: North (Kayanza, Kirundo, Muyinga, Ngozi)">North (Kayanza, Kirundo, Muyinga, Ngozi)</span></td>
									<td class="proper">67.60</td>
								</tr>
								<tr>
									<td class="region"><span title="BDIr102: South (Bururi, Makamba)">South (Bururi, Makamba)</span></td>
									<td class="proper">73.77</td>
								</tr>
								<tr class="country">
									<th>Cabo Verde (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CPVt: Total">Total</span></td>
									<td class="proper">79.06</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CPVr105: Fogo">Fogo</span></td>
									<td class="proper">81.20</td>
								</tr>
								<tr>
									<td class="region"><span title="CPVr106: Other islands (Boa Vista, Brava, Maio, So Nicola, Sal)">Other islands (Boa Vista, Brava, Maio, So Nicola, Sal)</span></td>
									<td class="proper">77.64</td>
								</tr>
								<tr>
									<td class="region"><span title="CPVr101: S.Antao">S.Antao</span></td>
									<td class="proper">82.40</td>
								</tr>
								<tr>
									<td class="region"><span title="CPVr102: S.Vicente">S.Vicente</span></td>
									<td class="proper">79.80</td>
								</tr>
								<tr>
									<td class="region"><span title="CPVr104: Santiago- Praia">Santiago- Praia</span></td>
									<td class="proper">75.94</td>
								</tr>
								<tr>
									<td class="region"><span title="CPVr103: Santiago-Interior">Santiago-Interior</span></td>
									<td class="proper">77.38</td>
								</tr>
								<tr class="country">
									<th>Cambodia (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="KHMt: Total">Total</span></td>
									<td class="proper">77.25</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="KHMr101: Banteay Mean Chey">Banteay Mean Chey</span></td>
									<td class="proper">74.09</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr113: Bat Dambang-Krong Pailin">Bat Dambang-Krong Pailin</span></td>
									<td class="proper">77.77</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr102: Kampong Cham (incl Tboung Khmum)">Kampong Cham (incl Tboung Khmum)</span></td>
									<td class="proper">74.54</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr103: Kampong Chhnang">Kampong Chhnang</span></td>
									<td class="proper">77.57</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr104: Kampong Spueu">Kampong Spueu</span></td>
									<td class="proper">79.71</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr105: Kampong Thum">Kampong Thum</span></td>
									<td class="proper">76.47</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr114: Kampot-Krong Kaeb-Krong Preah Sihanouk">Kampot-Krong Kaeb-Krong Preah Sihanouk</span></td>
									<td class="proper">81.99</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr106: Kandal">Kandal</span></td>
									<td class="proper">76.29</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr107: Kaoh Kong">Kaoh Kong</span></td>
									<td class="proper">84.78</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr116: Mondol Kiri-Rotanak Kiri">Mondol Kiri-Rotanak Kiri</span></td>
									<td class="proper">73.38</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr108: Phnom Penh">Phnom Penh</span></td>
									<td class="proper">76.42</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr110: Pousat">Pousat</span></td>
									<td class="proper">81.48</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr115: Preah Vihear-Stueng Traeng-Kracheh">Preah Vihear-Stueng Traeng-Kracheh</span></td>
									<td class="proper">75.31</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr109: Prey Veaeng">Prey Veaeng</span></td>
									<td class="proper">75.08</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr117: Siem Reab-Otdar Mean Chey">Siem Reab-Otdar Mean Chey</span></td>
									<td class="proper">75.39</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr111: Svay Rieng">Svay Rieng</span></td>
									<td class="proper">75.33</td>
								</tr>
								<tr>
									<td class="region"><span title="KHMr112: Takaev">Takaev</span></td>
									<td class="proper">77.73</td>
								</tr>
								<tr class="country">
									<th>Cameroon (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CMRt: Total">Total</span></td>
									<td class="proper">67.80</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CMRr101: Adamaoua">Adamaoua</span></td>
									<td class="proper">57.04</td>
								</tr>
								<tr>
									<td class="region"><span title="CMRr102: Centre (incl Yaounde)">Centre (incl Yaounde)</span></td>
									<td class="proper">73.98</td>
								</tr>
								<tr>
									<td class="region"><span title="CMRr103: Est">Est</span></td>
									<td class="proper">74.17</td>
								</tr>
								<tr>
									<td class="region"><span title="CMRr104: Extreme Nord">Extreme Nord</span></td>
									<td class="proper">38.82</td>
								</tr>
								<tr>
									<td class="region"><span title="CMRr105: Littoral (incl Douala)">Littoral (incl Douala)</span></td>
									<td class="proper">85.86</td>
								</tr>
								<tr>
									<td class="region"><span title="CMRr106: Nord">Nord</span></td>
									<td class="proper">47.88</td>
								</tr>
								<tr>
									<td class="region"><span title="CMRr107: Nord Ouest">Nord Ouest</span></td>
									<td class="proper">65.46</td>
								</tr>
								<tr>
									<td class="region"><span title="CMRr108: Ouest">Ouest</span></td>
									<td class="proper">69.31</td>
								</tr>
								<tr>
									<td class="region"><span title="CMRr109: Sud">Sud</span></td>
									<td class="proper">82.80</td>
								</tr>
								<tr>
									<td class="region"><span title="CMRr110: Sud Ouest">Sud Ouest</span></td>
									<td class="proper">82.69</td>
								</tr>
								<tr class="country">
									<th>Canada (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CANt: Total">Total</span></td>
									<td class="proper">72.38</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CANr109: Alberta">Alberta</span></td>
									<td class="proper">65.39</td>
								</tr>
								<tr>
									<td class="region"><span title="CANr110: British Columbia">British Columbia</span></td>
									<td class="proper">71.97</td>
								</tr>
								<tr>
									<td class="region"><span title="CANr107: Manitoba">Manitoba</span></td>
									<td class="proper">71.39</td>
								</tr>
								<tr>
									<td class="region"><span title="CANr104: New Brunswick">New Brunswick</span></td>
									<td class="proper">72.99</td>
								</tr>
								<tr>
									<td class="region"><span title="CANr101: Newfoundland and Labrador">Newfoundland and Labrador</span></td>
									<td class="proper">76.61</td>
								</tr>
								<tr>
									<td class="region"><span title="CANr103: Nova Scotia">Nova Scotia</span></td>
									<td class="proper">77.94</td>
								</tr>
								<tr>
									<td class="region"><span title="CANr106: Ontario">Ontario</span></td>
									<td class="proper">72.41</td>
								</tr>
								<tr>
									<td class="region"><span title="CANr102: Prince Edward Island, Yukon Territory, Northwest Territories, Nunavut">Prince Edward Island, Yukon Territory, Northwest Territories, Nunavut</span></td>
									<td class="proper">74.16</td>
								</tr>
								<tr>
									<td class="region"><span title="CANr105: Quebec">Quebec</span></td>
									<td class="proper">75.04</td>
								</tr>
								<tr>
									<td class="region"><span title="CANr108: Saskatchewan">Saskatchewan</span></td>
									<td class="proper">65.89</td>
								</tr>
								<tr class="country">
									<th>Central African Republic (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CAFt: Total">Total</span></td>
									<td class="proper">58.30</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CAFr106: Bangui">Bangui</span></td>
									<td class="proper">67.59</td>
								</tr>
								<tr>
									<td class="region"><span title="CAFr101: RS I (Ombella Mpoko, Lobaye, Kemo, Nana Grebizi, Ouaka)">RS I (Ombella Mpoko, Lobaye, Kemo, Nana Grebizi, Ouaka)</span></td>
									<td class="proper">61.25</td>
								</tr>
								<tr>
									<td class="region"><span title="CAFr102: RS II (Mambera Kadei, Nana Mambere, Sangha Mbaere)">RS II (Mambera Kadei, Nana Mambere, Sangha Mbaere)</span></td>
									<td class="proper">67.51</td>
								</tr>
								<tr>
									<td class="region"><span title="CAFr103: RS III (Ouham Pende, Ouham)">RS III (Ouham Pende, Ouham)</span></td>
									<td class="proper">54.27</td>
								</tr>
								<tr>
									<td class="region"><span title="CAFr104: RS IV (Haute-Kotto, Baminigui Bangoran, Vakaga)">RS IV (Haute-Kotto, Baminigui Bangoran, Vakaga)</span></td>
									<td class="proper">46.26</td>
								</tr>
								<tr>
									<td class="region"><span title="CAFr105: RS V (Basse Kotto, Mbornou, Houte Mbormou)">RS V (Basse Kotto, Mbornou, Houte Mbormou)</span></td>
									<td class="proper">52.88</td>
								</tr>
								<tr class="country">
									<th>Chad (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="TCDt: Total">Total</span></td>
									<td class="proper">35.63</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="TCDr101: Zone 1 (N'Djamena)">Zone 1 (N'Djamena)</span></td>
									<td class="proper">34.28</td>
								</tr>
								<tr>
									<td class="region"><span title="TCDr102: Zone 2 (Borkou, Ennedi, Tibesti, Kanem, Barh El Gazal, Lac)">Zone 2 (Borkou, Ennedi, Tibesti, Kanem, Barh El Gazal, Lac)</span></td>
									<td class="proper">20.83</td>
								</tr>
								<tr>
									<td class="region"><span title="TCDr103: Zone 3 (Guera, Batha, Salamat)">Zone 3 (Guera, Batha, Salamat)</span></td>
									<td class="proper">31.43</td>
								</tr>
								<tr>
									<td class="region"><span title="TCDr104: Zone 4 (Ouaddai, Assongha, Sila, Biltine - Wadi Fira)">Zone 4 (Ouaddai, Assongha, Sila, Biltine - Wadi Fira)</span></td>
									<td class="proper">25.97</td>
								</tr>
								<tr>
									<td class="region"><span title="TCDr105: Zone 5 (Chari-Baguimi, Dababa, Baguirmi, Hadjer Lamis)">Zone 5 (Chari-Baguimi, Dababa, Baguirmi, Hadjer Lamis)</span></td>
									<td class="proper">35.01</td>
								</tr>
								<tr>
									<td class="region"><span title="TCDr106: Zone 6 (Mayo-Kebbi Est and Ouest)">Zone 6 (Mayo-Kebbi Est and Ouest)</span></td>
									<td class="proper">41.64</td>
								</tr>
								<tr>
									<td class="region"><span title="TCDr107: Zone 7 (Logone Occidental &amp; Oriental, Monts de Lam, Tandjile Est &amp; Ouest)">Zone 7 (Logone Occidental &amp; Oriental, Monts de Lam, Tandjile Est &amp; Ouest)</span></td>
									<td class="proper">47.84</td>
								</tr>
								<tr>
									<td class="region"><span title="TCDr108: Zone 8 (Mandoul, Moyen-Chari, Bahr Koh, Lac Iro)">Zone 8 (Mandoul, Moyen-Chari, Bahr Koh, Lac Iro)</span></td>
									<td class="proper">48.02</td>
								</tr>
								<tr class="country">
									<th>Chile (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CHLt: Total">Total</span></td>
									<td class="proper">61.13</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CHLr111: Aisen">Aisen</span></td>
									<td class="proper">80.95</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr102: Antofagasta">Antofagasta</span></td>
									<td class="proper">25.65</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr109: Arbucania">Arbucania</span></td>
									<td class="proper">77.89</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr103: Atacama">Atacama</span></td>
									<td class="proper">40.35</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr108: Bio Bio">Bio Bio</span></td>
									<td class="proper">72.75</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr104: Coquimbo">Coquimbo</span></td>
									<td class="proper">54.93</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr110: Los Lagos (incl Los Rios)">Los Lagos (incl Los Rios)</span></td>
									<td class="proper">81.63</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr112: Magallanes and La Antartica Chilena">Magallanes and La Antartica Chilena</span></td>
									<td class="proper">78.17</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr107: Maule">Maule</span></td>
									<td class="proper">67.95</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr106: OHiggins">OHiggins</span></td>
									<td class="proper">64.10</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr113: Region Metropolitana">Region Metropolitana</span></td>
									<td class="proper">57.15</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr101: Tarapaca (incl Arica and Parinacota)">Tarapaca (incl Arica and Parinacota)</span></td>
									<td class="proper">31.19</td>
								</tr>
								<tr>
									<td class="region"><span title="CHLr105: Valparaiso (former Aconcagua)">Valparaiso (former Aconcagua)</span></td>
									<td class="proper">61.97</td>
								</tr>
								<tr class="country">
									<th>China (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CHNt: Total">Total</span></td>
									<td class="proper">64.00</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CHNr112: Anhui">Anhui</span></td>
									<td class="proper">68.81</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr101: Beijing">Beijing</span></td>
									<td class="proper">50.52</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr122: Chongqing">Chongqing</span></td>
									<td class="proper">73.00</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr113: Fujian">Fujian</span></td>
									<td class="proper">74.37</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr128: Gansu">Gansu</span></td>
									<td class="proper">45.31</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr119: Guangdong">Guangdong</span></td>
									<td class="proper">76.35</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr120: Guangxi">Guangxi</span></td>
									<td class="proper">76.39</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr124: Guizhou">Guizhou</span></td>
									<td class="proper">75.15</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr121: Hainan">Hainan</span></td>
									<td class="proper">82.60</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr103: Hebei">Hebei</span></td>
									<td class="proper">52.09</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr108: Heilongjiang">Heilongjiang</span></td>
									<td class="proper">63.46</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr116: Henan">Henan</span></td>
									<td class="proper">61.43</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr132: Hongkong">Hongkong</span></td>
									<td class="proper">78.28</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr117: Hubei">Hubei</span></td>
									<td class="proper">70.97</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr118: Hunan">Hunan</span></td>
									<td class="proper">71.26</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr105: Inner Mongolia">Inner Mongolia</span></td>
									<td class="proper">44.48</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr110: Jiangsu">Jiangsu</span></td>
									<td class="proper">69.08</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr114: Jiangxi">Jiangxi</span></td>
									<td class="proper">71.01</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr107: Jilin">Jilin</span></td>
									<td class="proper">63.69</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr106: Liaoning">Liaoning</span></td>
									<td class="proper">59.69</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr130: Ningxia">Ningxia</span></td>
									<td class="proper">45.31</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr129: Qinghai">Qinghai</span></td>
									<td class="proper">47.58</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr127: Shaanxi">Shaanxi</span></td>
									<td class="proper">60.50</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr115: Shandong">Shandong</span></td>
									<td class="proper">60.84</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr109: Shanghai">Shanghai</span></td>
									<td class="proper">74.15</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr104: Shanxi">Shanxi</span></td>
									<td class="proper">52.21</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr123: Sichuan">Sichuan</span></td>
									<td class="proper">70.96</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr133: Taiwan">Taiwan</span></td>
									<td class="proper">81.59</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr102: Tianjin">Tianjin</span></td>
									<td class="proper">52.25</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr126: Tibet">Tibet</span></td>
									<td class="proper">53.68</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr131: Xinjiang">Xinjiang</span></td>
									<td class="proper">40.50</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr125: Yunnan">Yunnan</span></td>
									<td class="proper">72.04</td>
								</tr>
								<tr>
									<td class="region"><span title="CHNr111: Zhejiang">Zhejiang</span></td>
									<td class="proper">72.36</td>
								</tr>
								<tr class="country">
									<th>Colombia (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="COLt: Total">Total</span></td>
									<td class="proper">81.98</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="COLr129: Amazonas">Amazonas</span></td>
									<td class="proper">87.12</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr101: Antioquia (incl Medellin)">Antioquia (incl Medellin)</span></td>
									<td class="proper">83.28</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr125: Arauca">Arauca</span></td>
									<td class="proper">77.86</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr102: Atlantico (incl Barranquilla)">Atlantico (incl Barranquilla)</span></td>
									<td class="proper">80.44</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr103: Bogota D.C.">Bogota D.C.</span></td>
									<td class="proper">82.13</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr104: Bolivar (Sur and Norte)">Bolivar (Sur and Norte)</span></td>
									<td class="proper">82.80</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr105: Boyaca">Boyaca</span></td>
									<td class="proper">82.87</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr106: Caldas">Caldas</span></td>
									<td class="proper">76.91</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr107: Caqueta">Caqueta</span></td>
									<td class="proper">83.91</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr126: Casanare">Casanare</span></td>
									<td class="proper">75.86</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr108: Cauca">Cauca</span></td>
									<td class="proper">86.00</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr109: Cesar">Cesar</span></td>
									<td class="proper">75.98</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr112: Choco">Choco</span></td>
									<td class="proper">87.42</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr110: Cordoba">Cordoba</span></td>
									<td class="proper">81.59</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr111: Cundinamarca">Cundinamarca</span></td>
									<td class="proper">79.23</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr130: Guainja">Guainja</span></td>
									<td class="proper">86.45</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr114: Guajira">Guajira</span></td>
									<td class="proper">76.82</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr131: Guaviare">Guaviare</span></td>
									<td class="proper">85.37</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr113: Huila">Huila</span></td>
									<td class="proper">77.90</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr115: Magdalena">Magdalena</span></td>
									<td class="proper">78.31</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr116: Meta">Meta</span></td>
									<td class="proper">79.12</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr117: Narino">Narino</span></td>
									<td class="proper">86.92</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr118: Norte de Santander">Norte de Santander</span></td>
									<td class="proper">79.21</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr127: Putumayo">Putumayo</span></td>
									<td class="proper">84.39</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr119: Quindio">Quindio</span></td>
									<td class="proper">86.08</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr120: Risaralda">Risaralda</span></td>
									<td class="proper">88.51</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr128: San Andres">San Andres</span></td>
									<td class="proper">82.08</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr121: Santander">Santander</span></td>
									<td class="proper">83.11</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr122: Sucre">Sucre</span></td>
									<td class="proper">81.32</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr123: Tolima">Tolima</span></td>
									<td class="proper">71.05</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr124: Valle (incl Cali)">Valle (incl Cali)</span></td>
									<td class="proper">87.07</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr132: Vaupis">Vaupis</span></td>
									<td class="proper">87.31</td>
								</tr>
								<tr>
									<td class="region"><span title="COLr133: Vichada">Vichada</span></td>
									<td class="proper">80.85</td>
								</tr>
								<tr class="country">
									<th>Comoros (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="COMt: Total">Total</span></td>
									<td class="proper">77.76</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="COMr103: Anjouan (Ndzouani)">Anjouan (Ndzouani)</span></td>
									<td class="proper">75.86</td>
								</tr>
								<tr>
									<td class="region"><span title="COMr101: Grande Comore (Ngazidja)">Grande Comore (Ngazidja)</span></td>
									<td class="proper">80.11</td>
								</tr>
								<tr>
									<td class="region"><span title="COMr102: Moheli">Moheli</span></td>
									<td class="proper">77.30</td>
								</tr>
								<tr class="country">
									<th>Congo, Dem. Rep. (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CODt: Total">Total</span></td>
									<td class="proper">74.11</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CODr103: Bandundu">Bandundu</span></td>
									<td class="proper">72.81</td>
								</tr>
								<tr>
									<td class="region"><span title="CODr102: Bas-Congo">Bas-Congo</span></td>
									<td class="proper">78.49</td>
								</tr>
								<tr>
									<td class="region"><span title="CODr104: Equateur">Equateur</span></td>
									<td class="proper">76.92</td>
								</tr>
								<tr>
									<td class="region"><span title="CODr111: Kasai Occidental">Kasai Occidental</span></td>
									<td class="proper">69.22</td>
								</tr>
								<tr>
									<td class="region"><span title="CODr110: Kasai Oriental">Kasai Oriental</span></td>
									<td class="proper">70.02</td>
								</tr>
								<tr>
									<td class="region"><span title="CODr109: Katanga">Katanga</span></td>
									<td class="proper">62.81</td>
								</tr>
								<tr>
									<td class="region"><span title="CODr101: Kinshasa">Kinshasa</span></td>
									<td class="proper">76.62</td>
								</tr>
								<tr>
									<td class="region"><span title="CODr108: Maniema">Maniema</span></td>
									<td class="proper">76.42</td>
								</tr>
								<tr>
									<td class="region"><span title="CODr106: Nord-Kivu">Nord-Kivu</span></td>
									<td class="proper">80.77</td>
								</tr>
								<tr>
									<td class="region"><span title="CODr105: Orientale">Orientale</span></td>
									<td class="proper">74.21</td>
								</tr>
								<tr>
									<td class="region"><span title="CODr107: Sud-Kivu">Sud-Kivu</span></td>
									<td class="proper">76.90</td>
								</tr>
								<tr class="country">
									<th>Congo, Rep. (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="COGt: Total">Total</span></td>
									<td class="proper">80.83</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="COGr204:  Bouenza"> Bouenza</span></td>
									<td class="proper">79.17</td>
								</tr>
								<tr>
									<td class="region"><span title="COGr211:  Brazzaville"> Brazzaville</span></td>
									<td class="proper">76.60</td>
								</tr>
								<tr>
									<td class="region"><span title="COGr207:  Cuvette"> Cuvette</span></td>
									<td class="proper">80.44</td>
								</tr>
								<tr>
									<td class="region"><span title="COGr208:  Cuvette Ouest"> Cuvette Ouest</span></td>
									<td class="proper">81.76</td>
								</tr>
								<tr>
									<td class="region"><span title="COGr201:  Kouilou"> Kouilou</span></td>
									<td class="proper">85.23</td>
								</tr>
								<tr>
									<td class="region"><span title="COGr203:  Lekoumou"> Lekoumou</span></td>
									<td class="proper">81.45</td>
								</tr>
								<tr>
									<td class="region"><span title="COGr210:  Likouala"> Likouala</span></td>
									<td class="proper">80.31</td>
								</tr>
								<tr>
									<td class="region"><span title="COGr202:  Niari"> Niari</span></td>
									<td class="proper">82.49</td>
								</tr>
								<tr>
									<td class="region"><span title="COGr206:  Plateaux"> Plateaux</span></td>
									<td class="proper">78.86</td>
								</tr>
								<tr>
									<td class="region"><span title="COGr212:  Pointe Noire"> Pointe Noire</span></td>
									<td class="proper">84.66</td>
								</tr>
								<tr>
									<td class="region"><span title="COGr205:  Pool"> Pool</span></td>
									<td class="proper">78.35</td>
								</tr>
								<tr>
									<td class="region"><span title="COGr209:  Sangha"> Sangha</span></td>
									<td class="proper">80.60</td>
								</tr>
								<tr class="country">
									<th>Costa Rica (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CRIt: Total">Total</span></td>
									<td class="proper">84.72</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CRIr102: Alajuela">Alajuela</span></td>
									<td class="proper">85.82</td>
								</tr>
								<tr>
									<td class="region"><span title="CRIr103: Cartago">Cartago</span></td>
									<td class="proper">85.58</td>
								</tr>
								<tr>
									<td class="region"><span title="CRIr105: Guanacaste">Guanacaste</span></td>
									<td class="proper">79.40</td>
								</tr>
								<tr>
									<td class="region"><span title="CRIr104: Heredia">Heredia</span></td>
									<td class="proper">86.50</td>
								</tr>
								<tr>
									<td class="region"><span title="CRIr107: Limon">Limon</span></td>
									<td class="proper">85.62</td>
								</tr>
								<tr>
									<td class="region"><span title="CRIr106: Puntarenas">Puntarenas</span></td>
									<td class="proper">84.96</td>
								</tr>
								<tr>
									<td class="region"><span title="CRIr101: San Jose">San Jose</span></td>
									<td class="proper">85.16</td>
								</tr>
								<tr class="country">
									<th>Cote d'Ivoire (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CIVt: Total">Total</span></td>
									<td class="proper">72.32</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CIVr101: Abidjan">Abidjan</span></td>
									<td class="proper">85.43</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr103: Bas Sassandra">Bas Sassandra</span></td>
									<td class="proper">83.47</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr104: Comoe">Comoe</span></td>
									<td class="proper">80.63</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr105: Denguele">Denguele</span></td>
									<td class="proper">58.70</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr106: Goh-Djiboua">Goh-Djiboua</span></td>
									<td class="proper">80.50</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr107: Lacs">Lacs</span></td>
									<td class="proper">71.87</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr108: Lagunes">Lagunes</span></td>
									<td class="proper">82.32</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr109: Montagnes">Montagnes</span></td>
									<td class="proper">74.84</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr110: Sassandra-Marahoue">Sassandra-Marahoue</span></td>
									<td class="proper">71.87</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr111: Savanes">Savanes</span></td>
									<td class="proper">58.69</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr112: Vallee du Bandama">Vallee du Bandama</span></td>
									<td class="proper">64.92</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr113: Woroba">Woroba</span></td>
									<td class="proper">64.61</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr102: Yamoussoukro">Yamoussoukro</span></td>
									<td class="proper">72.84</td>
								</tr>
								<tr>
									<td class="region"><span title="CIVr114: Zanzan">Zanzan</span></td>
									<td class="proper">61.74</td>
								</tr>
								<tr class="country">
									<th>Croatia (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="HRVt: Total">Total</span></td>
									<td class="proper">69.06</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="HRVr101: City of Zagreb">City of Zagreb</span></td>
									<td class="proper">69.15</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr107: County of Bjelovar-Bilogora">County of Bjelovar-Bilogora</span></td>
									<td class="proper">69.77</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr110: County of Brod-Posavina">County of Brod-Posavina</span></td>
									<td class="proper">69.39</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr121: County of Dubrovnik-Neretva">County of Dubrovnik-Neretva</span></td>
									<td class="proper">66.58</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr120: County of Istria">County of Istria</span></td>
									<td class="proper">69.76</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr113: County of Karlovac">County of Karlovac</span></td>
									<td class="proper">71.67</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr105: County of Koprivnica-Krizevc">County of Koprivnica-Krizevc</span></td>
									<td class="proper">69.31</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr103: County of Krapina-Zagorje">County of Krapina-Zagorje</span></td>
									<td class="proper">70.45</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr116: County of Lika-Senj">County of Lika-Senj</span></td>
									<td class="proper">72.01</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr106: County of Medimurje">County of Medimurje</span></td>
									<td class="proper">68.26</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr111: County of Osijek-Baranja">County of Osijek-Baranja</span></td>
									<td class="proper">68.52</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr109: County of Pozega-Slavonia">County of Pozega-Slavonia</span></td>
									<td class="proper">70.30</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr115: County of Primorje-Gorski Kotar">County of Primorje-Gorski Kotar</span></td>
									<td class="proper">72.66</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr118: County of Sibenik-Knin">County of Sibenik-Knin</span></td>
									<td class="proper">62.68</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr114: County of Sisak-Moslavina">County of Sisak-Moslavina</span></td>
									<td class="proper">69.24</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr119: County of Split-Dalmatia">County of Split-Dalmatia</span></td>
									<td class="proper">66.92</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr104: County of Varazdin">County of Varazdin</span></td>
									<td class="proper">70.44</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr108: County of Virovitica-Podravina">County of Virovitica-Podravina</span></td>
									<td class="proper">70.21</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr112: County of Vukovar-Srijem">County of Vukovar-Srijem</span></td>
									<td class="proper">67.47</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr117: County of Zadar">County of Zadar</span></td>
									<td class="proper">66.06</td>
								</tr>
								<tr>
									<td class="region"><span title="HRVr102: County of Zagreb">County of Zagreb</span></td>
									<td class="proper">69.36</td>
								</tr>
								<tr class="country">
									<th>Cuba (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CUBt: Total">Total</span></td>
									<td class="proper">76.32</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CUBr103: C. Habana">C. Habana</span></td>
									<td class="proper">75.48</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr109: Camaguey">Camaguey</span></td>
									<td class="proper">74.64</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr108: Ciego de Avila">Ciego de Avila</span></td>
									<td class="proper">76.40</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr106: Cienfuegos">Cienfuegos</span></td>
									<td class="proper">75.41</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr112: Granma">Granma</span></td>
									<td class="proper">72.45</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr114: Guantanamo">Guantanamo</span></td>
									<td class="proper">80.04</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr111: Holguin">Holguin</span></td>
									<td class="proper">77.50</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr115: Isla">Isla</span></td>
									<td class="proper">76.36</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr110: Las Tunas">Las Tunas</span></td>
									<td class="proper">74.63</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr104: Matanzas">Matanzas</span></td>
									<td class="proper">75.79</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr101: Pinar del Rio">Pinar del Rio</span></td>
									<td class="proper">77.78</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr102: Prov. Habana">Prov. Habana</span></td>
									<td class="proper">76.34</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr107: S.Spiritus">S.Spiritus</span></td>
									<td class="proper">76.37</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr113: Santiago de Cuba">Santiago de Cuba</span></td>
									<td class="proper">76.85</td>
								</tr>
								<tr>
									<td class="region"><span title="CUBr105: Villa Clara">Villa Clara</span></td>
									<td class="proper">78.75</td>
								</tr>
								<tr class="country">
									<th>Cyprus (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CYPt: Total">Total</span></td>
									<td class="proper">61.99</td>
								</tr>
								<tr class="country">
									<th>Czechia (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CZEt: Total">Total</span></td>
									<td class="proper">71.26</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CZEr106: Jihovychod">Jihovychod</span></td>
									<td class="proper">70.22</td>
								</tr>
								<tr>
									<td class="region"><span title="CZEr103: Jihozapad">Jihozapad</span></td>
									<td class="proper">72.93</td>
								</tr>
								<tr>
									<td class="region"><span title="CZEr108: Moravskoslezsko">Moravskoslezsko</span></td>
									<td class="proper">72.65</td>
								</tr>
								<tr>
									<td class="region"><span title="CZEr101: Praha">Praha</span></td>
									<td class="proper">69.00</td>
								</tr>
								<tr>
									<td class="region"><span title="CZEr105: Severovychod">Severovychod</span></td>
									<td class="proper">73.03</td>
								</tr>
								<tr>
									<td class="region"><span title="CZEr104: Severozapad">Severozapad</span></td>
									<td class="proper">71.04</td>
								</tr>
								<tr>
									<td class="region"><span title="CZEr102: Stredni Cechy">Stredni Cechy</span></td>
									<td class="proper">69.67</td>
								</tr>
								<tr>
									<td class="region"><span title="CZEr107: Stredni Morava">Stredni Morava</span></td>
									<td class="proper">71.52</td>
								</tr>
								<tr class="country">
									<th>Denmark (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="DNKt: Total">Total</span></td>
									<td class="proper">79.57</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="DNKr101: Hovedstaden">Hovedstaden</span></td>
									<td class="proper">79.03</td>
								</tr>
								<tr>
									<td class="region"><span title="DNKr104: Midtjylland">Midtjylland</span></td>
									<td class="proper">80.56</td>
								</tr>
								<tr>
									<td class="region"><span title="DNKr105: Nordjylland">Nordjylland</span></td>
									<td class="proper">79.53</td>
								</tr>
								<tr>
									<td class="region"><span title="DNKr102: Sjaelland">Sjaelland</span></td>
									<td class="proper">79.09</td>
								</tr>
								<tr>
									<td class="region"><span title="DNKr103: Syddanmark">Syddanmark</span></td>
									<td class="proper">79.63</td>
								</tr>
								<tr class="country">
									<th>Djibouti (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="DJIt: Total">Total</span></td>
									<td class="proper">55.82</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="DJIr101: Djibouti">Djibouti</span></td>
									<td class="proper">61.51</td>
								</tr>
								<tr>
									<td class="region"><span title="DJIr102: Other Districts">Other Districts</span></td>
									<td class="proper">50.13</td>
								</tr>
								<tr class="country">
									<th>Dominica (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="DMAt: Total">Total</span></td>
									<td class="proper">80.45</td>
								</tr>
								<tr class="country">
									<th>Dominican Republic (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="DOMt: Total">Total</span></td>
									<td class="proper">81.21</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="DOMr101: Region 0 (Distrito Nacional, Santo Domingo, Monte Plata)">Region 0 (Distrito Nacional, Santo Domingo, Monte Plata)</span></td>
									<td class="proper">84.77</td>
								</tr>
								<tr>
									<td class="region"><span title="DOMr102: Region I (Peravia, San Cristobal, San Jose de Ocoa, Azua)">Region I (Peravia, San Cristobal, San Jose de Ocoa, Azua)</span></td>
									<td class="proper">81.93</td>
								</tr>
								<tr>
									<td class="region"><span title="DOMr103: Region II (Espaillat, Puerto Plata, Santiago)">Region II (Espaillat, Puerto Plata, Santiago)</span></td>
									<td class="proper">80.45</td>
								</tr>
								<tr>
									<td class="region"><span title="DOMr104: Region III (Duarte, Maria Trinidad Sanchez, Salcedo, Samana)">Region III (Duarte, Maria Trinidad Sanchez, Salcedo, Samana)</span></td>
									<td class="proper">85.43</td>
								</tr>
								<tr>
									<td class="region"><span title="DOMr105: Region IV (Independencia, Bahoruco, Barahona, Pedernales)">Region IV (Independencia, Bahoruco, Barahona, Pedernales)</span></td>
									<td class="proper">77.37</td>
								</tr>
								<tr>
									<td class="region"><span title="DOMr106: Region V (El Seibo, La Altagracia, La Romana, San Pedro de Macoris, Hato Mayor)">Region V (El Seibo, La Altagracia, La Romana, San Pedro de Macoris, Hato Mayor)</span></td>
									<td class="proper">82.68</td>
								</tr>
								<tr>
									<td class="region"><span title="DOMr107: Region VI (San Juan, Elias Pina)">Region VI (San Juan, Elias Pina)</span></td>
									<td class="proper">78.32</td>
								</tr>
								<tr>
									<td class="region"><span title="DOMr108: Region VII (Dajabon, Monte Cristi, Santiago Rodriguez, Valverde)">Region VII (Dajabon, Monte Cristi, Santiago Rodriguez, Valverde)</span></td>
									<td class="proper">75.08</td>
								</tr>
								<tr>
									<td class="region"><span title="DOMr109: Region VIII (La Vega, Monsenor Nouel, Sanchez Ramirez)">Region VIII (La Vega, Monsenor Nouel, Sanchez Ramirez)</span></td>
									<td class="proper">84.86</td>
								</tr>
								<tr class="country">
									<th>Ecuador (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ECUt: Total">Total</span></td>
									<td class="proper">83.57</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ECUr101: Coste">Coste</span></td>
									<td class="proper">81.94</td>
								</tr>
								<tr>
									<td class="region"><span title="ECUr104: Galapagos">Galapagos</span></td>
									<td class="proper">84.61</td>
								</tr>
								<tr>
									<td class="region"><span title="ECUr103: Oriente">Oriente</span></td>
									<td class="proper">84.38</td>
								</tr>
								<tr>
									<td class="region"><span title="ECUr102: Sierra">Sierra</span></td>
									<td class="proper">83.38</td>
								</tr>
								<tr class="country">
									<th>Egypt, Arab Rep. (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="EGYt: Total">Total</span></td>
									<td class="proper">49.20</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="EGYr102: Alexandria">Alexandria</span></td>
									<td class="proper">66.41</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr118: Assuit">Assuit</span></td>
									<td class="proper">35.95</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr121: Aswan">Aswan</span></td>
									<td class="proper">24.98</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr112: Behera">Behera</span></td>
									<td class="proper">59.12</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr115: Beni Suef">Beni Suef</span></td>
									<td class="proper">42.59</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr101: Cairo">Cairo</span></td>
									<td class="proper">49.40</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr106: Dakahlia">Dakahlia</span></td>
									<td class="proper">60.08</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr105: Damietta">Damietta</span></td>
									<td class="proper">67.38</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr116: Fayoum">Fayoum</span></td>
									<td class="proper">46.95</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr122: Frontier governorates (Red Sea, New Valley, Matroh, North Sainai, South Sainai)">Frontier governorates (Red Sea, New Valley, Matroh, North Sainai, South Sainai)</span></td>
									<td class="proper">35.49</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr110: Gharbia">Gharbia</span></td>
									<td class="proper">55.94</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr114: Giza">Giza</span></td>
									<td class="proper">44.26</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr113: Ismailia">Ismailia</span></td>
									<td class="proper">56.62</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr109: Kafr El-Sheikh">Kafr El-Sheikh</span></td>
									<td class="proper">63.69</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr108: Kalyubia">Kalyubia</span></td>
									<td class="proper">51.43</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr111: Menoufia">Menoufia</span></td>
									<td class="proper">53.16</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr117: Menya">Menya</span></td>
									<td class="proper">39.78</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr103: Port Said">Port Said</span></td>
									<td class="proper">64.67</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr120: Qena">Qena</span></td>
									<td class="proper">28.11</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr107: Sharkia">Sharkia</span></td>
									<td class="proper">54.98</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr119: Souhag">Souhag</span></td>
									<td class="proper">31.48</td>
								</tr>
								<tr>
									<td class="region"><span title="EGYr104: Suez">Suez</span></td>
									<td class="proper">49.87</td>
								</tr>
								<tr class="country">
									<th>El Salvador (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SLVt: Total">Total</span></td>
									<td class="proper">70.03</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SLVr102: Central I">Central I</span></td>
									<td class="proper">67.96</td>
								</tr>
								<tr>
									<td class="region"><span title="SLVr103: Central II">Central II</span></td>
									<td class="proper">71.03</td>
								</tr>
								<tr>
									<td class="region"><span title="SLVr101: Occidental">Occidental</span></td>
									<td class="proper">71.13</td>
								</tr>
								<tr>
									<td class="region"><span title="SLVr104: Oriental">Oriental</span></td>
									<td class="proper">70.00</td>
								</tr>
								<tr class="country">
									<th>Equatorial Guinea (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GNQt: Total">Total</span></td>
									<td class="proper">86.70</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="GNQr101: Annobon, Bioko">Annobon, Bioko</span></td>
									<td class="proper">87.92</td>
								</tr>
								<tr>
									<td class="region"><span title="GNQr102: Centro Sur">Centro Sur</span></td>
									<td class="proper">88.49</td>
								</tr>
								<tr>
									<td class="region"><span title="GNQr103: Kie Ntem">Kie Ntem</span></td>
									<td class="proper">84.42</td>
								</tr>
								<tr>
									<td class="region"><span title="GNQr104: Litoral">Litoral</span></td>
									<td class="proper">88.46</td>
								</tr>
								<tr>
									<td class="region"><span title="GNQr105: Wele Nzas">Wele Nzas</span></td>
									<td class="proper">84.21</td>
								</tr>
								<tr class="country">
									<th>Eritrea (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ERIt: Total">Total</span></td>
									<td class="proper">47.35</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ERIr104: Anseba">Anseba</span></td>
									<td class="proper">41.71</td>
								</tr>
								<tr>
									<td class="region"><span title="ERIr106: Debub (Southern)">Debub (Southern)</span></td>
									<td class="proper">49.71</td>
								</tr>
								<tr>
									<td class="region"><span title="ERIr101: Debubawi Keyih Bahri (Southern Red Sea)">Debubawi Keyih Bahri (Southern Red Sea)</span></td>
									<td class="proper">48.65</td>
								</tr>
								<tr>
									<td class="region"><span title="ERIr105: Gash Barka">Gash Barka</span></td>
									<td class="proper">36.37</td>
								</tr>
								<tr>
									<td class="region"><span title="ERIr102: Maekel (Central including Asmara)">Maekel (Central including Asmara)</span></td>
									<td class="proper">55.61</td>
								</tr>
								<tr>
									<td class="region"><span title="ERIr103: Semenawi Keyih Bahri (Northern Red Sea)">Semenawi Keyih Bahri (Northern Red Sea)</span></td>
									<td class="proper">52.05</td>
								</tr>
								<tr class="country">
									<th>Estonia (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ESTt: Total">Total</span></td>
									<td class="proper">78.10</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ESTr103: Kesk-Eesti">Kesk-Eesti</span></td>
									<td class="proper">78.37</td>
								</tr>
								<tr>
									<td class="region"><span title="ESTr104: Kirde-Eesti">Kirde-Eesti</span></td>
									<td class="proper">78.44</td>
								</tr>
								<tr>
									<td class="region"><span title="ESTr102: Laane-Eesti">Laane-Eesti</span></td>
									<td class="proper">78.18</td>
								</tr>
								<tr>
									<td class="region"><span title="ESTr105: Louna-Eesti">Louna-Eesti</span></td>
									<td class="proper">77.42</td>
								</tr>
								<tr>
									<td class="region"><span title="ESTr101: Pohja-Eesti">Pohja-Eesti</span></td>
									<td class="proper">78.10</td>
								</tr>
								<tr class="country">
									<th>Eswatini (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SWZt: Total">Total</span></td>
									<td class="proper">71.52</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SWZr101: Hhohho">Hhohho</span></td>
									<td class="proper">72.83</td>
								</tr>
								<tr>
									<td class="region"><span title="SWZr104: Lubombo">Lubombo</span></td>
									<td class="proper">68.72</td>
								</tr>
								<tr>
									<td class="region"><span title="SWZr102: Manzini">Manzini</span></td>
									<td class="proper">72.19</td>
								</tr>
								<tr>
									<td class="region"><span title="SWZr103: Shiselweni">Shiselweni</span></td>
									<td class="proper">72.33</td>
								</tr>
								<tr class="country">
									<th>Ethiopia (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ETHt: Total">Total</span></td>
									<td class="proper">49.24</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ETHr110: Addis">Addis</span></td>
									<td class="proper">59.75</td>
								</tr>
								<tr>
									<td class="region"><span title="ETHr102: Affar">Affar</span></td>
									<td class="proper">36.56</td>
								</tr>
								<tr>
									<td class="region"><span title="ETHr103: Amhara">Amhara</span></td>
									<td class="proper">50.43</td>
								</tr>
								<tr>
									<td class="region"><span title="ETHr106: Ben-Gumz">Ben-Gumz</span></td>
									<td class="proper">46.96</td>
								</tr>
								<tr>
									<td class="region"><span title="ETHr111: Dire Dawa">Dire Dawa</span></td>
									<td class="proper">46.18</td>
								</tr>
								<tr>
									<td class="region"><span title="ETHr108: Gambela">Gambela</span></td>
									<td class="proper">52.56</td>
								</tr>
								<tr>
									<td class="region"><span title="ETHr109: Harari">Harari</span></td>
									<td class="proper">50.14</td>
								</tr>
								<tr>
									<td class="region"><span title="ETHr104: Oromiya">Oromiya</span></td>
									<td class="proper">54.59</td>
								</tr>
								<tr>
									<td class="region"><span title="ETHr107: SNNP">SNNP</span></td>
									<td class="proper">57.72</td>
								</tr>
								<tr>
									<td class="region"><span title="ETHr105: Somali">Somali</span></td>
									<td class="proper">42.92</td>
								</tr>
								<tr>
									<td class="region"><span title="ETHr101: Tigray">Tigray</span></td>
									<td class="proper">43.79</td>
								</tr>
								<tr class="country">
									<th>Fiji (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="FJIt: Total">Total</span></td>
									<td class="proper">82.77</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="FJIr108: Ba">Ba</span></td>
									<td class="proper">81.68</td>
								</tr>
								<tr>
									<td class="region"><span title="FJIr106: Cakaudrove, Bua">Cakaudrove, Bua</span></td>
									<td class="proper">82.21</td>
								</tr>
								<tr>
									<td class="region"><span title="FJIr105: Kadavu, Lau, Lomaiviti, Rotuma">Kadavu, Lau, Lomaiviti, Rotuma</span></td>
									<td class="proper">79.63</td>
								</tr>
								<tr>
									<td class="region"><span title="FJIr107: Macuata">Macuata</span></td>
									<td class="proper">81.58</td>
								</tr>
								<tr>
									<td class="region"><span title="FJIr109: Nadroga or Navosa">Nadroga or Navosa</span></td>
									<td class="proper">83.11</td>
								</tr>
								<tr>
									<td class="region"><span title="FJIr101: Naitasiri">Naitasiri</span></td>
									<td class="proper">85.59</td>
								</tr>
								<tr>
									<td class="region"><span title="FJIr110: Ra">Ra</span></td>
									<td class="proper">84.57</td>
								</tr>
								<tr>
									<td class="region"><span title="FJIr102: Rewa">Rewa</span></td>
									<td class="proper">82.57</td>
								</tr>
								<tr>
									<td class="region"><span title="FJIr103: Serua, Namosi">Serua, Namosi</span></td>
									<td class="proper">83.90</td>
								</tr>
								<tr>
									<td class="region"><span title="FJIr104: Tailevu">Tailevu</span></td>
									<td class="proper">82.90</td>
								</tr>
								<tr class="country">
									<th>Finland (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="FINt: Total">Total</span></td>
									<td class="proper">78.47</td>
								</tr>
								<tr class="country">
									<th>FInland (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="FINr105: Aland">Aland</span></td>
									<td class="proper">78.11</td>
								</tr>
								<tr class="country">
									<th>Finland (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="FINr103: Etela-Suomi">Etela-Suomi</span></td>
									<td class="proper">78.08</td>
								</tr>
								<tr>
									<td class="region"><span title="FINr102: Helsinki-Uusimaa">Helsinki-Uusimaa</span></td>
									<td class="proper">77.98</td>
								</tr>
								<tr>
									<td class="region"><span title="FINr101: Lansi-Suomi">Lansi-Suomi</span></td>
									<td class="proper">78.93</td>
								</tr>
								<tr>
									<td class="region"><span title="FINr104: Pohjois-ja Ita-Suomi">Pohjois-ja Ita-Suomi</span></td>
									<td class="proper">79.25</td>
								</tr>
								<tr class="country">
									<th>France (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="FRAt: Total">Total</span></td>
									<td class="proper">72.06</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="FRAr110: Alsace">Alsace</span></td>
									<td class="proper">69.94</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr115: Aquitaine">Aquitaine</span></td>
									<td class="proper">69.17</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr119: Auvergne">Auvergne</span></td>
									<td class="proper">69.89</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr106: Basse-Normandie">Basse-Normandie</span></td>
									<td class="proper">76.60</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr107: Bourgogne">Bourgogne</span></td>
									<td class="proper">70.02</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr113: Bretagne">Bretagne</span></td>
									<td class="proper">77.89</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr105: Centre">Centre</span></td>
									<td class="proper">70.14</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr102: Champagne-Ardenne">Champagne-Ardenne</span></td>
									<td class="proper">70.39</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr122: Corse">Corse</span></td>
									<td class="proper">69.46</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr111: Franche-Comte">Franche-Comte</span></td>
									<td class="proper">69.09</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr127: French Guyana">French Guyana</span></td>
									<td class="proper">83.82</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr104: Haute-Normandie">Haute-Normandie</span></td>
									<td class="proper">75.89</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr101: Ile de France">Ile de France</span></td>
									<td class="proper">71.03</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr120: Languedoc-Roussillon">Languedoc-Roussillon</span></td>
									<td class="proper">67.62</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr117: Limousin">Limousin</span></td>
									<td class="proper">71.67</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr109: Lorraine">Lorraine</span></td>
									<td class="proper">70.82</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr129: Mayotte">Mayotte</span></td>
									<td class="proper">76.80</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr116: Midi-Pyrenees">Midi-Pyrenees</span></td>
									<td class="proper">69.31</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr108: Nord">Nord</span></td>
									<td class="proper">74.75</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr112: Pays de la Loire">Pays de la Loire</span></td>
									<td class="proper">72.20</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr103: Picardie">Picardie</span></td>
									<td class="proper">72.90</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr114: Poitou-Charentes">Poitou-Charentes</span></td>
									<td class="proper">70.00</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr121: Provence-Alpes-Cote dAzur">Provence-Alpes-Cote dAzur</span></td>
									<td class="proper">64.06</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr128: Reunion">Reunion</span></td>
									<td class="proper">80.95</td>
								</tr>
								<tr>
									<td class="region"><span title="FRAr118: Rhone-Alpes">Rhone-Alpes</span></td>
									<td class="proper">66.96</td>
								</tr>
								<tr class="country">
									<th>French Polynesia (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="PYFt: Total">Total</span></td>
									<td class="proper">79.43</td>
								</tr>
								<tr class="country">
									<th>Gabon (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GABt: Total">Total</span></td>
									<td class="proper">83.31</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="GABr101: Estuaire">Estuaire</span></td>
									<td class="proper">86.07</td>
								</tr>
								<tr>
									<td class="region"><span title="GABr102: Haut Ogooue">Haut Ogooue</span></td>
									<td class="proper">81.23</td>
								</tr>
								<tr>
									<td class="region"><span title="GABr103: Moyen Ogooue">Moyen Ogooue</span></td>
									<td class="proper">84.01</td>
								</tr>
								<tr>
									<td class="region"><span title="GABr104: Ngounie">Ngounie</span></td>
									<td class="proper">84.82</td>
								</tr>
								<tr>
									<td class="region"><span title="GABr105: Nyanga">Nyanga</span></td>
									<td class="proper">85.57</td>
								</tr>
								<tr>
									<td class="region"><span title="GABr106: Ogooue Ivindo">Ogooue Ivindo</span></td>
									<td class="proper">80.74</td>
								</tr>
								<tr>
									<td class="region"><span title="GABr107: Ogooue Lolo">Ogooue Lolo</span></td>
									<td class="proper">81.13</td>
								</tr>
								<tr>
									<td class="region"><span title="GABr108: Ogooue Maritime">Ogooue Maritime</span></td>
									<td class="proper">85.28</td>
								</tr>
								<tr>
									<td class="region"><span title="GABr109: Woleu Ntem">Woleu Ntem</span></td>
									<td class="proper">80.92</td>
								</tr>
								<tr class="country">
									<th>Gambia, The (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GMBt: Total">Total</span></td>
									<td class="proper">58.79</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="GMBr101: Banjul">Banjul</span></td>
									<td class="proper">67.60</td>
								</tr>
								<tr>
									<td class="region"><span title="GMBr108: Basse">Basse</span></td>
									<td class="proper">45.20</td>
								</tr>
								<tr>
									<td class="region"><span title="GMBr103: Brikama">Brikama</span></td>
									<td class="proper">67.34</td>
								</tr>
								<tr>
									<td class="region"><span title="GMBr107: Janjabureh">Janjabureh</span></td>
									<td class="proper">48.38</td>
								</tr>
								<tr>
									<td class="region"><span title="GMBr102: Kanifing">Kanifing</span></td>
									<td class="proper">73.19</td>
								</tr>
								<tr>
									<td class="region"><span title="GMBr105: Kerewan">Kerewan</span></td>
									<td class="proper">60.94</td>
								</tr>
								<tr>
									<td class="region"><span title="GMBr106: Kuntaur">Kuntaur</span></td>
									<td class="proper">49.72</td>
								</tr>
								<tr>
									<td class="region"><span title="GMBr104: Mansakonko">Mansakonko</span></td>
									<td class="proper">57.98</td>
								</tr>
								<tr class="country">
									<th>Georgia (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GEOt: Total">Total</span></td>
									<td class="proper">70.74</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="GEOr101: Abkhazia">Abkhazia</span></td>
									<td class="proper">74.23</td>
								</tr>
								<tr>
									<td class="region"><span title="GEOr102: Ajaria">Ajaria</span></td>
									<td class="proper">78.01</td>
								</tr>
								<tr>
									<td class="region"><span title="GEOr103: Guria">Guria</span></td>
									<td class="proper">75.79</td>
								</tr>
								<tr>
									<td class="region"><span title="GEOr104: Imereti Racha-Lochkhumi Kvemo Svaneti">Imereti Racha-Lochkhumi Kvemo Svaneti</span></td>
									<td class="proper">71.66</td>
								</tr>
								<tr>
									<td class="region"><span title="GEOr105: Kakheti">Kakheti</span></td>
									<td class="proper">60.25</td>
								</tr>
								<tr>
									<td class="region"><span title="GEOr106: Kvemo Kartli">Kvemo Kartli</span></td>
									<td class="proper">66.38</td>
								</tr>
								<tr>
									<td class="region"><span title="GEOr107: Mtskheta-Mtianeti">Mtskheta-Mtianeti</span></td>
									<td class="proper">70.41</td>
								</tr>
								<tr>
									<td class="region"><span title="GEOr108: Samegrelo-Zemo Svateni">Samegrelo-Zemo Svateni</span></td>
									<td class="proper">71.49</td>
								</tr>
								<tr>
									<td class="region"><span title="GEOr109: Samtskhe-Javakheti">Samtskhe-Javakheti</span></td>
									<td class="proper">73.49</td>
								</tr>
								<tr>
									<td class="region"><span title="GEOr110: Shida Kartli">Shida Kartli</span></td>
									<td class="proper">70.96</td>
								</tr>
								<tr>
									<td class="region"><span title="GEOr111: Tbilisi">Tbilisi</span></td>
									<td class="proper">65.48</td>
								</tr>
								<tr class="country">
									<th>Germany (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="DEUt: Total">Total</span></td>
									<td class="proper">71.44</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="DEUr101: Baden-Wurttemberg">Baden-Wurttemberg</span></td>
									<td class="proper">70.26</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr102: Bayern">Bayern</span></td>
									<td class="proper">71.16</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr103: Berlin">Berlin</span></td>
									<td class="proper">68.38</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr104: Brandenburg">Brandenburg</span></td>
									<td class="proper">69.60</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr105: Bremen">Bremen</span></td>
									<td class="proper">75.12</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr106: Hamburg">Hamburg</span></td>
									<td class="proper">73.61</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr107: Hessen">Hessen</span></td>
									<td class="proper">70.01</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr108: Mecklenburg-Vorpommern">Mecklenburg-Vorpommern</span></td>
									<td class="proper">75.37</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr109: Niedersachsen">Niedersachsen</span></td>
									<td class="proper">72.72</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr110: Nordrhein-Westfalen">Nordrhein-Westfalen</span></td>
									<td class="proper">71.34</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr111: Rheinland-Pfalz">Rheinland-Pfalz</span></td>
									<td class="proper">69.63</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr112: Saarland">Saarland</span></td>
									<td class="proper">69.38</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr113: Sachsen">Sachsen</span></td>
									<td class="proper">69.98</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr114: Sachsen-Anhalt">Sachsen-Anhalt</span></td>
									<td class="proper">68.91</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr115: Schleswig-Holstein">Schleswig-Holstein</span></td>
									<td class="proper">77.51</td>
								</tr>
								<tr>
									<td class="region"><span title="DEUr116: Thuringen">Thuringen</span></td>
									<td class="proper">70.07</td>
								</tr>
								<tr class="country">
									<th>Ghana (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GHAt: Total">Total</span></td>
									<td class="proper">69.17</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="GHAr106: Ashanti">Ashanti</span></td>
									<td class="proper">72.81</td>
								</tr>
								<tr>
									<td class="region"><span title="GHAr107: Brong Ahafo">Brong Ahafo</span></td>
									<td class="proper">65.67</td>
								</tr>
								<tr>
									<td class="region"><span title="GHAr102: Central">Central</span></td>
									<td class="proper">82.65</td>
								</tr>
								<tr>
									<td class="region"><span title="GHAr105: Eastern">Eastern</span></td>
									<td class="proper">76.85</td>
								</tr>
								<tr>
									<td class="region"><span title="GHAr103: Greater Accra">Greater Accra</span></td>
									<td class="proper">81.11</td>
								</tr>
								<tr>
									<td class="region"><span title="GHAr108: Northern">Northern</span></td>
									<td class="proper">56.45</td>
								</tr>
								<tr>
									<td class="region"><span title="GHAr110: Upper East">Upper East</span></td>
									<td class="proper">48.67</td>
								</tr>
								<tr>
									<td class="region"><span title="GHAr109: Upper West">Upper West</span></td>
									<td class="proper">50.83</td>
								</tr>
								<tr>
									<td class="region"><span title="GHAr104: Volta">Volta</span></td>
									<td class="proper">74.41</td>
								</tr>
								<tr>
									<td class="region"><span title="GHAr101: Western">Western</span></td>
									<td class="proper">82.22</td>
								</tr>
								<tr class="country">
									<th>Gibraltar (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GIBt: Total">Total</span></td>
									<td class="proper">77.06</td>
								</tr>
								<tr class="country">
									<th>Greece (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GRCt: Total">Total</span></td>
									<td class="proper">66.08</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="GRCr105: Anatoliki Makedonia, Thraki">Anatoliki Makedonia, Thraki</span></td>
									<td class="proper">65.95</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr101: Attiki">Attiki</span></td>
									<td class="proper">60.70</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr111: Dytiki Ellada">Dytiki Ellada</span></td>
									<td class="proper">66.82</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr107: Dytiki Makedonia">Dytiki Makedonia</span></td>
									<td class="proper">60.56</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr110: Ionia Nisia">Ionia Nisia</span></td>
									<td class="proper">73.93</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr108: Ipeiros">Ipeiros</span></td>
									<td class="proper">67.63</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr106: Kentriki Makedonia">Kentriki Makedonia</span></td>
									<td class="proper">63.88</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr104: Kriti">Kriti</span></td>
									<td class="proper">68.88</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr103: Notio Aigaio">Notio Aigaio</span></td>
									<td class="proper">68.10</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr113: Peloponnisos">Peloponnisos</span></td>
									<td class="proper">62.24</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr112: Sterea Ellada">Sterea Ellada</span></td>
									<td class="proper">64.10</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr109: Thessalia">Thessalia</span></td>
									<td class="proper">62.88</td>
								</tr>
								<tr>
									<td class="region"><span title="GRCr102: Voreio Aigaio">Voreio Aigaio</span></td>
									<td class="proper">73.41</td>
								</tr>
								<tr class="country">
									<th>Greenland (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GRLt: Total">Total</span></td>
									<td class="proper">71.57</td>
								</tr>
								<tr class="country">
									<th>Grenada (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GRDt: Total">Total</span></td>
									<td class="proper">80.10</td>
								</tr>
								<tr class="country">
									<th>Guatemala (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GTMt: Total">Total</span></td>
									<td class="proper">77.07</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="GTMr105: Central">Central</span></td>
									<td class="proper">76.25</td>
								</tr>
								<tr>
									<td class="region"><span title="GTMr101: Metropolitan">Metropolitan</span></td>
									<td class="proper">70.45</td>
								</tr>
								<tr>
									<td class="region"><span title="GTMr102: North">North</span></td>
									<td class="proper">82.43</td>
								</tr>
								<tr>
									<td class="region"><span title="GTMr107: North-Occidental">North-Occidental</span></td>
									<td class="proper">79.26</td>
								</tr>
								<tr>
									<td class="region"><span title="GTMr103: North-Oriental">North-Oriental</span></td>
									<td class="proper">81.72</td>
								</tr>
								<tr>
									<td class="region"><span title="GTMr108: Peten">Peten</span></td>
									<td class="proper">75.34</td>
								</tr>
								<tr>
									<td class="region"><span title="GTMr106: South-Occidental">South-Occidental</span></td>
									<td class="proper">78.45</td>
								</tr>
								<tr>
									<td class="region"><span title="GTMr104: South-Oriental">South-Oriental</span></td>
									<td class="proper">72.70</td>
								</tr>
								<tr class="country">
									<th>Guinea (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GINt: Total">Total</span></td>
									<td class="proper">63.62</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="GINr101: Boke">Boke</span></td>
									<td class="proper">65.20</td>
								</tr>
								<tr>
									<td class="region"><span title="GINr102: Conakry">Conakry</span></td>
									<td class="proper">80.74</td>
								</tr>
								<tr>
									<td class="region"><span title="GINr103: Faranah">Faranah</span></td>
									<td class="proper">55.47</td>
								</tr>
								<tr>
									<td class="region"><span title="GINr104: Kankan">Kankan</span></td>
									<td class="proper">54.73</td>
								</tr>
								<tr>
									<td class="region"><span title="GINr105: Kindia">Kindia</span></td>
									<td class="proper">71.48</td>
								</tr>
								<tr>
									<td class="region"><span title="GINr106: Labe">Labe</span></td>
									<td class="proper">52.85</td>
								</tr>
								<tr>
									<td class="region"><span title="GINr107: Mamou">Mamou</span></td>
									<td class="proper">59.58</td>
								</tr>
								<tr>
									<td class="region"><span title="GINr108: N Zerekore">N Zerekore</span></td>
									<td class="proper">68.95</td>
								</tr>
								<tr class="country">
									<th>Guinea-Bissau (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GNBt: Total">Total</span></td>
									<td class="proper">64.98</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="GNBr106: Bafata">Bafata</span></td>
									<td class="proper">58.60</td>
								</tr>
								<tr>
									<td class="region"><span title="GNBr104: Biombo">Biombo</span></td>
									<td class="proper">68.17</td>
								</tr>
								<tr>
									<td class="region"><span title="GNBr109: Bissau">Bissau</span></td>
									<td class="proper">67.97</td>
								</tr>
								<tr>
									<td class="region"><span title="GNBr105: Bolama">Bolama</span></td>
									<td class="proper">73.28</td>
								</tr>
								<tr>
									<td class="region"><span title="GNBr108: Cacheu">Cacheu</span></td>
									<td class="proper">64.89</td>
								</tr>
								<tr>
									<td class="region"><span title="GNBr107: Gabu">Gabu</span></td>
									<td class="proper">57.05</td>
								</tr>
								<tr>
									<td class="region"><span title="GNBr103: Oio">Oio</span></td>
									<td class="proper">59.91</td>
								</tr>
								<tr>
									<td class="region"><span title="GNBr102: Quinara">Quinara</span></td>
									<td class="proper">65.87</td>
								</tr>
								<tr>
									<td class="region"><span title="GNBr101: Tombali">Tombali</span></td>
									<td class="proper">69.06</td>
								</tr>
								<tr class="country">
									<th>Guyana (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GUYt: Total">Total</span></td>
									<td class="proper">84.64</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="GUYr101: Barima-Waini">Barima-Waini</span></td>
									<td class="proper">86.76</td>
								</tr>
								<tr>
									<td class="region"><span title="GUYr107: Cuyuni-Mazaruni">Cuyuni-Mazaruni</span></td>
									<td class="proper">85.72</td>
								</tr>
								<tr>
									<td class="region"><span title="GUYr104: Demerara-Mahaica">Demerara-Mahaica</span></td>
									<td class="proper">84.90</td>
								</tr>
								<tr>
									<td class="region"><span title="GUYr106: East Berbice-Corentyne">East Berbice-Corentyne</span></td>
									<td class="proper">83.52</td>
								</tr>
								<tr>
									<td class="region"><span title="GUYr103: Essequibo Islands-West Demerara">Essequibo Islands-West Demerara</span></td>
									<td class="proper">86.13</td>
								</tr>
								<tr>
									<td class="region"><span title="GUYr105: Mahaica-Berbice">Mahaica-Berbice</span></td>
									<td class="proper">84.75</td>
								</tr>
								<tr>
									<td class="region"><span title="GUYr102: Pomeroon-Supenaam">Pomeroon-Supenaam</span></td>
									<td class="proper">86.12</td>
								</tr>
								<tr>
									<td class="region"><span title="GUYr108: Potaro-Siparuni">Potaro-Siparuni</span></td>
									<td class="proper">82.90</td>
								</tr>
								<tr>
									<td class="region"><span title="GUYr110: Upper Demerara-Berbice">Upper Demerara-Berbice</span></td>
									<td class="proper">84.99</td>
								</tr>
								<tr>
									<td class="region"><span title="GUYr109: Upper Takutu-Upper Essequibo">Upper Takutu-Upper Essequibo</span></td>
									<td class="proper">80.57</td>
								</tr>
								<tr class="country">
									<th>Haiti (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="HTIt: Total">Total</span></td>
									<td class="proper">78.05</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="HTIr105: Artibonite">Artibonite</span></td>
									<td class="proper">76.54</td>
								</tr>
								<tr>
									<td class="region"><span title="HTIr106: Centre">Centre</span></td>
									<td class="proper">72.31</td>
								</tr>
								<tr>
									<td class="region"><span title="HTIr108: Grande-Anse, Nippes">Grande-Anse, Nippes</span></td>
									<td class="proper">79.76</td>
								</tr>
								<tr>
									<td class="region"><span title="HTIr103: North">North</span></td>
									<td class="proper">82.40</td>
								</tr>
								<tr>
									<td class="region"><span title="HTIr104: North-East">North-East</span></td>
									<td class="proper">77.82</td>
								</tr>
								<tr>
									<td class="region"><span title="HTIr109: North-West">North-West</span></td>
									<td class="proper">76.58</td>
								</tr>
								<tr>
									<td class="region"><span title="HTIr107: South">South</span></td>
									<td class="proper">79.49</td>
								</tr>
								<tr>
									<td class="region"><span title="HTIr102: South-East">South-East</span></td>
									<td class="proper">79.80</td>
								</tr>
								<tr>
									<td class="region"><span title="HTIr101: West (incl Metropolitain area)">West (incl Metropolitain area)</span></td>
									<td class="proper">77.72</td>
								</tr>
								<tr class="country">
									<th>Honduras (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="HNDt: Total">Total</span></td>
									<td class="proper">77.97</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="HNDr101: Atlantida">Atlantida</span></td>
									<td class="proper">84.32</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr106: Choluteca">Choluteca</span></td>
									<td class="proper">67.83</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr102: Colon">Colon</span></td>
									<td class="proper">83.28</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr103: Comayagua">Comayagua</span></td>
									<td class="proper">77.51</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr104: Copan">Copan</span></td>
									<td class="proper">84.21</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr105: Cortes">Cortes</span></td>
									<td class="proper">83.29</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr107: El Paraiso">El Paraiso</span></td>
									<td class="proper">74.46</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr108: Francisco Morazan">Francisco Morazan</span></td>
									<td class="proper">71.04</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr109: Gracias a Dios">Gracias a Dios</span></td>
									<td class="proper">85.68</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr110: Intibuca">Intibuca</span></td>
									<td class="proper">75.03</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr111: Islas de la Bahia">Islas de la Bahia</span></td>
									<td class="proper">81.53</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr112: La Paz">La Paz</span></td>
									<td class="proper">71.66</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr113: Lempira">Lempira</span></td>
									<td class="proper">74.51</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr114: Ocotepeque">Ocotepeque</span></td>
									<td class="proper">79.54</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr115: Olancho">Olancho</span></td>
									<td class="proper">78.27</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr116: Santa Barbara">Santa Barbara</span></td>
									<td class="proper">82.79</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr117: Valle">Valle</span></td>
									<td class="proper">67.91</td>
								</tr>
								<tr>
									<td class="region"><span title="HNDr118: Yoro">Yoro</span></td>
									<td class="proper">80.63</td>
								</tr>
								<tr class="country">
									<th>Hungary (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="HUNt: Total">Total</span></td>
									<td class="proper">64.88</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="HUNr107: Del-Alfold">Del-Alfold</span></td>
									<td class="proper">65.02</td>
								</tr>
								<tr>
									<td class="region"><span title="HUNr104: Del-Dunantul">Del-Dunantul</span></td>
									<td class="proper">68.54</td>
								</tr>
								<tr>
									<td class="region"><span title="HUNr106: Eszak-Alfold">Eszak-Alfold</span></td>
									<td class="proper">61.37</td>
								</tr>
								<tr>
									<td class="region"><span title="HUNr105: Eszak-Magyarorszag">Eszak-Magyarorszag</span></td>
									<td class="proper">62.26</td>
								</tr>
								<tr>
									<td class="region"><span title="HUNr102: Kozep-Dunantul">Kozep-Dunantul</span></td>
									<td class="proper">67.36</td>
								</tr>
								<tr>
									<td class="region"><span title="HUNr101: Kozep-Magyarorszag">Kozep-Magyarorszag</span></td>
									<td class="proper">63.08</td>
								</tr>
								<tr>
									<td class="region"><span title="HUNr103: Nyugat-Dunantul">Nyugat-Dunantul</span></td>
									<td class="proper">66.55</td>
								</tr>
								<tr class="country">
									<th>Iceland (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ISLt: Total">Total</span></td>
									<td class="proper">83.18</td>
								</tr>
								<tr class="country">
									<th>India (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="INDt: Total">Total</span></td>
									<td class="proper">70.41</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="INDr136: Andaman and Nicobar Islands">Andaman and Nicobar Islands</span></td>
									<td class="proper">81.19</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr101: Andhra Pradesh">Andhra Pradesh</span></td>
									<td class="proper">68.26</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr125: Arunachal Pradesh">Arunachal Pradesh</span></td>
									<td class="proper">82.54</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr102: Assam">Assam</span></td>
									<td class="proper">80.27</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr103: Bihar">Bihar</span></td>
									<td class="proper">71.35</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr131: Chandigarth">Chandigarth</span></td>
									<td class="proper">59.71</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr129: Chhattisgarh">Chhattisgarh</span></td>
									<td class="proper">61.71</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr132: Dadra and Nagar Haveli">Dadra and Nagar Haveli</span></td>
									<td class="proper">68.43</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr134: Daman and Diu">Daman and Diu</span></td>
									<td class="proper">73.58</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr104: Goa">Goa</span></td>
									<td class="proper">77.09</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr105: Gujarat">Gujarat</span></td>
									<td class="proper">57.68</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr106: Haryana">Haryana</span></td>
									<td class="proper">59.41</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr107: Himachal Pradesh">Himachal Pradesh</span></td>
									<td class="proper">67.76</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr108: Jammu and Kashmir">Jammu and Kashmir</span></td>
									<td class="proper">65.48</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr128: Jharkhand">Jharkhand</span></td>
									<td class="proper">67.25</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr109: Karnataka">Karnataka</span></td>
									<td class="proper">66.38</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr110: Kerala">Kerala</span></td>
									<td class="proper">80.32</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr135: Lakshadweep">Lakshadweep</span></td>
									<td class="proper">78.60</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr111: Madhya Pradesh">Madhya Pradesh</span></td>
									<td class="proper">56.39</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr112: Maharashtra">Maharashtra</span></td>
									<td class="proper">59.55</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr113: Manipur">Manipur</span></td>
									<td class="proper">80.43</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr114: Meghalaya">Meghalaya</span></td>
									<td class="proper">82.16</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr115: Mizoram">Mizoram</span></td>
									<td class="proper">77.54</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr116: Nagaland">Nagaland</span></td>
									<td class="proper">82.10</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr124: New Delhi">New Delhi</span></td>
									<td class="proper">62.77</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr117: Orissa">Orissa</span></td>
									<td class="proper">70.66</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr133: Puducherry">Puducherry</span></td>
									<td class="proper">78.01</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr118: Punjab">Punjab</span></td>
									<td class="proper">64.03</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr119: Rajasthan">Rajasthan</span></td>
									<td class="proper">48.59</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr120: Sikkim">Sikkim</span></td>
									<td class="proper">82.07</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr121: Tamil Nadu">Tamil Nadu</span></td>
									<td class="proper">71.67</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr130: Telangana">Telangana</span></td>
									<td class="proper">62.81</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr126: Tripura">Tripura</span></td>
									<td class="proper">77.93</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr123: Uttar Pradesh">Uttar Pradesh</span></td>
									<td class="proper">65.68</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr127: Uttaranchal">Uttaranchal</span></td>
									<td class="proper">69.41</td>
								</tr>
								<tr>
									<td class="region"><span title="INDr122: West Bengal">West Bengal</span></td>
									<td class="proper">75.87</td>
								</tr>
								<tr class="country">
									<th>Indonesia (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="IDNt: Total">Total</span></td>
									<td class="proper">84.35</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="IDNr116: Bali">Bali</span></td>
									<td class="proper">85.68</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr109: Bangka Belitung">Bangka Belitung</span></td>
									<td class="proper">84.20</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr115: Banten">Banten</span></td>
									<td class="proper">83.70</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr107: Bengkulu">Bengkulu</span></td>
									<td class="proper">83.92</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr112: Central Java">Central Java</span></td>
									<td class="proper">83.65</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr121: Central Kalimantan">Central Kalimantan</span></td>
									<td class="proper">84.89</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr125: Central Sulawesi">Central Sulawesi</span></td>
									<td class="proper">84.91</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr101: DI Aceh">DI Aceh</span></td>
									<td class="proper">84.69</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr113: DI Yogyakarta">DI Yogyakarta</span></td>
									<td class="proper">84.48</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr110: DKI Jakarta">DKI Jakarta</span></td>
									<td class="proper">81.21</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr114: East Java">East Java</span></td>
									<td class="proper">83.34</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr123: East Kalimantan">East Kalimantan</span></td>
									<td class="proper">86.05</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr118: East Nusa Tenggara">East Nusa Tenggara</span></td>
									<td class="proper">80.51</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr128: Gorontalo">Gorontalo</span></td>
									<td class="proper">85.80</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr130: Irian Jaya (Papua and Papua Barat)">Irian Jaya (Papua and Papua Barat)</span></td>
									<td class="proper">84.62</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr105: Jambi">Jambi</span></td>
									<td class="proper">84.32</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr108: Lampung">Lampung</span></td>
									<td class="proper">84.21</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr129: Maluku">Maluku</span></td>
									<td class="proper">85.56</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr124: North Sulawesi">North Sulawesi</span></td>
									<td class="proper">86.36</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr102: North Sumatra">North Sumatra</span></td>
									<td class="proper">84.60</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr104: Riau (incl. Riau islands)">Riau (incl. Riau islands)</span></td>
									<td class="proper">85.18</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr122: South Kalimantan">South Kalimantan</span></td>
									<td class="proper">85.21</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr126: South Sulawesi (incl Sulawesi Barat)">South Sulawesi (incl Sulawesi Barat)</span></td>
									<td class="proper">83.28</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr106: South Sumatra">South Sumatra</span></td>
									<td class="proper">84.27</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr127: Southeast Sulawesi">Southeast Sulawesi</span></td>
									<td class="proper">84.25</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr111: West Java">West Java</span></td>
									<td class="proper">83.83</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr120: West Kalimantan">West Kalimantan</span></td>
									<td class="proper">86.52</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr117: West Nusa Tenggara">West Nusa Tenggara</span></td>
									<td class="proper">82.45</td>
								</tr>
								<tr>
									<td class="region"><span title="IDNr103: West Sumatra">West Sumatra</span></td>
									<td class="proper">84.59</td>
								</tr>
								<tr class="country">
									<th>Iran, Islamic Rep. (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="IRNt: Total">Total</span></td>
									<td class="proper">39.29</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="IRNr125: Ardebil">Ardebil</span></td>
									<td class="proper">61.66</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr119: Bushehr">Bushehr</span></td>
									<td class="proper">42.53</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr115: Chaharmahal and Bakhtiyari">Chaharmahal and Bakhtiyari</span></td>
									<td class="proper">36.26</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr104: EastAzarbayejan">EastAzarbayejan</span></td>
									<td class="proper">51.09</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr111: Esfahan">Esfahan</span></td>
									<td class="proper">24.63</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr108: Fars">Fars</span></td>
									<td class="proper">29.32</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr102: Gilan">Gilan</span></td>
									<td class="proper">74.48</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr128: Golestan">Golestan</span></td>
									<td class="proper">59.27</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr114: Hamedan">Hamedan</span></td>
									<td class="proper">32.25</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr123: Hormozgan">Hormozgan</span></td>
									<td class="proper">43.02</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr117: Ilam">Ilam</span></td>
									<td class="proper">31.96</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr109: Kerman">Kerman</span></td>
									<td class="proper">22.94</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr106: Kermanshah">Kermanshah</span></td>
									<td class="proper">35.94</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr110: Khorasan-e-Razavi">Khorasan-e-Razavi</span></td>
									<td class="proper">35.28</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr107: Khuzestan">Khuzestan</span></td>
									<td class="proper">32.44</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr118: Kohgiluyeh and Boyerahmad">Kohgiluyeh and Boyerahmad</span></td>
									<td class="proper">35.83</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr113: Kordestan">Kordestan</span></td>
									<td class="proper">38.53</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr116: Lorestan">Lorestan</span></td>
									<td class="proper">35.90</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr101: Markazi">Markazi</span></td>
									<td class="proper">30.56</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr103: Mazandaran">Mazandaran</span></td>
									<td class="proper">70.12</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr129: North Khorasan">North Khorasan</span></td>
									<td class="proper">49.15</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr127: Qazvin">Qazvin</span></td>
									<td class="proper">46.16</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr126: Qom">Qom</span></td>
									<td class="proper">27.91</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr121: Semnan">Semnan</span></td>
									<td class="proper">32.85</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr112: Sistanand Baluchestan">Sistanand Baluchestan</span></td>
									<td class="proper">27.31</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr130: South Khorasan">South Khorasan</span></td>
									<td class="proper">22.38</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr124: Tehran and Alborz">Tehran and Alborz</span></td>
									<td class="proper">36.38</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr105: WestAzarbayejan">WestAzarbayejan</span></td>
									<td class="proper">45.94</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr122: Yazd">Yazd</span></td>
									<td class="proper">19.61</td>
								</tr>
								<tr>
									<td class="region"><span title="IRNr120: Zanjan">Zanjan</span></td>
									<td class="proper">46.92</td>
								</tr>
								<tr class="country">
									<th>Iraq (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="IRQt: Total">Total</span></td>
									<td class="proper">30.44</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="IRQr107: Anbar">Anbar</span></td>
									<td class="proper">31.70</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr109: Babylon">Babylon</span></td>
									<td class="proper">28.05</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr108: Baghdad">Baghdad</span></td>
									<td class="proper">28.61</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr118: Basra">Basra</span></td>
									<td class="proper">27.91</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr106: Diala">Diala</span></td>
									<td class="proper">28.32</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr101: Dohouk">Dohouk</span></td>
									<td class="proper">40.92</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr105: Erbil">Erbil</span></td>
									<td class="proper">36.97</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr110: Kerbela">Kerbela</span></td>
									<td class="proper">33.23</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr117: Maysan">Maysan</span></td>
									<td class="proper">27.20</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr115: Muthanna">Muthanna</span></td>
									<td class="proper">25.70</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr113: Najaf">Najaf</span></td>
									<td class="proper">26.66</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr102: Nenava">Nenava</span></td>
									<td class="proper">34.16</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr114: Qadisiya">Qadisiya</span></td>
									<td class="proper">26.43</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr112: Salaheldeen">Salaheldeen</span></td>
									<td class="proper">32.35</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr103: Suleimaniya">Suleimaniya</span></td>
									<td class="proper">36.43</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr104: Ta-amem-Karkuk">Ta-amem-Karkuk</span></td>
									<td class="proper">30.46</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr116: Thi-Qar">Thi-Qar</span></td>
									<td class="proper">25.72</td>
								</tr>
								<tr>
									<td class="region"><span title="IRQr111: Wasit">Wasit</span></td>
									<td class="proper">27.16</td>
								</tr>
								<tr class="country">
									<th>Ireland (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="IRLt: Total">Total</span></td>
									<td class="proper">81.00</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="IRLr101: Border">Border</span></td>
									<td class="proper">81.79</td>
								</tr>
								<tr>
									<td class="region"><span title="IRLr104: Dublin">Dublin</span></td>
									<td class="proper">79.76</td>
								</tr>
								<tr>
									<td class="region"><span title="IRLr105: Mid-East">Mid-East</span></td>
									<td class="proper">80.24</td>
								</tr>
								<tr>
									<td class="region"><span title="IRLr106: Mid-West">Mid-West</span></td>
									<td class="proper">81.39</td>
								</tr>
								<tr>
									<td class="region"><span title="IRLr102: Midland">Midland</span></td>
									<td class="proper">80.48</td>
								</tr>
								<tr>
									<td class="region"><span title="IRLr107: South-East">South-East</span></td>
									<td class="proper">81.03</td>
								</tr>
								<tr>
									<td class="region"><span title="IRLr108: South-West">South-West</span></td>
									<td class="proper">81.80</td>
								</tr>
								<tr>
									<td class="region"><span title="IRLr103: West">West</span></td>
									<td class="proper">81.55</td>
								</tr>
								<tr class="country">
									<th>Isle of Man (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="IMNt: Total">Total</span></td>
									<td class="proper">80.88</td>
								</tr>
								<tr class="country">
									<th>Israel (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ISRt: Total">Total</span></td>
									<td class="proper">57.32</td>
								</tr>
								<tr class="country">
									<th>Italy (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ITAt: Total">Total</span></td>
									<td class="proper">68.57</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ITAr105: Abruzzo">Abruzzo</span></td>
									<td class="proper">68.62</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr109: Basilicata">Basilicata</span></td>
									<td class="proper">64.54</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr110: Calabria">Calabria</span></td>
									<td class="proper">71.55</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr107: Campania">Campania</span></td>
									<td class="proper">70.09</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr117: Emilia-Romagna">Emilia-Romagna</span></td>
									<td class="proper">69.02</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr116: Friuli-Venezia Giulia">Friuli-Venezia Giulia</span></td>
									<td class="proper">70.17</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr121: Lazio">Lazio</span></td>
									<td class="proper">67.82</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr103: Liguria">Liguria</span></td>
									<td class="proper">72.26</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr104: Lombardia">Lombardia</span></td>
									<td class="proper">66.63</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr120: Marche">Marche</span></td>
									<td class="proper">69.10</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr106: Molise">Molise</span></td>
									<td class="proper">68.60</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr101: Piemonte">Piemonte</span></td>
									<td class="proper">65.43</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr114: Provincia Autonoma di Trento">Provincia Autonoma di Trento</span></td>
									<td class="proper">68.71</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr108: Puglia">Puglia</span></td>
									<td class="proper">64.34</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr112: Sardegna">Sardegna</span></td>
									<td class="proper">68.09</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr111: Sicilia">Sicilia</span></td>
									<td class="proper">70.86</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr118: Toscana">Toscana</span></td>
									<td class="proper">71.35</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr119: Umbria">Umbria</span></td>
									<td class="proper">66.05</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr102: Valle dAosta">Valle dAosta</span></td>
									<td class="proper">67.79</td>
								</tr>
								<tr>
									<td class="region"><span title="ITAr115: Veneto">Veneto</span></td>
									<td class="proper">70.41</td>
								</tr>
								<tr class="country">
									<th>Jamaica (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="JAMt: Total">Total</span></td>
									<td class="proper">77.02</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="JAMr101: Kingston, St Andrew">Kingston, St Andrew</span></td>
									<td class="proper">78.84</td>
								</tr>
								<tr>
									<td class="region"><span title="JAMr106: Manchester, Clarendon">Manchester, Clarendon</span></td>
									<td class="proper">71.96</td>
								</tr>
								<tr>
									<td class="region"><span title="JAMr103: St Ann, St Catherine">St Ann, St Catherine</span></td>
									<td class="proper">76.96</td>
								</tr>
								<tr>
									<td class="region"><span title="JAMr105: St James, Hanover, Westmoreland">St James, Hanover, Westmoreland</span></td>
									<td class="proper">78.64</td>
								</tr>
								<tr>
									<td class="region"><span title="JAMr102: St Thomas, Portland, St Mary">St Thomas, Portland, St Mary</span></td>
									<td class="proper">80.92</td>
								</tr>
								<tr>
									<td class="region"><span title="JAMr104: Trelawny, St Elizabeth">Trelawny, St Elizabeth</span></td>
									<td class="proper">74.81</td>
								</tr>
								<tr class="country">
									<th>Japan (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="JPNt: Total">Total</span></td>
									<td class="proper">73.42</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="JPNr108: Chugoku (Tottori, Shimane, Okayama, Hiroshima, Yamaguchi)">Chugoku (Tottori, Shimane, Okayama, Hiroshima, Yamaguchi)</span></td>
									<td class="proper">71.38</td>
								</tr>
								<tr>
									<td class="region"><span title="JPNr101: Hokkaido">Hokkaido</span></td>
									<td class="proper">77.11</td>
								</tr>
								<tr>
									<td class="region"><span title="JPNr105: Hokuriku (Niigata, Toyama, Ishikawa, Fukui)">Hokuriku (Niigata, Toyama, Ishikawa, Fukui)</span></td>
									<td class="proper">76.74</td>
								</tr>
								<tr>
									<td class="region"><span title="JPNr107: Kansai region (Shiga, Kyoto, Osaka, Hyogo, Nara, Wakayama)">Kansai region (Shiga, Kyoto, Osaka, Hyogo, Nara, Wakayama)</span></td>
									<td class="proper">72.47</td>
								</tr>
								<tr>
									<td class="region"><span title="JPNr110: Kyushu (Fukuoka, Saga, Nagasaki, Kumamoto, Oita, Miyazaki, Kagoshima, Okinawa)">Kyushu (Fukuoka, Saga, Nagasaki, Kumamoto, Oita, Miyazaki, Kagoshima, Okinawa)</span></td>
									<td class="proper">73.42</td>
								</tr>
								<tr>
									<td class="region"><span title="JPNr103: Northern-Kanto, Koshin (Ibaraki, Tochigi, Gunma)">Northern-Kanto, Koshin (Ibaraki, Tochigi, Gunma)</span></td>
									<td class="proper">71.79</td>
								</tr>
								<tr>
									<td class="region"><span title="JPNr109: Shikoku (Tokushima, Kagawa, Ehime, Kochi)">Shikoku (Tokushima, Kagawa, Ehime, Kochi)</span></td>
									<td class="proper">72.07</td>
								</tr>
								<tr>
									<td class="region"><span title="JPNr104: Southern-Kanto (Saitama, Chiba, Tokyo, Kanagawa, Yamanashi, Nagano)">Southern-Kanto (Saitama, Chiba, Tokyo, Kanagawa, Yamanashi, Nagano)</span></td>
									<td class="proper">71.12</td>
								</tr>
								<tr>
									<td class="region"><span title="JPNr102: Tohoku (Aomori, Iwate, Miyagi, Akita, Yamagata, Fukushima)">Tohoku (Aomori, Iwate, Miyagi, Akita, Yamagata, Fukushima)</span></td>
									<td class="proper">76.60</td>
								</tr>
								<tr>
									<td class="region"><span title="JPNr106: Toukai (Gifu, Shizuoka, Aichi, Mie)">Toukai (Gifu, Shizuoka, Aichi, Mie)</span></td>
									<td class="proper">71.48</td>
								</tr>
								<tr class="country">
									<th>Jersey (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="JEYt: Total">Total</span></td>
									<td class="proper">79.87</td>
								</tr>
								<tr class="country">
									<th>Jordan (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="JORt: Total">Total</span></td>
									<td class="proper">47.09</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="JORr108: Aljoun">Aljoun</span></td>
									<td class="proper">53.83</td>
								</tr>
								<tr>
									<td class="region"><span title="JORr101: Amman">Amman</span></td>
									<td class="proper">44.84</td>
								</tr>
								<tr>
									<td class="region"><span title="JORr112: Aqaba">Aqaba</span></td>
									<td class="proper">42.46</td>
								</tr>
								<tr>
									<td class="region"><span title="JORr102: Balqa">Balqa</span></td>
									<td class="proper">52.72</td>
								</tr>
								<tr>
									<td class="region"><span title="JORr105: Irbid">Irbid</span></td>
									<td class="proper">56.99</td>
								</tr>
								<tr>
									<td class="region"><span title="JORr107: Jarash">Jarash</span></td>
									<td class="proper">53.32</td>
								</tr>
								<tr>
									<td class="region"><span title="JORr109: Karak">Karak</span></td>
									<td class="proper">48.58</td>
								</tr>
								<tr>
									<td class="region"><span title="JORr111: Maan">Maan</span></td>
									<td class="proper">37.29</td>
								</tr>
								<tr>
									<td class="region"><span title="JORr104: Madaba">Madaba</span></td>
									<td class="proper">51.85</td>
								</tr>
								<tr>
									<td class="region"><span title="JORr106: Mafraq">Mafraq</span></td>
									<td class="proper">35.84</td>
								</tr>
								<tr>
									<td class="region"><span title="JORr110: Tafiela">Tafiela</span></td>
									<td class="proper">46.65</td>
								</tr>
								<tr>
									<td class="region"><span title="JORr103: Zarqa">Zarqa</span></td>
									<td class="proper">40.73</td>
								</tr>
								<tr class="country">
									<th>Kazakhstan (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="KAZt: Total">Total</span></td>
									<td class="proper">53.63</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="KAZr101: Almaty city">Almaty city</span></td>
									<td class="proper">52.84</td>
								</tr>
								<tr>
									<td class="region"><span title="KAZr104: Central region (Karagandinskaya)">Central region (Karagandinskaya)</span></td>
									<td class="proper">52.55</td>
								</tr>
								<tr>
									<td class="region"><span title="KAZr106: East region (East-Kazakhstanskaya)">East region (East-Kazakhstanskaya)</span></td>
									<td class="proper">56.51</td>
								</tr>
								<tr>
									<td class="region"><span title="KAZr105: North region (Akmolinskaya (incl Astana city), Kostnaiskaya, Pavlodarskaya, North-Kazakhstanskaya)">North region (Akmolinskaya (incl Astana city), Kostnaiskaya, Pavlodarskaya, North-Kazakhstanskaya)</span></td>
									<td class="proper">59.44</td>
								</tr>
								<tr>
									<td class="region"><span title="KAZr102: South region (Almatinskaya, Zhambylskaya, Kyzylordinskaya, South-Kazakhstanskaya)">South region (Almatinskaya, Zhambylskaya, Kyzylordinskaya, South-Kazakhstanskaya)</span></td>
									<td class="proper">47.03</td>
								</tr>
								<tr>
									<td class="region"><span title="KAZr103: West region (Aktyubinskaya, Atyrauskaya, Mangistauskaya, West-Kazakhstanskaya)">West region (Aktyubinskaya, Atyrauskaya, Mangistauskaya, West-Kazakhstanskaya)</span></td>
									<td class="proper">53.44</td>
								</tr>
								<tr class="country">
									<th>Kenya (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="KENt: Total">Total</span></td>
									<td class="proper">62.82</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="KENr102: Central">Central</span></td>
									<td class="proper">71.43</td>
								</tr>
								<tr>
									<td class="region"><span title="KENr103: Coast">Coast</span></td>
									<td class="proper">66.96</td>
								</tr>
								<tr>
									<td class="region"><span title="KENr104: Eastern">Eastern</span></td>
									<td class="proper">52.33</td>
								</tr>
								<tr>
									<td class="region"><span title="KENr101: Nairobi">Nairobi</span></td>
									<td class="proper">64.18</td>
								</tr>
								<tr>
									<td class="region"><span title="KENr108: North Eastern">North Eastern</span></td>
									<td class="proper">54.01</td>
								</tr>
								<tr>
									<td class="region"><span title="KENr105: Nyanza">Nyanza</span></td>
									<td class="proper">71.37</td>
								</tr>
								<tr>
									<td class="region"><span title="KENr106: Rift Valley">Rift Valley</span></td>
									<td class="proper">52.65</td>
								</tr>
								<tr>
									<td class="region"><span title="KENr107: Western">Western</span></td>
									<td class="proper">69.63</td>
								</tr>
								<tr class="country">
									<th>Kiribati (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="KIRt: Total">Total</span></td>
									<td class="proper">78.92</td>
								</tr>
								<tr class="country">
									<th>Korea, Rep. (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="KORt: Total">Total</span></td>
									<td class="proper">66.00</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="KORr101: Capital Region">Capital Region</span></td>
									<td class="proper">67.30</td>
								</tr>
								<tr>
									<td class="region"><span title="KORr105: Chungcheong Region">Chungcheong Region</span></td>
									<td class="proper">65.90</td>
								</tr>
								<tr>
									<td class="region"><span title="KORr106: Gangwon Region">Gangwon Region</span></td>
									<td class="proper">64.81</td>
								</tr>
								<tr>
									<td class="region"><span title="KORr103: Gyeongbuk Region">Gyeongbuk Region</span></td>
									<td class="proper">60.45</td>
								</tr>
								<tr>
									<td class="region"><span title="KORr102: Gyeongnam Region">Gyeongnam Region</span></td>
									<td class="proper">61.57</td>
								</tr>
								<tr>
									<td class="region"><span title="KORr107: Jeju">Jeju</span></td>
									<td class="proper">73.76</td>
								</tr>
								<tr>
									<td class="region"><span title="KORr104: Jeolla Region">Jeolla Region</span></td>
									<td class="proper">68.23</td>
								</tr>
								<tr class="country">
									<th>Kosovo (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="XKOt: Total">Total</span></td>
									<td class="proper">67.23</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="KSVr107: Ferizaj">Ferizaj</span></td>
									<td class="proper">67.60</td>
								</tr>
								<tr>
									<td class="region"><span title="KSVr101: Gjakova">Gjakova</span></td>
									<td class="proper">67.36</td>
								</tr>
								<tr>
									<td class="region"><span title="KSVr102: Gjilan">Gjilan</span></td>
									<td class="proper">68.65</td>
								</tr>
								<tr>
									<td class="region"><span title="KSVr103: Mitrovica">Mitrovica</span></td>
									<td class="proper">66.46</td>
								</tr>
								<tr>
									<td class="region"><span title="KSVr104: Peja">Peja</span></td>
									<td class="proper">69.65</td>
								</tr>
								<tr>
									<td class="region"><span title="KSVr106: Pristina">Pristina</span></td>
									<td class="proper">65.08</td>
								</tr>
								<tr>
									<td class="region"><span title="KSVr105: Prizren">Prizren</span></td>
									<td class="proper">65.80</td>
								</tr>
								<tr class="country">
									<th>Kuwait (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="KWTt: Total">Total</span></td>
									<td class="proper">33.66</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="KWTr102: Ahmadi">Ahmadi</span></td>
									<td class="proper">29.98</td>
								</tr>
								<tr>
									<td class="region"><span title="KWTr101: Al Asimah, Hawalli, Al-Farwaniyah, Mubarak al-Sabah">Al Asimah, Hawalli, Al-Farwaniyah, Mubarak al-Sabah</span></td>
									<td class="proper">41.80</td>
								</tr>
								<tr>
									<td class="region"><span title="KWTr103: Al-Jahra">Al-Jahra</span></td>
									<td class="proper">29.19</td>
								</tr>
								<tr class="country">
									<th>Kyrgyz Republic (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="KGZt: Total">Total</span></td>
									<td class="proper">64.45</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="KGZr108: Batken">Batken</span></td>
									<td class="proper">63.35</td>
								</tr>
								<tr>
									<td class="region"><span title="KGZr101: Bishkek">Bishkek</span></td>
									<td class="proper">58.03</td>
								</tr>
								<tr>
									<td class="region"><span title="KGZr103: Chuy">Chuy</span></td>
									<td class="proper">66.08</td>
								</tr>
								<tr>
									<td class="region"><span title="KGZr102: Issyk-Kul">Issyk-Kul</span></td>
									<td class="proper">70.00</td>
								</tr>
								<tr>
									<td class="region"><span title="KGZr105: Jalal-Abad">Jalal-Abad</span></td>
									<td class="proper">63.58</td>
								</tr>
								<tr>
									<td class="region"><span title="KGZr107: Naryn">Naryn</span></td>
									<td class="proper">64.21</td>
								</tr>
								<tr>
									<td class="region"><span title="KGZr106: Osh">Osh</span></td>
									<td class="proper">64.30</td>
								</tr>
								<tr>
									<td class="region"><span title="KGZr104: Talas">Talas</span></td>
									<td class="proper">66.07</td>
								</tr>
								<tr class="country">
									<th>Lao PDR (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="LAOt: Total">Total</span></td>
									<td class="proper">80.13</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="LAOr117: Attapeu">Attapeu</span></td>
									<td class="proper">75.90</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr105: Bokeo">Bokeo</span></td>
									<td class="proper">78.82</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr111: Borikhamxay">Borikhamxay</span></td>
									<td class="proper">80.41</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr116: Champasack">Champasack</span></td>
									<td class="proper">78.48</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr107: Huaphanh">Huaphanh</span></td>
									<td class="proper">83.07</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr112: Khammuane">Khammuane</span></td>
									<td class="proper">80.10</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr103: Luangnamtha">Luangnamtha</span></td>
									<td class="proper">78.74</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr106: Luangprabang">Luangprabang</span></td>
									<td class="proper">81.36</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr104: Oudomxay">Oudomxay</span></td>
									<td class="proper">80.18</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr102: Phongsaly">Phongsaly</span></td>
									<td class="proper">81.76</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr114: Saravane">Saravane</span></td>
									<td class="proper">79.33</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr113: Savannakhet">Savannakhet</span></td>
									<td class="proper">78.29</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr108: Sayabury">Sayabury</span></td>
									<td class="proper">80.08</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr115: Sekong">Sekong</span></td>
									<td class="proper">81.82</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr101: Vientiane Municipality">Vientiane Municipality</span></td>
									<td class="proper">80.36</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr110: Vientiane Province">Vientiane Province</span></td>
									<td class="proper">80.47</td>
								</tr>
								<tr>
									<td class="region"><span title="LAOr109: Xiengkhuang">Xiengkhuang</span></td>
									<td class="proper">83.04</td>
								</tr>
								<tr class="country">
									<th>Latvia (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="LVAt: Total">Total</span></td>
									<td class="proper">77.14</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="LVAr104: Kurzeme region">Kurzeme region</span></td>
									<td class="proper">78.80</td>
								</tr>
								<tr>
									<td class="region"><span title="LVAr106: Latgale region">Latgale region</span></td>
									<td class="proper">75.92</td>
								</tr>
								<tr>
									<td class="region"><span title="LVAr101: Riga region">Riga region</span></td>
									<td class="proper">77.71</td>
								</tr>
								<tr>
									<td class="region"><span title="LVAr103: Vidzeme region">Vidzeme region</span></td>
									<td class="proper">77.22</td>
								</tr>
								<tr>
									<td class="region"><span title="LVAr105: Zemgale region">Zemgale region</span></td>
									<td class="proper">76.03</td>
								</tr>
								<tr class="country">
									<th>Lebanon (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="LBNt: Total">Total</span></td>
									<td class="proper">63.45</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="LBNr101: Beirut">Beirut</span></td>
									<td class="proper">67.20</td>
								</tr>
								<tr>
									<td class="region"><span title="LBNr104: Beqaa">Beqaa</span></td>
									<td class="proper">59.20</td>
								</tr>
								<tr>
									<td class="region"><span title="LBNr102: Mount Lebanon">Mount Lebanon</span></td>
									<td class="proper">64.51</td>
								</tr>
								<tr>
									<td class="region"><span title="LBNr103: Northern">Northern</span></td>
									<td class="proper">56.98</td>
								</tr>
								<tr>
									<td class="region"><span title="LBNr105: Southern, Nabtieh">Southern, Nabtieh</span></td>
									<td class="proper">69.36</td>
								</tr>
								<tr class="country">
									<th>Lesotho (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="LSOt: Total">Total</span></td>
									<td class="proper">59.81</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="LSOr103: Berea">Berea</span></td>
									<td class="proper">61.10</td>
								</tr>
								<tr>
									<td class="region"><span title="LSOr101: Butha-Buthe">Butha-Buthe</span></td>
									<td class="proper">61.39</td>
								</tr>
								<tr>
									<td class="region"><span title="LSOr102: Leribe">Leribe</span></td>
									<td class="proper">61.59</td>
								</tr>
								<tr>
									<td class="region"><span title="LSOr105: Mafeteng">Mafeteng</span></td>
									<td class="proper">59.32</td>
								</tr>
								<tr>
									<td class="region"><span title="LSOr104: Maseru">Maseru</span></td>
									<td class="proper">60.45</td>
								</tr>
								<tr>
									<td class="region"><span title="LSOr106: Mohale s Hoek">Mohale s Hoek</span></td>
									<td class="proper">59.85</td>
								</tr>
								<tr>
									<td class="region"><span title="LSOr109: Mokhotlong">Mokhotlong</span></td>
									<td class="proper">59.23</td>
								</tr>
								<tr>
									<td class="region"><span title="LSOr108: Qasha s Nek">Qasha s Nek</span></td>
									<td class="proper">57.45</td>
								</tr>
								<tr>
									<td class="region"><span title="LSOr107: Quthing">Quthing</span></td>
									<td class="proper">59.88</td>
								</tr>
								<tr>
									<td class="region"><span title="LSOr110: Thaba-Tseka">Thaba-Tseka</span></td>
									<td class="proper">57.85</td>
								</tr>
								<tr class="country">
									<th>Liberia (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="LBRt: Total">Total</span></td>
									<td class="proper">84.07</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="LBRr101: Bomi">Bomi</span></td>
									<td class="proper">87.15</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr102: Bong">Bong</span></td>
									<td class="proper">81.03</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr103: Gbarpolu">Gbarpolu</span></td>
									<td class="proper">81.13</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr104: Grand Bassa">Grand Bassa</span></td>
									<td class="proper">86.37</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr105: Grand Cape Mount">Grand Cape Mount</span></td>
									<td class="proper">85.66</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr106: Grand Gedeh">Grand Gedeh</span></td>
									<td class="proper">81.77</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr107: Grand Kru">Grand Kru</span></td>
									<td class="proper">86.16</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr108: Lofa">Lofa</span></td>
									<td class="proper">75.27</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr109: Margibi">Margibi</span></td>
									<td class="proper">86.04</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr110: Maryland">Maryland</span></td>
									<td class="proper">86.19</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr111: Montserrado">Montserrado</span></td>
									<td class="proper">86.90</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr112: Nimba">Nimba</span></td>
									<td class="proper">79.05</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr113: River Cess">River Cess</span></td>
									<td class="proper">86.53</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr114: River Gee">River Gee</span></td>
									<td class="proper">85.39</td>
								</tr>
								<tr>
									<td class="region"><span title="LBRr115: Sinoe">Sinoe</span></td>
									<td class="proper">86.41</td>
								</tr>
								<tr class="country">
									<th>Libya (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="LBYt: Total">Total</span></td>
									<td class="proper">34.93</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="LBYr101: Cyrenaica">Cyrenaica</span></td>
									<td class="proper">34.48</td>
								</tr>
								<tr>
									<td class="region"><span title="LBYr103: Fezzan">Fezzan</span></td>
									<td class="proper">27.38</td>
								</tr>
								<tr>
									<td class="region"><span title="LBYr102: Tripolitania">Tripolitania</span></td>
									<td class="proper">42.92</td>
								</tr>
								<tr class="country">
									<th>Liechtenstein (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="LIEt: Total">Total</span></td>
									<td class="proper">74.16</td>
								</tr>
								<tr class="country">
									<th>Lithuania (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="LTUt: Total">Total</span></td>
									<td class="proper">76.09</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="LTUr101: Alytus County">Alytus County</span></td>
									<td class="proper">75.35</td>
								</tr>
								<tr>
									<td class="region"><span title="LTUr102: Kaunas County">Kaunas County</span></td>
									<td class="proper">75.38</td>
								</tr>
								<tr>
									<td class="region"><span title="LTUr103: Klaipeda County">Klaipeda County</span></td>
									<td class="proper">77.28</td>
								</tr>
								<tr>
									<td class="region"><span title="LTUr104: Marijampole County">Marijampole County</span></td>
									<td class="proper">75.60</td>
								</tr>
								<tr>
									<td class="region"><span title="LTUr105: Panevezys County">Panevezys County</span></td>
									<td class="proper">74.82</td>
								</tr>
								<tr>
									<td class="region"><span title="LTUr106: Siauliai County">Siauliai County</span></td>
									<td class="proper">76.55</td>
								</tr>
								<tr>
									<td class="region"><span title="LTUr107: Taurage County">Taurage County</span></td>
									<td class="proper">77.23</td>
								</tr>
								<tr>
									<td class="region"><span title="LTUr108: Telsiai County">Telsiai County</span></td>
									<td class="proper">77.68</td>
								</tr>
								<tr>
									<td class="region"><span title="LTUr109: Utena County">Utena County</span></td>
									<td class="proper">75.59</td>
								</tr>
								<tr>
									<td class="region"><span title="LTUr110: Vilnius County">Vilnius County</span></td>
									<td class="proper">75.47</td>
								</tr>
								<tr class="country">
									<th>Luxembourg (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="LUXt: Total">Total</span></td>
									<td class="proper">72.46</td>
								</tr>
								<tr class="country">
									<th>Madagascar (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MDGt: Total">Total</span></td>
									<td class="proper">72.26</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MDGr112: Alaotra Mangoro">Alaotra Mangoro</span></td>
									<td class="proper">79.73</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr101: Analamanga">Analamanga</span></td>
									<td class="proper">74.39</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr111: Analanjirofo">Analanjirofo</span></td>
									<td class="proper">85.80</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr106: Anamoroni Mania">Anamoroni Mania</span></td>
									<td class="proper">72.10</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr118: Androy">Androy</span></td>
									<td class="proper">65.15</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr119: Anosy">Anosy</span></td>
									<td class="proper">69.57</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr117: Atsimo Andrefana">Atsimo Andrefana</span></td>
									<td class="proper">59.11</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr109: Atsimo Atsinanana">Atsimo Atsinanana</span></td>
									<td class="proper">82.46</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr110: Atsinanana">Atsinanana</span></td>
									<td class="proper">84.63</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr115: Betsiboka">Betsiboka</span></td>
									<td class="proper">64.23</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr113: Boeny">Boeny</span></td>
									<td class="proper">63.14</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr104: Bongolava">Bongolava</span></td>
									<td class="proper">65.73</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr121: Diana">Diana</span></td>
									<td class="proper">72.93</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr105: Haute Matsiatra">Haute Matsiatra</span></td>
									<td class="proper">71.47</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr108: Ihorombe">Ihorombe</span></td>
									<td class="proper">72.24</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr103: Itasy">Itasy</span></td>
									<td class="proper">69.39</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr116: Melaky">Melaky</span></td>
									<td class="proper">69.26</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr120: Menabe">Menabe</span></td>
									<td class="proper">63.46</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr122: Sava">Sava</span></td>
									<td class="proper">80.15</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr114: Sofia">Sofia</span></td>
									<td class="proper">69.58</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr102: Vakinankaratra">Vakinankaratra</span></td>
									<td class="proper">71.77</td>
								</tr>
								<tr>
									<td class="region"><span title="MDGr107: Vatovavy Fitovinany">Vatovavy Fitovinany</span></td>
									<td class="proper">83.35</td>
								</tr>
								<tr class="country">
									<th>Malawi (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MWIt: Total">Total</span></td>
									<td class="proper">69.09</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MWIr101: Blantyre">Blantyre</span></td>
									<td class="proper">70.96</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr102: Kasungu">Kasungu</span></td>
									<td class="proper">64.70</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr114: Likoma">Likoma</span></td>
									<td class="proper">70.03</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr109: Lilongwe">Lilongwe</span></td>
									<td class="proper">65.78</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr103: Machinga">Machinga</span></td>
									<td class="proper">67.97</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr104: Mangochi">Mangochi</span></td>
									<td class="proper">67.29</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr110: Mulanje">Mulanje</span></td>
									<td class="proper">72.52</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr105: Mzimba">Mzimba</span></td>
									<td class="proper">69.29</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr112: Other central (Nkhota Kota, Mchinji, Dowa, Ntchisi, Dedza, Ntcheu)">Other central (Nkhota Kota, Mchinji, Dowa, Ntchisi, Dedza, Ntcheu)</span></td>
									<td class="proper">68.21</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr111: Other northern (Chitipa, Karonga, Rumphi, Nkhata Bay)">Other northern (Chitipa, Karonga, Rumphi, Nkhata Bay)</span></td>
									<td class="proper">72.31</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr113: Other southern (Balaka, Mwanza, Phalombe, Chiradzulu, Chikwawa, Nsanje, neno)">Other southern (Balaka, Mwanza, Phalombe, Chiradzulu, Chikwawa, Nsanje, neno)</span></td>
									<td class="proper">68.72</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr106: Salima">Salima</span></td>
									<td class="proper">67.92</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr107: Thyolo">Thyolo</span></td>
									<td class="proper">72.67</td>
								</tr>
								<tr>
									<td class="region"><span title="MWIr108: Zomba">Zomba</span></td>
									<td class="proper">68.89</td>
								</tr>
								<tr class="country">
									<th>Malaysia (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MYSt: Total">Total</span></td>
									<td class="proper">82.86</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MYSr101: Johor">Johor</span></td>
									<td class="proper">83.83</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr102: Kedah">Kedah</span></td>
									<td class="proper">82.52</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr103: Kelantan">Kelantan</span></td>
									<td class="proper">84.58</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr114: Kuala Lumpur Federal Territory">Kuala Lumpur Federal Territory</span></td>
									<td class="proper">82.38</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr115: Labuan Federal Territory">Labuan Federal Territory</span></td>
									<td class="proper">80.51</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr104: Melaka">Melaka</span></td>
									<td class="proper">79.70</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr105: Negeri Sembilan">Negeri Sembilan</span></td>
									<td class="proper">81.71</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr106: Pahang">Pahang</span></td>
									<td class="proper">82.52</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr108: Perak">Perak</span></td>
									<td class="proper">82.24</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr109: Perlis">Perlis</span></td>
									<td class="proper">81.63</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr107: Pulau Pinang">Pulau Pinang</span></td>
									<td class="proper">81.21</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr112: Sabah">Sabah</span></td>
									<td class="proper">86.93</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr113: Sarawak">Sarawak</span></td>
									<td class="proper">86.89</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr110: Selangor">Selangor</span></td>
									<td class="proper">80.47</td>
								</tr>
								<tr>
									<td class="region"><span title="MYSr111: Terengganu">Terengganu</span></td>
									<td class="proper">85.80</td>
								</tr>
								<tr class="country">
									<th>Mali (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MLIt: Total">Total</span></td>
									<td class="proper">34.38</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MLIr108: Bamako">Bamako</span></td>
									<td class="proper">44.35</td>
								</tr>
								<tr>
									<td class="region"><span title="MLIr107: Gao and Kidal">Gao and Kidal</span></td>
									<td class="proper">16.87</td>
								</tr>
								<tr>
									<td class="region"><span title="MLIr101: Kayes">Kayes</span></td>
									<td class="proper">38.65</td>
								</tr>
								<tr>
									<td class="region"><span title="MLIr102: Koulikoro">Koulikoro</span></td>
									<td class="proper">39.02</td>
								</tr>
								<tr>
									<td class="region"><span title="MLIr105: Mopti">Mopti</span></td>
									<td class="proper">31.14</td>
								</tr>
								<tr>
									<td class="region"><span title="MLIr104: Segou">Segou</span></td>
									<td class="proper">36.87</td>
								</tr>
								<tr>
									<td class="region"><span title="MLIr103: Sikasso">Sikasso</span></td>
									<td class="proper">49.90</td>
								</tr>
								<tr>
									<td class="region"><span title="MLIr106: Tombouctou">Tombouctou</span></td>
									<td class="proper">18.26</td>
								</tr>
								<tr class="country">
									<th>Mauritania (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MRTt: Total">Total</span></td>
									<td class="proper">28.26</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MRTr107: Adrar">Adrar</span></td>
									<td class="proper">21.18</td>
								</tr>
								<tr>
									<td class="region"><span title="MRTr103: Assaba">Assaba</span></td>
									<td class="proper">28.00</td>
								</tr>
								<tr>
									<td class="region"><span title="MRTr105: Brakna">Brakna</span></td>
									<td class="proper">29.05</td>
								</tr>
								<tr>
									<td class="region"><span title="MRTr104: Gorgol">Gorgol</span></td>
									<td class="proper">31.88</td>
								</tr>
								<tr>
									<td class="region"><span title="MRTr110: Guidimagha">Guidimagha</span></td>
									<td class="proper">33.60</td>
								</tr>
								<tr>
									<td class="region"><span title="MRTr101: Hodh Charghi">Hodh Charghi</span></td>
									<td class="proper">22.02</td>
								</tr>
								<tr>
									<td class="region"><span title="MRTr102: Hodh Gharbi">Hodh Gharbi</span></td>
									<td class="proper">26.01</td>
								</tr>
								<tr>
									<td class="region"><span title="MRTr112: Inchiri">Inchiri</span></td>
									<td class="proper">29.72</td>
								</tr>
								<tr>
									<td class="region"><span title="MRTr108: Nouadhibou">Nouadhibou</span></td>
									<td class="proper">37.72</td>
								</tr>
								<tr>
									<td class="region"><span title="MRTr109: Tagant">Tagant</span></td>
									<td class="proper">23.26</td>
								</tr>
								<tr>
									<td class="region"><span title="MRTr111: Tiris-Zemmour">Tiris-Zemmour</span></td>
									<td class="proper">22.08</td>
								</tr>
								<tr>
									<td class="region"><span title="MRTr106: Trarza incl Nouakchott">Trarza incl Nouakchott</span></td>
									<td class="proper">34.61</td>
								</tr>
								<tr class="country">
									<th>Mauritius (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MUSt: Total">Total</span></td>
									<td class="proper">76.80</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MUSr104: Agalega Islands, Saint Brandon">Agalega Islands, Saint Brandon</span></td>
									<td class="proper">79.09</td>
								</tr>
								<tr>
									<td class="region"><span title="MUSr101: North (Port Louis, Pamplemousses, Riviere du Rempart, Flacq, Moka)">North (Port Louis, Pamplemousses, Riviere du Rempart, Flacq, Moka)</span></td>
									<td class="proper">76.54</td>
								</tr>
								<tr>
									<td class="region"><span title="MUSr103: Rodrigues">Rodrigues</span></td>
									<td class="proper">75.13</td>
								</tr>
								<tr>
									<td class="region"><span title="MUSr102: South (Grand Port, Savanne, Plaines Wilhems, Black River)">South (Grand Port, Savanne, Plaines Wilhems, Black River)</span></td>
									<td class="proper">76.43</td>
								</tr>
								<tr class="country">
									<th>Mexico (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MEXt: Total">Total</span></td>
									<td class="proper">60.92</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MEXr101: Aguascalientes">Aguascalientes</span></td>
									<td class="proper">43.16</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr102: Baja California">Baja California</span></td>
									<td class="proper">42.45</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr103: Baja California Sur">Baja California Sur</span></td>
									<td class="proper">53.08</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr104: Campeche">Campeche</span></td>
									<td class="proper">69.97</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr107: Chiapas">Chiapas</span></td>
									<td class="proper">77.82</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr108: Chihuahua">Chihuahua</span></td>
									<td class="proper">74.48</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr105: Coahuila">Coahuila</span></td>
									<td class="proper">44.71</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr106: Colima">Colima</span></td>
									<td class="proper">41.32</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr109: Distrito Federal">Distrito Federal</span></td>
									<td class="proper">63.47</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr110: Durango">Durango</span></td>
									<td class="proper">46.24</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr111: Guanajuato">Guanajuato</span></td>
									<td class="proper">51.47</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr112: Guerrero">Guerrero</span></td>
									<td class="proper">65.72</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr113: Hidalgo">Hidalgo</span></td>
									<td class="proper">71.22</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr114: Jalisco">Jalisco</span></td>
									<td class="proper">57.56</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr115: Mexico">Mexico</span></td>
									<td class="proper">61.23</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr116: Michoacan de Ocampo">Michoacan de Ocampo</span></td>
									<td class="proper">61.39</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr117: Morelos">Morelos</span></td>
									<td class="proper">54.68</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr118: Nayarit">Nayarit</span></td>
									<td class="proper">67.91</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr119: Nuevo Leon">Nuevo Leon</span></td>
									<td class="proper">56.62</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr120: Oaxaca">Oaxaca</span></td>
									<td class="proper">72.24</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr121: Puebla">Puebla</span></td>
									<td class="proper">64.68</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr122: Queretaro">Queretaro</span></td>
									<td class="proper">61.87</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr123: Quintana Roo">Quintana Roo</span></td>
									<td class="proper">78.47</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr124: San Luis Potosi">San Luis Potosi</span></td>
									<td class="proper">57.82</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr125: Sinaloa">Sinaloa</span></td>
									<td class="proper">64.69</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr126: Sonora">Sonora</span></td>
									<td class="proper">42.85</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr127: Tabasco">Tabasco</span></td>
									<td class="proper">78.52</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr128: Tamaulipas">Tamaulipas</span></td>
									<td class="proper">65.80</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr129: Tlaxcala">Tlaxcala</span></td>
									<td class="proper">63.18</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr130: Veracruz">Veracruz</span></td>
									<td class="proper">78.65</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr131: Yucatan">Yucatan</span></td>
									<td class="proper">73.81</td>
								</tr>
								<tr>
									<td class="region"><span title="MEXr132: Zacatecas">Zacatecas</span></td>
									<td class="proper">42.52</td>
								</tr>
								<tr class="country">
									<th>Micronesia, Fed. Sts. (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="FSMt: Total">Total</span></td>
									<td class="proper">82.37</td>
								</tr>
								<tr class="country">
									<th>Moldova (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MDAt: Total">Total</span></td>
									<td class="proper">63.88</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MDAr102: Center">Center</span></td>
									<td class="proper">64.96</td>
								</tr>
								<tr>
									<td class="region"><span title="MDAr104: Chisinau">Chisinau</span></td>
									<td class="proper">63.98</td>
								</tr>
								<tr>
									<td class="region"><span title="MDAr101: North">North</span></td>
									<td class="proper">64.97</td>
								</tr>
								<tr>
									<td class="region"><span title="MDAr103: South">South</span></td>
									<td class="proper">61.61</td>
								</tr>
								<tr class="country">
									<th>Monaco (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MCOt: Total">Total</span></td>
									<td class="proper">72.33</td>
								</tr>
								<tr class="country">
									<th>Mongolia (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MNGt: Total">Total</span></td>
									<td class="proper">46.79</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MNGr103: Central (Dornogovi, Dundgovi, Umnugovi, Selenge, Tuv, Darkhan-Uul, Govisumber)">Central (Dornogovi, Dundgovi, Umnugovi, Selenge, Tuv, Darkhan-Uul, Govisumber)</span></td>
									<td class="proper">38.69</td>
								</tr>
								<tr>
									<td class="region"><span title="MNGr104: Eastern (Dornod, Sukhbaatar, Khentii)">Eastern (Dornod, Sukhbaatar, Khentii)</span></td>
									<td class="proper">51.30</td>
								</tr>
								<tr>
									<td class="region"><span title="MNGr102: Khangai (Arkhangai, Bayankhongor, Bulgan, Uvurkhangai, Khuvsgul, Orkhon)">Khangai (Arkhangai, Bayankhongor, Bulgan, Uvurkhangai, Khuvsgul, Orkhon)</span></td>
									<td class="proper">45.75</td>
								</tr>
								<tr>
									<td class="region"><span title="MNGr105: Ulaanbaatar">Ulaanbaatar</span></td>
									<td class="proper">56.18</td>
								</tr>
								<tr>
									<td class="region"><span title="MNGr101: Western (Bayan-Ulgii, Govi-Altai, Zavkhan, Uvs, Khovd)">Western (Bayan-Ulgii, Govi-Altai, Zavkhan, Uvs, Khovd)</span></td>
									<td class="proper">42.05</td>
								</tr>
								<tr class="country">
									<th>Montenegro (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MNEt: Total">Total</span></td>
									<td class="proper">69.00</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MNEr102: Centre">Centre</span></td>
									<td class="proper">67.15</td>
								</tr>
								<tr>
									<td class="region"><span title="MNEr101: North">North</span></td>
									<td class="proper">71.40</td>
								</tr>
								<tr>
									<td class="region"><span title="MNEr103: South">South</span></td>
									<td class="proper">68.44</td>
								</tr>
								<tr class="country">
									<th>Morocco (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MARt: Total">Total</span></td>
									<td class="proper">46.34</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MARr103: Centre">Centre</span></td>
									<td class="proper">50.24</td>
								</tr>
								<tr>
									<td class="region"><span title="MARr102: Centre north">Centre north</span></td>
									<td class="proper">47.18</td>
								</tr>
								<tr>
									<td class="region"><span title="MARr105: Centre south">Centre south</span></td>
									<td class="proper">30.88</td>
								</tr>
								<tr>
									<td class="region"><span title="MARr104: Eastern">Eastern</span></td>
									<td class="proper">38.46</td>
								</tr>
								<tr>
									<td class="region"><span title="MARr101: North west">North west</span></td>
									<td class="proper">66.79</td>
								</tr>
								<tr>
									<td class="region"><span title="MARr107: South">South</span></td>
									<td class="proper">36.32</td>
								</tr>
								<tr>
									<td class="region"><span title="MARr106: Tensift">Tensift</span></td>
									<td class="proper">54.48</td>
								</tr>
								<tr class="country">
									<th>Mozambique (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MOZt: Total">Total</span></td>
									<td class="proper">68.94</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MOZr102: Cabo delgado">Cabo delgado</span></td>
									<td class="proper">69.85</td>
								</tr>
								<tr>
									<td class="region"><span title="MOZr109: Gaza">Gaza</span></td>
									<td class="proper">62.11</td>
								</tr>
								<tr>
									<td class="region"><span title="MOZr108: Inhambane">Inhambane</span></td>
									<td class="proper">69.54</td>
								</tr>
								<tr>
									<td class="region"><span title="MOZr106: Manica">Manica</span></td>
									<td class="proper">67.95</td>
								</tr>
								<tr>
									<td class="region"><span title="MOZr111: Maputo Cidade">Maputo Cidade</span></td>
									<td class="proper">74.30</td>
								</tr>
								<tr>
									<td class="region"><span title="MOZr110: Maputo Provincia">Maputo Provincia</span></td>
									<td class="proper">69.87</td>
								</tr>
								<tr>
									<td class="region"><span title="MOZr103: Nampula">Nampula</span></td>
									<td class="proper">71.42</td>
								</tr>
								<tr>
									<td class="region"><span title="MOZr101: Niassa">Niassa</span></td>
									<td class="proper">65.67</td>
								</tr>
								<tr>
									<td class="region"><span title="MOZr107: Sofala">Sofala</span></td>
									<td class="proper">72.55</td>
								</tr>
								<tr>
									<td class="region"><span title="MOZr105: Tete">Tete</span></td>
									<td class="proper">61.93</td>
								</tr>
								<tr>
									<td class="region"><span title="MOZr104: Zambezia">Zambezia</span></td>
									<td class="proper">73.09</td>
								</tr>
								<tr class="country">
									<th>Myanmar (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MMRt: Total">Total</span></td>
									<td class="proper">77.18</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MMRr114: Ayeyarwaddy">Ayeyarwaddy</span></td>
									<td class="proper">78.60</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr107: Bago">Bago</span></td>
									<td class="proper">76.91</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr104: Chin">Chin</span></td>
									<td class="proper">75.00</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr101: Kachin">Kachin</span></td>
									<td class="proper">80.65</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr102: Kayah">Kayah</span></td>
									<td class="proper">77.87</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr103: Kayin">Kayin</span></td>
									<td class="proper">80.92</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr108: Magway">Magway</span></td>
									<td class="proper">70.43</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr109: Mandalay, NayPyitaw">Mandalay, NayPyitaw</span></td>
									<td class="proper">69.87</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr110: Mon">Mon</span></td>
									<td class="proper">81.71</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr111: Rakhine">Rakhine</span></td>
									<td class="proper">78.22</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr105: Sagaing">Sagaing</span></td>
									<td class="proper">74.96</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr113: Shan">Shan</span></td>
									<td class="proper">75.28</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr106: Taninthayi">Taninthayi</span></td>
									<td class="proper">82.88</td>
								</tr>
								<tr>
									<td class="region"><span title="MMRr112: Yangon">Yangon</span></td>
									<td class="proper">77.16</td>
								</tr>
								<tr class="country">
									<th>Namibia (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="NAMt: Total">Total</span></td>
									<td class="proper">36.83</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="NAMr101: Caprivi">Caprivi</span></td>
									<td class="proper">48.69</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr102: Erongo">Erongo</span></td>
									<td class="proper">39.89</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr103: Hardap">Hardap</span></td>
									<td class="proper">31.99</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr104: Karas">Karas</span></td>
									<td class="proper">36.64</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr108: Kavango">Kavango</span></td>
									<td class="proper">43.62</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr105: Khomas">Khomas</span></td>
									<td class="proper">31.33</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr106: Kunene">Kunene</span></td>
									<td class="proper">38.38</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr107: Ohangwena">Ohangwena</span></td>
									<td class="proper">35.65</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr109: Omaheke">Omaheke</span></td>
									<td class="proper">37.52</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr110: Omusati">Omusati</span></td>
									<td class="proper">30.73</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr111: Oshana">Oshana</span></td>
									<td class="proper">31.80</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr112: Oshikoto">Oshikoto</span></td>
									<td class="proper">35.15</td>
								</tr>
								<tr>
									<td class="region"><span title="NAMr113: Otjozondjupa">Otjozondjupa</span></td>
									<td class="proper">37.39</td>
								</tr>
								<tr class="country">
									<th>Nepal (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="NPLt: Total">Total</span></td>
									<td class="proper">74.10</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="NPLr102: Central">Central</span></td>
									<td class="proper">75.52</td>
								</tr>
								<tr>
									<td class="region"><span title="NPLr101: Eastern">Eastern</span></td>
									<td class="proper">76.14</td>
								</tr>
								<tr>
									<td class="region"><span title="NPLr105: Far-western">Far-western</span></td>
									<td class="proper">72.22</td>
								</tr>
								<tr>
									<td class="region"><span title="NPLr104: Mid-western">Mid-western</span></td>
									<td class="proper">71.36</td>
								</tr>
								<tr>
									<td class="region"><span title="NPLr103: Western">Western</span></td>
									<td class="proper">75.27</td>
								</tr>
								<tr class="country">
									<th>Netherlands (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="NLDt: Total">Total</span></td>
									<td class="proper">75.60</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="NLDr103: Drenthe">Drenthe</span></td>
									<td class="proper">76.01</td>
								</tr>
								<tr>
									<td class="region"><span title="NLDr106: Flevoland">Flevoland</span></td>
									<td class="proper">76.60</td>
								</tr>
								<tr>
									<td class="region"><span title="NLDr102: Friesland">Friesland</span></td>
									<td class="proper">78.13</td>
								</tr>
								<tr>
									<td class="region"><span title="NLDr105: Gelderland">Gelderland</span></td>
									<td class="proper">74.34</td>
								</tr>
								<tr>
									<td class="region"><span title="NLDr101: Groningen">Groningen</span></td>
									<td class="proper">77.98</td>
								</tr>
								<tr>
									<td class="region"><span title="NLDr112: Limburg">Limburg</span></td>
									<td class="proper">70.98</td>
								</tr>
								<tr>
									<td class="region"><span title="NLDr111: Noord-Brabant">Noord-Brabant</span></td>
									<td class="proper">73.29</td>
								</tr>
								<tr>
									<td class="region"><span title="NLDr108: Noord-Holland">Noord-Holland</span></td>
									<td class="proper">77.97</td>
								</tr>
								<tr>
									<td class="region"><span title="NLDr104: Overijssel">Overijssel</span></td>
									<td class="proper">74.09</td>
								</tr>
								<tr>
									<td class="region"><span title="NLDr107: Utrecht">Utrecht</span></td>
									<td class="proper">75.88</td>
								</tr>
								<tr>
									<td class="region"><span title="NLDr110: Zeeland">Zeeland</span></td>
									<td class="proper">75.69</td>
								</tr>
								<tr>
									<td class="region"><span title="NLDr109: Zuid-Holland">Zuid-Holland</span></td>
									<td class="proper">76.20</td>
								</tr>
								<tr class="country">
									<th>New Zealand (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="NZLt: Total">Total</span></td>
									<td class="proper">80.12</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="NZLr102: Auckland">Auckland</span></td>
									<td class="proper">77.79</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr104: Bay of Plenty">Bay of Plenty</span></td>
									<td class="proper">79.70</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr113: Canterbury">Canterbury</span></td>
									<td class="proper">79.34</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr105: Gisborne">Gisborne</span></td>
									<td class="proper">80.57</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr106: Hawkes Bay">Hawkes Bay</span></td>
									<td class="proper">78.89</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr108: Manawatu-Wanganui">Manawatu-Wanganui</span></td>
									<td class="proper">80.48</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr111: Marlborough">Marlborough</span></td>
									<td class="proper">80.02</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr101: Northland">Northland</span></td>
									<td class="proper">79.37</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr114: Otago">Otago</span></td>
									<td class="proper">78.88</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr116: Other islands (Chatham Islands, Northern Islands, Southern Islands)">Other islands (Chatham Islands, Northern Islands, Southern Islands)</span></td>
									<td class="proper">78.40</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr115: Southland">Southland</span></td>
									<td class="proper">80.82</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr107: Taranaki">Taranaki</span></td>
									<td class="proper">80.56</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr110: Tasman - Nelson">Tasman - Nelson</span></td>
									<td class="proper">81.94</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr103: Waikato">Waikato</span></td>
									<td class="proper">79.31</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr109: Wellington">Wellington</span></td>
									<td class="proper">80.81</td>
								</tr>
								<tr>
									<td class="region"><span title="NZLr112: West Coast">West Coast</span></td>
									<td class="proper">83.35</td>
								</tr>
								<tr class="country">
									<th>Nicaragua (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="NICt: Total">Total</span></td>
									<td class="proper">79.14</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="NICr103: Atlantico (Rio San Juan, Atlantico Norte (Raan), Atlantico Sur (Raas))">Atlantico (Rio San Juan, Atlantico Norte (Raan), Atlantico Sur (Raas))</span></td>
									<td class="proper">86.03</td>
								</tr>
								<tr>
									<td class="region"><span title="NICr102: Central-Norte (Boaco, Chontales, Jinotega, Matagalpa, Esteli, Madriz, Nueva Segovia)">Central-Norte (Boaco, Chontales, Jinotega, Matagalpa, Esteli, Madriz, Nueva Segovia)</span></td>
									<td class="proper">80.40</td>
								</tr>
								<tr>
									<td class="region"><span title="NICr101: Pacifico (Chinandega, Leon, Managua, Masaya, Granada, Carazo, Rivas)">Pacifico (Chinandega, Leon, Managua, Masaya, Granada, Carazo, Rivas)</span></td>
									<td class="proper">70.99</td>
								</tr>
								<tr class="country">
									<th>Niger (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="NERt: Total">Total</span></td>
									<td class="proper">26.46</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="NERr101: Agadez">Agadez</span></td>
									<td class="proper">18.32</td>
								</tr>
								<tr>
									<td class="region"><span title="NERr102: Diffa">Diffa</span></td>
									<td class="proper">25.20</td>
								</tr>
								<tr>
									<td class="region"><span title="NERr103: Dosso">Dosso</span></td>
									<td class="proper">33.43</td>
								</tr>
								<tr>
									<td class="region"><span title="NERr104: Maradi">Maradi</span></td>
									<td class="proper">30.97</td>
								</tr>
								<tr>
									<td class="region"><span title="NERr106: Tahoua">Tahoua</span></td>
									<td class="proper">22.46</td>
								</tr>
								<tr>
									<td class="region"><span title="NERr105: Tillabery (incl Niamey)">Tillabery (incl Niamey)</span></td>
									<td class="proper">27.67</td>
								</tr>
								<tr>
									<td class="region"><span title="NERr107: Zinder">Zinder</span></td>
									<td class="proper">27.18</td>
								</tr>
								<tr class="country">
									<th>Nigeria (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="NGAt: Total">Total</span></td>
									<td class="proper">60.82</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="NGAr122: Abia">Abia</span></td>
									<td class="proper">77.16</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr137: Abuja FCT">Abuja FCT</span></td>
									<td class="proper">56.52</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr108: Adamawa">Adamawa</span></td>
									<td class="proper">46.90</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr101: Akwa Ibom">Akwa Ibom</span></td>
									<td class="proper">83.42</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr102: Anambra">Anambra</span></td>
									<td class="proper">71.62</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr103: Bauchi">Bauchi</span></td>
									<td class="proper">46.70</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr131: Bayelsa">Bayelsa</span></td>
									<td class="proper">83.07</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr105: Benue">Benue</span></td>
									<td class="proper">59.30</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr106: Borno">Borno</span></td>
									<td class="proper">38.07</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr107: Cross River">Cross River</span></td>
									<td class="proper">75.44</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr123: Delta">Delta</span></td>
									<td class="proper">81.05</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr132: Ebonyi">Ebonyi</span></td>
									<td class="proper">67.90</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr104: Edo">Edo</span></td>
									<td class="proper">76.01</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr133: Ekiti">Ekiti</span></td>
									<td class="proper">68.83</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr124: Enugu">Enugu</span></td>
									<td class="proper">67.54</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr134: Gombe">Gombe</span></td>
									<td class="proper">44.91</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr109: Imo">Imo</span></td>
									<td class="proper">77.71</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr125: Jigawa">Jigawa</span></td>
									<td class="proper">41.00</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr110: Kaduna">Kaduna</span></td>
									<td class="proper">50.72</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr111: Kano">Kano</span></td>
									<td class="proper">45.50</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr112: Katsina">Katsina</span></td>
									<td class="proper">42.16</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr126: Kebbi">Kebbi</span></td>
									<td class="proper">41.63</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr127: Kogi">Kogi</span></td>
									<td class="proper">62.16</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr113: Kwara">Kwara</span></td>
									<td class="proper">56.22</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr114: Lagos">Lagos</span></td>
									<td class="proper">83.23</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr135: Nassarawa">Nassarawa</span></td>
									<td class="proper">57.07</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr115: Niger">Niger</span></td>
									<td class="proper">50.89</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr116: Ogun">Ogun</span></td>
									<td class="proper">78.58</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr117: Ondo">Ondo</span></td>
									<td class="proper">78.03</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr128: Osun">Osun</span></td>
									<td class="proper">73.41</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr118: Oyo">Oyo</span></td>
									<td class="proper">65.64</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr119: Plateau">Plateau</span></td>
									<td class="proper">50.08</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr120: Rivers">Rivers</span></td>
									<td class="proper">83.10</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr121: Sokoto">Sokoto</span></td>
									<td class="proper">35.02</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr129: Taraba">Taraba</span></td>
									<td class="proper">52.27</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr130: Yobe">Yobe</span></td>
									<td class="proper">39.25</td>
								</tr>
								<tr>
									<td class="region"><span title="NGAr136: Zamfora">Zamfora</span></td>
									<td class="proper">42.36</td>
								</tr>
								<tr class="country">
									<th>North Macedonia (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="MKDt: Total">Total</span></td>
									<td class="proper">62.91</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="MKDr108: East">East</span></td>
									<td class="proper">63.93</td>
								</tr>
								<tr>
									<td class="region"><span title="MKDr104: North East">North East</span></td>
									<td class="proper">62.72</td>
								</tr>
								<tr>
									<td class="region"><span title="MKDr102: Pelagoniski">Pelagoniski</span></td>
									<td class="proper">60.31</td>
								</tr>
								<tr>
									<td class="region"><span title="MKDr107: Poloski">Poloski</span></td>
									<td class="proper">70.05</td>
								</tr>
								<tr>
									<td class="region"><span title="MKDr101: Skopski">Skopski</span></td>
									<td class="proper">61.45</td>
								</tr>
								<tr>
									<td class="region"><span title="MKDr106: South East">South East</span></td>
									<td class="proper">60.32</td>
								</tr>
								<tr>
									<td class="region"><span title="MKDr105: South West">South West</span></td>
									<td class="proper">67.15</td>
								</tr>
								<tr>
									<td class="region"><span title="MKDr103: Vardarski">Vardarski</span></td>
									<td class="proper">57.37</td>
								</tr>
								<tr class="country">
									<th>Norway (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="NORt: Total">Total</span></td>
									<td class="proper">76.60</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="NORr104: Agder og Rogaland">Agder og Rogaland</span></td>
									<td class="proper">79.00</td>
								</tr>
								<tr>
									<td class="region"><span title="NORr102: Hedmark og Oppland">Hedmark og Oppland</span></td>
									<td class="proper">74.19</td>
								</tr>
								<tr>
									<td class="region"><span title="NORr107: Nord-Norge">Nord-Norge</span></td>
									<td class="proper">79.72</td>
								</tr>
								<tr>
									<td class="region"><span title="NORr101: Oslo og Akershus">Oslo og Akershus</span></td>
									<td class="proper">71.64</td>
								</tr>
								<tr>
									<td class="region"><span title="NORr103: Sor-Ostlandet">Sor-Ostlandet</span></td>
									<td class="proper">74.53</td>
								</tr>
								<tr>
									<td class="region"><span title="NORr106: Trondelag">Trondelag</span></td>
									<td class="proper">78.85</td>
								</tr>
								<tr>
									<td class="region"><span title="NORr105: Vestlandet">Vestlandet</span></td>
									<td class="proper">78.27</td>
								</tr>
								<tr class="country">
									<th>Oman (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="OMNt: Total">Total</span></td>
									<td class="proper">41.24</td>
								</tr>
								<tr class="country">
									<th>Pakistan (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td></td>
								</tr>
								<tr>
									<td class="region"><span title="PAKt: Total">Total</span></td>
									<td class="proper">56.07</td>
								</tr>
								<tr>
									<td class="region"><span title="PRKt: Total">Total</span></td>
									<td class="proper">69.08</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="PAKr107: AJK">AJK</span></td>
									<td class="proper">65.54</td>
								</tr>
								<tr>
									<td class="region"><span title="PAKr104: Balochistan">Balochistan</span></td>
									<td class="proper">36.92</td>
								</tr>
								<tr>
									<td class="region"><span title="PAKr108: FATA">FATA</span></td>
									<td class="proper">52.14</td>
								</tr>
								<tr>
									<td class="region"><span title="PAKr106: Gilgit Baltistan">Gilgit Baltistan</span></td>
									<td class="proper">72.18</td>
								</tr>
								<tr>
									<td class="region"><span title="PAKr105: Islamabad (ICT)">Islamabad (ICT)</span></td>
									<td class="proper">56.89</td>
								</tr>
								<tr>
									<td class="region"><span title="PAKr103: Khyber Pakhtunkhwa (NWFrontier)">Khyber Pakhtunkhwa (NWFrontier)</span></td>
									<td class="proper">58.28</td>
								</tr>
								<tr>
									<td class="region"><span title="PAKr101: Punjab">Punjab</span></td>
									<td class="proper">53.55</td>
								</tr>
								<tr>
									<td class="region"><span title="PAKr102: Sindh">Sindh</span></td>
									<td class="proper">53.08</td>
								</tr>
								<tr class="country">
									<th>Panama (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="PANt: Total">Total</span></td>
									<td class="proper">84.60</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="PANr101: Bocas del Toro">Bocas del Toro</span></td>
									<td class="proper">85.25</td>
								</tr>
								<tr>
									<td class="region"><span title="PANr104: Chiriqui">Chiriqui</span></td>
									<td class="proper">83.57</td>
								</tr>
								<tr>
									<td class="region"><span title="PANr102: Cocle">Cocle</span></td>
									<td class="proper">85.56</td>
								</tr>
								<tr>
									<td class="region"><span title="PANr103: Colon">Colon</span></td>
									<td class="proper">86.27</td>
								</tr>
								<tr>
									<td class="region"><span title="PANr105: Darien">Darien</span></td>
									<td class="proper">85.72</td>
								</tr>
								<tr>
									<td class="region"><span title="PANr111: Embera Wounaan">Embera Wounaan</span></td>
									<td class="proper">86.26</td>
								</tr>
								<tr>
									<td class="region"><span title="PANr106: Herrera">Herrera</span></td>
									<td class="proper">81.68</td>
								</tr>
								<tr>
									<td class="region"><span title="PANr110: Kuna Yala">Kuna Yala</span></td>
									<td class="proper">84.73</td>
								</tr>
								<tr>
									<td class="region"><span title="PANr107: Los Santos">Los Santos</span></td>
									<td class="proper">81.82</td>
								</tr>
								<tr>
									<td class="region"><span title="PANr112: Ngobe Bugle">Ngobe Bugle</span></td>
									<td class="proper">85.73</td>
								</tr>
								<tr>
									<td class="region"><span title="PANr108: Panama">Panama</span></td>
									<td class="proper">85.21</td>
								</tr>
								<tr>
									<td class="region"><span title="PANr109: Veraguas">Veraguas</span></td>
									<td class="proper">83.35</td>
								</tr>
								<tr class="country">
									<th>Papua New Guinea (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="PNGt: Total">Total</span></td>
									<td class="proper">84.36</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="PNGr120: Autonomous Region of Bougainville">Autonomous Region of Bougainville</span></td>
									<td class="proper">85.36</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr103: Central">Central</span></td>
									<td class="proper">84.14</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr110: Chimbu, Simbu">Chimbu, Simbu</span></td>
									<td class="proper">84.71</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr118: East New Britain">East New Britain</span></td>
									<td class="proper">85.21</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr114: East Sepik">East Sepik</span></td>
									<td class="proper">83.60</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr111: Eastern Highlands">Eastern Highlands</span></td>
									<td class="proper">83.19</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr108: Enga">Enga</span></td>
									<td class="proper">85.05</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr102: Gulf">Gulf</span></td>
									<td class="proper">85.37</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr121: Hela">Hela</span></td>
									<td class="proper">86.55</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr122: Jiwaka">Jiwaka</span></td>
									<td class="proper">85.21</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr113: Madang">Madang</span></td>
									<td class="proper">83.43</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr116: Manus">Manus</span></td>
									<td class="proper">80.99</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr105: Milne Bay">Milne Bay</span></td>
									<td class="proper">84.58</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr112: Morobe">Morobe</span></td>
									<td class="proper">84.47</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr104: National Capital District">National Capital District</span></td>
									<td class="proper">81.67</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr117: New Ireland">New Ireland</span></td>
									<td class="proper">80.97</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr106: Northern, Oro">Northern, Oro</span></td>
									<td class="proper">86.05</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr107: Southern Highlands">Southern Highlands</span></td>
									<td class="proper">86.51</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr119: West New Britain">West New Britain</span></td>
									<td class="proper">86.22</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr115: West Sepik, Sandaun">West Sepik, Sandaun</span></td>
									<td class="proper">83.45</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr101: Western">Western</span></td>
									<td class="proper">84.86</td>
								</tr>
								<tr>
									<td class="region"><span title="PNGr109: Western Highlands">Western Highlands</span></td>
									<td class="proper">84.26</td>
								</tr>
								<tr class="country">
									<th>Paraguay (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="PRYt: Total">Total</span></td>
									<td class="proper">65.60</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="PRYr105: Central (Asuncion, Central)">Central (Asuncion, Central)</span></td>
									<td class="proper">66.09</td>
								</tr>
								<tr>
									<td class="region"><span title="PRYr102: North-East (Caaguazu, Alto Parana, Canideyu)">North-East (Caaguazu, Alto Parana, Canideyu)</span></td>
									<td class="proper">69.41</td>
								</tr>
								<tr>
									<td class="region"><span title="PRYr101: North-West (Boqueron, Alto Paraguay, Presidente Hayes, Conception, Amambay, San pedro, Cordillera)">North-West (Boqueron, Alto Paraguay, Presidente Hayes, Conception, Amambay, San pedro, Cordillera)</span></td>
									<td class="proper">57.88</td>
								</tr>
								<tr>
									<td class="region"><span title="PRYr104: South-East (Guaira, Misiones, Paraguari, Neembucu)">South-East (Guaira, Misiones, Paraguari, Neembucu)</span></td>
									<td class="proper">65.41</td>
								</tr>
								<tr>
									<td class="region"><span title="PRYr103: South-West (Caazapa, Itapua)">South-West (Caazapa, Itapua)</span></td>
									<td class="proper">69.20</td>
								</tr>
								<tr class="country">
									<th>Peru (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="PERt: Total">Total</span></td>
									<td class="proper">71.49</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="PERr106: Central (Huancavelica, Huanuco, Junin, Pasco)">Central (Huancavelica, Huanuco, Junin, Pasco)</span></td>
									<td class="proper">79.75</td>
								</tr>
								<tr>
									<td class="region"><span title="PERr103: East (Madre de Dios, Cusco, Puno, Apurimac)">East (Madre de Dios, Cusco, Puno, Apurimac)</span></td>
									<td class="proper">68.87</td>
								</tr>
								<tr>
									<td class="region"><span title="PERr101: North (Tumbes, Piura, Lambayeque, Cajamarca, La Libertad)">North (Tumbes, Piura, Lambayeque, Cajamarca, La Libertad)</span></td>
									<td class="proper">72.50</td>
								</tr>
								<tr>
									<td class="region"><span title="PERr102: North East (Amazonas, Loreto, San Martin, Ucayali)">North East (Amazonas, Loreto, San Martin, Ucayali)</span></td>
									<td class="proper">83.92</td>
								</tr>
								<tr>
									<td class="region"><span title="PERr104: South (Tacna, Moquegua, Arequipa, Ica, Ayacucho)">South (Tacna, Moquegua, Arequipa, Ica, Ayacucho)</span></td>
									<td class="proper">53.00</td>
								</tr>
								<tr>
									<td class="region"><span title="PERr105: West (Ancash, Lima, Callao)">West (Ancash, Lima, Callao)</span></td>
									<td class="proper">70.91</td>
								</tr>
								<tr class="country">
									<th>Philippines (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="PHLt: Total">Total</span></td>
									<td class="proper">82.95</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="PHLr117: ARMM">ARMM</span></td>
									<td class="proper">82.89</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr102: Cordillera Admin Region">Cordillera Admin Region</span></td>
									<td class="proper">84.44</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr103: I-Ilocos">I-Ilocos</span></td>
									<td class="proper">79.41</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr104: II-Cagayan Valley">II-Cagayan Valley</span></td>
									<td class="proper">84.20</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr105: III-Central Luzon">III-Central Luzon</span></td>
									<td class="proper">79.90</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr106: IVA-CALABARZON">IVA-CALABARZON</span></td>
									<td class="proper">82.91</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr107: IVB-MIMAROPA">IVB-MIMAROPA</span></td>
									<td class="proper">83.11</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr112: IX-Zamboanga Peninsula">IX-Zamboanga Peninsula</span></td>
									<td class="proper">83.94</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr101: National Capital Region">National Capital Region</span></td>
									<td class="proper">76.93</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr108: V-Bicol">V-Bicol</span></td>
									<td class="proper">84.05</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr109: VI-Western Visayas">VI-Western Visayas</span></td>
									<td class="proper">84.46</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr110: VII-Central Visayas">VII-Central Visayas</span></td>
									<td class="proper">83.26</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr111: VIII-Eastern Visayas">VIII-Eastern Visayas</span></td>
									<td class="proper">85.38</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr113: X-Northern Mindanao">X-Northern Mindanao</span></td>
									<td class="proper">84.49</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr114: XI-Davao">XI-Davao</span></td>
									<td class="proper">84.16</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr115: XII-SOCCSKSARGEN">XII-SOCCSKSARGEN</span></td>
									<td class="proper">82.16</td>
								</tr>
								<tr>
									<td class="region"><span title="PHLr116: XIII-Caraga">XIII-Caraga</span></td>
									<td class="proper">84.50</td>
								</tr>
								<tr class="country">
									<th>Poland (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="POLt: Total">Total</span></td>
									<td class="proper">72.73</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="POLr112: Dolnoslaskie">Dolnoslaskie</span></td>
									<td class="proper">70.92</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr114: Kujawsko-Pomorskie">Kujawsko-Pomorskie</span></td>
									<td class="proper">73.45</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr101: Lodzkie">Lodzkie</span></td>
									<td class="proper">71.99</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr105: Lubelskie">Lubelskie</span></td>
									<td class="proper">72.93</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr111: Lubuskie">Lubuskie</span></td>
									<td class="proper">68.15</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr103: Malopolskie">Malopolskie</span></td>
									<td class="proper">73.00</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr102: Mazowieckie">Mazowieckie</span></td>
									<td class="proper">73.02</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr113: Opolskie">Opolskie</span></td>
									<td class="proper">70.53</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr106: Podkarpackie">Podkarpackie</span></td>
									<td class="proper">72.30</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr108: Podlaskie">Podlaskie</span></td>
									<td class="proper">75.21</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr116: Pomorskie">Pomorskie</span></td>
									<td class="proper">77.34</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr104: Slaskie">Slaskie</span></td>
									<td class="proper">72.83</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr107: Swietokrzyskie">Swietokrzyskie</span></td>
									<td class="proper">72.59</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr115: Warminsko-Mazurskie">Warminsko-Mazurskie</span></td>
									<td class="proper">75.54</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr109: Wielkopolskie">Wielkopolskie</span></td>
									<td class="proper">69.49</td>
								</tr>
								<tr>
									<td class="region"><span title="POLr110: Zachodniopomorskie">Zachodniopomorskie</span></td>
									<td class="proper">74.38</td>
								</tr>
								<tr class="country">
									<th>Portugal (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="PRTt: Total">Total</span></td>
									<td class="proper">70.05</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="PRTr105: Alentejo">Alentejo</span></td>
									<td class="proper">61.01</td>
								</tr>
								<tr>
									<td class="region"><span title="PRTr102: Algarve">Algarve</span></td>
									<td class="proper">67.29</td>
								</tr>
								<tr>
									<td class="region"><span title="PRTr104: Area Metropolitana de Lisboa">Area Metropolitana de Lisboa</span></td>
									<td class="proper">71.32</td>
								</tr>
								<tr>
									<td class="region"><span title="PRTr103: Centro">Centro</span></td>
									<td class="proper">67.59</td>
								</tr>
								<tr>
									<td class="region"><span title="PRTr101: Norte">Norte</span></td>
									<td class="proper">68.25</td>
								</tr>
								<tr>
									<td class="region"><span title="PRTr107: Regiao Autonoma da Madeira">Regiao Autonoma da Madeira</span></td>
									<td class="proper">77.15</td>
								</tr>
								<tr>
									<td class="region"><span title="PRTr106: Regiao Autonoma dos Acores">Regiao Autonoma dos Acores</span></td>
									<td class="proper">77.74</td>
								</tr>
								<tr class="country">
									<th>Qatar (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="QATt: Total">Total</span></td>
									<td class="proper">49.68</td>
								</tr>
								<tr class="country">
									<th>Romania (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ROUt: Total">Total</span></td>
									<td class="proper">67.18</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ROUr108: Bucuresti">Bucuresti</span></td>
									<td class="proper">62.53</td>
								</tr>
								<tr>
									<td class="region"><span title="ROUr107: Centru">Centru</span></td>
									<td class="proper">70.86</td>
								</tr>
								<tr>
									<td class="region"><span title="ROUr101: Nord-Est">Nord-Est</span></td>
									<td class="proper">67.60</td>
								</tr>
								<tr>
									<td class="region"><span title="ROUr106: Nord-Vest">Nord-Vest</span></td>
									<td class="proper">70.99</td>
								</tr>
								<tr>
									<td class="region"><span title="ROUr103: Sud">Sud</span></td>
									<td class="proper">65.53</td>
								</tr>
								<tr>
									<td class="region"><span title="ROUr102: Sud-Est">Sud-Est</span></td>
									<td class="proper">63.77</td>
								</tr>
								<tr>
									<td class="region"><span title="ROUr104: Sud-Vest Oltenia">Sud-Vest Oltenia</span></td>
									<td class="proper">66.48</td>
								</tr>
								<tr>
									<td class="region"><span title="ROUr105: Vest">Vest</span></td>
									<td class="proper">69.70</td>
								</tr>
								<tr class="country">
									<th>Russian Federation (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="RUSt: Total">Total</span></td>
									<td class="proper">70.76</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="RUSr101: The Central Federal District">The Central Federal District</span></td>
									<td class="proper">72.39</td>
								</tr>
								<tr>
									<td class="region"><span title="RUSr108: The Far East  Federal District">The Far East  Federal District</span></td>
									<td class="proper">72.27</td>
								</tr>
								<tr>
									<td class="region"><span title="RUSr102: The North West Federal District">The North West Federal District</span></td>
									<td class="proper">78.16</td>
								</tr>
								<tr>
									<td class="region"><span title="RUSr104: The North-Caucasian Federal District">The North-Caucasian Federal District</span></td>
									<td class="proper">66.17</td>
								</tr>
								<tr>
									<td class="region"><span title="RUSr105: The Privolzhsky (Volga) Federal District">The Privolzhsky (Volga) Federal District</span></td>
									<td class="proper">70.50</td>
								</tr>
								<tr>
									<td class="region"><span title="RUSr107: The Siberian  Federal District">The Siberian  Federal District</span></td>
									<td class="proper">70.74</td>
								</tr>
								<tr>
									<td class="region"><span title="RUSr103: The South Federal District">The South Federal District</span></td>
									<td class="proper">62.49</td>
								</tr>
								<tr>
									<td class="region"><span title="RUSr106: The Urals  Federal District">The Urals  Federal District</span></td>
									<td class="proper">73.39</td>
								</tr>
								<tr class="country">
									<th>Rwanda (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="RWAt: Total">Total</span></td>
									<td class="proper">71.20</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="RWAr101: City of Kigali">City of Kigali</span></td>
									<td class="proper">69.52</td>
								</tr>
								<tr>
									<td class="region"><span title="RWAr105: East">East</span></td>
									<td class="proper">67.71</td>
								</tr>
								<tr>
									<td class="region"><span title="RWAr104: North">North</span></td>
									<td class="proper">73.70</td>
								</tr>
								<tr>
									<td class="region"><span title="RWAr102: South">South</span></td>
									<td class="proper">70.49</td>
								</tr>
								<tr>
									<td class="region"><span title="RWAr103: West">West</span></td>
									<td class="proper">74.58</td>
								</tr>
								<tr class="country">
									<th>Samoa (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="WSMt: Total">Total</span></td>
									<td class="proper">83.31</td>
								</tr>
								<tr class="country">
									<th>San Marino (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SMRt: Total">Total</span></td>
									<td class="proper">70.83</td>
								</tr>
								<tr class="country">
									<th>Sao Tome and Principe (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="STPt: Total">Total</span></td>
									<td class="proper">82.15</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="STPr101: Regiao Centro">Regiao Centro</span></td>
									<td class="proper">82.19</td>
								</tr>
								<tr>
									<td class="region"><span title="STPr104: Regiao do Principe">Regiao do Principe</span></td>
									<td class="proper">81.45</td>
								</tr>
								<tr>
									<td class="region"><span title="STPr103: Regiao Norte">Regiao Norte</span></td>
									<td class="proper">82.46</td>
								</tr>
								<tr>
									<td class="region"><span title="STPr102: Regiao Sul">Regiao Sul</span></td>
									<td class="proper">82.48</td>
								</tr>
								<tr class="country">
									<th>Saudi Arabia (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SAUt: Total">Total</span></td>
									<td class="proper">26.32</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SAUr101: Center (Riadh, Qassim)">Center (Riadh, Qassim)</span></td>
									<td class="proper">21.30</td>
								</tr>
								<tr>
									<td class="region"><span title="SAUr104: Eastern province">Eastern province</span></td>
									<td class="proper">25.79</td>
								</tr>
								<tr>
									<td class="region"><span title="SAUr105: North (Northern Borders, Al Jawf, Hail)">North (Northern Borders, Al Jawf, Hail)</span></td>
									<td class="proper">25.54</td>
								</tr>
								<tr>
									<td class="region"><span title="SAUr103: South (Bahah, Jizan, Asir, Najran)">South (Bahah, Jizan, Asir, Najran)</span></td>
									<td class="proper">29.27</td>
								</tr>
								<tr>
									<td class="region"><span title="SAUr102: West (Makka, Madinah, Tabuk)">West (Makka, Madinah, Tabuk)</span></td>
									<td class="proper">29.68</td>
								</tr>
								<tr class="country">
									<th>Senegal (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SENt: Total">Total</span></td>
									<td class="proper">53.93</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SENr101: Dakar">Dakar</span></td>
									<td class="proper">72.43</td>
								</tr>
								<tr>
									<td class="region"><span title="SENr103: Diourbel">Diourbel</span></td>
									<td class="proper">53.21</td>
								</tr>
								<tr>
									<td class="region"><span title="SENr109: Fatick">Fatick</span></td>
									<td class="proper">58.17</td>
								</tr>
								<tr>
									<td class="region"><span title="SENr106: Kaolack">Kaolack</span></td>
									<td class="proper">51.50</td>
								</tr>
								<tr>
									<td class="region"><span title="SENr110: Kolda">Kolda</span></td>
									<td class="proper">52.14</td>
								</tr>
								<tr>
									<td class="region"><span title="SENr108: Louga">Louga</span></td>
									<td class="proper">47.03</td>
								</tr>
								<tr>
									<td class="region"><span title="SENr104: Saint Louis">Saint Louis</span></td>
									<td class="proper">38.83</td>
								</tr>
								<tr>
									<td class="region"><span title="SENr105: Tambacounda">Tambacounda</span></td>
									<td class="proper">41.82</td>
								</tr>
								<tr>
									<td class="region"><span title="SENr107: Thies">Thies</span></td>
									<td class="proper">60.66</td>
								</tr>
								<tr>
									<td class="region"><span title="SENr102: Ziguinchor">Ziguinchor</span></td>
									<td class="proper">63.53</td>
								</tr>
								<tr class="country">
									<th>Serbia (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SRBt: Total">Total</span></td>
									<td class="proper">68.01</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SRBr101: Belgrade">Belgrade</span></td>
									<td class="proper">66.29</td>
								</tr>
								<tr>
									<td class="region"><span title="SRBr104: South and East Serbia">South and East Serbia</span></td>
									<td class="proper">69.70</td>
								</tr>
								<tr>
									<td class="region"><span title="SRBr103: Sumadija and West Serbia">Sumadija and West Serbia</span></td>
									<td class="proper">70.00</td>
								</tr>
								<tr>
									<td class="region"><span title="SRBr102: Vojvodina">Vojvodina</span></td>
									<td class="proper">66.07</td>
								</tr>
								<tr class="country">
									<th>Sierra Leone (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SLEt: Total">Total</span></td>
									<td class="proper">77.84</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SLEr114: Western Urban">Western Urban</span></td>
									<td class="proper">81.94</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr113: Western Rural">Western Rural</span></td>
									<td class="proper">82.62</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr109: Bo">Bo</span></td>
									<td class="proper">80.59</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr101: Bombali">Bombali</span></td>
									<td class="proper">69.80</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr110: Bonthe">Bonthe</span></td>
									<td class="proper">85.31</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr106: Kailahun">Kailahun</span></td>
									<td class="proper">75.78</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr102: Kambia">Kambia</span></td>
									<td class="proper">75.82</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr107: Kenema">Kenema</span></td>
									<td class="proper">79.03</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr103: Koinadugu">Koinadugu</span></td>
									<td class="proper">65.24</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr108: Kono">Kono</span></td>
									<td class="proper">71.22</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr111: Moyamba">Moyamba</span></td>
									<td class="proper">82.64</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr104: Port Loko">Port Loko</span></td>
									<td class="proper">79.74</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr112: Pujehun">Pujehun</span></td>
									<td class="proper">85.13</td>
								</tr>
								<tr>
									<td class="region"><span title="SLEr105: Tonkolili">Tonkolili</span></td>
									<td class="proper">74.96</td>
								</tr>
								<tr class="country">
									<th>Singapore (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SGPt: Total">Total</span></td>
									<td class="proper">82.24</td>
								</tr>
								<tr class="country">
									<th>Slovak Republic (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SVKt: Total">Total</span></td>
									<td class="proper">68.50</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SVKr101: Bratislavsky kraj">Bratislavsky kraj</span></td>
									<td class="proper">66.34</td>
								</tr>
								<tr>
									<td class="region"><span title="SVKr103: Stredne Slovensko">Stredne Slovensko</span></td>
									<td class="proper">71.69</td>
								</tr>
								<tr>
									<td class="region"><span title="SVKr104: Vychodne Slovensko">Vychodne Slovensko</span></td>
									<td class="proper">69.63</td>
								</tr>
								<tr>
									<td class="region"><span title="SVKr102: Zapadne Slovensko">Zapadne Slovensko</span></td>
									<td class="proper">66.33</td>
								</tr>
								<tr class="country">
									<th>Slovenia (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SVNt: Total">Total</span></td>
									<td class="proper">71.18</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SVNr110: Gorenjska">Gorenjska</span></td>
									<td class="proper">72.97</td>
								</tr>
								<tr>
									<td class="region"><span title="SVNr111: Goriska">Goriska</span></td>
									<td class="proper">71.57</td>
								</tr>
								<tr>
									<td class="region"><span title="SVNr107: Jugovzhodna Slovenija">Jugovzhodna Slovenija</span></td>
									<td class="proper">72.30</td>
								</tr>
								<tr>
									<td class="region"><span title="SVNr103: Koroska">Koroska</span></td>
									<td class="proper">73.64</td>
								</tr>
								<tr>
									<td class="region"><span title="SVNr112: Obalno-kraska">Obalno-kraska</span></td>
									<td class="proper">69.25</td>
								</tr>
								<tr>
									<td class="region"><span title="SVNr109: Osrednjeslovenska">Osrednjeslovenska</span></td>
									<td class="proper">70.89</td>
								</tr>
								<tr>
									<td class="region"><span title="SVNr102: Podravska">Podravska</span></td>
									<td class="proper">70.86</td>
								</tr>
								<tr>
									<td class="region"><span title="SVNr101: Pomurska">Pomurska</span></td>
									<td class="proper">68.43</td>
								</tr>
								<tr>
									<td class="region"><span title="SVNr106: Posavska">Posavska</span></td>
									<td class="proper">70.07</td>
								</tr>
								<tr>
									<td class="region"><span title="SVNr108: Primorsko-notranjska">Primorsko-notranjska</span></td>
									<td class="proper">72.10</td>
								</tr>
								<tr>
									<td class="region"><span title="SVNr104: Savinjska">Savinjska</span></td>
									<td class="proper">71.22</td>
								</tr>
								<tr>
									<td class="region"><span title="SVNr105: Zasavska">Zasavska</span></td>
									<td class="proper">70.81</td>
								</tr>
								<tr class="country">
									<th>Solomon Islands (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SLBt: Total">Total</span></td>
									<td class="proper">83.76</td>
								</tr>
								<tr class="country">
									<th>Somalia (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SOMt: Total">Total</span></td>
									<td class="proper">55.98</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SOMr102: Awdal">Awdal</span></td>
									<td class="proper">54.82</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr109: Bakool">Bakool</span></td>
									<td class="proper">49.14</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr116: Banadir">Banadir</span></td>
									<td class="proper">77.41</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr108: Bari">Bari</span></td>
									<td class="proper">53.23</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr110: Bay">Bay</span></td>
									<td class="proper">56.21</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr117: Galguduud">Galguduud</span></td>
									<td class="proper">56.10</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr111: Gedo">Gedo</span></td>
									<td class="proper">47.62</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr113: Hiran">Hiran</span></td>
									<td class="proper">53.69</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr118: Lower Juba">Lower Juba</span></td>
									<td class="proper">63.64</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr115: Lower Shabelle">Lower Shabelle</span></td>
									<td class="proper">67.45</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr112: Middle Juba">Middle Juba</span></td>
									<td class="proper">60.74</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr114: Middle Shabelle">Middle Shabelle</span></td>
									<td class="proper">68.63</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr106: Mudug">Mudug</span></td>
									<td class="proper">58.16</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr107: Nugal">Nugal</span></td>
									<td class="proper">53.99</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr103: Sanaag">Sanaag</span></td>
									<td class="proper">47.20</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr104: Sool">Sool</span></td>
									<td class="proper">44.03</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr105: Togdhere">Togdhere</span></td>
									<td class="proper">44.48</td>
								</tr>
								<tr>
									<td class="region"><span title="SOMr101: W Galbeed">W Galbeed</span></td>
									<td class="proper">51.01</td>
								</tr>
								<tr class="country">
									<th>South Africa (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ZAFt: Total">Total</span></td>
									<td class="proper">56.69</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ZAFr102: Eastern Cape">Eastern Cape</span></td>
									<td class="proper">61.85</td>
								</tr>
								<tr>
									<td class="region"><span title="ZAFr104: Free State">Free State</span></td>
									<td class="proper">54.09</td>
								</tr>
								<tr>
									<td class="region"><span title="ZAFr107: Gauteng">Gauteng</span></td>
									<td class="proper">56.42</td>
								</tr>
								<tr>
									<td class="region"><span title="ZAFr105: KwaZulu Natal">KwaZulu Natal</span></td>
									<td class="proper">69.80</td>
								</tr>
								<tr>
									<td class="region"><span title="ZAFr108: Mpumalanga">Mpumalanga</span></td>
									<td class="proper">64.27</td>
								</tr>
								<tr>
									<td class="region"><span title="ZAFr106: North West">North West</span></td>
									<td class="proper">50.79</td>
								</tr>
								<tr>
									<td class="region"><span title="ZAFr103: Northern Cape">Northern Cape</span></td>
									<td class="proper">42.03</td>
								</tr>
								<tr>
									<td class="region"><span title="ZAFr109: Northern Province">Northern Province</span></td>
									<td class="proper">55.50</td>
								</tr>
								<tr>
									<td class="region"><span title="ZAFr101: Western Cape">Western Cape</span></td>
									<td class="proper">55.47</td>
								</tr>
								<tr class="country">
									<th>South Sudan (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SSDt: Total">Total</span></td>
									<td class="proper">43.02</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SSDr109: Central Equatoria">Central Equatoria</span></td>
									<td class="proper">55.66</td>
								</tr>
								<tr>
									<td class="region"><span title="SSDr110: Eastern Equatoria">Eastern Equatoria</span></td>
									<td class="proper">46.76</td>
								</tr>
								<tr>
									<td class="region"><span title="SSDr102: Jonglei">Jonglei</span></td>
									<td class="proper">43.25</td>
								</tr>
								<tr>
									<td class="region"><span title="SSDr107: Lakes">Lakes</span></td>
									<td class="proper">46.30</td>
								</tr>
								<tr>
									<td class="region"><span title="SSDr105: Northern Bahr El Ghazal">Northern Bahr El Ghazal</span></td>
									<td class="proper">34.19</td>
								</tr>
								<tr>
									<td class="region"><span title="SSDr103: Unity">Unity</span></td>
									<td class="proper">37.28</td>
								</tr>
								<tr>
									<td class="region"><span title="SSDr101: Upper Nile">Upper Nile</span></td>
									<td class="proper">37.13</td>
								</tr>
								<tr>
									<td class="region"><span title="SSDr104: Warrap">Warrap</span></td>
									<td class="proper">38.93</td>
								</tr>
								<tr>
									<td class="region"><span title="SSDr106: Western Bahr El Ghazal">Western Bahr El Ghazal</span></td>
									<td class="proper">37.82</td>
								</tr>
								<tr>
									<td class="region"><span title="SSDr108: Western Equatoria">Western Equatoria</span></td>
									<td class="proper">52.88</td>
								</tr>
								<tr class="country">
									<th>Spain (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ESPt: Total">Total</span></td>
									<td class="proper">65.32</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ESPr115: Andalucia">Andalucia</span></td>
									<td class="proper">55.46</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr107: Aragon">Aragon</span></td>
									<td class="proper">56.55</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr119: Canarias">Canarias</span></td>
									<td class="proper">74.77</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr103: Cantabria">Cantabria</span></td>
									<td class="proper">75.08</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr109: Castilla y Leon">Castilla y Leon</span></td>
									<td class="proper">59.37</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr110: Castilla-la Mancha">Castilla-la Mancha</span></td>
									<td class="proper">50.97</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr112: Cataluna">Cataluna</span></td>
									<td class="proper">65.76</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr120: Ceuta y Melilla">Ceuta y Melilla</span></td>
									<td class="proper">78.75</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr108: Comunidad de Madrid">Comunidad de Madrid</span></td>
									<td class="proper">52.89</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr105: Comunidad Foral de Navarra">Comunidad Foral de Navarra</span></td>
									<td class="proper">67.32</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr113: Comunidad Valenciana">Comunidad Valenciana</span></td>
									<td class="proper">62.07</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr111: Extremadura">Extremadura</span></td>
									<td class="proper">53.63</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr101: Galicia">Galicia</span></td>
									<td class="proper">77.00</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr114: Illes Balears">Illes Balears</span></td>
									<td class="proper">71.83</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr106: La Rioja">La Rioja</span></td>
									<td class="proper">62.87</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr104: Pais Vasco">Pais Vasco</span></td>
									<td class="proper">74.18</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr102: Principado de Asturias">Principado de Asturias</span></td>
									<td class="proper">78.25</td>
								</tr>
								<tr>
									<td class="region"><span title="ESPr116: Region de Murcia">Region de Murcia</span></td>
									<td class="proper">58.98</td>
								</tr>
								<tr class="country">
									<th>Sri Lanka (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="LKAt: Total">Total</span></td>
									<td class="proper">80.53</td>
								</tr>
								<tr class="country">
									<th>St. Kitts and Nevis (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="KNAt: Total">Total</span></td>
									<td class="proper">78.83</td>
								</tr>
								<tr class="country">
									<th>St. Lucia (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="LCAt: Total">Total</span></td>
									<td class="proper">75.44</td>
								</tr>
								<tr class="country">
									<th>St. Vincent and the Grenadines (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="VCTt: Total">Total</span></td>
									<td class="proper">79.78</td>
								</tr>
								<tr class="country">
									<th>Sudan (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SDNt: Total">Total</span></td>
									<td class="proper">27.79</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SDNr105: Al Gedarif">Al Gedarif</span></td>
									<td class="proper">29.43</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr107: Al Gezira">Al Gezira</span></td>
									<td class="proper">24.95</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr110: Blue Nile">Blue Nile</span></td>
									<td class="proper">35.01</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr104: Kassala">Kassala</span></td>
									<td class="proper">31.98</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr106: Khartoum">Khartoum</span></td>
									<td class="proper">23.67</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr102: Nahr El Nil">Nahr El Nil</span></td>
									<td class="proper">22.32</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr113: North Darfur">North Darfur</span></td>
									<td class="proper">22.49</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr111: North Kordofan">North Kordofan</span></td>
									<td class="proper">25.68</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr101: Northern">Northern</span></td>
									<td class="proper">20.93</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr103: Red Sea">Red Sea</span></td>
									<td class="proper">32.91</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr109: Sinnar">Sinnar</span></td>
									<td class="proper">29.06</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr115: South Darfur">South Darfur</span></td>
									<td class="proper">29.44</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr112: South Kordofan">South Kordofan</span></td>
									<td class="proper">32.32</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr114: West Darfur">West Darfur</span></td>
									<td class="proper">29.43</td>
								</tr>
								<tr>
									<td class="region"><span title="SDNr108: White Nile">White Nile</span></td>
									<td class="proper">27.16</td>
								</tr>
								<tr class="country">
									<th>Suriname (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SURt: Total">Total</span></td>
									<td class="proper">84.38</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SURr105: Brokopondo and Sipaliwini">Brokopondo and Sipaliwini</span></td>
									<td class="proper">83.33</td>
								</tr>
								<tr>
									<td class="region"><span title="SURr104: Commewijne and Marowijne">Commewijne and Marowijne</span></td>
									<td class="proper">85.26</td>
								</tr>
								<tr>
									<td class="region"><span title="SURr103: Nickerie, Coronie and Saramacca">Nickerie, Coronie and Saramacca</span></td>
									<td class="proper">84.67</td>
								</tr>
								<tr>
									<td class="region"><span title="SURr101: Paramaribo">Paramaribo</span></td>
									<td class="proper">83.98</td>
								</tr>
								<tr>
									<td class="region"><span title="SURr102: Wanica and Para">Wanica and Para</span></td>
									<td class="proper">84.65</td>
								</tr>
								<tr class="country">
									<th>Svalbard and Jan Mayen (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SJMt: Total">Total</span></td>
									<td class="proper">84.72</td>
								</tr>
								<tr class="country">
									<th>Sweden (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SWEt: Total">Total</span></td>
									<td class="proper">75.97</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SWEr107: Mellersta Norrland">Mellersta Norrland</span></td>
									<td class="proper">75.31</td>
								</tr>
								<tr>
									<td class="region"><span title="SWEr106: Norra Mellansverige">Norra Mellansverige</span></td>
									<td class="proper">73.43</td>
								</tr>
								<tr>
									<td class="region"><span title="SWEr102: Ostra Mellansverige">Ostra Mellansverige</span></td>
									<td class="proper">74.21</td>
								</tr>
								<tr>
									<td class="region"><span title="SWEr108: Ovre Norrland">Ovre Norrland</span></td>
									<td class="proper">76.78</td>
								</tr>
								<tr>
									<td class="region"><span title="SWEr103: Smaland med oarna">Smaland med oarna</span></td>
									<td class="proper">76.11</td>
								</tr>
								<tr>
									<td class="region"><span title="SWEr101: Stockholm">Stockholm</span></td>
									<td class="proper">75.72</td>
								</tr>
								<tr>
									<td class="region"><span title="SWEr104: Sydsverige">Sydsverige</span></td>
									<td class="proper">79.31</td>
								</tr>
								<tr>
									<td class="region"><span title="SWEr105: Vastsverige">Vastsverige</span></td>
									<td class="proper">76.91</td>
								</tr>
								<tr class="country">
									<th>Switzerland (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="CHEt: Total">Total</span></td>
									<td class="proper">72.30</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="CHEr106: Central Switzerland">Central Switzerland</span></td>
									<td class="proper">75.11</td>
								</tr>
								<tr>
									<td class="region"><span title="CHEr105: Eastern Switzerland">Eastern Switzerland</span></td>
									<td class="proper">73.23</td>
								</tr>
								<tr>
									<td class="region"><span title="CHEr102: Espace Mittelland">Espace Mittelland</span></td>
									<td class="proper">72.93</td>
								</tr>
								<tr>
									<td class="region"><span title="CHEr101: Lake Geneva region">Lake Geneva region</span></td>
									<td class="proper">70.94</td>
								</tr>
								<tr>
									<td class="region"><span title="CHEr103: Northwestern Switzerland">Northwestern Switzerland</span></td>
									<td class="proper">72.70</td>
								</tr>
								<tr>
									<td class="region"><span title="CHEr107: Ticino">Ticino</span></td>
									<td class="proper">68.97</td>
								</tr>
								<tr>
									<td class="region"><span title="CHEr104: Zurich">Zurich</span></td>
									<td class="proper">72.26</td>
								</tr>
								<tr class="country">
									<th>Syrian Arab Republic (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="SYRt: Total">Total</span></td>
									<td class="proper">49.24</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="SYRr102: Rural Damascus">Rural Damascus</span></td>
									<td class="proper">41.65</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr111: Al Hasaka">Al Hasaka</span></td>
									<td class="proper">36.46</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr106: Al Latakia">Al Latakia</span></td>
									<td class="proper">69.70</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr114: Al Qunitara - Quneitra">Al Qunitara - Quneitra</span></td>
									<td class="proper">56.92</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr109: Al Raka-Raqqa">Al Raka-Raqqa</span></td>
									<td class="proper">41.67</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr112: Al Swida - Sweida">Al Swida - Sweida</span></td>
									<td class="proper">42.11</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr101: Damascus">Damascus</span></td>
									<td class="proper">45.81</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr113: Daraa">Daraa</span></td>
									<td class="proper">52.28</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr110: Der El Zour - Deir Ezzor">Der El Zour - Deir Ezzor</span></td>
									<td class="proper">36.38</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr107: Edlab Idleb">Edlab Idleb</span></td>
									<td class="proper">55.79</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr108: Halab - Aleppo">Halab - Aleppo</span></td>
									<td class="proper">47.50</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr104: Hamaa">Hamaa</span></td>
									<td class="proper">52.08</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr103: Homs">Homs</span></td>
									<td class="proper">42.07</td>
								</tr>
								<tr>
									<td class="region"><span title="SYRr105: Tartous">Tartous</span></td>
									<td class="proper">68.99</td>
								</tr>
								<tr class="country">
									<th>Tajikistan (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="TJKt: Total">Total</span></td>
									<td class="proper">56.94</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="TJKr104: DRS">DRS</span></td>
									<td class="proper">60.10</td>
								</tr>
								<tr>
									<td class="region"><span title="TJKr101: Duchanbe">Duchanbe</span></td>
									<td class="proper">52.34</td>
								</tr>
								<tr>
									<td class="region"><span title="TJKr105: GBAO">GBAO</span></td>
									<td class="proper">64.46</td>
								</tr>
								<tr>
									<td class="region"><span title="TJKr102: Khatlon">Khatlon</span></td>
									<td class="proper">47.50</td>
								</tr>
								<tr>
									<td class="region"><span title="TJKr103: Sughd (formerly Leninabad)">Sughd (formerly Leninabad)</span></td>
									<td class="proper">60.31</td>
								</tr>
								<tr class="country">
									<th>Tanzania (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="TZAt: Total">Total</span></td>
									<td class="proper">67.57</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="TZAr202:  Arusha, Manyara"> Arusha, Manyara</span></td>
									<td class="proper">61.13</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr207:  Dar Es Salam"> Dar Es Salam</span></td>
									<td class="proper">77.04</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr201:  Dodoma"> Dodoma</span></td>
									<td class="proper">59.25</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr211:  Iringa, Njombe"> Iringa, Njombe</span></td>
									<td class="proper">66.73</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr218:  Kagera"> Kagera</span></td>
									<td class="proper">69.51</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr216:  Kigoma"> Kigoma</span></td>
									<td class="proper">66.33</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr203:  Kilimanjaro"> Kilimanjaro</span></td>
									<td class="proper">66.16</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr208:  Lindi"> Lindi</span></td>
									<td class="proper">69.68</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr220:  Mara"> Mara</span></td>
									<td class="proper">61.24</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr212:  Mbeya"> Mbeya</span></td>
									<td class="proper">57.45</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr205:  Morogoro"> Morogoro</span></td>
									<td class="proper">67.60</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr209:  Mtwara"> Mtwara</span></td>
									<td class="proper">68.87</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr219:  Mwanza, Geita"> Mwanza, Geita</span></td>
									<td class="proper">63.96</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr224:  Pemba North"> Pemba North</span></td>
									<td class="proper">80.18</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr225:  Pemba South"> Pemba South</span></td>
									<td class="proper">80.04</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr206:  Pwani"> Pwani</span></td>
									<td class="proper">73.24</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr215:  Rukwa, Katavi"> Rukwa, Katavi</span></td>
									<td class="proper">61.44</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr210:  Ruvuma"> Ruvuma</span></td>
									<td class="proper">66.22</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr217:  Shinyanga, Simiyu"> Shinyanga, Simiyu</span></td>
									<td class="proper">54.00</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr213:  Singida"> Singida</span></td>
									<td class="proper">55.24</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr214:  Tabora"> Tabora</span></td>
									<td class="proper">55.02</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr204:  Tanga"> Tanga</span></td>
									<td class="proper">73.93</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr221:  Zanzibar North"> Zanzibar North</span></td>
									<td class="proper">79.76</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr222:  Zanzibar South"> Zanzibar South</span></td>
									<td class="proper">77.96</td>
								</tr>
								<tr>
									<td class="region"><span title="TZAr223:  Zanzibar West"> Zanzibar West</span></td>
									<td class="proper">77.38</td>
								</tr>
								<tr class="country">
									<th>Thailand (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="THAt: Total">Total</span></td>
									<td class="proper">77.52</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="THAr101: Bangkok">Bangkok</span></td>
									<td class="proper">75.43</td>
								</tr>
								<tr>
									<td class="region"><span title="THAr102: Central">Central</span></td>
									<td class="proper">77.13</td>
								</tr>
								<tr>
									<td class="region"><span title="THAr103: North">North</span></td>
									<td class="proper">76.70</td>
								</tr>
								<tr>
									<td class="region"><span title="THAr104: Northeast">Northeast</span></td>
									<td class="proper">74.78</td>
								</tr>
								<tr>
									<td class="region"><span title="THAr105: South">South</span></td>
									<td class="proper">83.57</td>
								</tr>
								<tr class="country">
									<th>Timor-Leste (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="TLSt: Total">Total</span></td>
									<td class="proper">80.43</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="TLSr101: Aileu">Aileu</span></td>
									<td class="proper">80.79</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr102: Ainaro">Ainaro</span></td>
									<td class="proper">80.87</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr103: Baucau">Baucau</span></td>
									<td class="proper">82.69</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr104: Bobonaro">Bobonaro</span></td>
									<td class="proper">80.69</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr105: Cova Lima">Cova Lima</span></td>
									<td class="proper">79.81</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr106: Dili">Dili</span></td>
									<td class="proper">78.25</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr107: Ermera">Ermera</span></td>
									<td class="proper">80.79</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr109: Lautem">Lautem</span></td>
									<td class="proper">81.74</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr108: Liquica">Liquica</span></td>
									<td class="proper">80.10</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr111: Manatuto">Manatuto</span></td>
									<td class="proper">80.95</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr110: Manufahi">Manufahi</span></td>
									<td class="proper">81.48</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr112: Oecussi">Oecussi</span></td>
									<td class="proper">75.47</td>
								</tr>
								<tr>
									<td class="region"><span title="TLSr113: Viqueque">Viqueque</span></td>
									<td class="proper">82.00</td>
								</tr>
								<tr class="country">
									<th>Togo (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="TGOt: Total">Total</span></td>
									<td class="proper">66.99</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="TGOr104: Centrale">Centrale</span></td>
									<td class="proper">62.38</td>
								</tr>
								<tr>
									<td class="region"><span title="TGOr105: Kara">Kara</span></td>
									<td class="proper">57.05</td>
								</tr>
								<tr>
									<td class="region"><span title="TGOr101: Lome">Lome</span></td>
									<td class="proper">82.35</td>
								</tr>
								<tr>
									<td class="region"><span title="TGOr102: Maritime">Maritime</span></td>
									<td class="proper">79.91</td>
								</tr>
								<tr>
									<td class="region"><span title="TGOr103: Plateaux">Plateaux</span></td>
									<td class="proper">71.31</td>
								</tr>
								<tr>
									<td class="region"><span title="TGOr106: Savanes">Savanes</span></td>
									<td class="proper">48.92</td>
								</tr>
								<tr class="country">
									<th>Tonga (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="TONt: Total">Total</span></td>
									<td class="proper">79.34</td>
								</tr>
								<tr class="country">
									<th>Trinidad and Tobago (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="TTOt: Total">Total</span></td>
									<td class="proper">81.40</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="TTOr103: Central">Central</span></td>
									<td class="proper">80.85</td>
								</tr>
								<tr>
									<td class="region"><span title="TTOr102: East">East</span></td>
									<td class="proper">82.52</td>
								</tr>
								<tr>
									<td class="region"><span title="TTOr101: North West">North West</span></td>
									<td class="proper">81.59</td>
								</tr>
								<tr>
									<td class="region"><span title="TTOr104: South West">South West</span></td>
									<td class="proper">81.82</td>
								</tr>
								<tr>
									<td class="region"><span title="TTOr105: Tobago">Tobago</span></td>
									<td class="proper">80.24</td>
								</tr>
								<tr class="country">
									<th>Tunisia (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="TUNt: Total">Total</span></td>
									<td class="proper">53.07</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="TUNr105: Centre Est (Sousse, Monastir, Mahdia, Sfax)">Centre Est (Sousse, Monastir, Mahdia, Sfax)</span></td>
									<td class="proper">57.75</td>
								</tr>
								<tr>
									<td class="region"><span title="TUNr104: Centre Ouest (Kairouan, Kasserine, Sidi Bouzid)">Centre Ouest (Kairouan, Kasserine, Sidi Bouzid)</span></td>
									<td class="proper">47.47</td>
								</tr>
								<tr>
									<td class="region"><span title="TUNr101: Grand Tunis (Tunis, Ariana, Ben Arous, Manouba)">Grand Tunis (Tunis, Ariana, Ben Arous, Manouba)</span></td>
									<td class="proper">65.29</td>
								</tr>
								<tr>
									<td class="region"><span title="TUNr102: Nord Est (Nabeul, Zaghouan, Bizerte)">Nord Est (Nabeul, Zaghouan, Bizerte)</span></td>
									<td class="proper">66.40</td>
								</tr>
								<tr>
									<td class="region"><span title="TUNr103: Nord Ouest (Beja, Jendouba, Kef, Siliana)">Nord Ouest (Beja, Jendouba, Kef, Siliana)</span></td>
									<td class="proper">54.92</td>
								</tr>
								<tr>
									<td class="region"><span title="TUNr107: Sud Est (Gabes, Medinine, Tataouine)">Sud Est (Gabes, Medinine, Tataouine)</span></td>
									<td class="proper">40.80</td>
								</tr>
								<tr>
									<td class="region"><span title="TUNr106: Sud Ouest (Gafsa, Tozeur, Kebili)">Sud Ouest (Gafsa, Tozeur, Kebili)</span></td>
									<td class="proper">38.88</td>
								</tr>
								<tr class="country">
									<th>Turkiye (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="TURt: Total">Total</span></td>
									<td class="proper">60.54</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="TURr103: Aegean (Afyon, Aydin, Denizli, Izmir, Kutahya, Man">Aegean (Afyon, Aydin, Denizli, Izmir, Kutahya, Man</span></td>
									<td class="proper">55.52</td>
								</tr>
								<tr>
									<td class="region"><span title="TURr107: Central Anatolia (Kayseri, Kirsehir, Nevsehir, Nig">Central Anatolia (Kayseri, Kirsehir, Nevsehir, Nig</span></td>
									<td class="proper">57.75</td>
								</tr>
								<tr>
									<td class="region"><span title="TURr111: Central East Anatolia (Bingol, Bitlis, Elazig, Hak">Central East Anatolia (Bingol, Bitlis, Elazig, Hak</span></td>
									<td class="proper">49.72</td>
								</tr>
								<tr>
									<td class="region"><span title="TURr109: East Black Sea (Artvin, Giresun, Gumushane, Ordu,">East Black Sea (Artvin, Giresun, Gumushane, Ordu,</span></td>
									<td class="proper">73.08</td>
								</tr>
								<tr>
									<td class="region"><span title="TURr104: East Marmara (Bilecik, Bolu, Bursa, Duzce, Eskiseh">East Marmara (Bilecik, Bolu, Bursa, Duzce, Eskiseh</span></td>
									<td class="proper">67.77</td>
								</tr>
								<tr>
									<td class="region"><span title="TURr101: Istanbul">Istanbul</span></td>
									<td class="proper">72.82</td>
								</tr>
								<tr>
									<td class="region"><span title="TURr106: Mediterranean (Adana, Antalya, Burdur, Hatay, Ispa">Mediterranean (Adana, Antalya, Burdur, Hatay, Ispa</span></td>
									<td class="proper">58.25</td>
								</tr>
								<tr>
									<td class="region"><span title="TURr110: North East Anatolia (Agri, Erzincan, Erzurum, Kars">North East Anatolia (Agri, Erzincan, Erzurum, Kars</span></td>
									<td class="proper">58.93</td>
								</tr>
								<tr>
									<td class="region"><span title="TURr112: South East Anatolia (Adiyaman, Diyarbakir, Gaziant">South East Anatolia (Adiyaman, Diyarbakir, Gaziant</span></td>
									<td class="proper">42.61</td>
								</tr>
								<tr>
									<td class="region"><span title="TURr105: West Anatolia (Ankara, Konya, Karaman)">West Anatolia (Ankara, Konya, Karaman)</span></td>
									<td class="proper">53.93</td>
								</tr>
								<tr>
									<td class="region"><span title="TURr108: West Black Sea (Amasya, Cankiri, Corum, Kastamonu,">West Black Sea (Amasya, Cankiri, Corum, Kastamonu,</span></td>
									<td class="proper">67.81</td>
								</tr>
								<tr>
									<td class="region"><span title="TURr102: West Marmara (Balikesir, Canakkale, Edirne, Kirkla">West Marmara (Balikesir, Canakkale, Edirne, Kirkla</span></td>
									<td class="proper">68.28</td>
								</tr>
								<tr class="country">
									<th>Turkmenistan (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="TKMt: Total">Total</span></td>
									<td class="proper">43.03</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="TKMr102: Akhal">Akhal</span></td>
									<td class="proper">40.22</td>
								</tr>
								<tr>
									<td class="region"><span title="TKMr101: Ashgabat City">Ashgabat City</span></td>
									<td class="proper">48.33</td>
								</tr>
								<tr>
									<td class="region"><span title="TKMr103: Balkan">Balkan</span></td>
									<td class="proper">47.73</td>
								</tr>
								<tr>
									<td class="region"><span title="TKMr104: Dashoguz">Dashoguz</span></td>
									<td class="proper">42.82</td>
								</tr>
								<tr>
									<td class="region"><span title="TKMr105: Lebap">Lebap</span></td>
									<td class="proper">38.88</td>
								</tr>
								<tr>
									<td class="region"><span title="TKMr106: Mary">Mary</span></td>
									<td class="proper">40.21</td>
								</tr>
								<tr class="country">
									<th>Turks &amp; Caicos Islands (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="TCAt: Total">Total</span></td>
									<td class="proper">78.76</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="TCAr102: Caicos">Caicos</span></td>
									<td class="proper">78.68</td>
								</tr>
								<tr>
									<td class="region"><span title="TCAr103: Providenciales">Providenciales</span></td>
									<td class="proper">78.52</td>
								</tr>
								<tr>
									<td class="region"><span title="TCAr101: Turks islands">Turks islands</span></td>
									<td class="proper">79.07</td>
								</tr>
								<tr class="country">
									<th>Uganda (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="UGAt: Total">Total</span></td>
									<td class="proper">69.21</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="UGAr101: Central 1 (Central South)">Central 1 (Central South)</span></td>
									<td class="proper">72.32</td>
								</tr>
								<tr>
									<td class="region"><span title="UGAr102: Central 2 (Central North)">Central 2 (Central North)</span></td>
									<td class="proper">71.41</td>
								</tr>
								<tr>
									<td class="region"><span title="UGAr104: East Central (Busoga)">East Central (Busoga)</span></td>
									<td class="proper">76.85</td>
								</tr>
								<tr>
									<td class="region"><span title="UGAr105: Eastern (Bukedi, Bugishu, Teso)">Eastern (Bukedi, Bugishu, Teso)</span></td>
									<td class="proper">66.20</td>
								</tr>
								<tr>
									<td class="region"><span title="UGAr103: Kampala">Kampala</span></td>
									<td class="proper">77.49</td>
								</tr>
								<tr>
									<td class="region"><span title="UGAr106: North (Karamoja, Lango, Acholi)">North (Karamoja, Lango, Acholi)</span></td>
									<td class="proper">58.81</td>
								</tr>
								<tr>
									<td class="region"><span title="UGAr109: Southwest (Ankole, Kigezi)">Southwest (Ankole, Kigezi)</span></td>
									<td class="proper">69.62</td>
								</tr>
								<tr>
									<td class="region"><span title="UGAr107: West Nile">West Nile</span></td>
									<td class="proper">61.31</td>
								</tr>
								<tr>
									<td class="region"><span title="UGAr108: Western (Bunyoro, Tooro)">Western (Bunyoro, Tooro)</span></td>
									<td class="proper">68.92</td>
								</tr>
								<tr class="country">
									<th>Ukraine (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="UKRt: Total">Total</span></td>
									<td class="proper">69.71</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="UKRr102: Central">Central</span></td>
									<td class="proper">69.64</td>
								</tr>
								<tr>
									<td class="region"><span title="UKRr103: East">East</span></td>
									<td class="proper">66.52</td>
								</tr>
								<tr>
									<td class="region"><span title="UKRr101: North">North</span></td>
									<td class="proper">71.84</td>
								</tr>
								<tr>
									<td class="region"><span title="UKRr104: South">South</span></td>
									<td class="proper">68.35</td>
								</tr>
								<tr>
									<td class="region"><span title="UKRr105: West">West</span></td>
									<td class="proper">72.19</td>
								</tr>
								<tr class="country">
									<th>United Arab Emirates (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="AREt: Total">Total</span></td>
									<td class="proper">43.25</td>
								</tr>
								<tr class="country">
									<th>United Kingdom (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="GBRt: Total">Total</span></td>
									<td class="proper">78.80</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="GBRr104: East Midlands">East Midlands</span></td>
									<td class="proper">76.11</td>
								</tr>
								<tr>
									<td class="region"><span title="GBRr106: East of England">East of England</span></td>
									<td class="proper">76.19</td>
								</tr>
								<tr>
									<td class="region"><span title="GBRr107: London">London</span></td>
									<td class="proper">75.71</td>
								</tr>
								<tr>
									<td class="region"><span title="GBRr101: North East">North East</span></td>
									<td class="proper">79.91</td>
								</tr>
								<tr>
									<td class="region"><span title="GBRr102: North West">North West</span></td>
									<td class="proper">81.13</td>
								</tr>
								<tr>
									<td class="region"><span title="GBRr112: Northern Ireland">Northern Ireland</span></td>
									<td class="proper">81.80</td>
								</tr>
								<tr>
									<td class="region"><span title="GBRr111: Scotland">Scotland</span></td>
									<td class="proper">81.89</td>
								</tr>
								<tr>
									<td class="region"><span title="GBRr108: South East">South East</span></td>
									<td class="proper">76.74</td>
								</tr>
								<tr>
									<td class="region"><span title="GBRr109: South West">South West</span></td>
									<td class="proper">78.99</td>
								</tr>
								<tr>
									<td class="region"><span title="GBRr110: Wales">Wales</span></td>
									<td class="proper">80.72</td>
								</tr>
								<tr>
									<td class="region"><span title="GBRr105: West Midlands">West Midlands</span></td>
									<td class="proper">77.37</td>
								</tr>
								<tr>
									<td class="region"><span title="GBRr103: Yorkshire and The Humber">Yorkshire and The Humber</span></td>
									<td class="proper">79.03</td>
								</tr>
								<tr class="country">
									<th>United States (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="USAt: Total">Total</span></td>
									<td class="proper">60.74</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="USAr101: Alabama">Alabama</span></td>
									<td class="proper">66.06</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr102: Alaska">Alaska</span></td>
									<td class="proper">74.33</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr103: Arizona">Arizona</span></td>
									<td class="proper">31.40</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr104: Arkansas">Arkansas</span></td>
									<td class="proper">62.90</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr105: California">California</span></td>
									<td class="proper">42.17</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr106: Colorado">Colorado</span></td>
									<td class="proper">45.54</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr107: Connecticut">Connecticut</span></td>
									<td class="proper">63.77</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr108: Delaware">Delaware</span></td>
									<td class="proper">65.59</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr109: District of Columbia">District of Columbia</span></td>
									<td class="proper">62.67</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr110: Florida">Florida</span></td>
									<td class="proper">71.78</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr111: Georgia">Georgia</span></td>
									<td class="proper">64.80</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr112: Hawaii">Hawaii</span></td>
									<td class="proper">76.07</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr113: Idaho">Idaho</span></td>
									<td class="proper">54.71</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr114: Illinois">Illinois</span></td>
									<td class="proper">65.24</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr115: Indiana">Indiana</span></td>
									<td class="proper">64.47</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr116: Iowa">Iowa</span></td>
									<td class="proper">62.79</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr117: Kansas">Kansas</span></td>
									<td class="proper">51.41</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr118: Kentucky">Kentucky</span></td>
									<td class="proper">63.41</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr119: Louisiana">Louisiana</span></td>
									<td class="proper">68.17</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr120: Maine">Maine</span></td>
									<td class="proper">71.07</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr121: Maryland">Maryland</span></td>
									<td class="proper">65.44</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr122: Massachusetts">Massachusetts</span></td>
									<td class="proper">64.69</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr123: Michigan">Michigan</span></td>
									<td class="proper">72.42</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr124: Minnesota">Minnesota</span></td>
									<td class="proper">67.57</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr125: Mississippi">Mississippi</span></td>
									<td class="proper">66.52</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr126: Missouri">Missouri</span></td>
									<td class="proper">62.16</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr127: Montana">Montana</span></td>
									<td class="proper">56.13</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr128: Nebraska">Nebraska</span></td>
									<td class="proper">51.20</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr129: Nevada">Nevada</span></td>
									<td class="proper">34.49</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr130: New Hampshire">New Hampshire</span></td>
									<td class="proper">65.65</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr131: New Jersey">New Jersey</span></td>
									<td class="proper">62.58</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr132: New Mexico">New Mexico</span></td>
									<td class="proper">35.65</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr133: New York">New York</span></td>
									<td class="proper">68.24</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr134: North Carolina">North Carolina</span></td>
									<td class="proper">66.02</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr135: North Dakota">North Dakota</span></td>
									<td class="proper">65.49</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr136: Ohio">Ohio</span></td>
									<td class="proper">65.85</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr137: Oklahoma">Oklahoma</span></td>
									<td class="proper">54.00</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr138: Oregon">Oregon</span></td>
									<td class="proper">56.51</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr139: Pennsylvania">Pennsylvania</span></td>
									<td class="proper">64.90</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr140: Rhode Island">Rhode Island</span></td>
									<td class="proper">66.88</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr141: South Carolina">South Carolina</span></td>
									<td class="proper">65.52</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr142: South Dakota">South Dakota</span></td>
									<td class="proper">57.33</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr143: Tennessee">Tennessee</span></td>
									<td class="proper">63.44</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr144: Texas">Texas</span></td>
									<td class="proper">50.17</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr145: Utah">Utah</span></td>
									<td class="proper">38.71</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr146: Vermont">Vermont</span></td>
									<td class="proper">67.66</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr147: Virginia">Virginia</span></td>
									<td class="proper">64.06</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr148: Washington">Washington</span></td>
									<td class="proper">63.13</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr149: West Virginia">West Virginia</span></td>
									<td class="proper">67.16</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr150: Wisconsin">Wisconsin</span></td>
									<td class="proper">68.38</td>
								</tr>
								<tr>
									<td class="region"><span title="USAr151: Wyoming">Wyoming</span></td>
									<td class="proper">51.48</td>
								</tr>
								<tr class="country">
									<th>Uruguay (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="URYt: Total">Total</span></td>
									<td class="proper">71.76</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="URYr105: Centro (Durazno and Tacuarembo)">Centro (Durazno and Tacuarembo)</span></td>
									<td class="proper">72.24</td>
								</tr>
								<tr>
									<td class="region"><span title="URYr106: Centro Sur (Flores, Florida and Lavalleja)">Centro Sur (Flores, Florida and Lavalleja)</span></td>
									<td class="proper">73.59</td>
								</tr>
								<tr>
									<td class="region"><span title="URYr103: Costa Este (Canelones, Maldonado and Rocha)">Costa Este (Canelones, Maldonado and Rocha)</span></td>
									<td class="proper">76.12</td>
								</tr>
								<tr>
									<td class="region"><span title="URYr107: Litoral Norte (Paysandu, Salto and Rio Negro)">Litoral Norte (Paysandu, Salto and Rio Negro)</span></td>
									<td class="proper">67.60</td>
								</tr>
								<tr>
									<td class="region"><span title="URYr104: Litoral Sur (Soriano, Colonia and San Jose)">Litoral Sur (Soriano, Colonia and San Jose)</span></td>
									<td class="proper">68.64</td>
								</tr>
								<tr>
									<td class="region"><span title="URYr101: Montevideo and Metropolitan area">Montevideo and Metropolitan area</span></td>
									<td class="proper">72.63</td>
								</tr>
								<tr>
									<td class="region"><span title="URYr102: Norte (Artigas, Rivera, Cerro Largo and Trienta y Tres)">Norte (Artigas, Rivera, Cerro Largo and Trienta y Tres)</span></td>
									<td class="proper">71.48</td>
								</tr>
								<tr class="country">
									<th>Uzbekistan (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="UZBt: Total">Total</span></td>
									<td class="proper">49.26</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="UZBr102: Central (Navoi, Bukhara, Samarkand)">Central (Navoi, Bukhara, Samarkand)</span></td>
									<td class="proper">42.60</td>
								</tr>
								<tr>
									<td class="region"><span title="UZBr104: Central-East (Dzhizak, Syrdarya)">Central-East (Dzhizak, Syrdarya)</span></td>
									<td class="proper">55.36</td>
								</tr>
								<tr>
									<td class="region"><span title="UZBr105: East (Namangan, Fergana, Andizhan)">East (Namangan, Fergana, Andizhan)</span></td>
									<td class="proper">48.95</td>
								</tr>
								<tr>
									<td class="region"><span title="UZBr103: South (Kashkadarya, Surkhandarya)">South (Kashkadarya, Surkhandarya)</span></td>
									<td class="proper">47.79</td>
								</tr>
								<tr>
									<td class="region"><span title="UZBr106: Tashkent">Tashkent</span></td>
									<td class="proper">54.98</td>
								</tr>
								<tr>
									<td class="region"><span title="UZBr101: West (Karakalpakstan, Khorezm)">West (Karakalpakstan, Khorezm)</span></td>
									<td class="proper">45.88</td>
								</tr>
								<tr class="country">
									<th>Vanuatu (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="VUTt: Total">Total</span></td>
									<td class="proper">82.60</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="VUTr103: Malampa">Malampa</span></td>
									<td class="proper">82.82</td>
								</tr>
								<tr>
									<td class="region"><span title="VUTr104: Penama">Penama</span></td>
									<td class="proper">82.30</td>
								</tr>
								<tr>
									<td class="region"><span title="VUTr105: Sanma">Sanma</span></td>
									<td class="proper">86.23</td>
								</tr>
								<tr>
									<td class="region"><span title="VUTr102: Shefa">Shefa</span></td>
									<td class="proper">81.16</td>
								</tr>
								<tr>
									<td class="region"><span title="VUTr101: Tafea">Tafea</span></td>
									<td class="proper">81.05</td>
								</tr>
								<tr>
									<td class="region"><span title="VUTr106: Torba">Torba</span></td>
									<td class="proper">82.06</td>
								</tr>
								<tr class="country">
									<th>Vatican City (Europe)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="VATt: Total">Total</span></td>
									<td class="proper">64.71</td>
								</tr>
								<tr class="country">
									<th>Venezuela, RB (America)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="VENt: Total">Total</span></td>
									<td class="proper">77.72</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="VENr110: Amacuros Delta Federal Territory">Amacuros Delta Federal Territory</span></td>
									<td class="proper">85.47</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr102: Amazonas Federal Territory">Amazonas Federal Territory</span></td>
									<td class="proper">84.58</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr103: Anzoategui">Anzoategui</span></td>
									<td class="proper">71.26</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr104: Apure">Apure</span></td>
									<td class="proper">71.96</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr105: Aragua">Aragua</span></td>
									<td class="proper">73.06</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr106: Barinas">Barinas</span></td>
									<td class="proper">72.01</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr107: Bolivar">Bolivar</span></td>
									<td class="proper">81.08</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr108: Carabobo">Carabobo</span></td>
									<td class="proper">81.00</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr109: Cojedes">Cojedes</span></td>
									<td class="proper">67.37</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr111: Falcon">Falcon</span></td>
									<td class="proper">73.92</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr101: Federal District">Federal District</span></td>
									<td class="proper">80.77</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr112: Guarico">Guarico</span></td>
									<td class="proper">65.98</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr113: Lara">Lara</span></td>
									<td class="proper">70.85</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr114: Merida">Merida</span></td>
									<td class="proper">84.86</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr115: Miranda">Miranda</span></td>
									<td class="proper">81.56</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr116: Monagas">Monagas</span></td>
									<td class="proper">80.26</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr117: Nueva Esparta">Nueva Esparta</span></td>
									<td class="proper">84.76</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr118: Portuguesa">Portuguesa</span></td>
									<td class="proper">69.93</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr119: Sucre">Sucre</span></td>
									<td class="proper">82.64</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr120: Tachira">Tachira</span></td>
									<td class="proper">81.01</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr121: Trujillo">Trujillo</span></td>
									<td class="proper">81.13</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr124: Vargas">Vargas</span></td>
									<td class="proper">80.95</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr122: Yaracuy">Yaracuy</span></td>
									<td class="proper">80.72</td>
								</tr>
								<tr>
									<td class="region"><span title="VENr123: Zulia">Zulia</span></td>
									<td class="proper">78.28</td>
								</tr>
								<tr class="country">
									<th>Viet Nam (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="VNMt: Total">Total</span></td>
									<td class="proper">80.17</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="VNMr104: Central Highlands">Central Highlands</span></td>
									<td class="proper">79.13</td>
								</tr>
								<tr>
									<td class="region"><span title="VNMr106: Mekong River Delta">Mekong River Delta</span></td>
									<td class="proper">80.44</td>
								</tr>
								<tr>
									<td class="region"><span title="VNMr103: North Central Coast and South Central Coast">North Central Coast and South Central Coast</span></td>
									<td class="proper">81.88</td>
								</tr>
								<tr>
									<td class="region"><span title="VNMr102: North East, North West">North East, North West</span></td>
									<td class="proper">81.84</td>
								</tr>
								<tr>
									<td class="region"><span title="VNMr101: Red River Delta">Red River Delta</span></td>
									<td class="proper">79.34</td>
								</tr>
								<tr>
									<td class="region"><span title="VNMr105: South East">South East</span></td>
									<td class="proper">78.41</td>
								</tr>
								<tr class="country">
									<th>West Bank and Gaza (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="PSEt: Total">Total</span></td>
									<td class="proper">61.31</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="PSEr104: Bethlehem, Hebron">Bethlehem, Hebron</span></td>
									<td class="proper">55.56</td>
								</tr>
								<tr>
									<td class="region"><span title="PSEr106: Deir El-Balah, Khan Yunis, Rafah">Deir El-Balah, Khan Yunis, Rafah</span></td>
									<td class="proper">64.90</td>
								</tr>
								<tr>
									<td class="region"><span title="PSEr101: Jenin, Tubas, Tulkarm, Nablus, Qalqiliya">Jenin, Tubas, Tulkarm, Nablus, Qalqiliya</span></td>
									<td class="proper">62.02</td>
								</tr>
								<tr>
									<td class="region"><span title="PSEr103: Jerusalem">Jerusalem</span></td>
									<td class="proper">57.11</td>
								</tr>
								<tr>
									<td class="region"><span title="PSEr105: North Gaza, Gaza">North Gaza, Gaza</span></td>
									<td class="proper">69.25</td>
								</tr>
								<tr>
									<td class="region"><span title="PSEr102: Salfit, Ramallah, Al-Bireh, Jericho, Al Aghwar">Salfit, Ramallah, Al-Bireh, Jericho, Al Aghwar</span></td>
									<td class="proper">59.05</td>
								</tr>
								<tr class="country">
									<th>Yemen, Rep. (Asia/Pacific)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="YEMt: Total">Total</span></td>
									<td class="proper">46.45</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="YEMr102: Abyan, Aden (town and countryside), Lahej, Ad Dali (Al Dhalih)">Abyan, Aden (town and countryside), Lahej, Ad Dali (Al Dhalih)</span></td>
									<td class="proper">54.19</td>
								</tr>
								<tr>
									<td class="region"><span title="YEMr104: Beida (Al Bayda), Dhamar, Raimah">Beida (Al Bayda), Dhamar, Raimah</span></td>
									<td class="proper">40.86</td>
								</tr>
								<tr>
									<td class="region"><span title="YEMr107: Hajja, Sada, Amran (Omran)">Hajja, Sada, Amran (Omran)</span></td>
									<td class="proper">43.81</td>
								</tr>
								<tr>
									<td class="region"><span title="YEMr108: Hodeida (Al Hudaydah), Mahweit (Al Mahwit)">Hodeida (Al Hudaydah), Mahweit (Al Mahwit)</span></td>
									<td class="proper">59.74</td>
								</tr>
								<tr>
									<td class="region"><span title="YEMr101: Ibb">Ibb</span></td>
									<td class="proper">51.18</td>
								</tr>
								<tr>
									<td class="region"><span title="YEMr106: Jawf, Hadramet, Shabda (Shabwah), Marib, Mohra (Al Mahrah), Socotra">Jawf, Hadramet, Shabda (Shabwah), Marib, Mohra (Al Mahrah), Socotra</span></td>
									<td class="proper">32.73</td>
								</tr>
								<tr>
									<td class="region"><span title="YEMr103: Sana a (capital)">Sana a (capital)</span></td>
									<td class="proper">35.26</td>
								</tr>
								<tr>
									<td class="region"><span title="YEMr105: Taiz">Taiz</span></td>
									<td class="proper">53.80</td>
								</tr>
								<tr class="country">
									<th>Zambia (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ZMBt: Total">Total</span></td>
									<td class="proper">58.69</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ZMBr101: Central">Central</span></td>
									<td class="proper">60.09</td>
								</tr>
								<tr>
									<td class="region"><span title="ZMBr102: Copperbelt">Copperbelt</span></td>
									<td class="proper">59.35</td>
								</tr>
								<tr>
									<td class="region"><span title="ZMBr103: Eastern">Eastern</span></td>
									<td class="proper">57.92</td>
								</tr>
								<tr>
									<td class="region"><span title="ZMBr104: Luapula">Luapula</span></td>
									<td class="proper">60.47</td>
								</tr>
								<tr>
									<td class="region"><span title="ZMBr105: Lusaka">Lusaka</span></td>
									<td class="proper">59.63</td>
								</tr>
								<tr>
									<td class="region"><span title="ZMBr107: North-Western">North-Western</span></td>
									<td class="proper">58.58</td>
								</tr>
								<tr>
									<td class="region"><span title="ZMBr106: Northern">Northern</span></td>
									<td class="proper">60.23</td>
								</tr>
								<tr>
									<td class="region"><span title="ZMBr108: Southern">Southern</span></td>
									<td class="proper">58.42</td>
								</tr>
								<tr>
									<td class="region"><span title="ZMBr109: Western">Western</span></td>
									<td class="proper">53.52</td>
								</tr>
								<tr class="country">
									<th>Zimbabwe (Africa)</th>
									<th colspan="1">&nbsp;</th>
								</tr>
								<tr>
									<td class="region"><span title="ZWEt: Total">Total</span></td>
									<td class="proper">58.81</td>
								</tr>
								<tr class="subseparator">
									<td class="region"><span title="ZWEr110: Bulawayo">Bulawayo</span></td>
									<td class="proper">55.58</td>
								</tr>
								<tr>
									<td class="region"><span title="ZWEr109: Harare">Harare</span></td>
									<td class="proper">61.53</td>
								</tr>
								<tr>
									<td class="region"><span title="ZWEr101: Manicaland">Manicaland</span></td>
									<td class="proper">67.06</td>
								</tr>
								<tr>
									<td class="region"><span title="ZWEr102: Mashonaland Central">Mashonaland Central</span></td>
									<td class="proper">58.99</td>
								</tr>
								<tr>
									<td class="region"><span title="ZWEr103: Mashonaland East">Mashonaland East</span></td>
									<td class="proper">62.17</td>
								</tr>
								<tr>
									<td class="region"><span title="ZWEr104: Mashonaland West">Mashonaland West</span></td>
									<td class="proper">57.08</td>
								</tr>
								<tr>
									<td class="region"><span title="ZWEr108: Masvingo">Masvingo</span></td>
									<td class="proper">61.39</td>
								</tr>
								<tr>
									<td class="region"><span title="ZWEr105: Matebeleland North">Matebeleland North</span></td>
									<td class="proper">53.03</td>
								</tr>
								<tr>
									<td class="region"><span title="ZWEr106: Matebeleland South">Matebeleland South</span></td>
									<td class="proper">54.35</td>
								</tr>
								<tr>
									<td class="region"><span title="ZWEr107: Midlands">Midlands</span></td>
									<td class="proper">56.96</td>
								</tr></tbody>
"""


# Parse the HTML content
# Parse the HTML content for countries and values
soup = BeautifulSoup(data, 'html.parser')

# Extract country names and their corresponding total humidity values
rows = []
current_country = None

for row in soup.find_all('tr'):
    if 'class' in row.attrs and 'country' in row['class']:
        # Update the current country
        current_country = row.find('th').text.strip()
    else:
        # Extract value if available
        region = row.find('td', class_='region')
        value = row.find('td', class_='proper')
        if region and value:
            # Check if the region contains "Total"
            if "Total" in region.text.strip():
                rows.append([current_country.split('(')[0].strip(), value.text.strip()])

# Write to CSV
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Country', 'Value'])
    writer.writerows(rows)