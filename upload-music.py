import os, json, re, shutil
# from termcolor import colored
from sys import exit
from ctypes import windll

windll.kernel32.SetConsoleTitleW("Subidor de musica")

def stop():
    os.system("pause")
    exit()

class Main():
    
    default_config: list = {
        "carpeta IN": "",
        "carpeta OUT": "",
        "url": "",
        "usuario": "elpepe",
        "servidor1": "ubuntu@129.151.112.189:/var/www/html",
        "servidor2": "gmod@XXX.XXX.XXX.XXX:/home/gmod/servidor/garrysmod/data/streamradio/playlists",
        "servidor3": "darkrp@XX.XX.XXX.XXX:/home/darkrp/servidor/garrysmod/data/streamradio/playlists",
        "archivo1": "db.pem",
        "archivo2": "gmod.pem",
        "archivo3": ""
    }

    error_dict: dict = {
        100: ["Archivo creado con exito"],
        101: ["Archivo reestablecido con exito"],
        102: ["Ya se"],
        103: ["Todo okay"],

        200: ["Musica subida sin errores", "Como lo ves, todo se subio ok"],

        300: ["Carpeta IN no especificada/vacia", "No colocaste ninguna carpeta en \"carpeta IN\" en el archivo de configuracion"],
        301: ["Carpeta IN con caracteres invalidos", "No coloques ningun simbolo especial ni numeros, solo coloca \"musica_in\" o \"music_entrada\"", "Es opcional pero es preferible que el nombre este en minusculas"],
        302: ["Carpeta IN con espacios", "No uses espacios, esto puede joder al programa y no queremos eso cierto?"],
        304: ["Carpeta IN no existe en la carpeta actual", "Quizas creaste la carpeta o talvez no, pero la carpeta que especificaste en el archivo de configuracion, no existe"],

        305: ["Carpeta OUT no especificada/vacia", "No colocaste ninguna carpeta en \"carpeta IN\" en el archivo de configuracion"],
        306: ["Carpeta OUT con caracteres invalidos", "No coloques ningun simbolo especial ni numeros, solo coloca \"musica_out\" o \"music_salida\"", "Es opcional pero es preferible que el nombre este en minusculas"],
        307: ["Carpeta OUT con espacios", "No uses espacios, esto puede joder al programa y no queremos eso cierto?"],
        308: ["Carpeta OUT no existe en la carpeta actual", "Quizas creaste la carpeta o talvez no, pero la carpeta que especificaste en el archivo de configuracion, no existe"],

        309: ["Url sin especificar", "No especificaste ninguna url para subir", "Tienes que poner algo como esto \"http://129.151.112.189/music\""],
        310: ["Url no valida", "La url que colocaste no es valida", "Osea, cuando me refiero que no es valida, me refiero a que posiblemente:", "  Lo colocaste mal", "  hay un simbolo raro", "  o colocaste un espacio, y puta la wea, no pongas espacios po"],

        303: ["Usuario no valido", "Pero xd, no puedes usar un usuario vacio", "Ponele un nombre minimo o lo que sea"],
        311: ["Usuario no valido", "El usuario que colocaste en el archivo de configuracion no es correcto", "recuerda solo poner minusculas ni simbolos"],
        312: ["Usuario no valido (elpepe)", "Dejaste por defecto el usuario elpepe", "Lamentablemente solo yo lo puedo usar, escoge otro como por ejemplo:", "  \"esotilin\"", "  \"milky\""],
        313: ["Usuario no valido (Espacios)", "Colocaste tu nombre de usuario con espacios", "y no po, no podi hacer eso que es malo para el server y para todos"],

        314: ["Servidor1 no valido", "Porque borraste de la config el servidor1?", "No enserio, dime porque?"],
        315: ["Servidor1 no valido (No es correcto)", "Tal parece que hubo un problema al cargar el servidor1, tipo", "esta tal como estaba en el codigo original?"],
        316: ["Servidor1 no valido (Espacios)", "Pero weon XD", "Porque insistes en ponerle espacios a las configuraciones?"],

        317: ["Servidor2 no valido", "Creo que tienes que colocar el servidor 2", "No era necesario borrar todo eso sabes?"],
        318: ["Servidor2 no valido (por defecto)", "Tienes la configuracion por defecto y eso esta mal", "tienes que colocar la configuracion porque si esto fuera estatico", "tendrias que pedirle a vicente a cada rato una nueva version del programa", "y yo no quiero eso, asique por esta razon es que puedes modificar la ip como quieras"],
        319: ["Servidor3 no valido (por defecto)", "Colocaste un archivo para el servidor 3, cool", "Pero se te olvido cambiar la configuracion por defecto del servidor 3", "Asique... XD"],

        320: ["Archivo1 no valido", "Porque quitaste el archivo1 de la configuracion?", "Osea, no te entiendo, porque? XD"],
        321: ["Archivo1 no valido (no es .pem)", "Solo aceptamos archivos .pem", "Cambiar el formato .ppk a .pem no funcionara"],
        322: ["Archivo1 no valido (Espacios)", "Y dale con lo mismo", "En ningun caso debes colocar espacios"],
        328: ["Archivo1 no existe", "Como el error lo dice, el archivo que especificaste no existe", "Tas seguro de que vicente te lo paso?"],

        323: ["Archivo2 no valido", "Porque quitaste el archivo1 de la configuracion?", "Osea, no te entiendo, porque? XD"],
        324: ["Archivo2 no valido (no es .pem)", "Solo aceptamos archivos .pem", "Cambiar el formato .ppk a .pem no funcionara"],
        325: ["Archivo2 no valido (Espacios)", "Y dale con lo mismo", "En ningun caso debes colocar espacios"],
        329: ["Archivo2 no existe", "Como el error lo dice, el archivo que especificaste no existe", "Tas seguro de que vicente te lo paso?"],

        326: ["Archivo3 no valido (no es .pem)", "Solo aceptamos archivos .pem", "Cambiar el formato .ppk a .pem no funcionara"],
        327: ["Archivo3 no valido (Espacios)", "Y dale con lo mismo", "En ningun caso debes colocar espacios"],
        330: ["Archivo3 no existe", "Como el error lo dice, el archivo que especificaste no existe", "Tas seguro de que vicente te lo paso?"],


    }

    def displayCode(code = int):
        displayStr: str = "Error: "
        displayColor: str = "red"

        windll.kernel32.SetConsoleTitleW("Error ", code)

        if code == None:
            return
        
        if code < 300:
            windll.kernel32.SetConsoleTitleW("Subidor de musica")
            displayStr: str = "Mensaje: "
            displayColor: str = "green"


        displayMessage: list = Main.error_dict[ code ]

        # print(colored("======================================================================================================================", "red"))
        print("======================================================================================================================")
        print("")
        #print("       " + colored(displayStr, displayColor))
        print("       " + displayStr)
        print("         - " + displayMessage.pop(0))

        if len( displayMessage ) >= 1:
            print("")
            #print(colored("       Ayuda:", "green"))
            print("       Ayuda:")
            
            for msg in range( 0, len(displayMessage) ):
                print("         - " + displayMessage.pop(0))


        print("")
        #print(colored("======================================================================================================================", "red"))
        print("======================================================================================================================")



    def config_reset():
        if not os.path.exists("configuracion.json"):

            with open("configuracion.json", "w") as configFile:
                json.dump( Main.default_config, configFile, indent=4 )
                Main.displayCode(310)
            configFile.close()

        else:
            os.remove("configuracion.json")
            Main.config_reset()



    def config_check() -> bool:
        return os.path.exists("configuracion.json")

    def config_load() -> list:
        with open("configuracion.json", "r") as config:
            return json.load( config )





    def check_errors(config: list):
        pattern = r'^[a-zA-Z_]+$'


        if config["carpeta IN"] == "":
            Main.displayCode(300)
            stop()

        if " " in config["carpeta IN"]:
            Main.displayCode(302)
            stop()

        if not re.search(pattern, config["carpeta IN"]):
            Main.displayCode(301)
            stop()

        if not os.path.exists(config["carpeta IN"]):
            Main.displayCode(304)
            stop()


        if config["carpeta OUT"] == "":
            Main.displayCode(305)
            stop()

        if " " in config["carpeta OUT"]:
            Main.displayCode(307)
            stop()

        if not re.search(pattern, config["carpeta OUT"]):
            Main.displayCode(306)
            stop()

        if not os.path.exists(config["carpeta OUT"]):
            Main.displayCode(308)
            stop()


        url: str = config["url"]
        if url == "":
            Main.displayCode(309)
            stop()


        if not url.startswith("http"):
            Main.displayCode(310)
            stop()

        if config["usuario"] == "":
            Main.displayCode(303)
            stop()

        if config["usuario"] == "elpepe":
            Main.displayCode(312)
            stop()
        
        if " " in config["usuario"]:
            Main.displayCode(313)
            stop()

        if not re.search(pattern, config["usuario"]):
            Main.displayCode(311)
            stop()

        servidor1: str = config["servidor1"]
        servidor2: str = config["servidor2"]
        if servidor1 == "":
            Main.displayCode(314)
            stop()
        
        if not servidor1.endswith("www/html"):
            Main.displayCode(315)
            stop()
        
        if " " in servidor1:
            Main.displayCode(316)
            stop()
        
        if servidor2 == "":
            Main.displayCode(317)
            stop()
        
        if servidor2 == Main.default_config["servidor2"]:
            Main.displayCode(318)
            stop()
        
        if config["archivo3"] != "" and config["servidor3"] == Main.default_config["servidor3"]:
            Main.displayCode(319)
            stop()
        
        archivo1: str = config["archivo1"]
        archivo2: str = config["archivo2"]
        if archivo1 == "":
            Main.displayCode(320)
            stop()
        
        if not archivo1.endswith(".pem"):
            Main.displayCode(321)
            stop()
        
        if not os.path.exists(archivo1):
            Main.displayCode(328)
            stop()
        
        if " " in archivo1:
            Main.displayCode(322)
            stop()

        if archivo2 == "":
            Main.displayCode(320)
            stop()
        
        if not archivo2.endswith(".pem"):
            Main.displayCode(321)
            stop()
        
        if not os.path.exists(archivo2):
            Main.displayCode(329)
            stop()
        
        if " " in archivo2:
            Main.displayCode(322)
            stop()
        
        fileExists: bool = False
        archivo3: str = ""
        if config["archivo3"] != "" :
            archivo3: str = config["archivo3"]

            if not archivo3.endswith(".pem"):
                Main.displayCode(326)
                stop()
            
            if " " in archivo3:
                Main.displayCode(327)
                stop()

            if not os.path.exists(archivo3):
                fileExists: bool = True







    def start():
        if not Main.config_check():
            
            Main.config_reset()
            Main.displayCode(100)
            print("")
            os.system("pause")
            stop()
        
        config = Main.config_load()
        
        Main.check_errors(config)

        print("======================================================================================================================")
        print("          ESTABLECIENDO PERMISOS DE LOS ARCHIVOS")
        print("======================================================================================================================")

        os.system("icacls " + config["archivo1"] + " /inheritance:r")
        os.system("icacls " + config["archivo2"] + " /inheritance:r")
    
        os.system("icacls " + config["archivo1"] + " /grant:r \"%username%\":\"(R)\"")
        os.system("icacls " + config["archivo2"] + " /grant:r \"%username%\":\"(R)\"")

        if not config["archivo3"] == "":
            os.system("icacls " + config["archivo3"] + " /inheritance:r")
            os.system("icacls " + config["archivo3"] + " /grant:r \"%username%\":\"(R)\"")

        print("======================================================================================================================")
        print("             PERMISOS DE LOS REESTABLECIDOS")
        print("======================================================================================================================")

        url:        str = config["url"]
        serv1:      str = config["servidor1"]
        serv2:      str = config["servidor2"]
        serv3:      str = ""
        user:       str = config["usuario"]
        path_in:    str = config["carpeta IN"]
        path_out:   str = config["carpeta OUT"]
        json_file:  str = config["usuario"] + "_json.txt"

        files:      list = []
        upfiles:    list = []

        if not config["servidor3"] == "":
            serv3:      str = config["servidor3"]
        
        if not url.endswith("/"):
            url: str = url + "/" + user + "/"
        else:
            url: str = url + user + "/"



        print("")
        print("Buscando muscia en: " + path_in)
        print("")

        for music in os.listdir(path_in):
            if not music.endswith(".mp3"):
                continue
            
            if "&" in music:
                print("El archivo" + music)
                print("Tiene un caracter no valido (&), saltando...")
                continue
    
            os.rename( path_in + "/" + music, path_in + "/" + music.replace(" ", "_") )


        for music in os.listdir(path_in):
            if not music.endswith(".mp3"):
                continue

            upfiles.append(music)


        for music in upfiles:
            if os.path.exists( path_out + "/" + music ):
                continue

            print("Moviendo  " + music + "  a ->  " + path_out)
            shutil.move( path_in + "/" + music, path_out )


        for filesculiaos in os.listdir(path_out):
            files.append(filesculiaos)

        print("\n")
        print("Creando lista de reproduccion: " + json_file)
        print("")

        json_data: list = []
        for file in files:
            json_data.append({"name": file.replace(".mp3","").replace("_"," "), "url":url+file})

        with open(json_file, 'w') as outfile:
            json.dump(json_data, outfile)

        print("\n")
        print("Subiendo lista de reproduccion " + json_file + "  a -> Servidor1")

        os.system("scp -i " + config["archivo2"] + " " + json_file + " " + serv2)

        if not config["servidor3"] == "":
            print("")
            print("Subiendo lista de reproduccion " + json_file + "  a -> Servidor2")
            os.system("scp -i " + config["archivo3"] + " " + json_file + " " + serv3)

        print("\n")
        print("Subiendo musica al servidor")
        print("")

        for file in upfiles:
            os.system("scp -i" + config["archivo1"] + " " + path_out + "/" + file + " " + serv1 + "/" + user )
            print("Subiendo  ->  " + file)


        Main.displayCode(103)


        print("======================================================================================================================")
        print("          REESTABLECIENDO PERMISOS DE LOS ARCHIVOS")
        print("======================================================================================================================")

        os.system("icacls " + config["archivo1"] + " /grant:r \"%username%\":\"(F)\"")
        os.system("icacls " + config["archivo2"] + " /grant:r \"%username%\":\"(F)\"")

        if not config["archivo3"] == "":
            os.system("icacls " + config["archivo3"] + " /grant:r \"%username%\":\"(F)\"")

        print("======================================================================================================================")
        print("             PERMISOS DE LOS REESTABLECIDOS")
        print("======================================================================================================================")


Main.start()
os.system("pause")