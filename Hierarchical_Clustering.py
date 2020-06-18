from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
import psycopg2

conn = psycopg2.connect(host="localhost", port=5432, database="GAPT", user="postgres", password="andrew")

cur = conn.cursor()

# A sample query of all data from the "vendors" table in the "suppliers" database
cur.execute("""SET search_path = 'NYCPV'; """)
cur.execute("""SELECT violation_code,issuer_code FROM parking WHERE registration_state = 'NY' LIMIT 10000;""")
A = cur.fetchall()
print(A)

cur.execute("""SET search_path = 'NYCPV'; """)
cur.execute("""SELECT violation_code,issuer_code FROM parking WHERE registration_state = 'NJ' LIMIT 10000;""")
B = cur.fetchall()
print(B)

concat = np.concatenate((A, B),)

print (concat.shape)
plt.scatter(concat[:,0], concat[:,1])
plt.show()

final_data = linkage(concat, 'single')

plt.figure(figsize=(20, 5))
plt.title('Dendrogram')
plt.ylabel('distance')
dendrogram(final_data, truncate_mode='lastp')
plt.show()

cur.close()
conn.close()


