from newspaper import Article
import validators
import re  
import whois




print("""
  _____                        _         _   _                        __  __ _                 
 |  __ \                      (_)       | \ | |                      |  \/  (_)                
 | |  | | ___  _ __ ___   __ _ _ _ __   |  \| | __ _ _ __ ___   ___  | \  / |_ _ __   ___ _ __ 
 | |  | |/ _ \| '_ ` _ \ / _` | | '_ \  | . ` |/ _` | '_ ` _ \ / _ \ | |\/| | | '_ \ / _ | '__|
 | |__| | (_) | | | | | | (_| | | | | | | |\  | (_| | | | | | |  __/ | |  | | | | | |  __| |   
 |_____/ \___/|_| |_| |_|\__,_|_|_| |_| |_| \_|\__,_|_| |_| |_|\___| |_|  |_|_|_| |_|\___|_|   

     Find Available Domain names from articles , content source from urls.                                                                                           
                                                                                               
""")

url = str(input("Enter url of the Article / content source : "))
validation = validators.url(url)

if validation:


   #check domain availibility

   def is_registered(domain_name):
    
       try:
          whois_check = whois.whois(domain_name)
       except Exception:
          return False
       else:
          return bool(whois_check.domain_name)

        
    
   #extract article content from url
        
   def extraction(article_url):
       article = Article(article_url)
       article.download()
       article.parse()
       return article.title,article.text


   title,text = extraction(url)

   print("\n Article Title : ",title,"\n")
   

   # removing special characters from the article text
   
   text =  re.sub(r'[^a-zA-Z0-9\s]+', '', text) 
   extracted_words = text.split()
   

   #domain extensions
   
   extensions = [".com",".in",".co"]
  
   #generating domain names from keywords and extensions
 
   for domain_extension in extensions:

      domain_list = open("available_domains.txt", "a+")    

      for words in extracted_words:
          domain_list = open("available_domains.txt", "a+")
          words = words + domain_extension
          domain = words.replace(" ", "")
          domain_name = domain
          if is_registered(domain_name):
             print(domain_name,"is not available")
          else:
             print(domain_name,"is available ^_^ ")
             domain_list.write("\n")
             domain_list.write(domain_name)
            

      domain_list.close()        

           

                 

   print("Happy Mining ^_^ ")   

else:
    
    print("URL is invalid")

