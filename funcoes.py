import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup as bs
import requests

def gerador_xml(list):
    dc = ET.Element('dublin_core', schema="dc")
    ET.SubElement(dc, 'dcvalue', element='contributor', qualifier='advisor').text = list[0]
    if list[1] != '':
        ET.SubElement(dc, 'dcvalue', element='contributor', qualifier='co-advisor').text = list[1]
    if list[2] != '':  
        ET.SubElement(dc, 'dcvalue', element='contributor', qualifier='co-advisor').text = list[2]
    if list[3] != '':
        ET.SubElement(dc, 'dcvalue', element='contributor', qualifier='co-advisor').text = list[3]   
    ET.SubElement(dc, 'dcvalue', element='contributor', qualifier='author').text = list[4]
    ET.SubElement(dc, 'dcvalue', element='date', qualifier='issued').text = list[5]
    ET.SubElement(dc, 'dcvalue', element='relation', qualifier='ispartof', language='pt_BR').text = list[6]
    if list[8] != '':
        ET.SubElement(dc, 'dcvalue', element='subject', qualifier='none', language='pt_BR').text = list[8]
    if list[9] != '':
        ET.SubElement(dc, 'dcvalue', element='subject', qualifier='none', language='pt_BR').text = list[9]
    if list[10] != '':
        ET.SubElement(dc, 'dcvalue', element='subject', qualifier='none', language='pt_BR').text = list[10]   
    ET.SubElement(dc, 'dcvalue', element='title', qualifier='none', language='pt_BR').text = list[11]
    ET.SubElement(dc, 'dcvalue', element='language', qualifier='iso', language='pt_BR').text = 'por'
    ET.SubElement(dc, 'dcvalue', element='rights', qualifier='none', language='*').text = 'Attribution-NonCommercial-NoDerivs 3.0 Brazil'
    ET.SubElement(dc, 'dcvalue', element='rights', qualifier='uri', language='*').text = 'http://creativecommons.org/licenses/by-nc-nd/3.0/br/'

    return ET.ElementTree(dc)

def baixar_pdf(handle):
    r = requests.get(handle)
    soup = bs(r.text, 'html.parser')
    bistream = soup.find(headers='t1').find('a').get('href')
    pdf = 'https://repositorio.inpa.gov.br'+bistream

    pdf = requests.get(pdf)

    return pdf
    
    
