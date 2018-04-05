def ws(miu, wq)
  wq + (1.0/miu)
end

def ls_1(ws, lam)
  lam * ws
end

def ls_2(lq, lam, miu)
  lq + (lam/miu)
end

def lq(wq, lam)
  lam * wq
end

def p(lam, miu, s)
  lam/(miu*s)
end

def main
  puts "Sistema de colas - Ley de Little \n Bernardo Ortega Septien \n Bernardo Gomez Romero \n Martín Alejandro Molinero"
  puts "Introduce la tasa media de servicio (miu): "
  miu = Float($stdin.readline())
  puts "Introduce la tasa media de llegadas (lambda): "
  lamb = Float($stdin.readline())
  puts "Introduce el tiempo esperado de espera en la cola (Ws): "
  w_q = Float($stdin.readline())
  w_s = ws(miu, w_q)
  l_q = lq(w_q, lamb)
  l_s = ls_1(w_s, lamb)
  # l_s = ls_2(ws, lamb)
  ro = p(lamb, miu, 1)

  puts "Ls: #{l_s.to_s}"
  puts "Lq: #{l_q.to_s}"
  puts "Wq: #{w_q.to_s}"
  puts "Ws: #{w_s.to_s}"
  puts "Ro con 1 servidor #{ro.to_s}"

end
main
