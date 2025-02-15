# Django Product Catalog and Web Scraper

This project is a Django-based web application that scrapes product information from Mercado Livre and displays it in a catalog format.

The application fetches product data for gaming computers, processes the information, and presents it in a user-friendly interface. It allows filtering of products based on free shipping and delivery type, and highlights products with the lowest price, highest price, and highest discount.

## Repository Structure

```
.
├── catalogo_ofertas/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── ofertas/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── migrations/
    │   ├── __init__.py
    │   └── 0001_initial.py
    ├── models.py
    ├── scraper.py
    ├── templates/
    │   └── ofertas/
    │       └── lista.html
    ├── tests.py
    ├── urls.py
    └── views.py
```

### Key Files:
- `manage.py`: Django's command-line utility for administrative tasks
- `catalogo_ofertas/settings.py`: Main settings file for the Django project
- `ofertas/models.py`: Defines the data model for products
- `ofertas/scraper.py`: Contains the web scraping logic
- `ofertas/views.py`: Handles the application's logic and rendering
- `ofertas/urls.py`: Defines URL patterns for the ofertas app

## Usage Instructions

### Installation

Prerequisites:
- Python 3.8+
- pip (Python package manager)

Steps:
1. Clone the repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```
   python manage.py migrate
   ```

### Running the Application

1. Start the Django development server:
   ```
   python manage.py runserver
   ```

2. Open a web browser and navigate to `http://127.0.0.1:8000/ofertas/` to view the product catalog.

### Configuration

The main configuration file is `catalogo_ofertas/settings.py`. Key settings include:
- `DEBUG`: Set to `True` for development, `False` for production
- `ALLOWED_HOSTS`: Add your domain or IP address when deploying
- `DATABASES`: Configure your database settings here

### Web Scraping

The `scraper.py` file contains the logic for scraping product data from Mercado Livre. It uses Selenium WebDriver to interact with the website. Ensure you have the appropriate WebDriver installed and configured for your system.

### Customization

To modify the search query or scraping behavior:
1. Open `ofertas/scraper.py`
2. Locate the `scrape_mercado_livre()` function
3. Modify the search query in the `search_box.send_keys()` line

### Troubleshooting

Common issues and solutions:

1. WebDriver issues:
   - Problem: `WebDriverException: Message: 'chromedriver' executable needs to be in PATH`
   - Solution: Ensure ChromeDriver is installed and its path is added to your system's PATH variable

2. Database errors:
   - Problem: `OperationalError: no such table: ofertas_produto`
   - Solution: Run `python manage.py migrate` to apply all migrations

3. Scraping failures:
   - Problem: No products are being scraped
   - Solution: Check your internet connection and verify that the Mercado Livre website structure hasn't changed

For debugging:
- Set `DEBUG = True` in `settings.py`
- Check the console output for error messages
- Review the Django debug page for detailed error information

## Data Flow

The application follows this data flow:

1. User requests the product catalog page
2. Django view (`listar_produtos` in `views.py`) is triggered
3. The view calls the scraper function (`scrape_mercado_livre` in `scraper.py`)
4. Scraper fetches product data from Mercado Livre
5. View processes and filters the scraped data
6. Processed data is saved to the database (`Produto` model)
7. View renders the data using the template (`lista.html`)
8. Rendered page is sent back to the user's browser

```
[User] -> [Django View] -> [Web Scraper] -> [Mercado Livre]
           ^                                       |
           |                                       v
[Database] <- [Data Processing] <- [Scraped Data]
           |
           v
[Template] -> [Rendered Page] -> [User]
```

Note: The scraper uses Selenium WebDriver to interact with the Mercado Livre website, which may require additional setup and maintenance to handle changes in the website's structure.