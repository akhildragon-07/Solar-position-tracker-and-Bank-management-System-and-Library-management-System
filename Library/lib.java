import java.util.ArrayList;
import java.util.Scanner;

class Book {
    String title, author;
    int year;

    Book(String title, String author, int year) {
        this.title = title;
        this.author = author;
        this.year = year;
    }

    public String toString() {
        return title + " by " + author + " (" + year + ")";
    }
}

public class Library {
    private ArrayList<Book> books = new ArrayList<>();

    public void addBook(Book b) {
        books.add(b);
    }

    public void displayBooks() {
        if (books.isEmpty()) {
            System.out.println("No books in library.");
        } else {
            for (Book b : books) {
                System.out.println(b);
            }
        }
    }

    public void searchBook(String title) {
        for (Book b : books) {
            if (b.title.equalsIgnoreCase(title)) {
                System.out.println("Found: " + b);
                return;
            }
        }
        System.out.println("Book not found.");
    }

    public static void main(String[] args) {
        Library lib = new Library();
        Scanner sc = new Scanner(System.in);

        lib.addBook(new Book("Java Basics", "James", 1995));
        lib.addBook(new Book("Python 101", "Guido", 2000));

        while (true) {
            System.out.println("\n1. Display Books\n2. Search Book\n3. Exit");
            int choice = sc.nextInt();
            sc.nextLine();

            if (choice == 1) {
                lib.displayBooks();
            } else if (choice == 2) {
                System.out.print("Enter book title: ");
                String title = sc.nextLine();
                lib.searchBook(title);
            } else break;
        }
        sc.close();
    }
}
