import numpy # type: ignore
array1=numpy.array([7,1,2,3,4,9,5,5])
print(array1)

mean=numpy.mean(array1)
print(mean)

median=numpy.median(array1)
print(median)

std_dev=numpy.std(array1)
print(std_dev)

min_val=numpy.min(array1)
print(min_val)

max_val=numpy.max(array1)
print(max_val)

sum_val=numpy.sum(array1)
print(sum_val)

product_val=numpy.prod(array1)
print(product_val)

cumulative_sum=numpy.cumsum(array1)
cumulative_product=numpy.cumprod(array1)
print(cumulative_sum)
print(cumulative_product)

sorted_array=numpy.sort(array1)
print(sorted_array)

unique_elements=numpy.unique(array1)
print(unique_elements)

array2=numpy.array([5,6,7,8])
concatenated_array=numpy.concatenate((array1,array2))
print(concatenated_array)

transposed_array=numpy.transpose(array1)
print(transposed_array)

flipped_array=numpy.flip(array1)
print(flipped_array)

sliced_array=array1[1:3]
print(sliced_array)

indexed_array=array1[[0,2,3]]
print(indexed_array)

resized_array=numpy.resize(array1,(2,2,2))
print(resized_array)

array3=numpy.array([1,2,3,4,5,6,7,8])
array4=numpy.array([9,10,11,12])
array5=numpy.concatenate((array3,array4))
print(array5)


