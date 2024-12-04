import pandas as pd
import evaluation


#*********** change two paths at process_kg.py (questionFile_root) and
# *********** at scrape.py (save_file_path)


movie_links = pd.read_excel("/mnt/Data/prabirmondal/prabir/python_program/movie_sense/SRI_KG/Movie_sense_KG/Movie_sense_KG/aspect_wise_knowledge_graph/workspace/Movie_list.xlsx", sheet_name = "hollywood", engine='openpyxl')

start_row = 0
end_row = start_row + 50

# Slice the DataFrame to get the middle 10 rows
movie_links_part = movie_links.iloc[start_row:end_row]

filmIndustry = "Hollywood"
nodeFile_root = "/mnt/Data/prabirmondal/prabir/python_program/movie_sense/SRI_KG/Movie_sense_KG/Movie_sense_KG/Dataset/Nodes_Edges/Hollywood"


evaluation.human_eval(movie_links_part, filmIndustry, nodeFile_root)