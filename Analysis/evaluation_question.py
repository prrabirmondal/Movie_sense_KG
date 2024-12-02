from process_kg import clear_terminal

# for question evaluation
#------------------------------
def eval_question(yes_no_questions, MCQ_S_questions, MCQ_M_questions, eval_dataframe_yes_no, eval_dataframe_MCQ_S, eval_dataframe_MCQ_M):
    def is_from_aspect(row, question_col, answer_col):
        response_list,qstn_rspns = [1, 0], None
        while qstn_rspns not in response_list:
            try:
                clear_terminal()
                print(f"Question : {row[question_col]}, \nAnswer : {row[answer_col]}")
                print("===================================================================================")
                qstn_rspns = int(input("Is the question from the aspect? Press 1 for Yes, 0 for No: "))
                if qstn_rspns not in response_list:
                    print("Wrong Entry, please enter again. Press Enter for try again.")
                    input()
            except:
                print("Wrong Entry, please enter again. Press Enter for try again.")
                input()
                continue       
        return qstn_rspns
    
    
    def is_meaningful(row, question_col, answer_col):
        response_list,qstn_rspns = [2, 1, 0], None
        while qstn_rspns not in response_list:
            try:
                clear_terminal()
                print(f"Question : {row[question_col]}, \nAnswer : {row[answer_col]}")
                print("===================================================================================")
                qstn_rspns = int(input("Is the question Meaningful? Press 2 for Strongly meaningful, 1 for Moderate meaningful, 0 for Meaningless: "))
                if qstn_rspns not in response_list:
                    print("Wrong Entry, please enter again. Press Enter for try again.")
                    input()    
            except:
                print("Wrong Entry, please enter again. Press Enter for try again.")
                input()
                continue    
        return qstn_rspns
    
    def is_answer_correct(row, question_col, answer_col):
        response_list,qstn_rspns = [2, 1, 0], None
        while qstn_rspns not in response_list:
            try:
                clear_terminal()
                print(f"Question : {row[question_col]}, \nAnswer : {row[answer_col]}")
                print("===================================================================================")
                qstn_rspns = int(input("Is the answer correct? Press 2 for Very correct, 1 for partially correct, 0 for incorrect: "))
                if qstn_rspns not in response_list:
                    print("Wrong Entry, please enter again. Press Enter for try again.")
                    input()     
            except:
                print("Wrong Entry, please enter again. Press Enter for try again.")
                input()
                continue   
        return qstn_rspns
    
    def question_complexity(row, question_col, answer_col):
        response_list,qstn_rspns = [2, 1, 0], None
        while qstn_rspns not in response_list:
            try:
                clear_terminal()
                print(f"Question : {row[question_col]}, \nAnswer : {row[answer_col]}")
                print("===================================================================================")
                qstn_rspns = int(input("How complex the question is? Press 2 for Very complex, 1 for Moderate, 0 for Simple: "))
                if qstn_rspns not in response_list:
                    print("Wrong Entry, please enter again. Press Enter for try again.")
                    input()  
            except:
                print("Wrong Entry, please enter again. Press Enter for try again.")
                input()
                continue      
        return qstn_rspns
    
    
    def single_question_eval(row, question_col, answer_col, eval_dataframe):
        is_from_aspect_reponse = is_from_aspect(row, question_col, answer_col)
        if is_from_aspect_reponse == 1:
            # update the count of aspect
            eval_dataframe["from_aspect"] += 1
            is_meaningful_reponse = is_meaningful(row, question_col, answer_col)
            if is_meaningful_reponse in [1, 2]:
                question_complexity_reponse = question_complexity(row, question_col, answer_col)
                is_answer_correct_reponse = is_answer_correct(row, question_col, answer_col)
                
                                
                # update the count of meaningfulness
                if is_meaningful_reponse == 1:
                    eval_dataframe["meaningful_1"] += 1
                else: eval_dataframe["meaningful_2"] += 1
                
                # update the count of complexity
                if question_complexity_reponse == 2:
                    eval_dataframe["complex"] += 1
                elif question_complexity_reponse == 1:
                    eval_dataframe["moderate"] += 1
                else: eval_dataframe["simple"] += 1
                
                #update correct answer
                if is_answer_correct_reponse == 2:
                    eval_dataframe["very_correct"] += 1
                elif is_answer_correct_reponse == 1:
                    eval_dataframe["partially_correct"] += 1
                else: eval_dataframe["incorrect"] += 1
                
                
            else: eval_dataframe["meaningful_0"] += 1
    
        else:
            eval_dataframe["not_from_aspect"] += 1
        
        return eval_dataframe
        
    for index, row in yes_no_questions.iterrows():
        question_col, answer_col = "Question", "Answer"
        eval_dataframe_yes_no = single_question_eval(row, question_col, answer_col, eval_dataframe_yes_no)
    
    for index, row in MCQ_S_questions.iterrows():
        question_col, answer_col = "Question & Options", "Correct Answer"
        eval_dataframe_MCQ_S = single_question_eval(row, question_col, answer_col, eval_dataframe_MCQ_S)
    
    for index, row in MCQ_M_questions.iterrows():
        question_col, answer_col = "Question & Options", "Correct Answer"
        eval_dataframe_MCQ_M = single_question_eval(row, question_col, answer_col, eval_dataframe_MCQ_M)
    
    
    return eval_dataframe_yes_no, eval_dataframe_MCQ_S, eval_dataframe_MCQ_M