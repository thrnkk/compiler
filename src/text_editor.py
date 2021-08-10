
# --------------------------------------------------------------------------- Imports -------------------------------------------------------------------------- #

import tkinter as tk

# ----------------------------------------------------------------- Classe do Contador de Linhas --------------------------------------------------------------- #

class TextLineNumbers(tk.Canvas):

    """
    Cria o contador de linhas.
    """

    def __init__(self, *args, **kwargs):

        tk.Canvas.__init__(self, *args, **kwargs)

        self.textwidget = None

    def attach(self, text_widget):

        """
        Conecta as linhas com o texto.
        """

        self.textwidget = text_widget

    def redraw(self, *args):

        """
        Recria os números.
        """

        self.delete("all")

        i = self.textwidget.index("@0,0")

        while True :

            dline = self.textwidget.dlineinfo(i)

            if dline is None: break

            y = dline[1]

            linenum = str(i).split(".")[0]

            self.create_text(2, y, anchor = "nw", text = linenum)

            i = self.textwidget.index("%s+1line" % i)

# ------------------------------------------------------------------------ Classe do Texto --------------------------------------------------------------------- #

class CustomText(tk.Text):

    """
    Cria um texto customizado.
    """

    def __init__(self, *args, **kwargs):

        tk.Text.__init__(self, *args, **kwargs)

        self.tk.eval('''

            proc widget_proxy {widget widget_command args} {

                # call the real tk widget command with the real args
                set result [uplevel [linsert $args 0 $widget_command]]

                # generate the event for certain types of commands
                if {([lindex $args 0] in {insert replace delete}) ||
                    ([lrange $args 0 2] == {mark set insert}) || 
                    ([lrange $args 0 1] == {xview moveto}) ||
                    ([lrange $args 0 1] == {xview scroll}) ||
                    ([lrange $args 0 1] == {yview moveto}) ||
                    ([lrange $args 0 1] == {yview scroll})} {

                    event generate  $widget <<Change>> -when tail
                }

                # return the result from the real widget command
                return $result

            }
            ''')

        self.tk.eval('''

            rename {widget} _{widget}
            interp alias {{}} ::{widget} {{}} widget_proxy {widget} _{widget}

        '''.format(widget=str(self)))

# ------------------------------------------------------------------------ Classe do Editor -------------------------------------------------------------------- #

class TextEditor(tk.Frame):

    """
    Cria o editor de texto.
    """

    def __init__(self, *args, **kwargs):

        tk.Frame.__init__(self, *args, **kwargs)

        self.text = CustomText(self)

        self.vsb = tk.Scrollbar(self, orient="vertical", command=self.text.yview)
        self.hsb = tk.Scrollbar(self, orient="horizontal", command=self.text.xview)

        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.configure(xscrollcommand=self.hsb.set)
        self.text.configure(wrap = tk.NONE)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))

        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.attach(self.text)

        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side="bottom", fill="x")

        self.linenumbers.pack(side="left", fill="y")

        self.text.pack(side="right", fill="both", expand=True)
        self.text.bind("<<Change>>", self.onChange)
        self.text.bind("<Configure>", self.onChange)

    def onChange(self, event):

        """
        Assiste as mudanças.
        """

        self.linenumbers.redraw()

    def setText(self, text):

        """
        Define o texto do editor.
        """

        self.clearText();
        self.text.insert('end', text)

    def copyText(self):

        """
        Copia o texto do editor.
        """

        self.text.clipboard_clear()
        selected = self.text.get("sel.first", "sel.last")
        self.text.clipboard_append(selected)

    def pasteText(self):

        """
        Cola o texto no editor.
        """

        copied = self.text.selection_get(selection='CLIPBOARD')
        self.text.insert('insert', copied)

    def cutText(self):

        """
        Recorta o texto do editor.
        """

        self.copyText()
        self.text.delete("sel.first", "sel.last")

    def clearText(self):

        """
        Limpa o texto do editor.
        """

        self.text.delete('1.0', 'end')

    def getText(self):

        """
        Retorna o texto do editor.
        """

        return self.text.get('1.0', 'end-1c')