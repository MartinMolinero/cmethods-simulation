
def decide_max(upper, lower)
  max = lower
  aux = 0
  for i in upper..lower
    aux = function(i)
    if aux > max then
      max = aux
    end
  end
end

def function1(val)
  (-1/6) + (val/12)
end

def function2(val)
  (4/3) - (val/6)
end


def method
  puts "Introduce el limite inferior de f1"
  low1 = Integer($stdin.readline(), 10)
  puts "Introduce el limite superior de f1"
  high1 = Integer($stdin.readline(), 10)
  puts "Introduce el limite inferior de f2"
  low2 = Integer($stdin.readline(), 10)
  puts "Introduce el limite superior de f2"
  high2 = Integer($stdin.readline(), 10)
  puts "Introduce m"
  m = Integer($stdin.readline(), 10)
  puts "Introduce cuántos números quieres generar"
  limit = Integer($stdin.readline(), 10)
  numbers = []
  puts "Max #{m}"
  while numbers.length < limit do
    r1 = rand().to_f
    r2 = rand().to_f
    x_star = low1 + (high2 - low1) * r1
    if(x_star >= low1 && x_star <= high1)
      f_x_star = function1(x_star)
    elsif(x_star >= low2 && x_star <= high2)
      f_x_star = function2(x_star)
    else
      f_x_star = 0
    end
      
    if r2 <= (f_x_star/m) then
      numbers.push(x_star)
    end
  end
  output = File.open("output.txt", "w")
  numbers.each do |n|
    output << n.to_s + "\n"
  end
  output.close
end

method
