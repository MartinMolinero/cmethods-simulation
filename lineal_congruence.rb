def recursive_formula(a, z_param, c, m)
  return   ((a*z_param) + c ) % m
end

def r_value(z, m)
  print "z/m" + z.to_s + m.to_s
  return Float(z) / Float(m)
end

def main_formula
  puts "M Value: "
  m = Integer($stdin.readline())
  puts "A Value: "
  a = Integer($stdin.readline())
  puts "C Value: "
  c = Integer($stdin.readline())
  puts "Z Value: "
  z_init = Integer($stdin.readline())
  z = z_init
  puts "Iterations: "
  itr = Integer($stdin.readline())

  #First iteration
  z_i = recursive_formula(a,z, c,m)
  r = r_value(z_i, m)
  z = z_i
  z_one = z_i
  puts "\n\n-Iteration: 1 \n-Z: " + z.to_s + "\n-R: " +  r.to_s

  #Rest of iterations
  for i in 2..(itr -1)
    z_i = recursive_formula(a,z, c,m)
    if (z_i == z_one)
      puts "\n\n-Cycle length: " + (i - 1).to_s
    break
    end
    r = r_value(z_i, m)
    z = z_i
    puts "\n\n-Iteration: " + i.to_s  + "\n-Z: " + z.to_s + "\n-R: " +  r.to_s
  end
end

main_formula
