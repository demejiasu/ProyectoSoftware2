const axios = require('axios');

const API_URL = process.env.API_URL || 'http://localhost:3000';

async function runTests() {
    let passed = 0;
    let failed = 0;

    async function test(name, fn) {
        try {
            await fn();
            console.log(`✓ ${name}`);
            passed++;
        } catch (e) {
            console.log(`✗ ${name}: ${e.message}`);
            failed++;
        }
    }

    console.log('\n=== Api Gateway Tests ===\n');

    await test('Health check returns ok', async () => {
        const res = await axios.get(`${API_URL}/api/health`);
        if (res.data.status !== 'ok') throw new Error('Status not ok');
    });

    await test('GET /users returns JSON', async () => {
        const res = await axios.get(`${API_URL}/users`);
        if (!res.data) throw new Error('No data returned');
    });

    await test('GET /products returns JSON list', async () => {
        const res = await axios.get(`${API_URL}/products`);
        if (!Array.isArray(res.data)) throw new Error('Not an array');
    });

    await test('GET /orders returns JSON', async () => {
        const res = await axios.get(`${API_URL}/orders`);
        if (!res.data) throw new Error('No data returned');
    });

    await test('Login with valid credentials returns token', async () => {
        const res = await axios.post(`${API_URL}/auth/login`, {
            email: 'admin@test.com',
            password: 'admin123'
        });
        if (!res.data.success) throw new Error('Login failed');
        if (!res.data.token) throw new Error('No token returned');
    });

    await test('Login with invalid credentials returns 401', async () => {
        try {
            await axios.post(`${API_URL}/auth/login`, {
                email: 'wrong@test.com',
                password: 'wrong'
            });
            throw new Error('Should have failed');
        } catch (e) {
            if (e.response?.status !== 401) throw new Error('Wrong status: ' + e.response?.status);
        }
    });

    console.log(`\nResults: ${passed} passed, ${failed} failed out of ${passed + failed} tests\n`);
    process.exit(failed > 0 ? 1 : 0);
}

runTests();