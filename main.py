from datetime import date
import shutil, bs4, re, os
import config

# To Path
tp = os.path.join("releases",date.today().strftime("%Y%m%d"))
# Path to Code Coverage:
ptcc = config.ORIGIN_PATH
# Path to Output
pto = os.path.join(os.getcwd(),tp)

"""
Copia los archivos desde el reporte hasta la carpeta que se se va colgar en la web
ignora los archivos finalizados en .ts.html
"""
def copyfiles():
    shutil.rmtree(pto, ignore_errors=True)
    # Copy all files except those that finish with .ts.html
    ignore = shutil.ignore_patterns("*.ts.html")
    shutil.copytree(ptcc,pto,False,ignore)

"""
Metodo 1: Reemplaza los links que terminan en '.ts.htm' con '#'
Lo hace mediante regex. Con este metodo no se pierden estilos en el html resultante
"""
def reemplazar_regex(path):
    was_changed = False
    f = os.path.join(path,"index.html")
    print("========================")
    file_ref = open(f,"r")
    text = file_ref.read()
    # print(text)
    regex = re.compile(r'href="(.*?)">')
    for tag in regex.findall(text):
        href = tag.split(".")
        if href[len(href)-2] == "ts" and href[len(href)-1] == "html":
            myreg = re.compile(r''+tag) 
            text = myreg.sub("#",text)
            was_changed = True

    print("")
    print(text)
    print("========================")
    file_ref.close()
    if was_changed:
        sobreescribir(text,f)


"""
Solo sobreescribe el archivo que fue reemplazado
"""
def sobreescribir(text,path):
    f = open(path,"w")
    f.write(text)
    f.close()




"""
Itera a lo largo de la rama y se llama de forma recursiva.
Recibe el path de donde buscar la lista de archivos.
"""
def develop(path):
    for ld in os.listdir(path):
        ext = ld.split(".")
        # print("========================")
        # print(ext)
        if len(ext) > 1:
            # print("Es un achivo")
            if ext[0] == "index":
                # print("Se encontro el INDEX")
                # Metodo uno funciona, pero se pierden algunos estilos..
                # replace_index(path)
                reemplazar_regex(path)
                return
        else:
            # Tengo que buscar dentro de esta carpeta:
            child_path = os.path.join(path,ext[0])
            # print("Se tiene que entrar a la carpeta: ")
            # print(child_path)
            develop(child_path)
            

"""
Metodo 2: Reemplaza los links que terminan en '.ts.htm' con '#'
con beautifulsoup y luego sobreescribe el archivo. Con este metodo se pierden algunos estilos en 
el css resultante.
"""
def replace_index(path):
    was_changed = False
    f = os.path.join(path,"index.html")
    file_ref = open(f)
    bsoup = bs4.BeautifulSoup(file_ref,"html.parser")
    elem = bsoup.select("a")
    for a in elem:
        href = a["href"].split(".")
        if href[len(href)-2] == "ts" and href[len(href)-1] == "html":
            a["href"] = "#"
            was_changed = True
    
    # Una vez que todos los links fueron reemplazados,
    # se sobreescribe el archivo abierto
    if was_changed:
        file_ref.close()
        print("Se sobreescribe: "+f)
        updates = open(f,"w")
        updates.write(str(bsoup))
        updates.close()
        return

    file_ref.close()


if __name__ == "__main__":
    # Copio los archivos desde el directorio:
    # copyfiles()

    # Reemplazo los archivos index
    # develop(pto)

    # app_path = os.path.join(pto,"src","app")
    # reemplazar_href(app_path)
    # reemplazar_regex(app_path)

    print(ptcc)