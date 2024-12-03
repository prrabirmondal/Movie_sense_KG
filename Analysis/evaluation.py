import pandas as pd
import os
import numpy as np


import scrape
import process_kg
import evaluation_question
import evaluation_node


seed_value = 42
np.random.seed(seed_value)


def human_eval(movie_links, filmIndustry, nodeFile_root):
    def load_eval_file(file_name, column_list):
        # Check if the file exists
        if os.path.exists(file_name):
            # Load the CSV file
            df = pd.read_csv(file_name)
        else:
            # Create a new DataFrame with specified columns
            df = pd.DataFrame(columns=column_list)
        return df



    columns = ["YoR", "movie_name", "imdb_rating", "wiki_link", "popular"]
    movie_links.columns = columns
    
    evaluated_movie = load_eval_file("evaluated_movie.csv", column_list=['film_industry','category', 'movie_name', 'yor', 'aspect'])
    # evaluated_movie = pd.DataFrame(columns=['film_industry','category', 'movie_name', 'yor', 'aspect'])
    
    node_eval_dataframe = load_eval_file("node_eval_dataframe.csv", column_list=["film_industry", "category", "aspect", "triplet_relevant", "triplet_irrelevant", "relation_relevant", "relation_irrelevant"])
    # node_eval_dataframe = pd.DataFrame(columns=["film_industry", "category", "aspect", "triplet_relevant", "triplet_irrelevant", "relation_relevant", "relation_irrelevant"])
    
    question_eval_dataframe = load_eval_file("question_eval_dataframe.csv", column_list=["film_industry", "category", "complexity", "question_type", "aspect",  "from_aspect", "not_from_aspect", "meaningful_0", "meaningful_1", "meaningful_2", "very_correct", "partially_correct", "incorrect", "complex", "moderate", "simple"])
    # question_eval_dataframe = pd.DataFrame(columns=["film_industry", "category", "complexity", "question_type", "aspect",  "from_aspect", "not_from_aspect", "meaningful_0", "meaningful_1", "meaningful_2", "very_correct", "partially_correct", "incorrect", "complex", "moderate", "simple"])


    Categories = os.listdir(nodeFile_root)


    aspect_list = ['Accolades',
    'Cast',
    'Guardians of the Galaxy Vol',
    'Music',
    'Plot',
    'Production',
    'Soundtrack',
    'Themes',
    'summary']


    # define the dictionaries to keep the evaluations
    #-------------------------------------------------

    # for the node evaluation
    #===============================
    for category in Categories:
        for aspect in aspect_list:
            total_movie = 0
            triplet_eval = {"film_industry": filmIndustry,
                            "category" : category,
                            "aspect" : aspect,
                            "triplet_relevant" : 0, 
                            "triplet_irrelevant" : 0,
                            "relation_relevant" : 0,
                            "relation_irrelevant" : 0}
            
    # for the questions evaluations
    #================================

            # for hop1------------------------------
            eval_dataframe_yes_no_h1 = {"film_industry": filmIndustry, "category" : category, "complexity" : "simple", "question_type" : "yes_no", "aspect" : aspect,  "from_aspect" : 0, "not_from_aspect" : 0, "meaningful_0" : 0, "meaningful_1" : 0, "meaningful_2" : 0, "very_correct" : 0, "partially_correct" : 0, "incorrect" : 0, "complex" : 0, "moderate" : 0, "simple" : 0}
        
            eval_dataframe_MCQ_S_h1 = {"film_industry": filmIndustry, "category" : category, "complexity" : "simple", "question_type" : "mcq_s", "aspect" : aspect,  "from_aspect" : 0, "not_from_aspect" : 0, "meaningful_0" : 0, "meaningful_1" : 0, "meaningful_2" : 0, "very_correct" : 0, "partially_correct" : 0, "incorrect" : 0, "complex" : 0, "moderate" : 0, "simple" : 0}
        
            eval_dataframe_MCQ_M_h1 = {"film_industry": filmIndustry, "category" : category, "complexity" : "simple", "question_type" : "mcq_m", "aspect" : aspect,  "from_aspect" : 0, "not_from_aspect" : 0, "meaningful_0" : 0, "meaningful_1" : 0, "meaningful_2" : 0, "very_correct" : 0, "partially_correct" : 0, "incorrect" : 0, "complex" : 0, "moderate" : 0, "simple" : 0}
            
            # for hop2------------------------------
            eval_dataframe_yes_no_h2 = {"film_industry": filmIndustry, "category" : category, "complexity" : "moderate", "question_type" : "yes_no", "aspect" : aspect,  "from_aspect" : 0, "not_from_aspect" : 0, "meaningful_0" : 0, "meaningful_1" : 0, "meaningful_2" : 0, "very_correct" : 0, "partially_correct" : 0, "incorrect" : 0, "complex" : 0, "moderate" : 0, "simple" : 0}
        
            eval_dataframe_MCQ_S_h2 = {"film_industry": filmIndustry, "category" : category, "complexity" : "moderate", "question_type" : "mcq_s", "aspect" : aspect,  "from_aspect" : 0, "not_from_aspect" : 0, "meaningful_0" : 0, "meaningful_1" : 0, "meaningful_2" : 0, "very_correct" : 0, "partially_correct" : 0, "incorrect" : 0, "complex" : 0, "moderate" : 0, "simple" : 0}
        
            eval_dataframe_MCQ_M_h2 = {"film_industry": filmIndustry, "category" : category, "complexity" : "moderate", "question_type" : "mcq_m", "aspect" : aspect,  "from_aspect" : 0, "not_from_aspect" : 0, "meaningful_0" : 0, "meaningful_1" : 0, "meaningful_2" : 0, "very_correct" : 0, "partially_correct" : 0, "incorrect" : 0, "complex" : 0, "moderate" : 0, "simple" : 0}
            
            # for hop3------------------------------
            eval_dataframe_yes_no_h3 = {"film_industry": filmIndustry, "category" : category, "complexity" : "complex", "question_type" : "yes_no", "aspect" : aspect,  "from_aspect" : 0, "not_from_aspect" : 0, "meaningful_0" : 0, "meaningful_1" : 0, "meaningful_2" : 0, "very_correct" : 0, "partially_correct" : 0, "incorrect" : 0, "complex" : 0, "moderate" : 0, "simple" : 0}
        
            eval_dataframe_MCQ_S_h3 = {"film_industry": filmIndustry, "category" : category, "complexity" : "complex", "question_type" : "mcq_s", "aspect" : aspect,  "from_aspect" : 0, "not_from_aspect" : 0, "meaningful_0" : 0, "meaningful_1" : 0, "meaningful_2" : 0, "very_correct" : 0, "partially_correct" : 0, "incorrect" : 0, "complex" : 0, "moderate" : 0, "simple" : 0}
        
            eval_dataframe_MCQ_M_h3 = {"film_industry": filmIndustry, "category" : category, "complexity" : "complex", "question_type" : "mcq_m", "aspect" : aspect,  "from_aspect" : 0, "not_from_aspect" : 0, "meaningful_0" : 0, "meaningful_1" : 0, "meaningful_2" : 0, "very_correct" : 0, "partially_correct" : 0, "incorrect" : 0, "complex" : 0, "moderate" : 0, "simple" : 0}

            
            
            # 8. add aspect in both dataframe of node and question
            
            node_file_names = os.listdir(os.path.join(nodeFile_root, category))
            node_file_names = [node_file_name for node_file_name in node_file_names if node_file_name.split(".")[0].split("_")[-1] == aspect]
            for node_file_name in node_file_names:
                
                movie_name, yor = node_file_name.split("_")[0], node_file_name.split("_")[1]
                # print(movie_name)
                
                condition = (evaluated_movie['category'] == category) & (evaluated_movie['movie_name'] == movie_name) & (evaluated_movie['aspect'] == aspect)
                
                # Check if any row satisfies the condition
                result = evaluated_movie[condition]

                # Output the result
                if not result.empty:
                    continue
                else:
                    
                    try:
                        # get the context from wikipedia
                        
                        wiki_link = movie_links[movie_links.movie_name == movie_name]["wiki_link"].iloc[0]

                        scraped_dict = scrape.scrape(wiki_link)
                    
                        node_file = pd.read_csv(os.path.join(nodeFile_root, category, node_file_name))

                        sample_30_count = int(0.3*len(node_file))
                        node_file = node_file.sample(n=sample_30_count, random_state=seed_value)
                        
                    except:
                        
                        continue
                        
                    if len(node_file)>=3:
                        
                        h1q1, h1q2, h1q3 = process_kg.fetch_questions(category, node_file_name, "Simple_hop1")
                        h2q1, h2q2, h2q3 = process_kg.fetch_questions(category, node_file_name, "Moderate_hop2")
                        h3q1, h3q2, h3q3 = process_kg.fetch_questions(category, node_file_name, "Complex_hop3")
                        
                        try:
                            #save the scraped aspect of the considered movie                
                            scrape.save_aspect(aspect, scraped_dict[aspect], movie_name, yor)
                            process_kg.clear_terminal()
                            print("\n Please check the content from the movie.txt file and then response the questions here. \nPress Enter to start.")
                            print("==================================================================================================================")                    
                            input()
                            
                                                
                            # 1. Evaluate nodes (use terminal clear in the eval method)
                            triplet_eval = evaluation_node.eval_nodes(node_file, triplet_eval) #returns relevant and irrelevant triplet counts and relation counts
                            
                            # 2. update the node evaluation dataframe of this aspect..........done
                            
                            # 3. Evaluate Questions
                            eval_dataframe_yes_no_h1, eval_dataframe_MCQ_S_h1, eval_dataframe_MCQ_M_h1 = evaluation_question.eval_question(h1q1, h1q2, h1q3, eval_dataframe_yes_no_h1, eval_dataframe_MCQ_S_h1, eval_dataframe_MCQ_M_h1)
                            eval_dataframe_yes_no_h2, eval_dataframe_MCQ_S_h2, eval_dataframe_MCQ_M_h2 = evaluation_question.eval_question(h2q1, h2q2, h2q3, eval_dataframe_yes_no_h2, eval_dataframe_MCQ_S_h2, eval_dataframe_MCQ_M_h2)
                            eval_dataframe_yes_no_h3, eval_dataframe_MCQ_S_h3, eval_dataframe_MCQ_M_h3 = evaluation_question.eval_question(h3q1, h3q2, h3q3, eval_dataframe_yes_no_h3, eval_dataframe_MCQ_S_h3, eval_dataframe_MCQ_M_h3)
                            
                            
                            
                            
                            # 7. check the movie count for taking decision for further process
                            
                            
                        except:
                            continue
                        
                        # 4. merge all the question evaluation
                            
                            # 5. update the question evaluation dataframe of this aspect
                        
                            
                        df1 = [triplet_eval]
                        df1 = pd.DataFrame.from_dict(df1)
                        node_eval_dataframe = pd.concat([df1, node_eval_dataframe], axis=0, ignore_index=False)
                        
                        
                        df2 = [eval_dataframe_yes_no_h1, eval_dataframe_MCQ_S_h1, eval_dataframe_MCQ_M_h1, eval_dataframe_yes_no_h2, eval_dataframe_MCQ_S_h2, eval_dataframe_MCQ_M_h2, eval_dataframe_yes_no_h3, eval_dataframe_MCQ_S_h3, eval_dataframe_MCQ_M_h3 ]
                        df2 = pd.DataFrame.from_dict(df2)
                        question_eval_dataframe = pd.concat([df2, question_eval_dataframe], axis=0, ignore_index=False)
                        
                        # 6. save the movie file name so that recompute is omit
                                
                        evaluated_movie.loc[len(evaluated_movie)] = [filmIndustry, category, movie_name, yor, aspect]
                        
                        # Save the DataFrame to a CSV file
                        evaluated_movie_path = "evaluated_movie.csv"
                        question_eval_dataframe_path = "question_eval_dataframe.csv"
                        node_eval_dataframe_path = "node_eval_dataframe.csv"
                        
                        evaluated_movie.to_csv(evaluated_movie_path, index=False) 
                        question_eval_dataframe.to_csv(question_eval_dataframe_path, index=False) 
                        node_eval_dataframe.to_csv(node_eval_dataframe_path, index=False) 
                        
                                                
                        total_movie += 1
                        process_kg.clear_terminal()
                        print(f"CONGRATULATIONS!!, total {total_movie} movie(s) of {aspect} aspect done. Keep doing. Thanks.\n Press Enter for the next movie.")
                        input()
                        if total_movie == 30:
                            break
                            
                            
                    
            
