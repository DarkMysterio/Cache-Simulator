import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a utility diagram for the application flow described by the user
fig, ax = plt.subplots(figsize=(10, 15))

# Function to draw a box with a label
def draw_box(ax, xy, width, height, label):
    rect = patches.Rectangle(xy, width, height, linewidth=2, edgecolor='black', facecolor='lightgrey')
    ax.add_patch(rect)
    ax.text(xy[0] + width / 2, xy[1] + height / 2, label, 
            horizontalalignment='center', verticalalignment='center', fontsize=10, weight='bold')

# Function to draw an arrow
def draw_arrow(ax, start, end, text=None):
    ax.annotate('', xy=end, xytext=start, arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5))
    if text:
        ax.text((start[0] + end[0]) / 2, (start[1] + end[1]) / 2, text, fontsize=9, ha='center', va='center')

# Draw the main flow
draw_box(ax, (4, 25), 6, 1.5, 'Pornește Aplicația')
draw_arrow(ax, (7, 24.5), (7, 23.5))
draw_box(ax, (4, 22), 6, 1.5, 'Utilizatorul Introduce Configurația Cache-ului')
draw_arrow(ax, (7, 21.5), (7, 20.5))
draw_box(ax, (4, 19), 6, 1.5, 'Utilizatorul Trimite Configurația')
draw_arrow(ax, (7, 18.5), (7, 17.5))
draw_box(ax, (4, 16), 6, 1.5, 'Aplicația Salvează Configurația')
draw_arrow(ax, (7, 15.5), (7, 14.5))
draw_box(ax, (4, 13), 6, 1.5, 'Începe Bucla')
draw_arrow(ax, (7, 12.5), (7, 11.5))
draw_box(ax, (4, 10), 6, 1.5, 'Utilizatorul Introduce Adresa și Selectează Operația (Read/Write)')
draw_arrow(ax, (7, 9.5), (7, 8.5))
draw_box(ax, (4, 7), 6, 1.5, 'Aplicația Procesează Adresa')

# Draw branches for Cache Hit and Cache Miss
draw_arrow(ax, (7, 6.5), (5, 5.5))
draw_box(ax, (2, 4), 6, 1.5, 'Cache Hit')
draw_arrow(ax, (5, 3.5), (5, 2.5))
draw_box(ax, (2, 1), 6, 1.5, 'Recuperează Datele din Cache')

draw_arrow(ax, (7, 6.5), (9, 5.5))
draw_box(ax, (8, 4), 6, 1.5, 'Cache Miss')
draw_arrow(ax, (11, 3.5), (11, 2.5))
draw_box(ax, (8, 1), 6, 1.5, 'Încarcă Blocul din RAM în Cache')

# Merge paths after Cache Hit and Cache Miss
draw_arrow(ax, (5, 0.5), (7, -0.5))
draw_arrow(ax, (11, 0.5), (7, -0.5))
draw_box(ax, (4, -2), 6, 1.5, 'Actualizează Cache-ul și Datele')
draw_arrow(ax, (7, -2.5), (7, -3.5))
draw_box(ax, (4, -5), 6, 1.5, 'Afișează Datele și Actualizează Consola')
draw_arrow(ax, (7, -5.5), (7, -6.5))
draw_box(ax, (4, -8), 6, 1.5, 'Actualizează Statisticile Cache-ului')
draw_arrow(ax, (7, -8.5), (7, -9.5))
draw_box(ax, (4, -11), 6, 1.5, 'Utilizatorul Decide să Acceseze o Altă Adresă?')

# Draw branches for Yes (Da) and No (Nu)
draw_arrow(ax, (7, -11.5), (5, -12.5))
draw_box(ax, (2, -14), 6, 1.5, 'Da (Bucla se Reia)')
draw_arrow(ax, (5, -14.5), (5, -15.5))
draw_arrow(ax, (7, -11.5), (9, -12.5))
draw_box(ax, (8, -14), 6, 1.5, 'Nu (Închide Aplicația)')

# Adjust plot limits and remove axes
ax.set_xlim(0, 15)
ax.set_ylim(-16, 26)
ax.axis('off')

# Show the diagram
plt.show()


