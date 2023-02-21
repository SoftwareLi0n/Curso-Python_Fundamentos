class Comprobante:
    def registrar_venta(self, id):
        self.id_comprobante = id
        print('venta registrada...')

    def imprimir(self):
        print('**** PRINT ****')
        print(self.id_comprobante)
        print('***************')

comprobante = Comprobante()
comprobante.registrar_venta('F001-120')
comprobante.imprimir()

mensaje = f'Venta exitosa: {comprobante.id_comprobante}'
print(mensaje)