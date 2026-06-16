import gradio as gr


def greet(name):
    return f"Hello {name}! Bienvenue sur l'application de recommandation de repas."


demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="Hello World - Recommandation de repas",
)

if __name__ == "__main__":
    demo.launch()
