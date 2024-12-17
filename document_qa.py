from langchain_google_genai import GoogleGenerativeAI
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os

# this class can load documents, process them, and answer questions
class DocumentQA:
    def __init__(self, api_key):
        os.environ["GOOGLE_API_KEY"] = api_key  # initializing the api key here
        
        self.llm = GoogleGenerativeAI(model="gemini-1.5-flash-latest", temperature=0.0)
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    def load_and_process_document(self, file_path):
        loader = TextLoader(file_path)
        documents = loader.load()
        # 200 character overlap bc it provides context for the model:
        text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200) 
        texts = text_splitter.split_documents(documents)
        # Facebook AI Similarity Search:
        # we turn the text chunks into vectors and store them in a vector store
        # when the question is asked, the vector store is used to find the most relevant chunks
        self.vectorstore = FAISS.from_documents(texts, self.embeddings)
        # Example:
        # Text: "The cat sat on the mat" → [0.23, 0.84, -0.44, 0.91, ...]
        # Text: "Dogs love to play fetch" → [0.56, -0.12, 0.77, 0.32, ...]
        # Question: "What is the cat doing?" → [0.25, 0.82, -0.41, 0.88, ...]
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever()
        )

    def ask_question(self, question):
        return self.qa_chain.run(question)


# creating an instance of the DocumentQA class to actually use it
if __name__ == "__main__":
    qa_system = DocumentQA("your_google_api_key_here")
    qa_system.load_and_process_document("path/to/your/document.txt")
    
    while True:
        question = input("\nEnter your question (or 'quit' to exit): ")
        if question.lower() == 'quit':
            break
        
        answer = qa_system.ask_question(question)
        print(f"\nAnswer: {answer}")















	





        

