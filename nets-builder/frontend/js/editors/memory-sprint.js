// frontend/js/editors/memory-sprint.js
// Memory Sprint editor: edits content_json.memory_sprint.

(function () {
  "use strict";

  window.Editors = window.Editors || {};

  const TYPES = [
    { value: "KO", label: "Ko'p variantli" },
    { value: "TF", label: "To'g'ri / Noto'g'ri" },
    { value: "YNNG", label: "Ha / Yo'q / Ma'lum emas" },
  ];

  function escapeHtml(value) {
    return String(value ?? "")
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#039;");
  }

  function stripHtml(value) {
    return String(value ?? "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
  }

  function clone(value) {
    return JSON.parse(JSON.stringify(value ?? []));
  }

  function defaultOptions(type) {
    if (type === "TF") return ["To'g'ri", "Noto'g'ri"];
    if (type === "YNNG") return ["Ha", "Yo'q", "Ma'lum emas"];
    return ["", "", "", ""];
  }

  function normalizeQuestion(question) {
    const type = ["KO", "TF", "YNNG"].includes(question?.type) ? question.type : "KO";
    const options = Array.isArray(question?.options) && question.options.length ? question.options : defaultOptions(type);
    const maxIndex = Math.max(0, options.length - 1);
    const parsedCorrect = Number(question?.correct);
    const correct = Number.isFinite(parsedCorrect) ? Math.min(Math.max(Math.trunc(parsedCorrect), 0), maxIndex) : 0;

    return {
      type,
      prompt: question?.prompt || "",
      subtitle: question?.subtitle || "",
      tags: question?.tags || "[Bloom: L1 | PISA: L1]",
      explain: question?.explain || "",
      options,
      correct,
    };
  }

  function normalize(data) {
    return Array.isArray(data) ? data.map(normalizeQuestion) : [];
  }

  function makeQuestion() {
    return normalizeQuestion({ type: "KO" });
  }

  function emit(state, onChange) {
    onChange(clone(state));
  }

  function renderTypeOptions(active) {
    return TYPES.map(
      (type) => `<option value="${type.value}" ${type.value === active ? "selected" : ""}>${escapeHtml(type.label)}</option>`
    ).join("");
  }

  function renderCorrectOptions(options, correct) {
    return options
      .map(
        (option, index) =>
          `<option value="${index}" ${index === correct ? "selected" : ""}>${index + 1}. ${escapeHtml(option || "Empty option")}</option>`
      )
      .join("");
  }

  function renderOptionInputs(question) {
    return question.options
      .map(
        (option, optionIndex) => `
          <div class="option-row" data-option-index="${optionIndex}">
            <input class="js-option" type="text" value="${escapeHtml(option)}" placeholder="Option ${optionIndex + 1}" ${
              question.type === "TF" || question.type === "YNNG" ? "readonly" : ""
            } />
            ${
              question.type === "KO"
                ? `<button class="icon-btn js-remove-option" type="button" title="Remove option">×</button>`
                : ""
            }
          </div>
        `
      )
      .join("");
  }

  function render(container, data, onChange) {
    const state = normalize(data);

    function repaint() {
      container.innerHTML = `
        <div class="editor-list">
          <section class="editor-card">
            <div class="editor-header">
              <div>
                <p class="eyebrow">Memory Sprint</p>
                <h3>${state.length} question${state.length === 1 ? "" : "s"}</h3>
              </div>
              <button class="btn btn-primary js-add-question" type="button">Add question</button>
            </div>
            <p class="muted-text">
              correct is a 0-based index into options. Tags must stay like <strong>[Bloom: L1 | PISA: L1]</strong>.
            </p>
          </section>

          ${
            state.length
              ? state
                  .map(
                    (question, index) => `
                      <section class="editor-card" data-index="${index}">
                        <div class="editor-header">
                          <div>
                            <p class="eyebrow">Question ${index + 1}</p>
                            <h3>${escapeHtml(stripHtml(question.prompt) || "Untitled question")}</h3>
                          </div>
                          <button class="btn btn-danger js-remove-question" type="button">Remove</button>
                        </div>

                        <div class="editor-grid">
                          <label class="field">
                            <span>Type</span>
                            <select class="js-type">
                              ${renderTypeOptions(question.type)}
                            </select>
                          </label>

                          <label class="field">
                            <span>Correct answer</span>
                            <select class="js-correct">
                              ${renderCorrectOptions(question.options, question.correct)}
                            </select>
                          </label>

                          <label class="field full-span">
                            <span>Prompt</span>
                            <div class="js-rich-host" data-key="prompt" data-index="${index}"></div>
                          </label>

                          <label class="field full-span">
                            <span>Subtitle</span>
                            <input class="js-field" data-key="subtitle" type="text" value="${escapeHtml(question.subtitle)}" placeholder="Optional subtitle" />
                          </label>

                          <label class="field">
                            <span>Tags</span>
                            <input class="js-field" data-key="tags" type="text" value="${escapeHtml(question.tags)}" />
                          </label>

                          <label class="field full-span">
                            <span>Explanation</span>
                            <div class="js-rich-host" data-key="explain" data-index="${index}"></div>
                          </label>
                        </div>

                        <div class="editor-card nested-card">
                          <div class="editor-header compact-header">
                            <div>
                              <p class="eyebrow">Options</p>
                              <h3>${question.options.length} option${question.options.length === 1 ? "" : "s"}</h3>
                            </div>
                            ${question.type === "KO" ? `<button class="btn btn-ghost js-add-option" type="button">Add option</button>` : ""}
                          </div>
                          <div class="editor-list">
                            ${renderOptionInputs(question)}
                          </div>
                        </div>
                      </section>
                    `
                  )
                  .join("")
              : `<div class="empty-state glass-card inline-empty">
                  <div class="empty-orb" aria-hidden="true">⚡</div>
                  <h3>No sprint questions yet</h3>
                  <p>Add quick recall questions for the memory sprint stage.</p>
                  <button class="btn btn-primary js-add-question" type="button">Add first question</button>
                </div>`
          }
        </div>
      `;

      // Mount RichField editors for `prompt` and `explain`.
      if (window.RichField) {
        container.querySelectorAll(".js-rich-host").forEach((host) => {
          const index = Number(host.dataset.index);
          const key = host.dataset.key;
          if (!Number.isFinite(index) || !key) return;
          const initial = state[index] ? state[index][key] : "";
          const placeholder = key === "prompt" ? "Question prompt..." : "Why this answer is correct...";
          const mini = window.RichField.create({
            value: initial || "",
            placeholder,
            compact: true,
            onChange: (html) => {
              if (!state[index]) return;
              state[index][key] = html;
              syncAndEmit();
            },
          });
          host.appendChild(mini);
        });
      }
    }

    function syncAndEmit() {
      state.forEach((question) => {
        if (question.correct >= question.options.length) question.correct = 0;
      });
      emit(state, onChange);
    }

    container.oninput = (event) => {
      const field = event.target.closest(".js-field");
      const option = event.target.closest(".js-option");

      if (field) {
        const index = Number(field.closest("[data-index]")?.dataset.index);
        state[index][field.dataset.key] = field.value;
        syncAndEmit();
        return;
      }

      if (option && !option.readOnly) {
        const questionIndex = Number(option.closest("[data-index]")?.dataset.index);
        const optionIndex = Number(option.closest("[data-option-index]")?.dataset.optionIndex);
        state[questionIndex].options[optionIndex] = option.value;
        syncAndEmit();
      }
    };

    container.onchange = (event) => {
      const typeSelect = event.target.closest(".js-type");
      const correctSelect = event.target.closest(".js-correct");

      if (typeSelect) {
        const index = Number(typeSelect.closest("[data-index]")?.dataset.index);
        const nextType = typeSelect.value;
        state[index].type = nextType;
        state[index].options = defaultOptions(nextType);
        state[index].correct = 0;
        syncAndEmit();
        repaint();
        return;
      }

      if (correctSelect) {
        const index = Number(correctSelect.closest("[data-index]")?.dataset.index);
        state[index].correct = Number(correctSelect.value);
        syncAndEmit();
      }
    };

    container.onclick = (event) => {
      if (event.target.closest(".js-add-question")) {
        state.push(makeQuestion());
        syncAndEmit();
        repaint();
        return;
      }

      if (event.target.closest(".js-remove-question")) {
        const index = Number(event.target.closest("[data-index]")?.dataset.index);
        state.splice(index, 1);
        syncAndEmit();
        repaint();
        return;
      }

      if (event.target.closest(".js-add-option")) {
        const index = Number(event.target.closest("[data-index]")?.dataset.index);
        state[index].options.push("");
        syncAndEmit();
        repaint();
        return;
      }

      if (event.target.closest(".js-remove-option")) {
        const questionIndex = Number(event.target.closest("[data-index]")?.dataset.index);
        const optionIndex = Number(event.target.closest("[data-option-index]")?.dataset.optionIndex);
        state[questionIndex].options.splice(optionIndex, 1);

        if (!state[questionIndex].options.length) {
          state[questionIndex].options.push("");
        }

        syncAndEmit();
        repaint();
      }
    };

    repaint();
    if (window.EditorUtils) {
      window.EditorUtils.bindPasteNormalizer(container);
      window.EditorUtils.bindStrictPasteNormalizer(container, 'input[data-key="tags"]');
    }
  }

  window.Editors.memorySprint = { render };
})();
