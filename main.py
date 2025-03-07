from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect(url_for("index"))
    return render_template("index.html", tasks=tasks, enumerate=enumerate)


@app.route("/delete/<int:task_id>")
def delete(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
