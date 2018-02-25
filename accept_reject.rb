
def decide_max(upper, lower)
  max = lower
  aux = 0
  for i in upper..lower
    aux = function(i)
    if aux > max then
      max = aux
    end
  end
  max
end

def function(val)
  2*val
end



def method
  puts "Introduce el limite inferior"
  low = Integer($stdin.readline(), 10)
  puts "Introduce el limite superior"
  high = Integer($stdin.readline(), 10)
  puts "Introduce cuántos números quieres generar"
  limit = Integer($stdin.readline(), 10)
  m = decide_max(low, high)
  numbers = []
  puts "Max #{m}"
  while numbers.length < limit do
    r1 = rand().to_f
    r2 = rand().to_f
    x_star = low + (high - low) * r1
    f_x_star = function(x_star)
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
