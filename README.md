```markdown
# AI Graph Builder

AI Graph Builder is an AI-powered Natural Language Processing (NLP) application that extracts meaningful entities and relationships from unstructured text and transforms them into a structured knowledge graph. The project demonstrates how natural language can be converted into connected information that can be visualized, analyzed, and explored.

## Features

- Extracts entities from unstructured text
- Identifies relationships between entities
- Uses Natural Language Processing for text analysis
- Automatically constructs knowledge graphs
- Represents entities as nodes and relationships as edges
- Converts unstructured text into structured knowledge
- Provides a visual representation of relationships
- Helps users explore connections between different entities

## Technologies Used

- Python
- Natural Language Processing (NLP)
- spaCy
- Knowledge Graphs
- Graph-based Data Representation
- HTML
- CSS
- JavaScript

## How It Works

The application follows an NLP-based pipeline to transform unstructured text into a knowledge graph.

User Input → Text Preprocessing → NLP Processing → Entity Extraction → Relationship Extraction → Graph Construction → Knowledge Graph

The user provides unstructured text as input. The system processes the text using NLP techniques to identify important entities such as people, organizations, locations, and concepts. Relationships between the extracted entities are then identified and represented as connections in the knowledge graph.

The extracted entities become nodes in the graph, while the relationships between those entities become edges. This allows information from plain text to be represented in a structured and connected format.

## Example

Input:

Apple was founded by Steve Jobs, Steve Wozniak and Ronald Wayne. Steve Jobs was the CEO of Apple.

Extracted Entities:

- Steve Jobs → PERSON
- Steve Wozniak → PERSON
- Ronald Wayne → PERSON
- Apple → ORGANIZATION

Extracted Relationships:

- Steve Jobs → founded → Apple
- Steve Wozniak → founded → Apple
- Ronald Wayne → founded → Apple
- Steve Jobs → CEO of → Apple

Generated Knowledge Graph:

Steve Jobs → founded → Apple  
Steve Wozniak → founded → Apple  
Ronald Wayne → founded → Apple  
Steve Jobs → CEO of → Apple

## Project Workflow

1. The user provides unstructured text as input.
2. The text is preprocessed for NLP analysis.
3. The NLP model analyzes the text and identifies relevant information.
4. Named entities such as people, organizations, locations, and concepts are extracted.
5. Relationships between the extracted entities are identified.
6. Entities and relationships are converted into graph components.
7. The knowledge graph is constructed from the extracted information.
8. The resulting graph can be used to understand and explore connections between entities.

## Project Structure

AI-Graph-Builder/
- static/
- templates/
- app.py
- requirements.txt
- README.md

## Installation

Clone the repository:

git clone https://github.com/shivani-avirneni/AI-Graph-Builder.git

Navigate to the project directory:

cd AI-Graph-Builder

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

For macOS/Linux:

source venv/bin/activate

Install the required dependencies:

pip install -r requirements.txt

If the project requires the spaCy English language model, install it using:

python -m spacy download en_core_web_sm

## Running the Application

Start the application using:

python app.py

After starting the application, open the local URL provided by the application in your browser.

For a Flask application, the URL is commonly:

http://127.0.0.1:5000/

## Applications

AI Graph Builder can be useful for:

- Knowledge management
- Information retrieval
- Document analysis
- Research assistance
- Relationship discovery
- Business intelligence
- Academic research
- Legal document analysis
- News and media analysis
- Enterprise knowledge management

## Advantages

- Automates the extraction of meaningful information from text
- Reduces the effort required to manually create knowledge graphs
- Makes relationships between entities easier to understand
- Converts unstructured information into a structured representation
- Provides a foundation for intelligent information retrieval and analysis
- Helps visualize complex relationships between different entities

## Future Enhancements

- Interactive knowledge graph visualization
- Neo4j database integration
- Advanced relationship extraction
- Large Language Model (LLM) integration
- PDF and document upload
- Automatic knowledge graph generation from documents
- Graph search functionality
- Entity linking and disambiguation
- Graph analytics and filtering
- Multiple language support
- Graph export functionality

## Limitations

The accuracy of entity and relationship extraction depends on the quality of the input text, NLP model capabilities, language complexity, ambiguous relationships, and domain-specific terminology. Automatically generated relationships may require verification for specialized applications.

## Project Objective

The objective of AI Graph Builder is to demonstrate how Artificial Intelligence and Natural Language Processing can be used to transform unstructured textual information into structured and connected knowledge.

The project combines Artificial Intelligence, Natural Language Processing, Information Extraction, Entity Recognition, Relationship Extraction, Knowledge Representation, and Graph-based Data Modeling.

## Author

Shivani Avirneni

GitHub: https://github.com/shivani-avirneni

## License

This project is developed for educational and academic purposes.
```
