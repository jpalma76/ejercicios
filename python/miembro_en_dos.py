
def miembro_en_dos(arr1,arr2,valor):
    if valor in arr1 and valor in arr2:
        return True
    return False

# Fin
arr1 = ["Nueva York", "Londres", "Tokio", "Sídney"]
arr2 = ["Londres", "París", "Tokio", "Berlín"]

print(miembro_en_dos(arr1, arr2, "Londres"))  
print(miembro_en_dos(arr1, arr2, "París"))   
print(miembro_en_dos(arr1, arr2, "Tokio"))  