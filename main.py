import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + " "+ "!" * round(intensity) + str(intensity)

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

if __name__ == "__main":
    demo.launch()
