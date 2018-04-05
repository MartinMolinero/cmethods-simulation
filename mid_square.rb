def get_n (number)
  return number.length / 2
end

def square(number)
  return number**2;
end

def transform(squared, n)
  while(squared.to_s.length < 4*n) do
    squared = '0' + squared.to_s
  end
  return squared
end

def return_substring(number, n)
  return number[0+n, number.length - n*2]

end

def method()
  puts "Introduce la semilla (Z0)"
  number = Integer($stdin.readline(), 10)
  puts "Introduce las iteraciones"
  iter = Integer($stdin.readline(), 10)
  n = get_n(number.to_s)
  while(iter > 0 ) do
    squared = square(number)
    squared = transform(squared, n)
    str = return_substring(squared.to_s, n)
    print "\nZi-1: " + number.to_s + "\t(Zi-1)^2: " + squared.to_s + "\tZi: " + str + "\tResult: " + "." + str
    number = str.to_i
    iter = iter - 1
  end

end

method
