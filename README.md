# Django Project

- Project idea:
  - Build upon online recipe cookbook from Project 3 that allows an online community share thier favorite recipes with each other.

- Models:
  - Chapter (collection of similar recipes based on the main protein (beef, pork, etc) or general use (desserts, appetizers, etc)
    - heading
    - thumbnail (an optional image that represents the chapter)
    - description
  - Recipe
    - name
    - image (an optional image the creator can upload)
    - chapter (FK)
    - ingredients (list of ingredients - 2.0 this would be another model that would be a list that could be iterated through, added, modified, etc.)
    - directions
