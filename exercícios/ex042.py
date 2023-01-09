s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento:'))
s3 = float(input('Terceiro segmento:'))

if (s1 + s2) > s3 and (s2 + s3) > s1 and (s1 + s3) > s2:
    if s1 == s2 == s3:
        print('Os segmentos formam um triângulo equilátero')
    elif s1 == s2 or s1 == s3 or s2 == s3:
        print('Os segmentos forma um triângulo isóceles')
    elif s1 != s2 != s3:
        print('Os segmentos formam um triânguilo escaleno')
else:
    print('Os segmentos não podem formar um triângulo')