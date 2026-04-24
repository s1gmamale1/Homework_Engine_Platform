// frontend/js/editors/games/sentence-fill.js
// Sentence Fill editor for production game break.
// Contract storage currently maps this game to content_json.gb_why_chain:
// { q, inv, reprompts[] }

(function () {
  "use strict";

  window.GameBreakEditors = window.GameBreakEditors || {};

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

  function normalize(items) {
    return Array.isArray(items)
      ? items.map((item) => ({
          q: item?.q || "",
          inv: item?.inv || "",
          reprompts: Array.isArray(item?.reprompts) && item.reprompts.length ? item.reprompts : [""],
        }))
      : [];
  }

  function makeItem() {
    return {
      q: "",
      inv: "",
      reprompts: [""],
    };
  }

  function emit(state, onChange) {
    state.forEach((item) => {
      if (!Array.isArray(item.reprompts) || !item.reprompts.length) item.reprompts = [""];
    });
    onChange(clone(state));
  }

  function renderReprompts(item) {
    return item.reprompts
      .map(
        (reprompt, repromptIndex) => `
          <div class="option-row" data-reprompt-index="${repromptIndex}">
            <input class="js-reprompt" type="text" value="${escapeHtml(reprompt)}" placeholder="Hint / reprompt ${repromptIndex + 1}" />
            <button class="icon-btn js-remove-reprompt" type="button" title="Remove reprompt">×</button>
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
          <section class="editor-card nested-card">
            <div class="editor-header compact-header">
              <div>
                <p class="eyebrow">Sentence Fill</p>
                <h3>${state.length} cloze prompt${state.length === 1 ? "" : "s"}</h3>
              </div>
              <button class="btn btn-primary js-add-item" type="button">Add cloze prompt</button>
            </div>
            <p class="muted-text">
              Use a blank in the prompt, for example <strong>43 × 20 = 43 × ___ × 10</strong>. The expected answer goes in <strong>inv</strong>.
            </p>
          </section>

          ${
            state.length
              ? state
                  .map(
                    (item, index) => `
                      <section class="editor-card nested-card" data-index="${index}">
                        <div class="editor-header compact-header">
                          <div>
                            <p class="eyebrow">Cloze ${index + 1}</p>
                            <h3>${escapeHtml(stripHtml(item.q) || "Untitled cloze prompt")}</h3>
                          </div>
                          <button class="btn btn-danger js-remove-item" type="button">Remove</button>
                        </div>

                        <div class="editor-grid">
                          <label class="field full-span">
                            <span>Prompt with blank</span>
                            <div class="js-rich-host" data-key="q" data-index="${index}"></div>
                          </label>

                          <label class="field full-span">
                            <span>Correct answer / invariant</span>
                            <input class="js-field" data-key="inv" type="text" value="${escapeHtml(item.inv)}" placeholder="20 = 2 × 10" />
                          </label>
                        </div>

                        <div class="editor-card nested-card">
                          <div class="editor-header compact-header">
                            <div>
                              <p class="eyebrow">Reprompts</p>
                              <h3>${item.reprompts.length} hint${item.reprompts.length === 1 ? "" : "s"}</h3>
                            </div>
                            <button class="btn btn-ghost js-add-reprompt" type="button">Add reprompt</button>
                          </div>
                          <div class="editor-list">
                            ${renderReprompts(item)}
                          </div>
                        </div>
                      </section>
                    `
                  )
                  .join("")
              : `<div class="empty-state glass-card inline-empty">
                  <div class="empty-orb" aria-hidden="true">🧩</div>
                  <h3>No cloze prompts</h3>
                  <p>Add sentence-fill prompts for contextual recall.</p>
                  <button class="btn btn-primary js-add-item" type="button">Add first cloze prompt</button>
                </div>`
          }
        </div>
      `;

      // Mount RichField editors for `q` (cloze prompt).
      if (window.RichField) {
        container.querySelectorAll(".js-rich-host").forEach((host) => {
          const index = Number(host.dataset.index);
          const key = host.dataset.key;
          if (!Number.isFinite(index) || !key) return;
          const initial = state[index] ? state[index][key] : "";
          const mini = window.RichField.create({
            value: initial || "",
            placeholder: "Bo'shliqni to'ldiring: 43 × 20 = 43 × ___ × 10",
            compact: true,
            onChange: (html) => {
              if (!state[index]) return;
              state[index][key] = html;
              emit(state, onChange);
            },
          });
          host.appendChild(mini);
        });
      }
    }

    container.oninput = (event) => {
      const field = event.target.closest(".js-field");
      const reprompt = event.target.closest(".js-reprompt");

      if (field) {
        const index = Number(field.closest("[data-index]")?.dataset.index);
        state[index][field.dataset.key] = field.value;
        emit(state, onChange);
        return;
      }

      if (reprompt) {
        const itemIndex = Number(reprompt.closest("[data-index]")?.dataset.index);
        const repromptIndex = Number(reprompt.closest("[data-reprompt-index]")?.dataset.repromptIndex);
        state[itemIndex].reprompts[repromptIndex] = reprompt.value;
        emit(state, onChange);
      }
    };

    container.onclick = (event) => {
      if (event.target.closest(".js-add-item")) {
        state.push(makeItem());
        emit(state, onChange);
        repaint();
        return;
      }

      if (event.target.closest(".js-remove-item")) {
        const index = Number(event.target.closest("[data-index]")?.dataset.index);
        state.splice(index, 1);
        emit(state, onChange);
        repaint();
        return;
      }

      if (event.target.closest(".js-add-reprompt")) {
        const index = Number(event.target.closest("[data-index]")?.dataset.index);
        state[index].reprompts.push("");
        emit(state, onChange);
        repaint();
        return;
      }

      if (event.target.closest(".js-remove-reprompt")) {
        const itemIndex = Number(event.target.closest("[data-index]")?.dataset.index);
        const repromptIndex = Number(event.target.closest("[data-reprompt-index]")?.dataset.repromptIndex);
        state[itemIndex].reprompts.splice(repromptIndex, 1);
        if (!state[itemIndex].reprompts.length) state[itemIndex].reprompts.push("");
        emit(state, onChange);
        repaint();
      }
    };

    repaint();
    if (window.EditorUtils) {
      window.EditorUtils.bindPasteNormalizer(container);
      window.EditorUtils.bindStrictPasteNormalizer(
        container,
        'input.js-field[data-key="inv"]'
      );
    }
  }

  window.GameBreakEditors.sentenceFill = { render };
})();
