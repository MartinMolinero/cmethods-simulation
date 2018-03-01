def function(r, a, b)
    x = r * (b - a) + a
    return x
end

def method
    puts "Introduce el limite inferior"
    a = Integer($stdin.readline(), 10)
    puts "Introduce el limite superior"
    b = Integer($stdin.readline(), 10)
    puts "Introduce el número de iteraciones"
    i = Integer($stdin.readline(), 10)
    for j in 1..i
        r = rand().to_f
        x = function(r, a, b)
        puts x
    end
end

method