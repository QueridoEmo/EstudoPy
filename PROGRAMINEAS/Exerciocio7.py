m_Conv = int (input('Quantos metros deseja calcular? '))
dam_conv = int(m_Conv) / 10
hm_conv = int(dam_conv) / 10
km_conv = int(hm_conv) / 10
#
dm_conv = int(dam_conv) * 10
cm_conv = int(dm_conv) * 10
mm_conv = int(cm_conv) * 10
print (f'{m_Conv}M equivale a:\n Km: {km_conv}\n Hm: {hm_conv}\n Dam: {dam_conv}\n Dm: {dm_conv}\n Cm: {cm_conv}\n Mm: {mm_conv}\n :D!')
