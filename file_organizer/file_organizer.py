from  pathlib import Path 
import shutil

#path of your downlaod folder
folder_path = Path(r"")

def move_safely(item, Destination ):
    target = Destination/item.name
    counter = 1 
    while target.exists():
        new_name = f"{item.stem}_{counter}{item.suffix}"
        target = Destination/new_name
        counter = counter +1
    try: 
        shutil.move(str(item), str(target))
        print(f"{item.name} moved ")
    except OSError as error:
        print(f"Skipped:{item.name} - {error}")


#loop for the items in the folder 
for item in folder_path.iterdir():
    if not item.is_file():
        continue
# for images 
    if item.suffix.lower() in  (".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg") :
        Destination = folder_path/"Images"
        Destination.mkdir(exist_ok=True)
        move_safely(item,Destination)
#for docs
    elif item.suffix.lower() in (".pdf", ".docx", ".doc",".txt", ".pptx", ".xlsx", ".csv"):
        Destination = folder_path/"Documents"
        Destination.mkdir(exist_ok=True)
        move_safely(item,Destination)
    
#vids
    elif item.suffix.lower() in (".mp4", ".mkv", ".avi", ".mov", ".webm"):
        Destination = folder_path/"Videos"
        Destination.mkdir(exist_ok=True)
        move_safely(item,Destination)
#archives
    elif item.suffix.lower() in (".zip" , ".rar", ".7z", ".tar", ".gz"):
        Destination = folder_path/"Archives"
        Destination.mkdir(exist_ok=True)
        move_safely(item,Destination)
#scripts
    elif item.suffix.lower() in (".py", ".js", ".ps1", ".sh", ".bat"):
        Destination = folder_path/"Scripts"
        Destination.mkdir(exist_ok=True)
        move_safely(item,Destination)


#remaining files
    else:
        Destination = folder_path/"Others"
        Destination.mkdir(exist_ok=True)
        move_safely(item,Destination)
    
    
    
        

        
        


   
            
            



            
   
       
       
    









