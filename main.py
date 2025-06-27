import streamlit as st
from router.controller import route_query
from rag.rag_handler import query_vector_db
from llms.mistral import query_mistral
from llms.codelama import query_codelama
from response.builder import build_final_response

def handle_query(user_input):
    # Decide which model/tool to use
    route = route_query(user_input)
    
    # Display route
    st.info(f"🔀 Route decided: **{route}**")

    # Handle according to route
    if route == "RAG":
        context = query_vector_db(user_input)
        llm_input = (
            f"You are an assistant answering based only on provided context.\n"
            f"Context:\n{context}\n"
            f"Question: {user_input}\n"
            f"Answer:"
        )
        llm_output = query_mistral(llm_input)
    elif route == "MODEL:CODELAMA":
        llm_output = query_codelama(user_input)
    else:
        llm_output = query_mistral(user_input)

    final_response = build_final_response(llm_output)
    return final_response

def main():
    st.set_page_config(page_title="🧠 Hybrid LLM Router with RAG", page_icon="🌟")
    st.title("🌟 Hybrid LLM Router with RAG")
    st.write("Ask me anything! Your query will be routed to the best model automatically. 🚀")

    with st.form("query_form"):
        user_input = st.text_area("📝 **Enter your query:**", height=150, placeholder="Type your question here...")
        submitted = st.form_submit_button("Submit")

    if submitted and user_input.strip():
        with st.spinner("Processing your query..."):
            final_response = handle_query(user_input.strip())
            st.success("✅ **Response:**")
            st.write(final_response)

    st.markdown("---")
    st.caption("👋 Type `exit` in the console version to quit. Here, just close the tab! 🖖")

if __name__ == "__main__":
    main()
