# Define the recipe structured class
class Recipe:
    def __init__(self, title, ingredients):
        self.title = title  # A string for the recipe title
        self.ingredients = ingredients  # A list of ingredient strings

    def __str__(self):
        return f"Recipe: {self.title}\nIngredients:\n" + "\n".join(f"- {item}" for item in self.ingredients)


#### RECIPE DEFINITIONS ####

beef_and_onion = Recipe(
    "Beef and Onion Stir Fry",
    [
        "sliced beef",
        "onion",
        "ginger",
        "green onion",
        "soy sauce",
        "cooking wine",
        "sesame oil",
        "corn starch",
        "oyster sauce",
        "hoisin sauce"
    ]
)

hamburger_steak = Recipe(
    "Hamburger Steak with Mushroom Gravy",
    [
        "ground beef (1 lb)",
        "onion (1.5 cups)",
        "sliced mushrooms (1 cup)",
        "beef stock (1.5 cups)",
        "red wine vinegar",
        "mashed potato"
    ]
)

chicken_udon = Recipe(
    "Teriyaki Chicken Udon Stir Fry",
    [
        "chicken",
        "udon noodle",
        "cabbage (2 cups)",
        "carrot (1 cup)",
        "onion",
        "soy sauce",
        "honey",
        "sesame oil",
        "ginger",
        "corn starch"
    ]
)

taiwan_chicken_rice = Recipe(
    "Taiwanese Chicken and Rice",
    [
        "chicken",
        "chicken stock (2.5 cups)",
        "ginger",
        "green onions",
        "five spice powder",
        "shallots (3)",
        "soy sauce"
    ]
)

chicken_parm_soup = Recipe(
    "Chicken Parm Soup",
    [
        "onion",
        "diced tomatoes (2 cans)",
        "chicken broth (4 cups)",
        "ditalini or penne pasta (2 cups)",
        "shredded chicken",
        "mozzarella cheese (3 oz)"
    ]
)

fryer_chicken_parm = Recipe(
    "Air Fryer Chicken Parmesan",
    [
        "chicken",
        "eggs (2)",
        "panko breadcrumbs (0.5 cup)",
        "parmesan cheese (0.5 cup)",
        "marinara sauce (1 cup)",
        "fresh mozzarella",
        "basil"
    ]
)

greek_salad = Recipe(
    "Greek Pasta Salad",
    [
        "salami or chicken",
        "bow tie pasta (2 lbs)",
        "red wine vinegar",
        "lemon juice",
        "grape tomates (1 pt)",
        "red onion (0.5 cup)",
        "cucumber (1.5 cups)",
        "olives (1 cup)",
        "feta cheese (0.5 cup)"
    ]
)

caprese_chicken = Recipe(
    "Caprese Chicken",
    [
        "cherry tomatoes (2 cups)",
        "pesto",
        "balsamic reduction",
        "chicken (1.5 lbs)",
        "fresh mozzarella",
        "ciabatta bread",
        "basil"
    ]
)

stroganoff_soup = Recipe(
    "Beef Stroganoff Soup",
    [
        "carrots (1 cup)",
        "onion",
        "ground beef (1 lb)",
        "cremini mushrooms (0.5 lb)",
        "mustard",
        "worcestershire sauce",
        "tomato paste",
        "beef broth (4 cups)",
        "dried egg noodles (1.5 cups)",
        "sour cream (0.5 cup)",
        "frozen peas (1 cup)"
    ]
)

pesto_sausage_pasta = Recipe(
    "Pesto Pasta with Sausage",
    [
        "pesto",
        "smoked sausage",
        "rotini pasta",
        "parmesan cheese"
    ]
)

dankaroni = Recipe(
    "Dankaroni and Cheese",
    [
        "smoked sausage",
        "thick/creamy mac & cheese (2 boxes)",
        "shredded cheese"
    ]
)


# Compile the list of all recipes
recipe_book = [beef_and_onion, 
               stroganoff_soup,
               pesto_sausage_pasta,
               hamburger_steak,
               taiwan_chicken_rice,
               chicken_udon,
               chicken_parm_soup,
               caprese_chicken,
               fryer_chicken_parm,
               greek_salad,
               dankaroni
            
               ]

# Compile the list of quick recipes
quick_recipes = [pesto_sausage_pasta,
                 greek_salad,
                 dankaroni,
                 stroganoff_soup

                 ]