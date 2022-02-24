# Assignment  2 (18103074)
Create Use-case and Sequence diagrams using PLantUML tool.

## 1. Sequence Diagram
### Diagram
![Sequence Diagram](https://github.com/akshitm169/Software-Testing/blob/main/Assignment%201/Sequence.png?raw=true)

### Code
```
@startuml
actor User as user
participant "BookGenics" as BookGenics
participant "Database" as Database

user->BookGenics: Register
BookGenics->Database: User Registered
user->BookGenics: Login
BookGenics->Database: Details Checked

alt if user is registered
    BookGenics<-- Database: Valid User
    user<-BookGenics: Login Successful
else else
    BookGenics<-- Database: Invalid User
    user<-BookGenics: Login Rejected
end

user->BookGenics: Sort Books
user<--BookGenics: Books Shown

user->BookGenics: Filter Books
BookGenics->Database: Filtering Books
BookGenics<--Database: Filtered Books
user<--BookGenics: Books Shown

user->BookGenics: Read Content
BookGenics->Database: Get Content
BookGenics<--Database: Content
user<--BookGenics: Show Content


user->BookGenics: Update/Detete Book
BookGenics->Database: Book Updated/Deleted

user->BookGenics: Favourite/Unfavourite Book
BookGenics->Database: Book Favourited/Unfavourited

user->BookGenics: Input Book for prediction
user<--BookGenics: Predicted Genres 

user->BookGenics: Add Book
BookGenics->Database: Book Searching 

alt if book is not found in database 
    BookGenics<-- Database: Book not found
    BookGenics-> Database: Adding Book
    BookGenics<- Database: Book added
    user<-BookGenics: Request Successful 
else else
    BookGenics<-- Database: Book found
    user<-BookGenics: Request Rejected 
end

user->BookGenics: Change userdata
BookGenics->Database: Userdata changed


user->BookGenics: Logout
user<-BookGenics: Logout Successful
@enduml
```

## 2. UseCase Diagram
### Diagram
![UseCase Diagram](https://raw.githubusercontent.com/akshitm169/Software-Testing/main/Assignment%201/UseCase.png)

### Code
```
@startuml
left to right direction

actor User
actor "Normal User" as NU
actor Admin
Actor Db

User <|-- NU
User <|-- Admin

rectangle Bookgenics {
    User --down-> (Login)
    (Login) <. (Verify Password): includes
    (Login) .down. (Display Error): extends

    User --right-> (Register)
    (Register) <. (Display Error): extends
    
    User --right-> (Change User Data)
    
    

    Db --left-> (Add Books)
    Db --left-> (Register)
    Db --left-> (Change User Data)
    Db --left-> (Display Books)

    (Display Books) <|-- (Show All Books)
    (Display Books) <|-- (Show Favorites)
    (Display Books) <|-- (Show Added Books)
    
    User --down-> (Predict Genre)
    (Predict Genre) <. (Add Books): extends

    (Display Books) .down. (Filter/Sort Book): extends
    (Display Books) .down. (Read Content): extends
    (Display Books) .down. (Edit Book): extends
    (Display Books) .down. (Favorite/Unfavorite Book): extends
    
    (Edit Book) .down. (Delete Book): extends
    (Edit Book) .down. (Update Book): extends

    (Update Book) <|-- (Change Author)
    (Update Book) <|-- (Change Title)
}

@enduml
```
