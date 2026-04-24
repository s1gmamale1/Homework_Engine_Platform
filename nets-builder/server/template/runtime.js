/**
 * NETS_AI — Runtime tutor bridge.
 * Loaded by the homework HTML when served by the backend (not standalone).
 * Exposes window.NETS_AI with 4 async methods mirroring /api/ai/* endpoints.
 *
 * The homework template should call these from its answer-check paths.
 */
(function() {
    // Detect if we're running inside the NETS backend (has /api routes available)
    // vs standalone file:// — fall back to no-AI mode gracefully.
    const isBackendHosted = window.location.protocol !== 'file:'
                         && window.location.origin
                         && !window.location.origin.startsWith('null');

    // Subject/grade injected by backend into the page (via data attributes on <body> or a global).
    // Fallback to safe defaults if missing.
    const ctx = window.NETS_CTX || {};

    const API_BASE = (ctx.apiBase || '') + '/api/ai';

    async function _post(path, body) {
        if (!isBackendHosted) {
            return { _offline: true, correct: null, feedback: 'AI tutor not available offline.' };
        }
        try {
            const res = await fetch(API_BASE + path, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(body),
            });
            if (!res.ok) {
                const err = await res.json().catch(() => ({}));
                return { _error: true, message: err.detail?.error || res.statusText };
            }
            return await res.json();
        } catch (e) {
            return { _error: true, message: String(e) };
        }
    }

    /**
     * Check a typed answer semantically.
     * Use when exact string match against ans[] fails but you want to give partial credit.
     * @param {Object} opts
     * @param {string} opts.question - The question text
     * @param {string} opts.studentAnswer - What the student typed
     * @param {string[]} opts.expectedAnswers - The accepted answers from ans[]
     * @param {string} opts.tier - "EASY" | "MEDIUM" | "HARD"
     * @param {string} [opts.context] - Optional extra context (e.g., recent flashcards)
     * @returns {Promise<{correct, score, feedback, matched_expected}>}
     */
    async function checkAnswer(opts) {
        return _post('/check-answer', {
            question: opts.question,
            student_answer: opts.studentAnswer,
            expected_answers: opts.expectedAnswers || [],
            subject: ctx.subject || 'math-algebra',
            grade: ctx.grade || 8,
            tier: opts.tier || 'MEDIUM',
            context: opts.context || null,
        });
    }

    /**
     * Boss combat turn. Call on every boss answer submission.
     * @param {Object} opts
     * @param {string} opts.bossQuestion
     * @param {string} opts.studentAnswer
     * @param {string[]} opts.expectedAnswers
     * @param {number} opts.damageValue - base damage for this question
     * @param {number} opts.hpRemaining - boss HP remaining
     * @param {number} opts.attemptNumber - 1 for first try, 2 for retry, etc
     * @returns {Promise<{correct, damage_dealt, boss_response, hint, score}>}
     */
    async function bossTurn(opts) {
        return _post('/boss-turn', {
            boss_question: opts.bossQuestion,
            student_answer: opts.studentAnswer,
            expected_answers: opts.expectedAnswers || [],
            damage_value: opts.damageValue || 10,
            hp_remaining: opts.hpRemaining || 100,
            attempt_number: opts.attemptNumber || 1,
            subject: ctx.subject || 'math-algebra',
            grade: ctx.grade || 8,
        });
    }

    /**
     * Get personalized reflection feedback.
     * @param {Object} opts
     * @param {string} opts.studentReflection
     * @param {Object} opts.performance - {correct, total, time_minutes, weak_phase}
     * @returns {Promise<{feedback, next_steps, encouragement}>}
     */
    async function reflectionFeedback(opts) {
        return _post('/reflection', {
            homework_title: ctx.homeworkTitle || '',
            homework_summary: ctx.homeworkSummary || '',
            student_reflection: opts.studentReflection,
            performance: opts.performance || {},
            subject: ctx.subject || 'math-algebra',
            grade: ctx.grade || 8,
        });
    }

    /**
     * General tutor help. Use for open-ended questions, "I'm stuck" prompts, etc.
     * @param {Object} opts
     * @param {string} opts.phase - current phase name
     * @param {string} opts.question
     * @param {string} opts.studentInput
     * @param {string} [opts.context]
     * @returns {Promise<{response, guidance_type}>}
     */
    async function tutor(opts) {
        return _post('/tutor', {
            phase: opts.phase,
            question: opts.question,
            student_input: opts.studentInput,
            subject: ctx.subject || 'math-algebra',
            grade: ctx.grade || 8,
            context: opts.context || null,
        });
    }

    // Convenience: check if AI is available right now
    function isAvailable() { return isBackendHosted; }

    // Expose
    window.NETS_AI = {
        checkAnswer,
        bossTurn,
        reflectionFeedback,
        tutor,
        isAvailable,
        _ctx: ctx,
    };

    // Log readiness once
    console.log('[NETS_AI] ready. Available:', isAvailable(), 'Context:', ctx);
})();
