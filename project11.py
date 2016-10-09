sentence = raw_input('Enter your input:') #Ζητούμε από τον χρήστη να εισάγει το κείμενο   
#του αποτελούμενο απο NSFW ανάλογα με την κατεύθυνση που θέλει να δώσει

t = input('Insert the time you want to be completed: ')  # Ζητάμε από τον χρήστη να μας δώσει τον     #χρόνο στον οποίο θέλει να ολοκληρωθούν οι κινήσεις

def  ChessBoard(t,sentence): 
   d = sentence.count('N,S,F,W') # με τη βοήθεια της συνάρτησης count μετράμε των αριθμό                      #των N S F W που υπάρχουν στο δοσμένο κείμενο.
 if : 
          d == t    # γίνεται σύγκριση και εάν οι κινήσεις μπορούν να ολοκληρωθούν στο δοσμένο 
  result  = True    #χρόνο η συνάρτηση επιστρέφει True διαφορετικά επιστρέφει false      
    else:
        result = False

    return result

print(ChessBoard(t,sentence)) # εμφανίζουμε το αποτέλεσμα στο χρήστη  