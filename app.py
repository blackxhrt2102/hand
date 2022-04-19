
#-------- Modules ------------------------------------------------------
import streamlit as st  # For webpage
import pickle           # Installing model
from PIL import Image   
import requests         
import numpy as np



#-------------- Page Configuration -----------------------
st.set_page_config(page_title='Book Recommender', page_icon='📚',
                   layout='centered', initial_sidebar_state='expanded')

#----------------- Recommenation book ------------------
def main():
  #---------Loading model -------------------------------------
  pivot_table=pickle.load(open('/content/book_tag.pkl','rb'))
  model=pickle.load(open('/content/model.pkl','rb'))
  image=pickle.load(open('/content/image (1).pkl','rb'))
  book_info=pickle.load(open('/content/info_book.pkl','rb'))

  st.title('Book Recommendation Engine 📖')
  book=st.selectbox('Enter name of the book',pivot_table.index)
  if book is not None:
    url=image[image['Book-Title']==book]['Image-URL-M'].values[0]
    im2= Image.open(requests.get(url, stream=True).raw)
    st.sidebar.markdown('**Book you choose**:- **{}**'.format(book))
    st.sidebar.image(im2,width=120)
    st.sidebar.text('------------------------------------------')
  
    recommendation=st.button('Recommend Book')
    index=np.where(pivot_table.index==book)[0][0]
    distances,suggestion=model.kneighbors(pivot_table.iloc[index,:].values.reshape(1,-1),n_neighbors=6)
    with st.spinner():
      if (recommendation is not False):
        book1,book2,book3,book4,book5=pivot_table.index[suggestion[0][1:]]
        col1,col2, col3, col4, col5= st.columns(5)
        with col1:
          st.markdown('**{}**'.format(book1))
          url=image[image['Book-Title']==book1]['Image-URL-L'].values[0]
          im2=Image.open(requests.get(url, stream=True).raw)
          st.image(im2)
    
        with col2:
          st.markdown('**{}**'.format(book2))
          url=image[image['Book-Title']==book2]['Image-URL-L'].values[0]
          im2=Image.open(requests.get(url, stream=True).raw)
          st.image(im2)
    

        with col3:
          st.markdown('**{}**'.format(book3))
          url=image[image['Book-Title']==book3]['Image-URL-L'].values[0]
          im2=Image.open(requests.get(url, stream=True).raw)
          st.image(im2)
    
    
        with col4: 
          st.markdown('**{}**'.format(book4))
          url=image[image['Book-Title']==book4]['Image-URL-L'].values[0]
          im2=Image.open(requests.get(url, stream=True).raw)     
          st.image(im2)
   
  
        with col5:  
          st.markdown('**{}**'.format(book5))
          url=image[image['Book-Title']==book5]['Image-URL-L'].values[0]
          im2=Image.open(requests.get(url, stream=True).raw) 
          st.image(im2)

