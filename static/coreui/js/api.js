
async function apiFetch(url, options = {}) {
    const token = localStorage.getItem("access_token");

    // Add authentication and default headers
    const headers = {
        "Content-Type": "application/json",
        ...options.headers,
    };

    if (token) {
        headers["Authorization"] = `Bearer ${token}`;
    }

    const response = await fetch(url, {
        ...options,
        headers,
    });

    if (!response.ok) {
        throw new Error(`HTTP error: ${response.status}`);
    }
    if (response.status === 204) {
        return null;
    }

    return response.json();
}
