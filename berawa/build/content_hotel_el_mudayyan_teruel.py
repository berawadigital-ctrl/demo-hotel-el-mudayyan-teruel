# Contenido de la demo Hotel El Mudayyan (Teruel) (es/en/fr/de). Hechos de elmudayyan.com leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el hotel real.','en':' Images are illustrations and do not show the actual hotel.','fr':' Les images sont des illustrations et ne montrent pas l’hôtel réel.','de':' Die Bilder sind Illustrationen und zeigen nicht das tatsächliche Hotel.'}
H={'es':['Habitación doble estándar','Habitación doble superior','Habitación familiar'],'en':['Standard double room','Superior double room','Family room'],'fr':['Chambre double standard','Chambre double supérieure','Chambre familiale'],'de':['Doppelzimmer Standard','Doppelzimmer Superior','Familienzimmer']}
RD={
'es':['Para una o dos personas, con cama de matrimonio o dos camas. En estilo mudéjar o modernista y adaptada a personas con movilidad reducida.','Para dos adultos o dos adultos con un niño en cama supletoria, con cama de matrimonio o dos camas. Más amplia que la estándar.','Más amplia, equipada para tres o cuatro personas (quíntuples bajo petición). Adaptada a personas con movilidad reducida.'],
'en':['For one or two guests, with a double bed or two beds. In Mudéjar or Modernist style and adapted for guests with reduced mobility.','For two adults or two adults with a child on an extra bed, with a double bed or two beds. More spacious than the standard room.','More spacious, equipped for three or four guests (rooms for five on request). Adapted for guests with reduced mobility.'],
'fr':['Pour une ou deux personnes, avec un lit double ou deux lits. De style mudéjar ou moderniste et adaptée aux personnes à mobilité réduite.','Pour deux adultes ou deux adultes avec un enfant en lit d’appoint, avec un lit double ou deux lits. Plus spacieuse que la standard.','Plus spacieuse, équipée pour trois ou quatre personnes (cinq sur demande). Adaptée aux personnes à mobilité réduite.'],
'de':['Für eine oder zwei Personen, mit Doppelbett oder zwei Betten. Im Mudéjar- oder Jugendstil und barrierefrei für Personen mit eingeschränkter Mobilität.','Für zwei Erwachsene oder zwei Erwachsene mit einem Kind im Zustellbett, mit Doppelbett oder zwei Betten. Geräumiger als das Standardzimmer.','Geräumiger, ausgestattet für drei oder vier Personen (fünf auf Anfrage). Barrierefrei für Personen mit eingeschränkter Mobilität.']}
ART={
'hero':('arches',9411,['#1d1a1f','#a35a3c','#efd9bf','#6b4334','#41302a','#221b18']),
'intro':('columns',9412,['#f3ede4','#fbf7f1','#8f4f35','#5e3a2b','#2b1f1a']),
'r1':('arches',9421,['#eee5d8','#cf9a70','#8f4f35','#5e3a2b','#2b1f1a']),
'r2':('skyline',9422,['#1d1a1f','#b76c48','#f0dcc4','#714b3a','#48352c','#241c18']),
'r3':('columns',9423,['#efe6da','#f8f1e7','#9a5a3d','#66412f','#2c201a']),
'g1':('skyline',9431,['#1d1a1f','#a35a3c','#efd9bf','#6b4334','#41302a','#221b18']),
'g2':('hills',9432,['#ebe2d4','#f0dfc6','#cf9a70','#a0866a','#74604c','#4a3d31']),
'g3':('arches',9433,['#f2ebe1','#faf4ec','#9a5a3d','#66412f','#2c201a']),
'g4':('waves',9434,['#1d1a1f','#b76c48','#f0dcc4','#714b3a','#48352c','#241c18'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Hotel El Mudayyan · Hotel con encanto en el centro de Teruel',see_rooms='Ver las habitaciones',hero_k='Teruel · Calle Nueva, 18',hero_t='El encanto en el centro de Teruel',hero_s='Pequeño hotel de 3 estrellas, coqueto y de ambiente familiar, en pleno centro histórico.',
 intro_t='Dos hoteles en uno: el mudéjar y el modernista',intro_p1='El Mudayyan tiene 28 acogedoras habitaciones de dos estilos: mudéjar y modernista. Su fachada modernista es obra del arquitecto Pablo Monguió.',
 intro_p2='En el sótano hay un conjunto arqueológico del siglo XIV, con un pasadizo que en la Edad Media unía la casa del sacerdote con la iglesia del Salvador. Se puede visitar con una visita guiada.',
 stats=['Centro histórico de Teruel','28 habitaciones','Wifi gratis','Recepción 24/7'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Todas con wifi gratis, aire acondicionado, minibar, secador de pelo, TV y baño privado.',
 svcs=['Visita guiada por la galería medieval','Desayuno básico gratis reservando en su web, por teléfono o por correo','Tetería y cafetería','Salas privadas para reuniones y celebraciones','Excursiones a Albarracín y Mora de Rubielos','Wifi gratuito'],
 loc_p='Calle Nueva, 18 · 44001 Teruel. Recepción: 978 62 30 42. WhatsApp: 628 473 662. Correo: info@elmudayyan.com.',
 chips=['¿Qué habitaciones tenéis?','¿Hay habitaciones familiares?','¿Hay desayuno?','¿Cómo reservo?']),
'en':dict(title='Hotel El Mudayyan · Charming hotel in central Teruel',see_rooms='See the rooms',hero_k='Teruel · Calle Nueva, 18',hero_t='Charm in the centre of Teruel',hero_s='A small, cosy 3-star hotel with a family atmosphere, right in the historic centre.',
 intro_t='Two hotels in one: Mudéjar and Modernist',intro_p1='El Mudayyan has 28 cosy rooms in two styles: Mudéjar and Modernist. Its Modernist façade was designed by the architect Pablo Monguió.',
 intro_p2='The basement holds a fourteenth-century archaeological site, with a passage that in the Middle Ages linked the priest’s house to the church of El Salvador. It can be seen on a guided tour.',
 stats=['Historic centre of Teruel','28 rooms','Free wifi','Reception 24/7'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='All with free wifi, air conditioning, minibar, hairdryer, TV and private bathroom.',
 svcs=['Guided tour of the medieval gallery','Free basic breakfast when booking on their website, by phone or by email','Tea room and café','Private rooms for meetings and celebrations','Excursions to Albarracín and Mora de Rubielos','Free wifi'],
 loc_p='Calle Nueva, 18 · 44001 Teruel. Reception: +34 978 62 30 42. WhatsApp: +34 628 473 662. Email: info@elmudayyan.com.',
 chips=['Which rooms do you have?','Do you have family rooms?','Is there breakfast?','How do I book?']),
'fr':dict(title='Hôtel El Mudayyan · Hôtel de charme au centre de Teruel',see_rooms='Voir les chambres',hero_k='Teruel · Calle Nueva, 18',hero_t='Le charme au centre de Teruel',hero_s='Petit hôtel 3 étoiles, coquet et à l’ambiance familiale, en plein centre historique.',
 intro_t='Deux hôtels en un : le mudéjar et le moderniste',intro_p1='El Mudayyan compte 28 chambres accueillantes de deux styles : mudéjar et moderniste. Sa façade moderniste est l’œuvre de l’architecte Pablo Monguió.',
 intro_p2='Le sous-sol abrite un ensemble archéologique du XIVe siècle, avec un passage qui reliait au Moyen Âge la maison du prêtre à l’église du Salvador. On peut le découvrir en visite guidée.',
 stats=['Centre historique de Teruel','28 chambres','Wifi gratuit','Réception 24h/24'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Toutes avec wifi gratuit, climatisation, minibar, sèche-cheveux, TV et salle de bains privée.',
 svcs=['Visite guidée de la galerie médiévale','Petit-déjeuner basique offert en réservant sur leur site, par téléphone ou par e-mail','Salon de thé et cafétéria','Salles privées pour réunions et célébrations','Excursions à Albarracín et Mora de Rubielos','Wifi gratuit'],
 loc_p='Calle Nueva, 18 · 44001 Teruel. Réception : +34 978 62 30 42. WhatsApp : +34 628 473 662. E-mail : info@elmudayyan.com.',
 chips=['Quelles chambres avez-vous ?','Avez-vous des chambres familiales ?','Y a-t-il un petit-déjeuner ?','Comment réserver ?']),
'de':dict(title='Hotel El Mudayyan · Charmantes Hotel im Zentrum von Teruel',see_rooms='Zimmer ansehen',hero_k='Teruel · Calle Nueva, 18',hero_t='Charme im Zentrum von Teruel',hero_s='Kleines, gemütliches 3-Sterne-Hotel mit familiärer Atmosphäre, mitten im historischen Zentrum.',
 intro_t='Zwei Hotels in einem: Mudéjar und Jugendstil',intro_p1='El Mudayyan hat 28 gemütliche Zimmer in zwei Stilen: Mudéjar und Jugendstil. Die Jugendstilfassade stammt vom Architekten Pablo Monguió.',
 intro_p2='Im Keller liegt eine archäologische Anlage aus dem XIV. Jahrhundert mit einem Gang, der im Mittelalter das Haus des Priesters mit der Kirche El Salvador verband. Sie lässt sich bei einer Führung besichtigen.',
 stats=['Historisches Zentrum von Teruel','28 Zimmer','Kostenloses WLAN','Rezeption rund um die Uhr'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Alle mit kostenlosem WLAN, Klimaanlage, Minibar, Haartrockner, TV und eigenem Bad.',
 svcs=['Führung durch die mittelalterliche Galerie','Kostenloses einfaches Frühstück bei Buchung über die Website, per Telefon oder E-Mail','Teestube und Café','Private Räume für Meetings und Feiern','Ausflüge nach Albarracín und Mora de Rubielos','Kostenloses WLAN'],
 loc_p='Calle Nueva, 18 · 44001 Teruel. Rezeption: +34 978 62 30 42. WhatsApp: +34 628 473 662. E-Mail: info@elmudayyan.com.',
 chips=['Welche Zimmer gibt es?','Haben Sie Familienzimmer?','Gibt es Frühstück?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
R='https://booking.avirato.com/?code=64315562&lang='
BOOK=dict(mode='engine',url=dict(es=R+'es',en=R+'en',fr=R+'fr',de=R+'de'))
D=dict(name='Hotel El Mudayyan',ac='#1f1a1d',ac2='#9a5a3d',ac2_a11y='#7a4129',book=BOOK,around=[],foot=FOOT,
 address='Calle Nueva, 18 · 44001 Teruel',phones=['+34 978 62 30 42','+34 628 473 662'],emails=['info@elmudayyan.com'],maps='Hotel El Mudayyan, Calle Nueva 18, 44001 Teruel',t=T)
META=dict(repo='demo-hotel-el-mudayyan-teruel',name='Hotel El Mudayyan',legal_name='OTIMARATE SL, NIF B67940007 (aviso legal de su web, nombre comercial Hotel Mudayyan)',registry_ids=['B67940007'],
 url='https://elmudayyan.com/',domain='elmudayyan.com',municipality='Teruel',province='Teruel',sector='hotel con encanto de 3 estrellas en el centro historico de Teruel',
 read_at='2026-11-02T09:15:00+01:00',created_at='2026-11-02T09:14:00+01:00',built_at='2026-11-02T09:30:00+01:00',audit_date='2026-11-02T09:15:00+01:00',
 rating=dict(value=4.6,coincide=['tel','web'],date='2026-10-29',url='https://www.google.com/maps/place/Hotel+El+Mudayyan/@40.3418115,-1.1080474,17z'),
 book=dict(mode='engine',url='https://booking.avirato.com/?code=64315562',note='motor Avirato enlazado desde el boton Reservar de su web (code=64315562), HTTP 200 en es/en/fr/de (02/11/2026 09:15).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('Viajamos en familia, ¿hay sitio para cuatro?','K02'),('¿Qué tienen las habitaciones?','K03'),('¿Hay desayuno?','K04'),('¿Se puede visitar la galería medieval?','K05'),('¿Tenéis tetería?','K06'),('¿Hay aparcamiento cerca?','K07'),('¿Dónde estáis?','K08'),('¿Cómo reservo?','K09'),('¿Podéis confirmarme disponibilidad para mañana?','K09'),('¿Cuál es la política de cancelación?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Hacéis excursiones a Albarracín?','K12'),('¿Cuánto cuesta la noche?',None),('¿Tenéis piscina?',None)],
'en':[('Which rooms do you have?','K01'),('We are a family, is there space for four?','K02'),('What do the rooms include?','K03'),('Is there breakfast?','K04'),('Can I visit the medieval gallery?','K05'),('Do you have a tea room?','K06'),('Is there parking nearby?','K07'),('Where are you?','K08'),('How do I book?','K09'),('Can you confirm availability for tomorrow?','K09'),('What is the cancellation policy?','K10'),('What is your phone number?','K11'),('Do you run excursions to Albarracín?','K12'),('How much is a night?',None),('Do you have a pool?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Nous voyageons en famille, y a-t-il de la place pour quatre ?','K02'),('Que comprennent les chambres ?','K03'),('Y a-t-il un petit-déjeuner ?','K04'),('Peut-on visiter la galerie médiévale ?','K05'),('Avez-vous un salon de thé ?','K06'),('Où se garer ?','K07'),('Où êtes-vous ?','K08'),('Comment réserver ?','K09'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K09'),('Quelle est la politique d’annulation ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Organisez-vous des excursions à Albarracín ?','K12'),('Combien coûte la nuit ?',None),('Avez-vous une piscine ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Wir reisen als Familie, gibt es Platz für vier?','K02'),('Was bieten die Zimmer?','K03'),('Gibt es Frühstück?','K04'),('Kann man die mittelalterliche Galerie besichtigen?','K05'),('Haben Sie eine Teestube?','K06'),('Wo kann ich parken?','K07'),('Wo liegt das Hotel?','K08'),('Wie kann ich buchen?','K09'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K09'),('Wie sind die Stornobedingungen?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Gibt es Ausflüge nach Albarracín?','K12'),('Was kostet eine Nacht?',None),('Haben Sie einen Pool?',None)]}
