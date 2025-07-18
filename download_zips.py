import os
from bs4 import BeautifulSoup
import requests
from irs990config import IRS990Config

BASE_IRS_URL = "https://www.irs.gov/charities-non-profits/form-990-series-downloads"

CONFIG = IRS990Config()

def get_bundle_zip_links():

    response = requests.get(BASE_IRS_URL)

    soup = BeautifulSoup(response.content, 'html.parser')

    links = []
    for link  in soup.find_all('a'):
        href = link.get('href')
        if href and href.endswith('zip'):
            links.append(href)
    return links


def download_bundle_files():
    if not os.path.exists(CONFIG.file_repo):
        os.mkdir(CONFIG.file_repo)
    bundle_links = get_bundle_zip_links()
    for link in bundle_links:
        file_path = os.path.join(CONFIG.file_repo, os.path.basename(link))
        response = requests.get(link)
        with open(file_path, 'wb') as file_out:
            file_out.write(response.content)


# for bundle_zip_url in all_bundle_zip_urls:
#     print(bundle_zip_url)
#     response = requests.get(bundle_zip_url, stream=True)
#     with ZipFile(BytesIO(response.content)) as xml_bundle_zip:
#         print(len(xml_bundle_zip.namelist()))
#         count = 0
#         for i, xml_name in enumerate(xml_bundle_zip.namelist()):
#             print(xml_name, end=" ")
#             try:
#                 root = et.fromstring(xml_bundle_zip.read(xml_name).decode())
#             except Exception as err:
#                 print(err)
#             else:
#                 preparer_name = root.find('.//BusinessNameLine1Txt', root.nsmap)
#                 print(preparer_name.text)
#                 count += 1

#     break # only process first bundled zip for now

if __name__ == "__main__":
    # download_bundle_files()
    all_links = get_bundle_zip_links()
    for link in all_links:
        print(link)