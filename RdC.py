import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Read and Complete Exercise", layout="centered")

st.markdown("## 📘 Read and Complete Exercise")

# ---------- INPUT TEXT AREA ----------
st.markdown("### Paste your text here")

user_text = st.text_area(
    "",
    height=180,
    placeholder=(
        "Haru likes to take camping trips in the summer.\n"
        "He d_____s into the mountains and goes h_____g in the woods.\n"
        "He l____s in the city, so he is g____ to g__ into n_____e when he can.\n"
        "His favorite part is sleeping under the stars."
    )
)

generate = st.button("🔁 Convert to exercise")

# ---------- RENDER FUNCTION ----------
def render_exercise(text):
    html = ""

    for char in text:
        if char == "_":
            html += """
            <input type="text" maxlength="1" class="letter"/>
            """
        else:
            if char == "\n":
                html += "<br>"
            elif char == " ":
                html += "&nbsp;"
            else:
                html += f"<span class='text-char'>{char}</span>"

    components.html(
        f"""
        <style>
            .letter {{
                width: 22px;
                height: 30px;
                font-size: 16px;
                text-align: center;
                border-radius: 6px;
                border: 2px solid #bbb;
                margin: 0 1px;
                background-color: transparent;
                color: white;
                outline: none;
                display: inline-block;
                vertical-align: middle;
            }}

            .text-char {{
                color: white;
            }}
        </style>

        <div id="exercise" style="
            font-size: 18px;
            line-height: 2.2;
            font-family: system-ui, sans-serif;
            max-width: 900px;
            margin-top: 20px;

            white-space: nowrap;
            overflow-x: auto;
        ">
            {html}
        </div>

        <script>
            const inputs = Array.from(document.querySelectorAll("#exercise input"));

            inputs.forEach((input, index) => {{
                input.addEventListener("input", () => {{
                    if (input.value.length === 1 && index < inputs.length - 1) {{
                        inputs[index + 1].focus();
                    }}
                }});

                input.addEventListener("keydown", (e) => {{
                    if (e.key === "ArrowRight" && index < inputs.length - 1) {{
                        inputs[index + 1].focus();
                    }}

                    if (e.key === "ArrowLeft" && index > 0) {{
                        inputs[index - 1].focus();
                    }}

                    if (e.key === "Backspace" && input.value === "" && index > 0) {{
                        inputs[index - 1].focus();
                    }}
                }});
            }});
        </script>
        """,
        height=360,
    )

# ---------- OUTPUT ----------
if generate and user_text.strip():
    st.markdown("### ✏️ Exercise")
    render_exercise(user_text)
