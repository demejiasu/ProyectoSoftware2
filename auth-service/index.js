const express = require('express');
const app = express();

app.use(express.json());

app.post('/login', (req, res) => {
    const { email, password } = req.body;
    res.json({ 
        message: 'login ok', 
        user: { email: email || 'test@test.com' },
        token: 'fake-jwt-token-12345'
    });
});

app.post('/logout', (req, res) => {
    res.json({ message: 'logout ok' });
});

app.post('/recover', (req, res) => {
    const { email } = req.body;
    res.json({ 
        message: 'recovery email sent', 
        email: email || 'test@test.com' 
    });
});

app.listen(8000, () => console.log('Auth service running on port 8000'));