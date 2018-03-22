class Float
  def fact
    (1..self).reduce(:*) || 1
  end
end

class Integer
  def fact
    (1..self).reduce(:*) || 1
  end
end

def lq(miu, lam, ro, s, p_0)
  ((((lam / miu)**s) * p_0 * ro) / (s.fact * (1 - ro)**2))
end

def wq(l_q, lam)
  l_q / lam
end

def ws(w_q, miu)
  w_q + (1 / miu)
end

def ls(lam, w_s)
  lam * w_s
end

def ro(miu, lam, s)
  lam / (miu * s)
end

def have_0_clients_system(miu, lam, ro, s)
  x = 0
  for n in 0..(s - 1)
    x += ((lam / miu)**n) / n.fact
  end
  y = ((lam / miu)**s) / (s.fact * (1.0 - ro))
  1.0 / (x + y)
end

def have_n_clients_system(miu, lam, ro, s, p_0, n)
  if n >= 0 && n <= s
    (((lam / miu)**n) * p_0) / n.fact
  elsif n > s
    (((lam / miu)**n) * p_0) / (s.fact * s**(n-s))
  end
end

def main
  puts "Sistema de colas MMS\n Bernardo Ortega Septien \n Bernardo Gomez Romero \n Martin Alejandro Molinero"
  puts "Introduce la tasa media de servicio: "
  miu = Float($stdin.readline())
  puts "Introduce la tasa media de llegadas: "
  lam = Float($stdin.readline())
  puts "Introduce el numero de sistemas: "
  systems = Float($stdin.readline())
  puts "Introduce el numero de personas (n) para obtener probabilidad p(n): "
  n = Float($stdin.readline())
  puts "Introduce el costo por sistema: "
  cc = Float($stdin.readline())
  puts "Introduce el costo por cola: "
  cw = Float($stdin.readline())
  ro = ro(miu, lam, systems) # listo
  p_0 = have_0_clients_system(miu, lam, ro, systems)
  l_q = lq(miu, lam, ro, systems, p_0)
  w_q = wq(l_q, lam)
  w_s = ws(w_q, miu)
  l_s = ls(lam, w_s)
  (n == 0) ? p_n = p_0 : p_n = have_n_clients_system(miu, lam, ro, systems, p_0, n)
  cc_s = cc * systems
  cw_ls = cw * l_s
  cTotal = cc_s + cw_ls

  puts "\nRo: #{ro.to_s}"
  puts "Ls: #{l_s.to_s}"
  puts "Lq: #{l_q.to_s}"
  puts "Wq: #{w_q.to_s}"
  puts "Ws: #{w_s.to_s}"
  puts "Probabilidad de n: #{p_n.to_s}"
  puts "\nCosto Total: #{cTotal.to_s}"
end

main