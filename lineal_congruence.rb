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
  puts "A Value"
  a = Integer($stdin.readline())
  puts "C Value"
  c = Integer($stdin.readline())
  puts "Z Value"
  z = Integer($stdin.readline())
  puts "Iteration"
  itr = Integer($stdin.readline())
  for i in 1..itr
    z_i = recursive_formula(a,z, c,m)
    r = r_value(z_i, m)
    z = z_i
    puts "\n\n Itr: " + i.to_s  + "\nZ: " + z.to_s + "\n R: " +  r.to_s
  end
end

main_formula
