from bs4 import BeautifulSoup
import requests
# from pathlib import Path
# from tqdm import tqdm

def save_aspect(aspect, content, movie_name, yor, save_file_path = "/mnt/Data/prabirmondal/prabir/python_program/movie_sense/SRI_KG/Movie_sense_KG/Movie_sense_KG/Analysis/movie.txt"):
    # print(f"from save aspect, {aspect}")
    introduction = f"Movie_name = {movie_name}, Year or release = {yor}.\n HERE IS THE DETAILS OF MOVIE'S {aspect.upper()}: \n"
    underline = "-----------------------------------------------------\n"
    para = introduction + underline + content
    # print(para)
    # input()
    # print(para)
    # Open the file in write mode and save the paragraph
    with open(save_file_path, 'w') as file:
        file.write(para)
    
    # print(f"Paragraph saved to {save_file_path} for {aspect}.")


def scrape(wiki_link):
    Aspects = [
        'Plot',
        'Cast',
        'Production',
        'Music',
        'Soundtrack',
        'Themes',
        'Accolades',
        ]

    Aspects = [aspect.lower() for aspect in Aspects]
    
    # Send a request to the Wikipedia page
    response = requests.get(wiki_link)
    
    # Parse the page content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    scraped_dict = {}
    
    #-------------------Summary scraping--------------------------
    # Find the first paragraph after the title, which is usually the summary
    summary_paragraphs = []
    # Wikipedia's summary paragraphs are inside <p> tags but before any <h2> tag
    for paragraph in soup.find_all('p'):
        
        # Ensure the paragraph has text and is not empty
        if paragraph.get_text().strip():
            summary_paragraphs.append(paragraph.get_text().strip())
        
        # Stop once we hit the first section heading (e.g. 'Plot' or 'Contents')
        if paragraph.find_next_sibling(['h2', 'h3']):
            break
    
    scraped_dict["summary"] =  ' '.join(summary_paragraphs)
    
    
    # -------------------Other Aspect Scraping---------------------
    Headings = soup.find_all('div', class_ = 'mw-heading mw-heading2')
    for heading in Headings:
        try:
            aspect, _ = (heading.text).split('[')
        except:
            aspect = heading.text
            
        if aspect.lower() in Aspects:
            next_siblings = heading.find_next_siblings()
            text = ''
            for next_sibling in next_siblings:
                next_sibling_name = next_sibling.name
                # sub_sibling = ''
                # print(f"............next_sibling_name = {next_sibling_name}")
                if (next_sibling_name =='style'):
                    continue
                
                elif (next_sibling_name == 'div'):
                    clss = next_sibling.get('class')
                    
                    if ('mw-heading2' in clss):  # break because heading ended
                        break
                text += " "+ next_sibling.text
            scraped_dict[aspect] = text 
    return scraped_dict