import os
import numpy as np
import cv2
from time import *
from sklearn import preprocessing
from calculate import *
#from sklearn.metrics.pairwise import cosine_similarity

dir = r'C:\\Users\\ASUS\\Documents\\Programming\\Python\\Algeo02-21067\\dataset\\train'
tesdir = r'C:\\Users\\ASUS\\Documents\\Programming\\Python\\Algeo02-21067\\dataset\\test'

label_training = labelimg(dir)
label_test = labelimg(tesdir)
#Training
A = A_Matrix(dir)
kov = covariance(A)
#Bagian yang harus kita kulik sendiri, ga boleh pakai library linear algebra
eigenvalues, eigenvectors, = theEigen(kov,50)
eigenvalues, eigenvectors = eigenSort(eigenvalues,eigenvectors)
eigenfaces = get_eigenfaces(eigenvectors,20) #20 Eigenfaces terbanyak
w_base = get_weight(eigenfaces,A)

# # #TESTING# # #
test = get_test(tesdir)
avg = avg_image(dir)
norm_test = test - avg

# recon = avg + np.dot(w_base[1, :],proj_data)
# kov_test = covariance(norm_test)
# eigenvalues, eigenvectors, = eigen(kov_test)
# eigenvalues, eigenvectors = eigenSort(eigenvalues,eigenvectors)
# proj_test = np.dot(A.T,eigenvectors)
# proj_test = proj_test.T

# w_0 = np.array([np.dot(proj_test,i) for i in test])
# print(w_0.shape,w_base.shape)




weight_0 = np.array([np.dot(eigenfaces,i) for i in norm_test])

z = 0
for k in weight_0:
    ctr = 0
    mark = 0
    for i in w_base:
        if ctr == 0:
            euclidian_distance = np.linalg.norm(k-i)
            cos_sim = cosine_sim(k,i)
        else:
            if np.linalg.norm(k-i) < euclidian_distance:
                euclidian_distance = np.linalg.norm(k-i)
                mark = ctr
                cos_sim = cosine_sim(k,i)
        ctr += 1
    print(f"yang sesuai dengan dataset: {label_training[mark]}")
    print(f"label test {z}: {label_test[z]}")
    print(f"euclidian distance: {euclidian_distance}")
    print(f"cos_sim: {cos_sim}")
    print("++++++++++++++++++++++++++++")
    z+= 1


















#MENAMPILKAN EXAMPLE EIGENFACE
#img = proj_data[4].reshape(256,256).astype('uint8')
# a = (proj_data[2]).reshape(256,256)
# a = np.interp(a, (a.min(), a.max()), (0, 256))
# img = (a).reshape(256,256).astype('uint8')

# grayImage = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# cv2.imshow('image',grayImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




#def eigenvector():
#print("Dengan dekomposisi QR: ",eigenval(C,20))
#print("Dengan library eigen dari numpy: ",w)

# def eigenVectorMajor(v,A):
#     container = np.array([])
#     for i in range (v.shape[0]):
#         temp = A @ v[i] 
#         container = np.concatenate((container,temp),axis=0)
#     container = container.reshape((int(len(container)/v.shape[0]),v.shape[0]))
#     return container


# average = avg_image(dir).reshape(256,256).astype('uint8')
# img = norm_img(cv2.imread(dir+'\\Chris Hemsworth111_393.jpg')).reshape(256,256)
# img = np.subtract(img,average)
# print(average)

# img = norm_img(cv2.imread(dir+'\\Chris Hemsworth111_393.jpg')).reshape(256,256)
# print(img.dtype)

# grayImage = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

# cv2.imshow('image',grayImage)
# cv2.waitKey(0)

# cv2.destroyAllWindows()
# v_major = eigenVectorMajor(v,A)
# v_major = v_major.T
# print(v_major.shape)


# eigenfaces1 = preprocessing.minmax_scale(v_major[0], feature_range=(0,255))
# eigenfaces1 = v_major[3]
# eigenfaces1 = eigenfaces1.reshape(256,256).astype('uint8')

# print(eigenfaces1)


# grayImage = cv2.cvtColor(eigenfaces1, cv2.COLOR_GRAY2BGR)

# cv2.imshow('image',grayImage)
# cv2.waitKey(0)

# cv2.destroyAllWindows()




    
    


#print(w.shape)
# u = np.array([])
# for i in range(10):
#     k = A.T@v[i]
#     u = np.concatenate((u,k),axis=0)

# u = u.reshape((10,int(len(u)/10)))
# print(u)








    

        




    

