#!/usr/bin/python3
# Generate documenation
# * README.md
# * README.html
import sys

def gen_readme_html():
    """generate README.html"""
    import cgi
    f = open("templates/README.html").read()
    sampleClass = open("CppHeaderParser/examples/SampleClass.h").read()
    readSampleClass = open("CppHeaderParser/examples/readSampleClass.py").read()
    
    f = f.replace("{SAMPLE_CLASS_H}", cgi.escape(sampleClass))
    f = f.replace("{READ_SAMPLE_CLASS_PY}", cgi.escape(readSampleClass))
    f = f.replace("{READ_SAMPLE_CLASS_PY_OUTPUT}", cgi.escape(get_sample_class_output()))
    open("README.html", "wa").write(f)


def gen_readme_txt():
    """generate README.md"""
    import cgi
    f = open("templates/README.md", "r").read()
    sampleClass = open("CppHeaderParser/examples/SampleClass.h").read()
    readSampleClass = open("CppHeaderParser/examples/readSampleClass.py", "r").read()
    
    f = f.replace("{SAMPLE_CLASS_H}", "    " + sampleClass.replace("\n", "\n    "))
    f = f.replace("{READ_SAMPLE_CLASS_PY}", "    " + readSampleClass.replace("\n", "\n    "))
    f = f.replace("{READ_SAMPLE_CLASS_PY_OUTPUT}", "    " + get_sample_class_output().replace("\n", "\n    "))
    open("README.md", "w").write(f)
    print("wrote README.md")
    
    import markdown
    h = markdown.markdown(open("README.md").read())
    open("README.html", "w").write(h)
    print("wrote README.html")


def get_sample_class_output():
    import subprocess
    return subprocess.Popen(["python3", "readSampleClass.py"],
        stdout=subprocess.PIPE,
        cwd="CppHeaderParser/examples"
        ).communicate()[0].decode('ascii', 'ignore')




if __name__ == "__main__":
    gen_readme_txt()
