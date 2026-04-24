// frontend/js/editors/games/adaptive-quiz.js
// Adaptive Quiz game editor.
// Based on production contract shape: { q, tags, tier, ans[], capture }.

(function () {
  "use strict";

  window.GameBreakEditors = window.GameBreakEditors || {};

  const TIERS = ["EASY", "MEDIUM", "HARD"];

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
          tags: item?.tags || "[Bloom: L1 | PISA: L1]",
          tier: TIERS.includes(item?.tier) ? item.tier : "EASY",
          ans: Array.isArray(item?.ans) && item.ans.length ? item.ans : [""],
          capture: Boolean(item?.capture),
        }))
      : [];
  }

  function makeItem() {
    return {
      q: "",
      tags: "[Bloom: L1 | PISA: L1]",
      tier: "EASY",
      ans: [""],
      capture: false,
    };
  }

  function emit(state, onChange) {
    state.forEach((item) => {
      if (!Array.isArray(item.ans) || !item.ans.length) item.ans = [""];
      if (!TIERS.includes(item.tier)) item.tier = "EASY";
    });
    onChange(clone(state));
  }

  function renderTierOptions(active) {
    return TIERS.map(
      (tier) => `<option value="${tier}" ${tier === active ? "selected" : ""}>${tier}</option>`
    ).join("");
  }

  function renderAnswers(item) {
    return item.ans
      .map(
        (ans, ansIndex) => `
          <div class="option-row" data-ans-index="${ansIndex}">
            <input class="js-answer" type="text" value="${escapeHtml(ans)}" placeholder="Accepted answer ${ansIndex + 1}" />
            <button class="icon-btn js-remove-answer" type="button" title="Remove answer">×</button>
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
                <p class="eyebrow">Adaptive Quiz</p>
                <h3>${state.length} question${state.length === 1 ? "" : "s"}</h3>
              </div>
              <button class="btn btn-primary js-add-item" type="button">Add question</button>
            </div>
            <p class="muted-text">
              Student types an answer. Correctness checks against <strong>ans[]</strong>. Capture can require notebook/photo confirmation.
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
                            <p class="eyebrow">Question ${index + 1}</p>
                            <h3>${escapeHtml(stripHtml(item.q) || "Untitled adaptive question")}</h3>
                          </div>
                          <button class="btn btn-danger js-remove-item" type="button">Remove</button>
                        </div>

                        <div class="editor-grid">
                          <label class="field full-span">
                            <span>Question</span>
                            <div class="js-rich-host" data-key="q" data-index="${index}"></div>
                          </label>

                          <label class="field">
                            <span>Tier</span>
                            <select class="js-field" data-key="tier">
                              ${renderTierOptions(item.tier)}
                            </select>
                          </label>

                          <label class="field">
                            <span>Capture</span>
                            <select class="js-capture">
                              <option value="false" ${!item.capture ? "selected" : ""}>false</option>
                              <option value="true" ${item.capture ? "selected" : ""}>true</option>
                            </select>
                          </label>

                          <label class="field full-span">
                            <span>Tags</span>
                            <input class="js-field" data-key="tags" type="text" value="${escapeHtml(item.tags)}" />
                          </label>
                        </div>

                        <div class="editor-card nested-card">
                          <div class="editor-header compact-header">
                            <div>
                              <p class="eyebrow">Accepted answers</p>
                              <h3>${item.ans.length} answer${item.ans.length === 1 ? "" : "s"}</h3>
                            </div>
                            <button class="btn btn-ghost js-add-answer" type="button">Add answer</button>
                          </div>
                          <div class="editor-list">
                            ${renderAnswers(item)}
                          </div>
                        </div>
                      </section>
                    `
                  )
                  .join("")
              : `<div class="empty-state glass-card inline-empty">
                  <div class="empty-orb" aria-hidden="true">🎯</div>
                  <h3>No adaptive questions</h3>
                  <p>Add apply-level questions with accepted answers.</p>
                  <button class="btn btn-primary js-add-item" type="button">Add first question</button>
                </div>`
          }
        </div>
      `;

      // Mount RichField editors for `q` (adaptive quiz question).
      if (window.RichField) {
        container.querySelectorAll(".js-rich-host").forEach((host) => {
          const index = Number(host.dataset.index);
          const key = host.dataset.key;
          if (!Number.isFinite(index) || !key) return;
          const initial = state[index] ? state[index][key] : "";
          const mini = window.RichField.create({
            value: initial || "",
            placeholder: "43 × 20 ni hisoblang.",
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
      const answer = event.target.closest(".js-answer");

      if (field) {
        const index = Number(field.closest("[data-index]")?.dataset.index);
        state[index][field.dataset.key] = field.value;
        emit(state, onChange);
        return;
      }

      if (answer) {
        const itemIndex = Number(answer.closest("[data-index]")?.dataset.index);
        const ansIndex = Number(answer.closest("[data-ans-index]")?.dataset.ansIndex);
        state[itemIndex].ans[ansIndex] = answer.value;
        emit(state, onChange);
      }
    };

    container.onchange = (event) => {
      const capture = event.target.closest(".js-capture");

      if (capture) {
        const index = Number(capture.closest("[data-index]")?.dataset.index);
        state[index].capture = capture.value === "true";
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

      if (event.target.closest(".js-add-answer")) {
        const index = Number(event.target.closest("[data-index]")?.dataset.index);
        state[index].ans.push("");
        emit(state, onChange);
        repaint();
        return;
      }

      if (event.target.closest(".js-remove-answer")) {
        const itemIndex = Number(event.target.closest("[data-index]")?.dataset.index);
        const ansIndex = Number(event.target.closest("[data-ans-index]")?.dataset.ansIndex);
        state[itemIndex].ans.splice(ansIndex, 1);
        if (!state[itemIndex].ans.length) state[itemIndex].ans.push("");
        emit(state, onChange);
        repaint();
      }
    };

    repaint();
    if (window.EditorUtils) {
      window.EditorUtils.bindPasteNormalizer(container);
      window.EditorUtils.bindStrictPasteNormalizer(
        container,
        'input[data-key="tags"], input.js-answer'
      );
    }
  }

  window.GameBreakEditors.adaptiveQuiz = { render };
})();
