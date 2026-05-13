const axios = require('axios');

const API_URL = process.env.API_URL || 'http://api-gateway:3000';

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

    console.log('\n=== Order Service Tests ===\n');

    await test('GET /orders returns orders list', async () => {
        const res = await axios.get(`${API_URL}/orders`);
        if (!res.data || !res.data.orders) throw new Error('No orders field');
    });

    await test('POST /orders creates a new order', async () => {
        const res = await axios.post(`${API_URL}/orders`, {
            product: 'Test Product',
            quantity: 2,
            total: 29.99
        });
        if (!res.data) throw new Error('No response data');
    });

    await test('PUT /orders/:id updates an order', async () => {
        const res = await axios.put(`${API_URL}/orders/1`, {
            status: 'completed'
        });
        if (!res.data) throw new Error('No response data');
    });

    await test('DELETE /orders/:id deletes an order', async () => {
        const res = await axios.delete(`${API_URL}/orders/1`);
        if (!res.data) throw new Error('No response data');
    });

    console.log(`\nResults: ${passed} passed, ${failed} failed out of ${passed + failed} tests\n`);
    process.exit(failed > 0 ? 1 : 0);
}

runTests();