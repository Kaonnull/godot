
import os;
import glob;
import string;


#Generate include files

f=open("theme_data.h","wb")

f.write("// THIS FILE HAS BEEN AUTOGENERATED, DONT EDIT!!\n");

f.write("\n\n");

#Generate png image block

pixmaps = glob.glob("*.png");

pixmaps.sort();

f.write("\n\n\n");

for x in pixmaps:

    var_str=x[:-4]+"_png";

    f.write("static const unsigned char "+ var_str +"[]={\n");

    pngf=open(x,"rb");

    b=pngf.read(1);
    while(len(b)==1):
        f.write(hex(ord(b)))
        b=pngf.read(1);
        if (len(b)==1):
            f.write(",")

    f.write("\n};\n\n\n");
    pngf.close();

#Generate shaders block

shaders = glob.glob("*.gsl")

shaders.sort();

f.write("\n\n\n");

for x in shaders:

    var_str=x[:-4]+"_shader_code";

    f.write("static const char *"+ var_str +"=\n");

    sf=open(x,"rb");


    b=sf.readline();
    while(b!=""):
        if (b.endswith("\r\n")):
            b=b[:-2]
        if (b.endswith("\n")):
            b=b[:-1]
        f.write("			\""+b)
        b=sf.readline();
        if (b!=""):
            f.write("\"\n")

    f.write("\";\n\n\n");
    sf.close();

f.close();
