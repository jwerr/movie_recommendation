Content-Based Movie Recommendation System

This is a content-based recommendation system that suggests movies based on a user's textual input. The system uses TF-IDF vectorization and cosine similarity to find the most relevant movies from a dataset.

Overview

The goal of this project is to build a simple yet functional content-based recommendation system. Given a short text description of a user’s preferences, the system suggests similar items (e.g., movies) from a small dataset. The system processes the user's input, compares it to the dataset, and returns the top 3–5 closest matches.


Example Use Case


User Input
"I love thrilling action movies set in space, with a comedic twist."

Output
                                       Love Actually          0.366720
                                        Ghostbusters          0.362867
                                              Aliens          0.306904
   The Lord of the Rings: The Fellowship of the Ring           0.206456
                                         Interstellar          0.205904


Dataset

Source
The dataset used in this project is a small collection of movies with their titles , plot summaries and genre . It is included in the repository as `movies.csv`.

Format
The dataset contains the following columns:
- `title`: The title of the movie.
- `plot_summary`: A short description of the movie's plot.
- `genre`: The genre of the movie (optional).

Loading the Dataset
The dataset is loaded using `pandas`:

```def load_data(filepath):
    """
    Load the dataset from a CSV file.
    """
    data = pd.read_csv(filepath)
    return data```

System Workflow
1. Preprocessing:
   - The user's input is preprocessed (e.g., lowercasing, removing stopwords).
   - Example processed query: `"love thrilling action movie set space comedic twist"`.

2. TF-IDF Vectorization:
   - The user's input and movie plot summaries are transformed into TF-IDF vectors.

3. Cosine Similarity:
   - Cosine similarity is computed between the user's input vector and all movie description vectors.

4. Top Recommendations:
   - The system returns the top 3–5 movies with the highest similarity scores.

System Output
The system outputs the recommended movies along with their similarity scores.

Set Up the Project
Clone the Repository (Optional):
If the code is hosted on GitHub, clone the repository:


git clone https://github.com/your-username/movie-recommendation.git
cd movie-recommendation

Dataset:
movies.csv file is placed it in the data/ folder inside the project directory.
We can view the data by this command.

python data_view.py

If you don’t have a dataset, you can use the example dataset provided in the repository or create your own.

Project Directory Structure:
Ensure your project directory looks like this:

movie-recommendation/
├── data/
│   └── movies.csv
├── recommend.py
├── requirements.txt
└── README.md

Step 3: Set Up a Virtual Environment (Optional but Recommended)
Create a virtual environment:


python -m venv venv
Activate the virtual environment:

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

Step 4: Install Dependencies
Install the required Python libraries by running:
pip install -r requirements.txt

Step 5: Run the Recommendation System
Run the Python script:


python recommend.py
Enter a description of the movie you’re in the mood for when prompted. For example:


What kind of movie are you in the mood for? Describe your preferences: I love thrilling action movies set in space.
View the recommendations:
The script will output the top 5 recommended movies based on your input. For example:


Top Recommendations:
                title  similarity_score
2       Interstellar          0.876543
0          Toy Story          0.654321
1     The Dark Knight         0.543210

Troubleshooting
File Not Found Error:
Ensure the movies.csv file is in the data/ folder and the path in the code is correct.

Module Not Found Error:
Ensure all dependencies are installed by running pip install -r requirements.txt.

Empty Recommendations:
Try a different query or check if the dataset contains relevant movies.



Sample Queries
Here are some sample queries you can use to test the movie recommendation system:

Action Movies:
"I love action-packed movies with lots of explosions and fight scenes."
Sci-Fi Movies:
"I’m in the mood for a sci-fi movie set in space with advanced technology."
Comedy Movies:
"I want to watch a funny movie that will make me laugh out loud."
Romantic Movies:
"I’m looking for a romantic movie with a heartfelt love story.
Thriller Movies:
I enjoy thrilling movies with suspense and unexpected twists."
Adventure Movies:
"I want to watch an adventure movie with exciting journeys and exploration."
Drama Movies:
"I’m in the mood for a dramatic movie with deep emotional themes."
Family-Friendly Movies:
"I need a family-friendly movie that’s suitable for kids."
Horror Movies:
"I want to watch a scary horror movie that will give me chills."

Sample Output:
Input:"I love action-packed movies with lots of explosions and fight scenes"

```title  similarity_score
112          The Dark Knight          0.511962
121             The Avengers          0.366994
123                Gladiator          0.220587
3               Men in Black          0.169483
0    Guardians of the Galaxy          0.167968```


