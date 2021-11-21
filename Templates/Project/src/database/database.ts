import API_APPINESS from '../config/config';
import knex from 'knex';

const initknex = knex({
    client: 'pg',
    version: '13',
    connection: {
        host: API_APPINESS.API.getInstance().Database.Host,
        port: API_APPINESS.API.getInstance().Database.Port,
        user: API_APPINESS.API.getInstance().Database.User,
        password: API_APPINESS.API.getInstance().Database.Password,
        database: API_APPINESS.API.getInstance().Database.Database
    }
});

export default initknex