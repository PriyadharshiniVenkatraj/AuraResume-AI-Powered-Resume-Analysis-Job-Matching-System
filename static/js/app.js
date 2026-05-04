document.addEventListener('DOMContentLoaded', () => {

    // --- File Upload UI ---
    const fileInput = document.getElementById('resume');
    const fileNameDisplay = document.getElementById('file-name-display');

    if (fileInput && fileNameDisplay) {
        fileInput.addEventListener('change', (e) => {
            if (e.target.files.length > 0) {
                fileNameDisplay.textContent = e.target.files[0].name;
            } else {
                fileNameDisplay.textContent = 'Click to browse or drag file here';
            }
        });
    }

    // --- Analysis Form Submission ---
    const analyzeForm = document.getElementById('analyze-form');
    if (analyzeForm) {
        analyzeForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            
            const btn = document.getElementById('analyze-btn');
            const btnText = btn.querySelector('.btn-text');
            const spinner = btn.querySelector('.spinner');
            const resultsContainer = document.getElementById('results-container');
            
            // UI Loading state
            btn.disabled = true;
            btnText.textContent = 'Analyzing...';
            spinner.classList.remove('hidden');
            resultsContainer.classList.add('hidden');

            const formData = new FormData(analyzeForm);

            try {
                const response = await fetch('/api/analyze', {
                    method: 'POST',
                    body: formData
                });
                
                const data = await response.json();
                
                if (!response.ok) {
                    throw new Error(data.error || 'Server error occurred');
                }

                // Populate Results
                document.getElementById('res-score').textContent = `${data.match_percentage}%`;
                setTimeout(() => {
                    document.getElementById('res-progress').style.width = `${data.match_percentage}%`;
                }, 100);

                document.getElementById('res-name').textContent = data.extracted_info.name || 'Unknown';
                document.getElementById('res-email').textContent = data.extracted_info.email || 'None found';
                document.getElementById('res-phone').textContent = data.extracted_info.phone || 'None found';

                // Populate Skills
                const matchedContainer = document.getElementById('res-matched');
                const missingContainer = document.getElementById('res-missing');
                
                matchedContainer.innerHTML = '';
                missingContainer.innerHTML = '';

                if (data.matched_skills.length === 0) matchedContainer.innerHTML = '<span class="text-muted">None</span>';
                data.matched_skills.forEach(skill => {
                    matchedContainer.innerHTML += `<div class="tag match">${skill}</div>`;
                });

                if (data.missing_skills.length === 0) missingContainer.innerHTML = '<span class="text-muted">None</span>';
                data.missing_skills.forEach(skill => {
                    missingContainer.innerHTML += `<div class="tag miss">${skill}</div>`;
                });

                // Show results
                resultsContainer.classList.remove('hidden');

            } catch (err) {
                alert(`Error: ${err.message}`);
            } finally {
                // Reset UI
                btn.disabled = false;
                btnText.textContent = 'Analyze Candidate';
                spinner.classList.add('hidden');
            }
        });
    }

    // --- History Page Loading ---
    const historyBody = document.getElementById('history-body');
    if (historyBody) {
        fetch('/api/history')
            .then(res => res.json())
            .then(data => {
                historyBody.innerHTML = '';
                
                if (data.length === 0) {
                    historyBody.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--text-muted); padding: 3rem;">No candidates analyzed yet.</td></tr>`;
                    return;
                }

                data.forEach(item => {
                    const row = document.createElement('tr');
                    
                    // Parse matched array strings safely
                    let matchedSkills = '';
                    try {
                        const skills = JSON.parse(item.matched.replace(/'/g, '"'));
                        matchedSkills = skills.map(s => `<span class="tag match" style="padding: 2px 8px; font-size: 0.75rem;">${s}</span>`).join('');
                    } catch(e) {
                        matchedSkills = item.matched;
                    }

                    row.innerHTML = `
                        <td>
                            <div style="font-weight: 500">${item.name || 'Unknown'}</div>
                        </td>
                        <td>
                            <div style="color: var(--text-muted); font-size: 0.9rem">${item.email || '-'}</div>
                            <div style="color: var(--text-muted); font-size: 0.9rem">${item.phone || '-'}</div>
                        </td>
                        <td>
                            <div style="font-weight: 700; color: ${item.match_score > 50 ? 'var(--success)' : 'var(--text-primary)'}">
                                ${item.match_score}%
                            </div>
                        </td>
                        <td>
                            <div class="tag-container" style="gap: 4px;">${matchedSkills}</div>
                        </td>
                    `;
                    historyBody.appendChild(row);
                });
            })
            .catch(err => {
                historyBody.innerHTML = `<tr><td colspan="4" style="text-align: center; color: var(--danger);">Failed to load history</td></tr>`;
                console.error(err);
            });
    }

});
