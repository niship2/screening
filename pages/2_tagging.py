import pandas as pd
import streamlit as st


st.set_page_config(page_title="Tagging", page_icon="🌍")
st.markdown("# タグ付与")


def check(state):
    st.write(state)


with st.sidebar:
    st.selectbox("付与方法",["通常","RAG"])

    st.markdown("---")
    st.write("付与したいタグの指定") 

  
    
    if st.button("読み込み"):
        tag_df = pd.read_table('temptag.tsv')
        #st.session_state.my_key = tag_df.to_dict(orient="index")
    else:
        st.write(st.session_state.my_key)
        tag_df = pd.DataFrame.from_dict(st.session_state.my_key).T

        

    #st.write(tag_df)
    #add = st.session_state.my_key["edited_rows"]
    #edt = st.session_state.my_key["added_rows"]

    #tag_df = pd.concat([pd.DataFrame(add).T,pd.DataFrame(edt)])

    #st.write(tag_df)
    #if not "タグ名" in tag_df.columns.tolist():
    #    tag_df["タグ名"] = ""#old_tag_df["タグ名"]
    #if not "タグの説明" in tag_df.columns.tolist():
    #    tag_df["タグの説明"] = ""#old_tag_df["タグの説明"]

    #st.write(tag_df.columns.tolist())
    #st.write(pd.DataFrame(st.session_state.my_key["edited_rows"]).T)
    #st.write(pd.DataFrame(st.session_state.my_key["added_rows"],columns=["","3"]))        

    #tempdict = {}
    #tempdict["edited_rows"] = tag_df.to_dict(orient="index")
    #st.session_state.my_key = tempdict
    edited = st.data_editor(tag_df,key="my_key",num_rows= "dynamic",hide_index=True,use_container_width=True)

    #st.write(edited)
    edited2 = pd.DataFrame.from_dict(st.session_state.my_key["edited_rows"]).T
    edited3 = pd.DataFrame.from_dict(st.session_state.my_key["added_rows"])
    #st.write(st.session_state.my_key)
    if st.button("保存"):
        pd.concat([edited2,edited3]).to_csv("./temptag.tsv",sep="\t",index=None)
        st.info("保存しました")
    
    #st.session_state.edited_rows = st.session_state.my_key["edited_rows"]
    #st.session_state.added_rows = st.session_state.my_key["added_rows"]
    #st.write(st.session_state.added_rows)