package dw;

import java.net.*;
import java.util.*;
import com.sun.net.httpserver.*;
import java.io.*;

//Class is a data structure for the relevant info for the player
class userData {
   public String word = "apple";
   public int misses;
   public int state;
   public String guesses = "";
   
   public userData()
   {
      //word = MyHttpServer.randomWord();
      misses = 0;
      state = 1;
   }
}

public class MyHttpServer {

	static final String RESOURCE_DIR = "src/main/resources/";
	static final int PORT = 8080;
   
	//Hashtable contains the users data keyed to cookies
   static Hashtable<String, userData> hangmanUsers = new Hashtable<String, userData>();
   
	public static void main(String[] args) {

		try {
			HttpServer server = HttpServer.create(new InetSocketAddress(PORT), 0);
			System.out.print("Server started. ");
			// Display current directory
			System.out.print("pwd=" + System.getProperty("user.dir"));
			server.createContext("/", new MyHandler());
			server.setExecutor(null); // creates a default executor
			server.start();
			System.out.println();
			System.out.println("MyHttp Server running.");
		} catch (Exception e) {
			System.out.println("My HttpServer Exception: " + e.getMessage());
		}
	}

	static class MyHandler implements HttpHandler {

		public void handle(HttpExchange t) throws IOException {

			String uri = t.getRequestURI().toString();
			System.out.println("URI=" + uri);
			if (uri.endsWith(".gif") || uri.endsWith(".ico")) {
				// http get request for an image file
				sendFile(t, uri.substring(1));
			} else {
				// come here to play the game
				playGame(t);
			}
		}
	}

	/**
	 * random word list used in game
	 */
	static ArrayList<String> wordlist = null;

	/**
	 * generate random word.
	 * 
	 * @return a word from the list
	 */
	public static String randomWord() {
		try {
			if (wordlist == null) {
				wordlist = new ArrayList<String>();
				// read in word list
				Scanner infile = new Scanner(new File(RESOURCE_DIR + "wordlist.txt"));
				while (infile.hasNextLine()) {
					wordlist.add(infile.nextLine());
				}
				infile.close();
			}
			int t = generator.nextInt(wordlist.size());
			return wordlist.get(t);

		} catch (Exception e) {
			System.out.println("Error randomWord: reading wordlist. " + e.getMessage());
			System.exit(0);
			return null; // to keep compiler happy
		}
	}

	static Random generator = new Random();

	/*
	 * generate a random cookie which is a random long integer
	 */
	public static String generateCookie() {
		return Long.toString(generator.nextLong());
	}

	/*
	 * send a gif file
	 */
   public static void sendFile(HttpExchange t, String filename) {

      try {
         InputStream is = MyHttpServer.class.getClassLoader().getResourceAsStream(filename);
         byte[] fileData = new byte[20000];
         int dataLength = is.read(fileData);
         is.close();
         
         System.out.println(dataLength);
         t.getResponseHeaders().set("Content-Type", "image/gif");
         t.sendResponseHeaders(200, dataLength);
         OutputStream os = t.getResponseBody();
         os.write(fileData, 0, dataLength);
         os.close();

      } catch (Exception e) {
        System.out.println("Error in sendFile:" + filename + " " + e.getMessage());
      }

   }

	/*
	 * process a user guess return page saying game over user win or lost, or
	 * return page with updated game display
	 */
	
	
	public static void playGame(HttpExchange t) {

		try {
			boolean lost =false;
			boolean win = false;
			String newcookie;
			String response;
			String uri = t.getRequestURI().toString();
			String cookie = t.getRequestHeaders().getFirst("Cookie");
			
			//checks for null cookie value (an issue for chrome compatibility)
			if (cookie == null)
			   cookie = generateCookie();
			
			//Generates new hashed user if necessary
			if (!hangmanUsers.containsKey(cookie))
			{
			   cookie = generateCookie();
			   hangmanUsers.put(cookie, new userData());
			}
			
			
			System.out.println("Cookie=" + cookie);

			//pulls current guess
         char guess = uri.charAt(uri.length() - 1);

         //regulates whether to add the key to guesses or not
         boolean isIn = false;
         for (int i = 0; i < hangmanUsers.get(cookie).guesses.length(); i++)
         {
            if (hangmanUsers.get(cookie).guesses.charAt(i) == guess)
            {
               isIn = true;
            }
         }
         if (isIn == false)
         {
            hangmanUsers.get(cookie).guesses += guess;
         }
         
         //checks if the key is a miss
         boolean roundMiss = true;
         for (int i = 0; i < hangmanUsers.get(cookie).word.length(); i++)
         {
            if (hangmanUsers.get(cookie).word.charAt(i) == guess)
            {
               roundMiss = false;
            }
         }
         
         //if its a muiss, updates the userData appropriately
         if (roundMiss == true)
         {
            if (hangmanUsers.get(cookie).state < 7 && guess != '/')
            {
               hangmanUsers.get(cookie).misses += 1;
               hangmanUsers.get(cookie).state += 1;
            }
         }
			
         //checks for a lose condition
         if (hangmanUsers.get(cookie).state == 7)
            lost = true;
			// you must change the following code to play a game

			if (true) {
				newcookie = cookie;
				String currGuess = "";
				win = true;
				
				//build current state of word
				for (int i = 0; i < hangmanUsers.get(cookie).word.length(); i++)
				{
				   boolean tmpIn = false;
				   for (int j = 0; j < hangmanUsers.get(cookie).guesses.length(); j++)
				   {
				      if (hangmanUsers.get(cookie).guesses.charAt(j) == hangmanUsers.get(cookie).word.charAt(i))
				      {
				         tmpIn = true;
				         currGuess += hangmanUsers.get(cookie).guesses.charAt(j);
				      }
				      
				   }
				   
				   if (tmpIn == false)
				   {
				      currGuess += "_";
				      win = false;
				   }
				}
						
				response = "<!DOCTYPE html><html><head><title>MyHttpServer</title></head><body><h2>Hangman</h2>"
						+ "<img src=\"" + "h" + hangmanUsers.get(cookie).state + ".gif" + "\">"
						+ "<h2 style=\"font-family:'Lucida Console', monospace\"> " + currGuess + "</h2>"
						+ "<form action=\"/\" method=\"get\"> "
						+ "Guess a character <input type=\"text\" name=\"guess\"><br>"
						+ "<input type=\"submit\" value=\"Submit\">" + "</form></body></html>";
			}

			// if the player has lost 
		    if (lost){
				newcookie = "none";
				response = "<!DOCTYPE html><html><head><title>MyHttpServer</title></head><body><h2>Hangman</h2>"
						+ "<img src=\"" + "h7.gif" + "\">" + "<h2>You lost!  The word is " + hangmanUsers.get(cookie).word + "</h2>"
						+ "</body></html>";
		    }
		    if (win) {
			// if the player has correctly guessed all letters of the word
				newcookie = "none";
				response = "<!DOCTYPE html><html><head><title>MyHttpServer</title></head><body><h2>Hangman</h2>"
						+ "<img src=\"" + "h" + hangmanUsers.get(cookie).state + ".gif" + "\">"
						+ "<h2 style=\"font-family:'Lucida Console', monospace\"> " + "</h2>"
						+ "<h2>Congratulations you win!</h2>" + "</body></html>";
			}

			// send response
			t.getResponseHeaders().set("Content-Type", "text/html");
			t.getResponseHeaders().set("Set-Cookie", newcookie);
			System.out.println("New cookie:" + newcookie);

			t.sendResponseHeaders(200, response.length());
			System.out.println("response=" + response);
			OutputStream os = t.getResponseBody();
			os.write(response.getBytes());
			os.close();

		} catch (Exception e) {
			System.out.println("Error playGame." + e.getMessage());
			e.printStackTrace();
		}
	}

}