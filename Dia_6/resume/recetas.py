from pathlib import Path
import subprocess

def make_dir(path: Path):
    Path.mkdir(path, exist_ok=True)
    print(f"Directorio '{path}' creado exitosamente.")

def make_file(path: Path, nombre_archivo: str, contenido: str = ""):
    file_path = path / nombre_archivo
    file_path.write_text(contenido, encoding="utf-8")
    print(f"Archivo '{file_path}' creado exitosamente.")

def manage_new_recipes_dirs(dir_recipes: Path):
    recipes_dirs = {
        "Carnes": dir_recipes / "Carnes",
        "Ensaladas": dir_recipes / "Ensaladas",
        "Pastas": dir_recipes / "Pastas",
        "Postres": dir_recipes / "Postres"
    }

    recipes_files = {
        "Carnes": ["Pollo al horno.txt", "Carne asada.txt"],
        "Ensaladas": ["Ensalada César.txt", "Ensalada de frutas.txt"],
        "Pastas": ["Espaguetis a la boloñesa.txt", "Lasaña.txt"],
        "Postres": ["Tarta de manzana.txt", "Brownies.txt"]
    }
    make_dir(dir_recipes)
    for recipe_dir in recipes_dirs.values():
        make_dir(recipe_dir)
    
    for category, files in recipes_files.items():
        for file in files:
            content = f"Receta de {file.replace('.txt', '')} en la categoría {category}."
            make_file(recipes_dirs[category], file, content)

    return True

def count_directories(dir_recipes: Path):
    total_directories = 0
    for dir_recipe in dir_recipes.glob("**/"):
        if dir_recipe == dir_recipes:
            continue
        total_directories += 1
    return total_directories

def count_recipes(dir_recipes: Path):
    total_recipes = 0
    for txt in dir_recipes.glob("**/*.txt"):
        total_recipes += 1
    return total_recipes

def get_categories(dir_recipes: Path):
    categories = {}
    index = 1
    for category in dir_recipes.iterdir():
        if category.is_dir():
            categories[index] = category
            print(f"{index}. {category.name}")  # Imprime el número y el nombre de cada categoría encontrada
            index += 1
    return categories

def get_recipes_by_category(dir_recipes: Path, category_name: str):
    category_path = dir_recipes / category_name
    if not category_path.exists() or not category_path.is_dir():
        print(f"La categoría '{category_name}' no existe.")
        return []
    
    recipes = []
    for recipe in category_path.glob("*.txt"):
        recipes.append(recipe)
    return recipes

def clear_console():
    current_os = subprocess.run("uname", capture_output=True, text=True).stdout.strip()
    if current_os == "Linux" or current_os == "Darwin":
        subprocess.run(["clear"])
    else:
        subprocess.run(["cls"], shell=True)

def get_recipe_content(recipe_path: Path):
    if not recipe_path.exists() or not recipe_path.is_file():
        print(f"La receta '{recipe_path}' no existe.")
        return None
    return recipe_path.read_text(encoding="utf-8")

def read_recipe_by_category(dir_recipes: Path, total_directories: int, categories: dict):
    option_category = validate_option(input("Seleccione una categoría para ver las recetas (ingrese el número correspondiente): "), 1, total_directories)
    selected_category = categories[option_category]
    print(f"Recetas en la categoría '{selected_category.name}':")
    recipes = get_recipes_by_category(dir_recipes, selected_category.name)
    for i, recipe in enumerate(recipes, start=1):
        print(f"  {i}. {recipe.name}")
    option_recipe = validate_option(input("Seleccione una receta para leer su contenido (ingrese el número correspondiente): "), 1, len(recipes))
    selected_recipe = recipes[option_recipe - 1]
    content = get_recipe_content(selected_recipe)
    print(f"Contenido de la receta '{selected_recipe.name}':\n{content}")

def create_new_recipe(dir_recipes: Path, total_directories: int, categories: dict):
    option_category = validate_option(input("Seleccione una categoría para crear la nueva receta (ingrese el número correspondiente): "), 1, total_directories)
    selected_category = categories[option_category]
    recipe_name = input("Ingrese el nombre de la nueva receta (sin extensión .txt): ")
    recipe_content = input("Ingrese el contenido de la nueva receta: ")
    new_recipe_path = dir_recipes / selected_category / f"{recipe_name}.txt"
    if new_recipe_path.exists():
        print(f"Ya existe una receta con el nombre '{recipe_name}' en la categoría '{selected_category.name}'.")
        return
    make_file(selected_category, f"{recipe_name}.txt", recipe_content)

def delete_recipe(dir_recipes: Path, total_directories: int, categories: dict):
    option_category = validate_option(input("Seleccione una categoría para eliminar una receta (ingrese el número correspondiente): "), 1, total_directories)
    selected_category = categories[option_category]
    recipes = get_recipes_by_category(dir_recipes, selected_category.name)
    if not recipes:
        print(f"No hay recetas disponibles en la categoría '{selected_category.name}' para eliminar.")
        return
    for i, recipe in enumerate(recipes, start=1):
        print(f"  {i}. {recipe.name}")
    option_recipe = validate_option(input("Seleccione una receta para eliminar (ingrese el número correspondiente): "), 1, len(recipes))
    selected_recipe = recipes[option_recipe - 1]
    selected_recipe.unlink()  # Elimina el archivo de la receta
    print(f"Receta '{selected_recipe.name}' eliminada exitosamente.")

def validate_option(option: str, min_value: int, max_value: int):
    while not option.isdigit() or int(option) < min_value or int(option) > max_value:
        option = input(f"Opción inválida. Por favor, seleccione una opción válida (ingrese un número entre {min_value} y {max_value}): ")
    return int(option)

def show_menu():
    print(""" 
            Estas son las opciones disponibles:
            1. Leer receta por categoría
            2. Crear nueva receta
            3. Crear categoría
            4. Eliminar receta
            5. Eliminar categoría
            6. Salir
        """)

def main():
    cwd = Path(__file__).parent
    dir_recipes = Path(cwd, "Recipes")

    dirs_ok = manage_new_recipes_dirs(dir_recipes)
    clear_console()
    if not dirs_ok:
        print("Hubo un error al crear los directorios y archivos de recetas.")
        return
    print("Árbol de directorios y archivos creado exitosamente.")
    total_directories = count_directories(dir_recipes)
    total_recipes = count_recipes(dir_recipes)

    print(f"""
            Bienvenido al programa de gestión de recetas.
            El directorio de recetas es: {dir_recipes}
            Hay {total_directories} directorios.
            Hay un total de {total_recipes} recetas.
        """)

    show_menu()
    option_action = validate_option(input("Seleccione una opción (ingrese el número correspondiente): "), 1, 6)
    while option_action != 6:
        if option_action == 1:
            continue_reading = "s"
            while continue_reading.lower() == "s":
                categories = get_categories(dir_recipes)
                read_recipe_by_category(dir_recipes, total_directories, categories)
                continue_reading = input("¿Desea leer otra receta? (s/n): ")

        if option_action == 2:
            continue_creating = "s"
            while continue_creating.lower() == "s":
                categories = get_categories(dir_recipes)
                create_new_recipe(dir_recipes, total_directories, categories)
                continue_creating = input("¿Desea crear otra receta? (s/n): ")

        if option_action == 3:
            continue_creating_category = "s"
            while continue_creating_category.lower() == "s":
                new_category_name = input("Ingrese el nombre de la nueva categoría: ")
                new_category_path = dir_recipes / new_category_name
                if new_category_path.exists():
                    print(f"Ya existe una categoría con el nombre '{new_category_name}'.")
                    continue_creating_category = input("¿Desea intentar con otro nombre de categoría? (s/n): ")
                else:
                    make_dir(new_category_path)
                    print(f"Categoría '{new_category_name}' creada exitosamente.")
                    continue_creating_category = input("¿Desea crear otra categoría? (s/n): ")

        if option_action == 4:
            continue_deleting = "s"
            while continue_deleting.lower() == "s":
                categories = get_categories(dir_recipes)
                delete_recipe(dir_recipes, total_directories, categories)
                continue_deleting = input("¿Desea eliminar otra receta? (s/n): ")

        if option_action == 5:
            continue_deleting_category = "s"
            while continue_deleting_category.lower() == "s":
                categories = get_categories(dir_recipes)
                option_category = validate_option(input("Seleccione una categoría para eliminar (ingrese el número correspondiente): "), 1, total_directories)
                selected_category = categories[option_category]
                if any(selected_category.glob("*.txt")):
                    print(f"No se puede eliminar la categoría '{selected_category.name}' porque contiene recetas. Elimine las recetas primero.")
                    continue_deleting_category = input("¿Desea intentar eliminar otra categoría? (s/n): ")
                else:
                    selected_category.rmdir()  # Elimina el directorio de la categoría
                    print(f"Categoría '{selected_category.name}' eliminada exitosamente.")
                    continue_deleting_category = input("¿Desea eliminar otra categoría? (s/n): ")

        input("Presione Enter para continuar al menú principal...")
        clear_console()
        show_menu()

        option_action = validate_option(input("Seleccione una opción (ingrese el número correspondiente): "), 1, 6)
    print("Gracias por usar el programa de gestión de recetas. ¡Hasta luego!")

if __name__ == "__main__":
    main()