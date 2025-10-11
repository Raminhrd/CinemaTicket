🎟️ Cinema Ticket — Django REST API for Movie Booking

A complete cinema management and ticket booking API built with Django REST Framework.
Supports movies, cinemas, screenings, ticketing, comments, and reviews.

🚀 Features
🏢 Cinema & Screening Management

Create and manage cinemas with:

name, address, capacity, and optional image

Each cinema can host multiple screenings (Sans)

Screenings include: movie, cinema, play_at (date & time)

🎬 Movies

Each movie includes:

name, price, time, score, votes

director, actors, genres, description

Supports many-to-many relationships:

A movie can have multiple actors and genres

🎭 Actors & Genres

Add actors with name and image

Create genres and assign them to movies

Use filters and search to find actors or genres easily

🎟️ Tickets

Authenticated users can view and book tickets

Each ticket is linked to a Sans (screening) and a User

Prevents duplicate or invalid bookings

💬 Comments & Criticism

Users can comment on movies they’ve seen

Admins can post critic reviews with estimated read time

🧠 API Logic

1️⃣ Admins create movies, actors, and cinemas
2️⃣ Admins set up screenings (Sans)
3️⃣ Users:

View available screenings

Book tickets for a specific movie session

Leave comments on movies they watched
4️⃣ Admins:

View all data

Post professional reviews and manage content

🧰 API Endpoints
Method	Endpoint	Description	Permission
GET	/cinema/	List cinemas	Authenticated
POST	/cinema/	Add a cinema	Admin
GET	/movies/	List all movies	Authenticated
POST	/movies/	Add a movie	Admin
GET	/sans/	List screenings	Authenticated
POST	/sans/	Add screening	Admin
GET	/tickets/	List all tickets	Authenticated
POST	/tickets/	Book ticket	Authenticated
GET	/comments/	List comments	Authenticated
POST	/comments/	Add comment	Authenticated
🔍 Filtering & Searching

Supported fields:

🎥 Movie → search_fields=['name'], ordering=['price', 'score', 'votes']

🎭 Actor → search_fields=['name']

🏢 Cinema → search_fields=['name'], ordering=['capacity']

🧾 Example API Request

Book a ticket

{
  "user": 3,
  "sans": 5
}

Add a comment

{
  "user": 3,
  "movie": 2,
  "text": "Amazing performance and visuals!",
  "date": "2025-10-11"
}

🧰 Tech Stack
Tool	Purpose
🐍 Python	Backend language
🦄 Django	Web framework
⚙️ Django REST Framework	API management
🗃️ SQLite	Database
🔍 Django Filters	Advanced search and filtering
