def imprimir(cliente, comprobante, total = '1.00'):
    print('---------------------')
    print(f'Cliente: {cliente}')
    print(f'Comprobante: {comprobante}')
    print(f'Total: {total}')
    print('**************')

imprimir('Software Lion', 'Factura', '100.25')
imprimir('Liones Messi', 'Boleta', '1.50')
imprimir('Magali Medina', 'Tiket')