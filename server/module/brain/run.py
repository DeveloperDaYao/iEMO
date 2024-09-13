import gradio as gr
from chat_his import output_history
import send

def sentence_builder(text):
    res = send.chat(text)
    t = f"""user：{text} \n assistant：{res}"""
    output_history.add(t)
    return output_history.text(False)

demo = gr.Interface(
    sentence_builder,
    inputs=[
        gr.Textbox(label="iEMO", info="这是一个儿童陪伴助手。请你扮演10岁以下的儿童和它对话。")
    ],
    outputs=["text"],
)



if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0")