# using a few sample documents

import pprint 
from langchain.prompts import PromptTemplate 
from langchain.embeddings import HuggingFaceEmbeddings 
from langchain.vectorstores import FAISS 
from langchain.llms import CTransformers 
from langchain.chains import RetrievalQA 

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2") 

custom_prompt_template = """Use the following pieces of information to answer the user's question. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Context: {context} 
Question: {question} 
Only return the helpful answer below and nothing else. 
Give me the answer in table format. 
Helpful answer:
""" 

def set_custom_prompt(): 
    prompt = PromptTemplate(template=custom_prompt_template, 
    input_variables=['context', 'question']) 
    return prompt 

def load_llm(): 
    llm = CTransformers( 
    model="llama-2-7b-chat.ggmlv3.q2_K.bin", 
    model_type="llama", 
    max_new_tokens=512, 
    temperature=0.1 
    ) 
    return llm 

def retrieval_qa_chain(llm, prompt, db): 
    qa_chain = RetrievalQA.from_chain_type( 
    llm=llm, 
    chain_type='stuff', 
    retriever=db.as_retriever(search_kwargs={'k': 2}), 
    return_source_documents=True, 
    chain_type_kwargs={'prompt': prompt} 
    ) 
    return qa_chain 

def qa_bot(): 
    documents = {} 
    
    documents[0] = "CourseID=C101,CourseName=Mathematics,CourseStartDate=2023-09-01,CourseEndDate=2023-06-15,InstructorID=I101,CourseDescr iption=Standard Level Math Course" 
    documents[1] = "CourseID=C102,CourseName=Science,CourseStartDate=2023-09-15,CourseEndDate=2023-06-30,InstructorID=I102,CourseDescript ion=In-depth Science Exploration" 
    documents[2] = "CourseID=C103,CourseName=History,CourseStartDate=2023-09-10,CourseEndDate=2023-06-20,InstructorID=I103,CourseDescription=World History Studies" 
    documents[3] = "CourseID=C104,CourseName=English Literature,CourseStartDate=2023-09-05,CourseEndDate=2023-06-25,InstructorID=I104,CourseDescription=In-depth Literary Analysis"
    documents[4] = "CourseID=C105,CourseName=Visual Arts,CourseStartDate=2023-09-20,CourseEndDate=2023-06-10,InstructorID=I105,CourseDescription=Creative Visual Expression" 
    documents[5] = "StudentID=101,CourseID=C101,EnrollmentDate=2023-09-01,CompletionDate=2023-12-10,CourseSta tus=Completed" 
    documents[6] = "StudentID=101,CourseID=C102,EnrollmentDate=2023-09-15,CompletionDate=2023-12-20,CourseSta tus=Completed" 
    documents[7] = "StudentID=101,CourseID=C105,EnrollmentDate=2023-09-20,CompletionDate=2023-12-15,CourseSta tus=Not-Completed" 
    documents[8] = "StudentID=102,CourseID=C103,EnrollmentDate=2023-09-10,CompletionDate=2023-12-18,CourseSta tus=Not-Completed" 
    documents[9] = "StudentID=103,CourseID=C108,EnrollmentDate=2023-09-12,CompletionDate=2023-12-28,CourseSta tus=Not-Completed" 
    documents[10] = "AssignmentID=A101,CourseID=C101,AssignmentName=Algebra Quiz 1,AssignmentType=Quiz,DueDate=2023-10-10,TotalPoints=20,Description=First quiz on algebra topics" 
    documents[11] = "AssignmentID=A102,CourseID=C101,AssignmentName=Algebra Homework 1,AssignmentType=Homework,DueDate=2023-10-15,TotalPoints=15,Description=Practice problems" 
    documents[12] = "AssignmentID=A103,CourseID=C102,AssignmentName=Science Essay,AssignmentType=Essay,DueDate=2023-10-18,TotalPoints=30,Description=Write an essay on a science topic" 
    documents[13] = "AssignmentID=A104,CourseID=C102,AssignmentName=Lab Report,AssignmentType=Project,DueDate=2023-10-25,TotalPoints=25,Description=Submit lab report" 
    documents[14] = "AssignmentID=A105,CourseID=C103,AssignmentName=History Research,AssignmentType=Project,DueDate=2023-10-20,TotalPoints=35,Description=Research and present on a historical event" 
    
    db = FAISS.from_texts(list(documents.values()), embedding) 
    llm = load_llm() 
    qa_prompt = set_custom_prompt() 
    qa = retrieval_qa_chain(llm, qa_prompt, db) 
    return qa 

def final_result(query): 
    print("The question you asked:\n", query) 
    qa_result = qa_bot() 
    response = qa_result({'query': query}) 
    pp = pprint.PrettyPrinter(indent=4) 
    pp.pprint(response["source_documents"]) 
    return response["result"]


print(final_result("Give me details of all courses")) 