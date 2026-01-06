const axios = require('axios');

const base = 'http://localhost:3000/api/employees';

async function run() {
  try {
    console.log('GET /employees');
    let res = await axios.get(base);
    console.log(res.data);

    console.log('POST /employees');
    res = await axios.post(base, { id: '99', name: 'Test User', email: 'test@example.com', gender: 'other' });
    console.log(res.data);

    console.log('GET /employees/99');
    res = await axios.get(base + '/99');
    console.log(res.data);

    console.log('PUT /employees/99');
    res = await axios.put(base + '/99', { name: 'Test User Updated', email: 'test2@example.com', gender: 'male' });
    console.log(res.data);

    console.log('DELETE /employees/99');
    res = await axios.delete(base + '/99');
    console.log(res.data);

    console.log('Final GET /employees');
    res = await axios.get(base);
    console.log(res.data);
  } catch (err) {
    console.error(err.response ? err.response.data : err.message);
  }
}

run();
