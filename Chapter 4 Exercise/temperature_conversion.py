def fahrenheit(celsius):

    calculate_celsius = (9 / 5) * celsius + 32
   
    return calculate_celsius
    
    
print(fahrenheit(60))



print(f'{"Celsius":>10}{"Fahrenheit":>15}')

for celsius in range(0, 101):

    print(f'{celsius:>10}{fahrenheit(celsius):>15.1f}')
    
    
    
    
