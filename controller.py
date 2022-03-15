#!/usr/bin/python3
import modelo
import vista


class axiomaTerminalController:
    def __init__(self):
        self.model = modelo.axiomaModel()
        self.view = vista.vistaAxiomasPorTerminal()

    def run(self):
        try: 
            vNroDeAxiomaEscogido = int(self.view.escojeAxioma())
            vAxioma = self.model.obtenerAxioma(vNroDeAxiomaEscogido)
            self.view.mostrar(vAxioma)
        except ValueError as e:
            print(e)