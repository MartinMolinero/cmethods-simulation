def ls(miu, lam)
  lam/(lam-miu)
end

def lq(miu, lam)
  (lam**2.0)/miu*(miu-lam)
end

def ws(miu, lam)
  1.0/(miu-lam)
end

def wq(miu, lam)
  lam/miu*(miu-lam)
end

def ro(miu, lam)
  lam/miu
end

def have_n_clients_system(ro, n)
  (1.0-ro)*(ro**n)
end

def clients_wait_queue_greater(ro, miu, t)
  ro*Math.exp(-miu*(1.0-ro)*t)
end

def clients_wait_system_greater(ro, miu, t)
  Math.exp(-miu*(1.0-ro)*t)
end

def clients_wait_system(ro, n)
  ro**(n+1.0)
end



def main
  puts "Sistema de colas \n Bernardo Ortega Septien \n Bernardo Gomez Romero \n Martín Alejandro Molinero"
  puts "Introduce la tasa media de servicio"
  miu = Float($stdin.readline())
  puts "Introduce la tasa media de llegadas"
  lamb = Float($stdin.readline())
  l_s = ls(miu, lamb)
  l_q = ls(miu, lamb)
  w_q = wq(miu, lamb)
  w_s = ws(miu, lamb)
  p = ro(miu, lamb)
  have_0_clients_system = have_n_clients_system(p, 0)
  cumulative = have_n_clients_system(p, 0) + have_n_clients_system(p, 1) + have_n_clients_system(p, 2) + have_n_clients_system(p, 3)
  have_queue_more_3 = 1- cumulative
  wait_more_30_min_queue = clients_wait_queue_greater(p, miu, 30)
  wait_more_30_min_system = clients_wait_system_greater(p,miu,30)
  intersection = wait_more_30_min_queue * wait_more_30_min_system

  puts "Ls: #{l_s.to_s}"
  puts "Lq: #{l_q.to_s}"
  puts "Wq: #{w_q.to_s}"
  puts "Ws: #{w_s.to_s}"

  puts "Probabilidad de tener 0 clientes #{have_0_clients_system.to_s}"
  puts "Probabilidad de tener cola mayor a 3 #{have_queue_more_3.to_s}"
  puts "Probabilidad de esperar +30 min en cola #{wait_more_30_min_queue.to_s}"
  puts "Probabilidad de esperar +30 min en cola #{wait_more_30_min_system.to_s}"
  puts "Interseccion anterior #{intersection.to_s}"
end
main
