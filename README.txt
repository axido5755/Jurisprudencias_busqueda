Pasos de desarrollo
    -Pag Juridico
	- Estudiar WEB Scraping
	- Minar la pagina entendiendo la logica
	- Encontrar el list en network con el https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list
	- Leer documentacion de Request Python
	- Estudiar logica de POST sin una api
	- Funciono!!!! funcionamiento correcto del post

    -Django
	- Estudiar Django
	- Estudiar conexion PostgresSQL con Django
	- Estudiar conexion Boostrap5 con Django
	- Estudiar estructura
	- Conectar todo y que funcione todo 

    -Conexion
	//url CHR_1/templates/...
	- Creacion de base con nav
	- Creacion de un home con busqueda
	
	//url Jurisprudencia/models.py
	- Creacion de migracion
	//url Jurisprudencia/views.py
	- Creacion de contructor

	//url Jurisprudencia/urls.py
	- Conexion con contructor

	//url CHR_1/urls.py
	- Conexion con home
	- Conexion con contructor
	
	- Conexion con <from> y botones

EJECUCION 
	- python manage.py migrate       
	- python manage.py makemigrations
	- python manage.py runserver

ESTRUCTURA 
	- HOME home con un panel simple de busqueda
		- Al hacer clic o enter busca y guarda SIN REPETIDO los resultados obtenidos o entrega un null como plantilla
	- Lista_bdd Lo que esta en la base de datos guardado