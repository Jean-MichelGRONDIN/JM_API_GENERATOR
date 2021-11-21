import API_APPINESS from "./src/config/config";
import path from 'path'

module.exports = {
  development: {
    client: "pg",
    connection: {
      database: API_APPINESS.API.getInstance().Database.Database,
      user: API_APPINESS.API.getInstance().Database.User,
      password: API_APPINESS.API.getInstance().Database.Password,
      port: API_APPINESS.API.getInstance().Database.Port
    },
    pool: {
      min: 2,
      max: 10
    },
    migrations: {
      directory: path.resolve(__dirname, 'db/migrations'),
    },
    seeds: {
      directory: path.resolve(__dirname, 'db/seeds'),
    },
  },
  production: {
    client: "pg",
    connection: {
      database: API_APPINESS.API.getInstance().Database.Database,
      user: API_APPINESS.API.getInstance().Database.User,
      password: API_APPINESS.API.getInstance().Database.Password,
      port: API_APPINESS.API.getInstance().Database.Port
    },
    pool: {
      min: 2,
      max: 10
    },
    migrations: {
      directory: path.resolve(__dirname, 'db/prod_migrations'),
    },
    seeds: {
      directory: path.resolve(__dirname, 'db/prod_seeds'),
    },
  }  
};

// staging: {
//   client: "pg",
//   connection: {
//     database: "my_db",
//     user: "username",
//     password: "password"
//   },
//   pool: {
//     min: 2,
//     max: 10
//   },
//   migrations: {
//     tableName: "knex_migrations"
//   }
// },

// production: {
//   client: "pg",
//   connection: {
//     database: "my_db",
//     user: "username",
//     password: "password"
//   },
//   pool: {
//     min: 2,
//     max: 10
//   },
//   migrations: {
//     tableName: "knex_migrations"
//   }
// }