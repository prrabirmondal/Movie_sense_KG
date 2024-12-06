from process_kg import clear_terminal

# node evaluation
#------------------------
def eval_nodes(node_file, triplet_eval):    
    def triplet_eval_response(row):
        response_list,triplet_rspns = [1, 0], None
        while triplet_rspns not in response_list:
            try:
                clear_terminal()
                print(f"Node_1 : {row['node_1']}, \nNode_2 : {row['node_2']}, \nRelation : {row['edge']}")
                print("===================================================================================")
                triplet_rspns = int(input("Is the triplet from the aspect? Press 1 for Yes, 0 for No: "))
                if triplet_rspns not in response_list:
                    print("Wrong Entry, please enter again. Press Enter for try again.")
                    input()
            except:
                print("Wrong Entry, please enter again. Press Enter for try again.")
                input()
                continue
        return triplet_rspns
    
    def triplet_relation_eval_response(row):
        response_list,triplet_rspns = [1, 0], None
        while triplet_rspns not in response_list:
            try:
                clear_terminal()
                print(f"Node_1 : {row['node_1']}, \nNode_2 : {row['node_2']}, \nRelation : {row['edge']}")
                print("===================================================================================")
                triplet_rspns = int(input("Is the relation true between the two nodes? Press 1 for Yes, 0 for No: "))
                if triplet_rspns not in response_list:
                    print("Wrong Entry, please enter again. Press Enter for try again.")
                    input()
            except:
                print("Wrong Entry, please enter again. Press Enter for try again.")
                input()
                continue
        return triplet_rspns
        
        

    
    for index, row in node_file.iterrows():  
        # print(f"node = {index}/{len(node_file)}"); input()      
        triplet_eval_response_1 = triplet_eval_response(row)
        if triplet_eval_response_1 == 1:
            triplet_eval["triplet_relevant"] += 1           
            triplet_relation_eval_response_1 = triplet_relation_eval_response(row)
            if triplet_relation_eval_response_1 == 1:
                triplet_eval["relation_relevant"] += 1
            else: triplet_eval["relation_irrelevant"] += 1
            
        else: triplet_eval["triplet_irrelevant"] += 1
        # break
    return triplet_eval