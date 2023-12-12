from tensorflow.keras.layers import TextVectorization

input_text=str(st.text_area("write here : "))

vectorizer = TextVectorization(max_tokens=MAX_FEATURES,
                               output_sequence_length=1800,
                               output_mode='int')

input_text = vectorizer(np.array([input_text]))
res = model.predict(input_text)

res=(res > 0.5).astype(int)
s=["toxic",	"severe_toxic",	"obscene",	"threat",	"insult",	"identity_hate"]
for i in len(res[0]):
  if res[0][i] ==1:
    st.write(s[i])