from langchain.text_splitter import RecursiveCharacterTextSplitter 

text = """
Artificial Intelligence (AI) is a branch of computer science that focuses on creating intelligent machines that can work and react like humans. It involves the development of algorithms and computer programs that can perform tasks that typically require human intelligence, such as visual perception, speech recognition, decision making, and language translation.

AI is a broad field that encompasses many different approaches and techniques, including machine learning, natural language processing, computer vision, and robotics. These techniques allow machines to learn from data, recognize patterns, and make decisions based on that information.

One of the key goals of AI is to create machines that can think, reason, and learn like humans. This is known as artificial general intelligence (AGI) and is often portrayed in science fiction as human-like robots with emotions and consciousness. While AGI is a long-term goal of AI research, the current focus is on creating more specialized forms of AI, known as narrow AI, that can perform specific tasks
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300, 
    chunk_overlap = 0
)

chunks = splitter.split_text(text)

print(len(chunks))
print(chunks[0])