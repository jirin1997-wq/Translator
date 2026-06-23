"""
Škoda Auto multilingual glossary.
Used by call_openai_skoda() to correct brand-specific terminology after DeepL translation.
"""

# Base English terms (reference)
# Each language dict maps: "English term (lowercase)" -> "correct local term"

SKODA_GLOSSARY = {

    # -------------------------------------------------------------------------
    # CS — Czech (primary market, most complete)
    # -------------------------------------------------------------------------
    "cs": """
Dodržuj toto závazné názvosloví Škoda Auto:

MODELY (nepřekládej): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

VÝBAVOVÉ LINIE (nepřekládej): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo, Drive, Fresh

INTERIÉRY (nepřekládej): Studio, Loft, Lodge, Lounge, Suite, Suite Cognac, ecoSuite

ASISTENČNÍ SYSTÉMY:
- Assisted Driving 1.5+/2.0+/2.5+/2.6 → Asistovaná jízda 1.5+/2.0+/2.5+/2.6
- Adaptive Cruise Control → Adaptivní tempomat
- Predictive Cruise Control → Prediktivní tempomat
- Lane Assist / Adaptive Lane Assist → Adaptivní vedení v jízdním pruhu
- Traffic Jam Assist → Asistent při jízdě v koloně
- Side Assist → Hlídání mrtvého úhlu
- Emergency Assist → Nouzový asistent
- Traffic Sign Recognition → Rozpoznávání dopravních značek
- Park Assist → Automatické parkování
- Crew Protect Assist → Proaktivní ochrana cestujících
- Lane Change Assist → Asistent změny jízdního pruhu
- Exit Warning → Varování při vystupování
- Turn Assist → Asistent při odbočování
- Driver Fatigue Detection → Rozpoznání únavy řidiče
- High Beam Assist → Asistent dálkových světel
- Hill Hold Assist → Asistent rozjezdu do kopce

KONEKTIVITA:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda
- Connect S/M/L → Connect S/M/L
- Care Connect – Remote Access → Care Connect – Vzdálený přístup
- Proactive Service → Proaktivní servis
- Infotainment Online → Infotainment Online
- Remote iV Services → Vzdálené služby iV
- Service Visit Planning → Plánování návštěvy servisu
- Roadside Assistance → Pomoc na cestě
- Online System Updates → Aktualizace systému online
- Online Personalisation → Personalizace online
- Last Parking Position → Poslední parkovací pozice
- Digital Certificate → Digitální certifikát
- Functions on Demand → Funkce na vyžádání
- Virtual Cockpit → Virtuální kokpit
- Head-up display → Head-up displej
- Virtual assistant Laura → Virtuální asistentka Laura
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Traffication → Traffication
- Ambient Lighting – Additional Colors → Ambientní osvětlení – další barvy
- Ambient Lighting – Extended Functions → Ambientní osvětlení – rozšířené funkce

POHONNÉ JEDNOTKY (nepřekládej): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVIS A ZÁRUKY:
- Extended Warranty → Škoda Prodloužená záruka
- Prepaid Service → Předplacený servis
- Prepaid Service Standard → Škoda Předplacený servis Standard
- Prepaid Service Plus → Škoda Předplacený servis Plus
- Warranty Mobility → Škoda Záruka mobility
- Lifetime Warranty Mobility → Škoda Doživotní záruka mobility
- Škoda Assistance → Škoda Assistance
- Voucher Booklet → Šeková knížka plná slev
- Tyre Insurance → Škoda Pneugarance
- Tyre Hotel → Škoda Pneuhotel
- Recall Action → Svolávací akce
- MOT Preparation → Příprava na STK a měření emisí
- Air Conditioning Service → Servis klimatizace
- Wheel Alignment → Geometrie náprav vozidla

FINANCOVÁNÍ A POJIŠTĚNÍ:
- Škoda Financial Services → Škoda Financial Services
- Škoda Bez starostí → Škoda Bez starostí
- Škoda Insurance Standard → Škoda Pojištění Standard
- Škoda Insurance Plus → Škoda Pojištění Plus
- GAP Insurance → GAP pojištění
- Home Service → Domovský servis

FIREMNÍ PROGRAMY:
- Corporate Program → Firemní program Škoda
- Employee Program → Zaměstnanecký program
- Fleet Centers → Fleetová centra
- Fleet Configurator → Fleet Konfigurátor

OSTATNÍ:
- Škoda Plus → Škoda Plus
- Škoda Explore → Škoda Explore
- Genuine Parts → Originální díly ŠKODA
- Genuine Accessories → Originální příslušenství ŠKODA
- Škoda iV Charger → Škoda iV Charger
- Powerpass → Powerpass
- Škoda Stromky → Škoda Stromky
""",

    # -------------------------------------------------------------------------
    # DE — German
    # -------------------------------------------------------------------------
    "de": """
Beachte folgende verbindliche Škoda Auto Terminologie:

MODELLE (nicht übersetzen): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

AUSSTATTUNGSLINIEN (nicht übersetzen): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASSISTENZSYSTEME:
- Adaptive Cruise Control → Adaptive Geschwindigkeitsregelanlage
- Traffic Sign Recognition → Erkennung von Verkehrszeichen
- High Beam Assist → Fernlichtkontrolle
- Lane Assist → Spurhalteassistent
- Side Assist → Totwinkelüberwachung
- Emergency Assist → Notfallassistent
- Park Assist → Park Assist

KONNEKTIVITÄT:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda App
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Remote Access
- Care Connect: Proactive Service → Care Connect: Proaktive Dienste
- Care Connect: iV Remote Services → Care Connect: iV Remote-Dienste
- Functions on Demand → Functions on Demand
- Ambient Lighting – Additional Colors → Ambientebeleuchtung – zusätzliche Farben
- Ambient Lighting – Extended Functions → Ambientebeleuchtung – zusätzliche Funktionen
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up Display
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- SmartLink → SmartLink+

ANTRIEB (nicht übersetzen): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVICE UND GARANTIE:
- Extended Warranty → Škoda Garantie Verlängerung
- Warranty Mobility → Škoda Mobilitätsgarantie
- Prepaid Service → Wartungsvertrag
- Genuine Parts → ŠKODA Original-Teile
- Genuine Accessories → ŠKODA Original-Zubehör
- Recall Action → Rückrufaktion
- Air Conditioning Service → Klimaanlagenservice
- Wheel Alignment → Achsvermessung

FINANZIERUNG:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP-Versicherung
- Operative Leasing → Operatives Leasing

SONSTIGES:
- Škoda Plus → Škoda Plus
- Fleet Configurator → Fleet Konfigurator
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # FR — French
    # -------------------------------------------------------------------------
    "fr": """
Respecte la terminologie officielle Škoda Auto suivante:

MODÈLES (ne pas traduire): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

NIVEAUX DE FINITION (ne pas traduire): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

SYSTÈMES D'ASSISTANCE:
- Adaptive Cruise Control → Régulateur de vitesse adaptatif
- Traffic Sign Recognition → Reconnaissance des panneaux de signalisation
- High Beam Assist → Fonctions avancées des phares
- Lane Assist → Aide au maintien de voie
- Side Assist → Surveillance des angles morts
- Park Assist → Park Assist
- Emergency Assist → Assistant d'urgence
- Travel Assist → Travel Assist

CONNECTIVITÉ:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Application MyŠkoda
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Accès à distance
- Care Connect: Proactive Service → Care Connect: Service proactif
- Care Connect: iV Remote Services → Care Connect: Services iV à distance
- Functions on Demand → Fonctions à la demande
- Ambient Lighting – Additional Colors → Éclairage d'ambiance – couleurs supplémentaires
- Ambient Lighting – Extended Functions → Éclairage d'ambiance – fonctions avancées
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Affichage tête haute
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Assistant vocal Laura
- SmartLink → SmartLink

MOTORISATION (ne pas traduire): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVICE ET GARANTIE:
- Extended Warranty → Extension de garantie
- Warranty Mobility → Garantie Mobilité / Škoda Assistance
- Prepaid Service → Contrat d'entretien
- Genuine Parts → Pièces d'origine ŠKODA
- Genuine Accessories → Accessoires d'origine ŠKODA
- Recall Action → Campagne de rappel
- Air Conditioning Service → Entretien de climatisation

FINANCEMENT:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → Assurance GAP
- Operative Leasing → Leasing opérationnel

DIVERS:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
- Traffication → Traffication
""",

    # -------------------------------------------------------------------------
    # ES — Spanish
    # -------------------------------------------------------------------------
    "es": """
Respeta la terminología oficial de Škoda Auto:

MODELOS (no traducir): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

NIVELES DE EQUIPAMIENTO (no traducir): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

SISTEMAS DE ASISTENCIA:
- Adaptive Cruise Control → Control de velocidad adaptativo
- Traffic Sign Recognition → Reconocimiento de señales de tráfico
- High Beam Assist → Control de luces largas
- Lane Assist → Asistente de carril
- Side Assist → Monitorización de ángulo muerto
- Park Assist → Park Assist
- Emergency Assist → Asistente de emergencia
- Travel Assist → Travel Assist

CONECTIVIDAD:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Aplicación MyŠkoda
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Acceso remoto
- Care Connect: Proactive Service → Care Connect: Servicio proactivo
- Care Connect: iV Remote Services → Care Connect: Servicios iV remotos
- Functions on Demand → Funciones bajo demanda
- Ambient Lighting – Additional Colors → Iluminación ambiental – colores adicionales
- Ambient Lighting – Extended Functions → Iluminación ambiental – funciones adicionales
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up Display
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Asistente de voz Laura
- SmartLink → SmartLink
- Phone Box → Phone Box

MOTORIZACIÓN (no traducir): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVICIO Y GARANTÍA:
- Extended Warranty → Garantía extendida
- Warranty Mobility → Garantía de movilidad
- Prepaid Service → Servicio prepagado
- Genuine Parts → Recambios originales ŠKODA
- Genuine Accessories → Accesorios originales ŠKODA
- Recall Action → Campaña de revisión

FINANCIACIÓN:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → Seguro GAP

OTROS:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # IT — Italian
    # -------------------------------------------------------------------------
    "it": """
Rispetta la terminologia ufficiale Škoda Auto:

MODELLI (non tradurre): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

LIVELLI DI ALLESTIMENTO (non tradurre): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

SISTEMI DI ASSISTENZA:
- Adaptive Cruise Control → Cruise control adattivo
- Traffic Sign Recognition → Riconoscimento dei segnali stradali
- High Beam Assist → Controllo luci abbaglianti
- Lane Assist → Assistente di corsia
- Side Assist → Monitoraggio angolo cieco
- Park Assist → Park Assist
- Emergency Assist → Assistente di emergenza
- Travel Assist → Travel Assist

CONNETTIVITÀ:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → App MyŠkoda
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Accesso remoto
- Care Connect: Proactive Service → Care Connect: Servizio proattivo
- Care Connect: iV Remote Services → Care Connect: Servizi iV remoti
- Functions on Demand → Funzioni su richiesta
- Ambient Lighting – Additional Colors → Illuminazione ambientale – colori aggiuntivi
- Ambient Lighting – Extended Functions → Illuminazione ambientale – funzioni aggiuntive
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up Display
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Assistente vocale Laura
- SmartLink → SmartLink

MOTORIZZAZIONE (non tradurre): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVIZIO E GARANZIA:
- Extended Warranty → Garanzia estesa
- Warranty Mobility → Garanzia di mobilità
- Prepaid Service → Servizio prepagato
- Genuine Parts → Ricambi originali ŠKODA
- Genuine Accessories → Accessori originali ŠKODA
- Recall Action → Campagna di richiamo

FINANZIAMENTO:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → Assicurazione GAP

ALTRO:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # PL — Polish
    # -------------------------------------------------------------------------
    "pl": """
Stosuj obowiązującą terminologię Škoda Auto:

MODELE (nie tłumacz): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

LINIE WYPOSAŻENIA (nie tłumacz): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

SYSTEMY ASYSTENTA:
- Adaptive Cruise Control → Adaptacyjny tempomat
- Traffic Sign Recognition → Rozpoznawanie znaków drogowych
- High Beam Assist → Asystent świateł drogowych
- Lane Assist → Asystent pasa ruchu
- Side Assist → Monitorowanie martwego pola
- Park Assist → Park Assist
- Emergency Assist → Asystent awaryjny
- Travel Assist → Travel Assist

ŁĄCZNOŚĆ:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Aplikacja MyŠkoda
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Zdalny dostęp
- Care Connect: Proactive Service → Care Connect: Usługa proaktywna
- Care Connect: iV Remote Services → Care Connect: Zdalne usługi iV
- Functions on Demand → Funkcje na żądanie
- Ambient Lighting – Additional Colors → Oświetlenie ambientowe – dodatkowe kolory
- Ambient Lighting – Extended Functions → Oświetlenie ambientowe – rozszerzone funkcje
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Wyświetlacz HUD
- Service Visit Planning → Wizyta w serwisie
- Roadside Assistance → Rozmowa w sprawie awarii
- Online System Updates → Aktualizacja systemu online
- Online Personalisation → Personalizacja online
- Last Parking Position → Miejsce zaparkowania
- Horn and Flash → Zatrąb i mrugnij
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Asystentka głosowa Laura
- SmartLink → SmartLink
- Traffication → Traffication

NAPĘD (nie tłumacz): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERWIS I GWARANCJA:
- Extended Warranty → Przedłużona gwarancja
- Warranty Mobility → Gwarancja mobilności
- Prepaid Service → Przedpłacony serwis
- Genuine Parts → Oryginalne części ŠKODA
- Genuine Accessories → Oryginalne akcesoria ŠKODA
- Recall Action → Akcja serwisowa

FINANSOWANIE:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → Ubezpieczenie GAP

INNE:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # SK — Slovak
    # -------------------------------------------------------------------------
    "sk": """
Dodržuj záväznú terminológiu Škoda Auto:

MODELY (neprekladaj): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

VÝBAVOVÉ LÍNIE (neprekladaj): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASISTENČNÉ SYSTÉMY:
- Adaptive Cruise Control → Adaptívny tempomat
- Traffic Sign Recognition → Rozpoznávanie dopravných značiek
- High Beam Assist → Asistent diaľkových svetiel
- Lane Assist → Adaptívne vedenie v jazdnom pruhu
- Side Assist → Hlídanie mŕtveho uhla
- Park Assist → Automatické parkovanie
- Emergency Assist → Núdzový asistent
- Travel Assist → Travel Assist

KONEKTIVITA:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Aplikácia MyŠkoda
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Vzdialený prístup
- Care Connect: Proactive Service → Care Connect: Proaktívna služba
- Care Connect: iV Remote Services → Care Connect: Vzdialené služby iV
- Functions on Demand → Funkcie na želanie / Nové funkcie vozidla na želanie
- Ambient Lighting – Additional Colors → Ambientné osvetlenie – doplnkové farby
- Ambient Lighting – Extended Functions → Ambientné osvetlenie – rozšírené funkcie
- Virtual Cockpit → Virtuálny kokpit
- Head-up display → Head-up displej
- Service Visit Planning → Plánovanie návštevy servisu
- Last Parking Position → Posledná parkovacia pozícia
- Horn and Flash → Húkanie a blikanie
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Virtuálna asistentka Laura

POHON (neprekladaj): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVIS A ZÁRUKY:
- Extended Warranty → Predĺžená záruka
- Warranty Mobility → Záruka mobility
- Prepaid Service → Predplatený servis
- Genuine Parts → Originálne diely ŠKODA
- Genuine Accessories → Originálne príslušenstvo ŠKODA

FINANCOVANIE:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP poistenie

OSTATNÉ:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # NL — Dutch
    # -------------------------------------------------------------------------
    "nl": """
Gebruik de officiële Škoda Auto terminologie:

MODELLEN (niet vertalen): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

UITRUSTINGSNIVEAUS (niet vertalen): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASSISTENTIESYSTEMEN:
- Adaptive Cruise Control → Adaptive Cruise Control
- Traffic Sign Recognition → Verkeersbordherkenning
- High Beam Assist → High Beam Control
- Lane Assist → Rijstrookassistent
- Side Assist → Dodehoekbewaking
- Park Assist → Park Assist
- Emergency Assist → Noodassistent
- Travel Assist → Travel Assist

CONNECTIVITEIT:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda App
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Remote Access
- Care Connect: Proactive Service → Care Connect: Proactieve service
- Care Connect: iV Remote Services → Care Connect: iV Remote-diensten
- Functions on Demand → Functions on Demand
- Ambient Lighting – Additional Colors → Ambient lighting – Extra kleuren
- Ambient Lighting – Extended Functions → Ambient Lighting – Extra functies
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up Display
- Online Navigation → Online navigatie
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Spraakassistent Laura
- SmartLink → SmartLink
- Traffication → Traffication

AANDRIJVING (niet vertalen): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVICE EN GARANTIE:
- Extended Warranty → Verlengde garantie
- Warranty Mobility → Mobiliteitsgarantie
- Prepaid Service → Onderhoudscontract
- Genuine Parts → ŠKODA Originele onderdelen
- Genuine Accessories → ŠKODA Originele accessoires
- Recall Action → Terugroepactie

FINANCIERING:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP-verzekering

OVERIG:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # SV — Swedish
    # -------------------------------------------------------------------------
    "sv": """
Använd den officiella Škoda Auto-terminologin:

MODELLER (ej översätt): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

UTRUSTNINGSNIVÅER (ej översätt): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASSISTANSSYSTEM:
- Adaptive Cruise Control → Adaptiv farthållare
- Traffic Sign Recognition → Trafikskyltavläsning
- High Beam Assist → Fjärrljusassistent
- Lane Assist → Körfältsassistent
- Side Assist → Dödavinkelsövervakning
- Park Assist → Park Assist
- Emergency Assist → Nödassistent
- Travel Assist → Travel Assist

KONNEKTIVITET:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda-appen
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Fjärråtkomst
- Care Connect: Proactive Service → Care Connect: Proaktiv service
- Care Connect: iV Remote Services → Care Connect: iV-fjärrtjänster
- Functions on Demand → Funktioner på begäran
- Ambient Lighting – Additional Colors → Ambient belysning – extra färger
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up Display
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Škoda Powerpass
- Virtual assistant Laura → Röstassistenten Laura
- SmartLink → SmartLink
- Traffication → Traffication
- Service booking → Servicebokning

DRIVLINA (ej översätt): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVICE OCH GARANTI:
- Extended Warranty → Förlängd garanti
- Warranty Mobility → Mobilitetsgaranti
- Prepaid Service → Förbetald service
- Genuine Parts → ŠKODA Originaldelar
- Genuine Accessories → ŠKODA Originaltillbehör
- Recall Action → Återkallelsekampanj

FINANSIERING:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP-försäkring

ÖVRIGT:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # DA — Danish
    # -------------------------------------------------------------------------
    "da": """
Brug den officielle Škoda Auto-terminologi:

MODELLER (oversæt ikke): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

UDSTYRSNIVEAUER (oversæt ikke): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASSISTENTSYSTEMER:
- Adaptive Cruise Control → Adaptiv fartpilot
- Traffic Sign Recognition → Trafikskiltgenkendelse
- High Beam Assist → Fjernlysassistent
- Lane Assist → Vognbaneassistent
- Side Assist → Overvågning af blinde vinkler
- Park Assist → Park Assist
- Emergency Assist → Nødassistent
- Travel Assist → Travel Assist

KONNEKTIVITET:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda-appen
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Fjernadgang
- Care Connect: Proactive Service → Care Connect: Proaktiv service
- Care Connect: iV Remote Services → Care Connect: iV-fjerntjenester
- Functions on Demand → Funktioner efter behov
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up Display
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Stemmeassistenten Laura
- SmartLink → SmartLink
- Service booking → Serviceplanlægning
- Emergency Call → Nødopkald

DRIVLINJE (oversæt ikke): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVICE OG GARANTI:
- Extended Warranty → Forlænget garanti
- Warranty Mobility → Mobilitetsgaranti
- Prepaid Service → Forudbetalt service
- Genuine Parts → ŠKODA Originale reservedele
- Genuine Accessories → ŠKODA Originalt tilbehør
- Recall Action → Tilbagekaldelseskampagne

FINANSIERING:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP-forsikring

ANDET:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # NB — Norwegian
    # -------------------------------------------------------------------------
    "nb": """
Bruk den offisielle Škoda Auto-terminologien:

MODELLER (ikke oversett): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

UTSTYRSNIVÅER (ikke oversett): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASSISTENTSYSTEMER:
- Adaptive Cruise Control → Adaptiv cruisekontroll
- Traffic Sign Recognition → Skiltgjenkjenning
- High Beam Assist → Fjernlysassistent
- Lane Assist → Filholderassistent
- Side Assist → Blindsonovervåking
- Park Assist → Park Assist
- Emergency Assist → Nødassistent
- Travel Assist → Travel Assist

TILKOBLING:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda-appen
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Remote Access
- Care Connect: Proactive Service → Care Connect: Proaktive tjenester
- Care Connect: iV Remote Services → Care Connect: iV fjernstyrte tjenester
- Functions on Demand → Funksjoner når du trenger de
- Ambient Lighting – Additional Colors → Ambientebelysning – ekstra farger
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up Display
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Stemmeassistenten Laura
- SmartLink → SmartLink

DRIVLINJE (ikke oversett): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVICE OG GARANTI:
- Extended Warranty → Utvidet garanti
- Warranty Mobility → Mobilitetsgaranti
- Prepaid Service → Forhåndsbetalt service
- Genuine Parts → ŠKODA Originaldeler
- Genuine Accessories → ŠKODA Originaltilbehør
- Recall Action → Tilbakekallingskampanje

FINANSIERING:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP-forsikring

ANNET:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # FI — Finnish
    # -------------------------------------------------------------------------
    "fi": """
Käytä virallista Škoda Auto -terminologiaa:

MALLIT (älä käännä): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

VARUSTELUTASOT (älä käännä): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

AVUSTINJÄRJESTELMÄT:
- Adaptive Cruise Control → Adaptiivinen vakionopeudensäädin
- Traffic Sign Recognition → Liikennemerkkien tunnistus
- High Beam Assist → Kaukovaloapuri
- Lane Assist → Kaistapysymisavustin
- Side Assist → Kuolleen kulman valvonta
- Park Assist → Park Assist
- Emergency Assist → Hätäavustin
- Travel Assist → Travel Assist

YHDISTETTÄVYYS:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda-sovellus
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Etäkäyttö
- Care Connect: Proactive Service → Care Connect: Ennakoiva palvelu
- Care Connect: iV Remote Services → Care Connect: iV-etäpalvelut
- Functions on Demand → Toiminnot tarpeen mukaan
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up Display
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Ääniavustaja Laura
- SmartLink → SmartLink

VOIMANSIIRTO (älä käännä): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

HUOLTO JA TAKUU:
- Extended Warranty → Laajennettu takuu
- Warranty Mobility → Liikkuvuustakuu
- Prepaid Service → Ennakkoon maksettu huolto
- Genuine Parts → ŠKODA Alkuperäisosat
- Genuine Accessories → ŠKODA Alkuperäistarvikkeet
- Recall Action → Takaisinkutsukampanja

RAHOITUS:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP-vakuutus

MUUT:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # PT — Portuguese
    # -------------------------------------------------------------------------
    "pt": """
Respeita a terminologia oficial da Škoda Auto:

MODELOS (não traduzir): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

NÍVEIS DE EQUIPAMENTO (não traduzir): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

SISTEMAS DE ASSISTÊNCIA:
- Adaptive Cruise Control → Controlo de velocidade adaptativo
- Traffic Sign Recognition → Reconhecimento de sinais de trânsito
- High Beam Assist → Assistente de máximos
- Lane Assist → Assistente de faixa de rodagem
- Side Assist → Monitorização de ângulo morto
- Park Assist → Park Assist
- Emergency Assist → Assistente de emergência
- Travel Assist → Travel Assist

CONECTIVIDADE:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Aplicação MyŠkoda
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Acesso remoto
- Care Connect: Proactive Service → Care Connect: Serviços Proativos
- Care Connect: iV Remote Services → Care Connect: Serviços iV remotos
- Functions on Demand → Funções a pedido
- Ambient Lighting – Additional Colors → Iluminação ambiente – cores adicionais
- Ambient Lighting – Extended Functions → Iluminação ambiente – funções adicionais
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up Display
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Assistente de voz Laura
- SmartLink → SmartLink
- Emergency Call → Chamada de emergência

MOTORIZAÇÃO (não traduzir): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVIÇO E GARANTIA:
- Extended Warranty → Extensão de garantia
- Warranty Mobility → Serviço de Mobilidade Premium
- Prepaid Service → Planos de Manutenção
- Genuine Parts → Peças originais ŠKODA
- Genuine Accessories → Acessórios originais ŠKODA
- Recall Action → Campanha de recall

FINANCIAMENTO:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → Seguro GAP

OUTROS:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # RO — Romanian
    # -------------------------------------------------------------------------
    "ro": """
Respectă terminologia oficială Škoda Auto:

MODELE (nu traduce): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

NIVELURI DE ECHIPARE (nu traduce): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

SISTEME DE ASISTENȚĂ:
- Adaptive Cruise Control → Control adaptiv al vitezei de croazieră
- Traffic Sign Recognition → Recunoașterea semnelor de circulație
- High Beam Assist → Asistent fază lungă
- Lane Assist → Asistent de bandă
- Side Assist → Monitorizare unghi mort
- Park Assist → Park Assist
- Emergency Assist → Asistent de urgență
- Travel Assist → Travel Assist

CONECTIVITATE:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Aplicația MyŠkoda
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Acces la distanță
- Care Connect: Proactive Service → Care Connect: Servicii Proactive
- Care Connect: iV Remote Services → Care Connect: Servicii Online iV
- Functions on Demand → Funcții la cerere
- Ambient Lighting – Additional Colors → Iluminare ambientală – culori suplimentare
- Ambient Lighting – Extended Functions → Iluminare ambientală – Caracteristici suplimentare
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up Display
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Asistentul vocal Laura
- Navigation → Navigație

PROPULSIE (nu traduce): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVICE ȘI GARANȚIE:
- Extended Warranty → Garanție extinsă
- Warranty Mobility → Garanție de mobilitate
- Prepaid Service → Serviciu prepaid
- Genuine Parts → Piese originale ŠKODA
- Genuine Accessories → Accesorii originale ŠKODA
- Recall Action → Campanie de rechemare

FINANȚARE:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → Asigurare GAP

ALTELE:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # HU — Hungarian
    # -------------------------------------------------------------------------
    "hu": """
Használd a Škoda Auto kötelező terminológiáját:

MODELLEK (ne fordítsd): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

FELSZERELTSÉGI SZINTEK (ne fordítsd): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASSZISZTENS RENDSZEREK:
- Adaptive Cruise Control → Adaptív tempomat
- Traffic Sign Recognition → Közlekedési táblák felismerése
- High Beam Assist → Távfényasszisztens
- Lane Assist → Sávtartó asszisztens
- Side Assist → Holttér-figyelés
- Park Assist → Park Assist
- Emergency Assist → Vészhelyzeti asszisztens
- Travel Assist → Travel Assist

KAPCSOLÓDÁS:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda alkalmazás
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Távoli hozzáférés
- Care Connect: Proactive Service → Care Connect: Proaktív szolgáltatások
- Care Connect: iV Remote Services → Care Connect: iV távolszolgáltatások
- Functions on Demand → Igény szerinti funkciók
- Ambient Lighting – Additional Colors → Hangulatvilágítás – további színek
- Virtual Cockpit → Virtuális műszerfal
- Head-up display → Head-up kijelző
- Service Visit Planning → Szervizidőpont-egyeztetés
- Last Parking Position → Parkolási pozíció
- Horn and Flash → Kürt és villogás
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Laura hangasszisztens
- Emergency Call → Vészhívó

HAJTÁSLÁNC (ne fordítsd): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SZERVIZ ÉS GARANCIA:
- Extended Warranty → Kiterjesztett garancia
- Warranty Mobility → Škoda Mobilitásgarancia
- Prepaid Service → Előre fizetett szerviz
- Genuine Parts → ŠKODA Eredeti alkatrészek
- Genuine Accessories → ŠKODA Eredeti kiegészítők
- Recall Action → Visszahívási kampány

FINANSZÍROZÁS:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP biztosítás

EGYÉB:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # BG — Bulgarian
    # -------------------------------------------------------------------------
    "bg": """
Спазвай задължителната терминология на Škoda Auto:

МОДЕЛИ (не превеждай): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

НИВА НА ЕКИПИРОВКА (не превеждай): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

АСИСТЕНТСКИ СИСТЕМИ:
- Adaptive Cruise Control → Адаптивен темпомат
- Traffic Sign Recognition → Разпознаване на пътни знаци
- High Beam Assist → Асистент за дълги светлини
- Lane Assist → Асистент за лентата
- Side Assist → Наблюдение на мъртва точка
- Park Assist → Park Assist
- Emergency Assist → Спешен асистент
- Travel Assist → Travel Assist

СВЪРЗАНОСТ:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Приложение MyŠkoda
- Infotainment Online → Онлайн инфоразвлечения
- Care Connect: Remote Access → Care Connect: Отдалечен достъп
- Care Connect: Proactive Service → Care Connect: Проактивни услуги
- Care Connect: iV Remote Services → Care Connect: iV Отдалечени услуги
- Functions on Demand → Функции при поискване
- Ambient Lighting – Additional Colors → Амбиентно осветление – допълнителни цветове
- Ambient Lighting – Extended Functions → Амбиентно осветление – допълнителни функции
- Virtual Cockpit → Виртуален кокпит
- Head-up display → Head-up дисплей
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Гласов асистент Laura
- Navigation → Навигация
- Emergency Call → Спешно повикване / eCall

ЗАДВИЖВАНЕ (не превеждай): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

СЕРВИЗ И ГАРАНЦИЯ:
- Extended Warranty → Удължена гаранция
- Warranty Mobility → Гаранция за мобилност
- Prepaid Service → Предплатен сервиз
- Genuine Parts → Оригинални части ŠKODA
- Genuine Accessories → Оригинални аксесоари ŠKODA
- Recall Action → Кампания за изтегляне

ФИНАНСИРАНЕ:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP застраховка

ДРУГО:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # ET — Estonian
    # -------------------------------------------------------------------------
    "et": """
Kasuta Škoda Auto ametlikku terminoloogiat:

MUDELID (ära tõlgi): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

VARUSTUSTASEMED (ära tõlgi): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ABISÜSTEEMID:
- Adaptive Cruise Control → Adaptiivne kiirushoidja
- Traffic Sign Recognition → Liiklusmärkide tuvastamine
- High Beam Assist → Kaugtuledeasistent
- Lane Assist → Roolikaasassistent
- Side Assist → Surnud nurga jälgimine
- Park Assist → Park Assist
- Emergency Assist → Hädaolukorra assistent
- Travel Assist → Travel Assist

ÜHENDUVUS:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda rakendus
- Infotainment Online → Online-teabeteenus
- Care Connect: Remote Access → Care Connect: Kaugjuurdepääs
- Care Connect: Proactive Service → Care Connect: Hooldus- ja rikketugi
- Care Connect: iV Remote Services → Care Connect: iV kaugteenused
- Functions on Demand → Funktsioonid vastavalt vajadusele
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up Display
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Häälassistent Laura
- SmartLink → SmartLink

JÕUALLIKAS (ära tõlgi): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

HOOLDUS JA GARANTII:
- Extended Warranty → Pikendatud garantii
- Warranty Mobility → Liikuvusgarantii
- Prepaid Service → Eelmakstud hooldus
- Genuine Parts → ŠKODA Originaalvaruosad
- Genuine Accessories → ŠKODA Originaaltarvikud
- Recall Action → Tagasikutsumiskampaania

FINANTSEERIMINE:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP-kindlustus

MUU:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # LV — Latvian
    # -------------------------------------------------------------------------
    "lv": """
Lieto Škoda Auto oficiālo terminoloģiju:

MODEĻI (netulko): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

APRĪKOJUMA LĪMEŅI (netulko): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASISTENTA SISTĒMAS:
- Adaptive Cruise Control → Adaptīvais ātruma regulators
- Traffic Sign Recognition → Ceļa zīmju atpazīšana / Funkcijas pēc pieprasījuma
- High Beam Assist → Tālās gaismas asistents
- Lane Assist → Joslas noturēšanas asistents
- Side Assist → Aklās zonas uzraudzība
- Park Assist → Park Assist
- Emergency Assist → Avārijas asistents
- Travel Assist → Travel Assist

SAVIENOJAMĪBA:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda lietotne
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Attālinātā piekļuve
- Care Connect: Proactive Service → Care Connect: Proaktīvais serviss
- Care Connect: iV Remote Services → Care Connect: iV attālinātie pakalpojumi
- Functions on Demand → Funkcijas pēc pieprasījuma
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up displejs
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Balss asistente Laura
- SmartLink → SmartLink

DZINĒJS (netulko): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

APKOPE UN GARANTIJA:
- Extended Warranty → Pagarinātā garantija
- Warranty Mobility → Mobilitātes garantija
- Prepaid Service → Priekšapmaksas apkope
- Genuine Parts → ŠKODA Oriģinālās rezerves daļas
- Genuine Accessories → ŠKODA Oriģinālie piederumi
- Recall Action → Atsaukšanas kampaņa

FINANSĒŠANA:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP apdrošināšana

CITS:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # LT — Lithuanian
    # -------------------------------------------------------------------------
    "lt": """
Naudok privalomą Škoda Auto terminologiją:

MODELIAI (neversk): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

KOMPLEKTACIJOS LYGIAI (neversk): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

PAGALBINĖS SISTEMOS:
- Adaptive Cruise Control → Adaptyvusis tempomatas
- Traffic Sign Recognition → Kelio ženklų atpažinimas
- High Beam Assist → Tolimųjų žibintų asistentas
- Lane Assist → Eismo juostos asistentas
- Side Assist → Aklosios zonos stebėjimas
- Park Assist → Park Assist
- Emergency Assist → Avarinės situacijos asistentas
- Travel Assist → Travel Assist

RYŠYS:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda programa
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Nuotolinė prieiga
- Care Connect: Proactive Service → Care Connect: Proaktyvioji paslauga
- Care Connect: iV Remote Services → Care Connect: iV nuotolinės paslaugos
- Functions on Demand → Funkcijos pagal poreikį
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up ekranas
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Balso asistentė Laura
- SmartLink → SmartLink

PAVARA (neversk): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

TECHNINĖ PRIEŽIŪRA IR GARANTIJA:
- Extended Warranty → Pratęsta garantija
- Warranty Mobility → Mobilumo garantija
- Prepaid Service → Iš anksto apmokėta techninė priežiūra
- Genuine Parts → ŠKODA Originalios atsarginės dalys
- Genuine Accessories → ŠKODA Originalūs priedai
- Recall Action → Atšaukimo kampanija

FINANSAVIMAS:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP draudimas

KITA:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # UK — Ukrainian
    # -------------------------------------------------------------------------
    "uk": """
Дотримуйся обов'язкової термінології Škoda Auto:

МОДЕЛІ (не перекладай): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

РІВНІ КОМПЛЕКТАЦІЇ (не перекладай): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

СИСТЕМИ АСИСТУВАННЯ:
- Adaptive Cruise Control → Адаптивний темпомат
- Traffic Sign Recognition → Розпізнавання дорожніх знаків
- High Beam Assist → Асистент дальнього світла
- Lane Assist → Асистент смуги руху
- Side Assist → Контроль сліпої зони
- Park Assist → Park Assist
- Emergency Assist → Аварійний асистент
- Travel Assist → Travel Assist

ЗВ'ЯЗОК:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Додаток MyŠkoda
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Віддалений доступ
- Care Connect: Proactive Service → Care Connect: Проактивний сервіс
- Care Connect: iV Remote Services → Care Connect: iV дистанційні послуги
- Functions on Demand → Функції на вимогу
- Virtual Cockpit → Віртуальна кабіна
- Head-up display → Head-up дисплей
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Голосовий асистент Laura
- SmartLink → SmartLink+
- Emergency Call → Виклик екстреної допомоги

ПРИВІД (не перекладай): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

СЕРВІС ТА ГАРАНТІЯ:
- Extended Warranty → Подовжена гарантія
- Warranty Mobility → Гарантія мобільності
- Prepaid Service → Передплачений сервіс
- Genuine Parts → Оригінальні запчастини ŠKODA
- Genuine Accessories → Оригінальні аксесуари ŠKODA
- Recall Action → Сервісна кампанія

ФІНАНСУВАННЯ:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP страхування

ІНШЕ:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # EL — Greek
    # -------------------------------------------------------------------------
    "el": """
Χρησιμοποίησε την επίσημη ορολογία της Škoda Auto:

ΜΟΝΤΕΛΑ (μη μεταφράζεις): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

ΕΠΙΠΕΔΑ ΕΞΟΠΛΙΣΜΟΥ (μη μεταφράζεις): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ΣΥΣΤΗΜΑΤΑ ΒΟΗΘΕΙΑΣ:
- Adaptive Cruise Control → Προσαρμοστικός ρυθμιστής ταχύτητας
- Traffic Sign Recognition → Αναγνώριση πινακίδων κυκλοφορίας
- High Beam Assist → Βοηθός μακρινών φώτων
- Lane Assist → Βοηθός διατήρησης λωρίδας
- Side Assist → Παρακολούθηση τυφλού σημείου
- Park Assist → Park Assist
- Emergency Assist → Βοηθός έκτακτης ανάγκης
- Travel Assist → Travel Assist

ΣΥΝΔΕΣΙΜΟΤΗΤΑ:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Εφαρμογή MyŠkoda
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Απομακρυσμένη πρόσβαση
- Care Connect: Proactive Service → Care Connect: Προληπτική υπηρεσία
- Functions on Demand → Λειτουργίες κατ' απαίτηση
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Οθόνη Head-up
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Φωνητικός βοηθός Laura

ΚΙΝΗΤΗΡΑΣ (μη μεταφράζεις): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

ΣΕΡΒΙΣ ΚΑΙ ΕΓΓΥΗΣΗ:
- Extended Warranty → Εκτεταμένη εγγύηση
- Warranty Mobility → Εγγύηση κινητικότητας
- Prepaid Service → Προπληρωμένη συντήρηση
- Genuine Parts → Γνήσια ανταλλακτικά ŠKODA
- Genuine Accessories → Γνήσια αξεσουάρ ŠKODA

ΧΡΗΜΑΤΟΔΟΤΗΣΗ:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → Ασφάλεια GAP

ΑΛΛΑ:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # SL — Slovenian
    # -------------------------------------------------------------------------
    "sl": """
Upoštevaj obvezno terminologijo Škoda Auto:

MODELI (ne prevajaj): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

STOPNJE OPREME (ne prevajaj): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASISTENČNI SISTEMI:
- Adaptive Cruise Control → Adaptivni tempomat
- Traffic Sign Recognition → Prepoznavanje prometnih znakov
- High Beam Assist → Asistent dolgih luči
- Lane Assist → Asistent za ohranjanje voznega pasu
- Side Assist → Nadzor mrtvega kota
- Park Assist → Park Assist
- Emergency Assist → Asistent v sili
- Travel Assist → Travel Assist

POVEZLJIVOST:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Aplikacija MyŠkoda
- Infotainment Online → Infotainment Online
- Care Connect: Remote Access → Care Connect: Oddaljeni dostop
- Care Connect: Proactive Service → Care Connect: Proaktivna storitev
- Functions on Demand → Funkcije na zahtevo
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up zaslon
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Glasovni asistent Laura

POGONSKI SKLOP (ne prevajaj): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVIS IN GARANCIJA:
- Extended Warranty → Podaljšana garancija
- Warranty Mobility → Garancija mobilnosti
- Prepaid Service → Predplačani servis
- Genuine Parts → Originalni deli ŠKODA
- Genuine Accessories → Originalna oprema ŠKODA
- Recall Action → Servisna akcija

FINANCIRANJE:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP zavarovanje

OSTALO:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # HR — Croatian  (translated via OpenAI directly, glossary in system prompt)
    # -------------------------------------------------------------------------
    "hr": """
Koristi obveznu terminologiju Škoda Auto:

MODELI (ne prevodi): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

RAZINE OPREME (ne prevodi): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASISTENTSKI SUSTAVI:
- Adaptive Cruise Control → Adaptivni tempomat
- Traffic Sign Recognition → Prepoznavanje prometnih znakova
- High Beam Assist → Asistent dugih svjetala
- Lane Assist → Asistent trake
- Side Assist → Nadzor mrtvog kuta
- Park Assist → Park Assist
- Emergency Assist → Asistent u hitnim slučajevima
- Travel Assist → Travel Assist

POVEZIVOST:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Aplikacija MyŠkoda
- Functions on Demand → Funkcije na zahtjev
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up zaslon
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Glasovni asistent Laura

POGON (ne prevodi): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVIS I JAMSTVO:
- Extended Warranty → Produženo jamstvo
- Warranty Mobility → Jamstvo mobilnosti
- Genuine Parts → Originalni dijelovi ŠKODA
- Genuine Accessories → Originalna oprema ŠKODA

OSTALO:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # SR — Serbian
    # -------------------------------------------------------------------------
    "sr": """
Koristi obaveznu terminologiju Škoda Auto:

MODELI (ne prevodi): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

NIVOI OPREME (ne prevodi): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASISTENTSKI SISTEMI:
- Adaptive Cruise Control → Adaptivni tempomat
- Traffic Sign Recognition → Prepoznavanje saobraćajnih znakova
- High Beam Assist → Asistent dugih svetala
- Lane Assist → Asistent trake
- Side Assist → Nadzor mrtvog ugla
- Park Assist → Park Assist
- Emergency Assist → Asistent u hitnim situacijama
- Travel Assist → Travel Assist

POVEZIVOST:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Aplikacija MyŠkoda
- Functions on Demand → Funkcije na zahtev
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up displej
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Glasovni asistent Laura

POGON (ne prevodi): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVIS I GARANCIJA:
- Extended Warranty → Produžena garancija
- Warranty Mobility → Garancija mobilnosti
- Genuine Parts → Originalni delovi ŠKODA
- Genuine Accessories → Originalna oprema ŠKODA

OSTALO:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # BS — Bosnian
    # -------------------------------------------------------------------------
    "bs": """
Koristi obaveznu terminologiju Škoda Auto:

MODELI (ne prevodi): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

NIVOI OPREME (ne prevodi): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

ASISTENTSKI SISTEMI:
- Adaptive Cruise Control → Adaptivni tempomat
- Traffic Sign Recognition → Prepoznavanje saobraćajnih znakova
- High Beam Assist → Asistent dalekih svjetala
- Lane Assist → Asistent trake
- Side Assist → Nadzor mrtvog ugla
- Park Assist → Park Assist
- Emergency Assist → Asistent u hitnim situacijama
- Travel Assist → Travel Assist

POVEZIVOST:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Aplikacija MyŠkoda
- Functions on Demand → Funkcije na zahtjev
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up displej
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Glasovni asistent Laura

POGON (ne prevodi): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

SERVIS I GARANCIJA:
- Extended Warranty → Produžena garancija
- Warranty Mobility → Garancija mobilnosti
- Genuine Parts → Originalni dijelovi ŠKODA
- Genuine Accessories → Originalna oprema ŠKODA

OSTALO:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # MK — Macedonian
    # -------------------------------------------------------------------------
    "mk": """
Користи задолжителна терминологија на Škoda Auto:

МОДЕЛИ (не преведувај): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

НИВОА НА ОПРЕМА (не преведувај): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo

АСИСТЕНТСКИ СИСТЕМИ:
- Adaptive Cruise Control → Адаптивен темпомат
- Traffic Sign Recognition → Препознавање сообраќајни знаци
- High Beam Assist → Асистент за долги светла
- Lane Assist → Асистент за лента
- Side Assist → Надзор на слепа точка
- Park Assist → Park Assist
- Emergency Assist → Асистент во итни случаи
- Travel Assist → Travel Assist

ПОВРЗАНОСТ:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → Апликација MyŠkoda
- Functions on Demand → Функции на барање
- Virtual Cockpit → Virtual Cockpit
- Head-up display → Head-up дисплеј
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Гласовен асистент Laura

ПОГОН (не преведувај): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

СЕРВИС И ГАРАНЦИЈА:
- Extended Warranty → Продолжена гаранција
- Warranty Mobility → Гаранција за мобилност
- Genuine Parts → Оригинални делови ŠKODA
- Genuine Accessories → Оригинална опрема ŠKODA

ОСТАНАТО:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV Charger
""",

    # -------------------------------------------------------------------------
    # IS — Icelandic
    # -------------------------------------------------------------------------
    "is": """
Notaðu skylduhugtök Škoda Auto:

LÍKÖN (ekki þýða): Fabia, Scala, Octavia, Octavia Combi, Superb, Superb Combi,
Kamiq, Karoq, Kodiaq, Enyaq, Enyaq Coupé, Elroq, Elroq RS, Peaq, Epiq

BÚNAÐARSTIG (ekki þýða): Classic, Dynamic, Essence, Selection, Top Selection,
Exclusive Selection, Sportline, Scout, RS, Laurin & Klement, Monte Carlo, Drive, Fresh

INNRÉTTINGAR (ekki þýða): Studio, Loft, Lodge, Lounge, Suite, Suite Cognac, ecoSuite

AÐSTOÐARKERFI:
- Adaptive Cruise Control → Aðlægt hraðastillir
- Predictive Cruise Control → Spáhraðastillir
- Lane Assist / Adaptive Lane Assist → Aðlæg akreinaaðstoð
- Traffic Jam Assist → Umferðarstöðuaðstoð
- Side Assist → Dauðhornseftirlit
- Emergency Assist → Neyðaraðstoð
- Traffic Sign Recognition → Umferðarskiltatuvísun
- Park Assist → Bílastæðaaðstoð
- Crew Protect Assist → Hlífðarkerfi farþega
- Driver Fatigue Detection → Þreytuskynjun ökumanns
- High Beam Assist → Langlýsisaðstoð
- Hill Hold Assist → Brekkuhaldsaðstoð
- Travel Assist → Travel Assist

TENGINGAR:
- ŠKODA Connect → ŠKODA Connect
- MyŠKODA → MyŠkoda forritið
- Functions on Demand → Aðgerðir að beiðni
- Virtual Cockpit → Sýndarstuðpallur
- Head-up display → Head-up skjár
- Pay to Fuel → Pay to Fuel
- Pay to Park → Pay to Park
- Powerpass → Powerpass
- Virtual assistant Laura → Sýndaraðstoðarmaðurinn Laura

DRIFKRAFTUR (ekki þýða): TSI, TDI, DSG, m-HEV, PHEV, iV, BEV, 4x4, DCC+

ÞJÓNUSTA OG ÁBYRGÐ:
- Extended Warranty → Škoda framlengd ábyrgð
- Prepaid Service → Fyrirfram greiddur þjónustusamningur
- Warranty Mobility → Škoda ferðaábyrgð
- Škoda Assistance → Škoda aðstoð
- Genuine Parts → Upprunalegar ŠKODA varahlutir
- Genuine Accessories → Upprunalegur ŠKODA aukahlutir

FJÁRMÖGNUN:
- Škoda Financial Services → Škoda Financial Services
- GAP Insurance → GAP trygging

ANNAÐ:
- Škoda Plus → Škoda Plus
- Škoda iV Charger → Škoda iV hleðslutæki
""",
}


def get_glossary(lang_code: str) -> str:
    """Return the glossary for a given language code (e.g. 'cs', 'de', 'fr')."""
    return SKODA_GLOSSARY.get(lang_code.lower(), "")
