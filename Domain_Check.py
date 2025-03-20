{\rtf1\ansi\ansicpg1252\cocoartf2821
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\froman\fcharset0 Times-Roman;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww28600\viewh17520\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import requests\
\
# List of domains to check\
domains = [\
    "https://newportsensors.com/",\
    "https://mcetsensors.com/",\
    "https://www.optowares.com/",\
    "https://legacy.www.sbir.gov/node/2264559",\
    "https://preteckt.com/",\
    "https://sossecinc.com/company/intelligent-automation-inc/",\
    "https://migmapd.com/contact.htm",\
    "https://www.nsti.org/directory/org.html?i=848",\
    "https://indiana-company.com/co/saytech-corporation",\
    "https://www.sncorp.com/company/locations/",\
    "https://www.vieuxinc.com/",\
    "https://pitchbook.com/profiles/company/56278-27#overview",\
    "https://www.atcorp.com/about/",\
    "https://www.dakotatechnologies.com/",\
    "https://optics.org/buyers/B000013250",\
    "https://jfaucett.com/",\
    "https://www.physicalacoustics.com/",\
    "https://phoenix-scientific.com/",\
    "https://www.thecollaborative.com/",\
    "https://www.qinetiq.com/en-us/",\
    "https://imcorp.com/",\
    "https://www.ionoptics.com",\
    "http://www.i-a-i.com",\
    "http://www.optimus.com",\
    "https://rletech.com/",\
    "https://inforfusion.org/",\
    "http://www.ajboggs.com/",\
    "https://www.readthomas.com/",\
    "http://www.creativepultrusions.com",\
    "http://www.geosystems.com",\
    "http://www.faucett.com",\
    "https://www.kjsassociates.net/",\
    "https://lowbluelights.com/",\
    "https://www.safetybydesigninc.com/",\
    "https://foster-miller.com/",\
    "https://gky.com",\
    "https://multisystems.com/",\
    "http://newconceptinc.com/index2.html",\
    "https://rletech.com/contact/",\
    "http://www.sqm.com",\
    "https://www.wphassociates.com",\
    "https://www.arcca.com",\
    "https://www.ara.com",\
    "https://www.ensco.com",\
    "http://www.quanticnow.com",\
    "http://www.robotronics.com",\
    "http://www.stressphotonics.com",\
    "https://www.ves-systems.com",\
    "https://www.aerotech.com",\
    "https://www.aegisis.com/contact/",\
    "https://www.tscti.com/company",\
    "https://www.colography.com",\
    "http://www.dvppumps.com",\
    "https://gaeaglobal.com",\
    "https://www.kvh.com",\
    "http://midgatransportationconsulting.com",\
    "https://aisignal.com",\
    "https://nicholsresearch.com/",\
    "https://www.blackmoninsgrp.com",\
    "https://www.datacm.com/",\
    "https://davidgordongroup.com/",\
    "https://easternanalytical.com",\
    "https://www.solvay.com/en/",\
    "https://www.msasafety.com/global",\
    "https://www.gd.com",\
    "https://www.sei-sdrs.com",\
    "https://www.stress.com",\
    "https://davidgordongroup.com/contact",\
    "https://www.energyinnovations.com",\
    "https://www.philips.com",\
    "https://lsrtech.com",\
    "https://www.gdit.com",\
    "https://www.rapiscansystems.com",\
    "http://www.quanex.com",\
    "https://www.systemscontrol.com/",\
    "https://www.tensor-technology.com",\
    "https://unison-ucg.com",\
    "https://www.femtometrix.com/",\
    "https://www.jensenhughes.com",\
    "https://www.invocon.com",\
    "https://www.viasat.com/about/who-we-are/locations/",\
    "https://amerasiatech.com",\
    "https://www.buzzfile.com/business/Carlow-International-Inc-571-434-9222",\
    "https://www.bizapedia.com/tx/exodyne-technologies-inc.html",\
    "https://www.horizonmarine.com/",\
    "https://www.materials-engr.com/",\
    "https://overlooksys.com/",\
    "https://www.intellicorp.net/marketing",\
    "https://www.owec.com/about.html",\
    "http://pepinassociates.com/aboutus.html",\
    "https://www.savi.com/company/",\
    "https://scientech-inc.com/",\
    "https://beltrantechnologies.com/contact-us/",\
    "https://www.humrro.org/corpsite/",\
    "https://www.redmannlaw.com/about-us/our-team/edward-l-moreno/",\
    "https://gst.jamku.app/gstin/33AEUPD0094D1ZR",\
    "https://www.tau-trade.com/sal_frt/",\
    "https://www.flowwaterjet.com/en",\
    "https://jjtech.com/",\
    "https://ssrc.com/",\
    "https://westcoastresearch.com/",\
    "https://cage.report/NCAGE/8P690",\
    "https://www.fluidynecorp.com/",\
    "https://www.quantix.com/",\
    "https://imi-technology.com/",\
    "https://www.innotech-sys.com/",\
    "https://www.jflsln.com/",\
    "https://www.klawindustries.com/",\
    "https://www.nalariscientific.com/",\
    "https://www.infrasense.com/",\
    "https://thesensorgroup.com/",\
    "https://www.polymaterialsapp.com/",\
    "https://www.protection-consultants.com/",\
    "https://revoltbatterytechnology.com/",\
    "https://bluefusion.com/",\
    "https://mosaicatm.com/",\
    "https://www.saferstreetsolutions.com/",\
    "https://www.psicorp.com/",\
    "https://www.blueflite.com/2024/09/20/",\
    "https://www.legacy.us/",\
    "https://toolinc.com/",\
    "https://corrolytics.com/",\
    "https://senslytics.com/",\
    "https://nanosonic.com/",\
    "https://www.friedmanresearch.com/",\
    "https://biointerphase.com/"\
]\
\
# Function to check if a URL is working\
def check_domain_status(url):\
    try:\
        response = requests.get(url, timeout=5)\
        # Check if the status code is in the 200 range\
        if response.status_code == 200:\
            return "Up"\
        else:\
            return f"Down (Status code: \{response.status_code\})"\
    except requests.RequestException as e:\
        return f"Down (Error: \{e\})"\
\
# Check the status of each domain\
domain_status = \{\}\
for domain in domains:\
    status = check_domain_status(domain)\
    domain_status[domain] = status\
\
# Print the status of each domain\
for domain, status in domain_status.items():\
    print(f"\{domain\}: \{status\}")}