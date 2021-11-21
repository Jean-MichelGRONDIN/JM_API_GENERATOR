## NODE SCRIPT (those cmds run on windows, linux and mac)

# Create migration file

_This commande will create a migration file inside **db/migrations** ._

```
npm run make-migrate [FILE NAME]
```

```js
export async function up(knex: Knex): Promise<void> {
    /* Create your schema */
}

export async function down(knex: Knex): Promise<void> {
    /* Drop your schema */
}
```

# Exec migration files

_This commande will exec all migrations files inside **db/migrations** ._

```
npm run migrate [MODE="development or production"]
```

```js
export async function up(knex: Knex): Promise<void> {
    return knex.schema.createTable('user', table => {
        table.uuid('id').primary().notNullable().defaultTo(uuidv4());
        table.string('firstname');
        table.string('lastname');
        table.string('email');
        table.string('password');
    });
}

export async function down(knex: Knex): Promise<void> {
    return knex.schema.dropTable('user');
}
```

# Drop the latest migration

_This commande will drop the leatest migration file inside **db/migrations** ._

```
npm run migrate-rollback [MODE="development or production"]
```

# Create seed file

_This commande will create a migration file inside **db/seeds** ._

```
npm run make-seed [FILE NAME]
```

```js
export async function seed(knex: Knex): Promise<void> {
    // Deletes ALL existing entries
    await knex('table_name').del();

    // Inserts seed entries
    await knex('table_name').insert([
        { id: 1, colName: 'rowValue1' },
        { id: 2, colName: 'rowValue2' },
        { id: 3, colName: 'rowValue3' }
    ]);
}
```

# Exec seeds files

_This commande will exec all seeds files inside **db/seeds** ._

```
npm run seed
```

```js
export async function seed(knex: Knex): Promise<void> {
    // Deletes ALL existing entries
    await knex('user').del();

    // Inserts seed entries
    await knex('user').insert([
        {
            firstname: 'madi',
            lastname: 'abdillah',
            email: 'abdillah@epitech.eu'
        }
    ]);
}
```

## MAKEFILE RULES (those cmds run on linux and mac)

# Run the API with logs

```
make api-dev-log
```

# Run the API in background

```
make api-dev
```

# Stop the that runnig in background

```
make api-dev-down
```

# Run unit test

```
make api-test
```

# Create migration file

_This commande will create a migration file inside **db/migrations** ._

```
make create-migrate NAME=[FILE NAME]
```

```js
export async function up(knex: Knex): Promise<void> {
    /* Create your schema */
}

export async function down(knex: Knex): Promise<void> {
    /* Drop your schema */
}
```

# Exec migration files

_This commande will exec all migrations files inside **db/migrations** ._

```
make migrate MODE=["development or production"]
```

```js
export async function up(knex: Knex): Promise<void> {
    return knex.schema.createTable('user', table => {
        table.uuid('id').primary().notNullable().defaultTo(uuidv4());
        table.string('firstname');
        table.string('lastname');
        table.string('email');
        table.string('password');
    });
}

export async function down(knex: Knex): Promise<void> {
    return knex.schema.dropTable('user');
}
```

# Drop the latest migration

_This commande will drop the leatest migration file inside **db/migrations** ._

```
make migrate-rollback MODE=["development or production"]
```

# Create seed file

_This commande will create a migration file inside **db/seeds** ._

```
make create-seed NAME=[FILE NAME]
```

```js
export async function seed(knex: Knex): Promise<void> {
    // Deletes ALL existing entries
    await knex('table_name').del();

    // Inserts seed entries
    await knex('table_name').insert([
        { id: 1, colName: 'rowValue1' },
        { id: 2, colName: 'rowValue2' },
        { id: 3, colName: 'rowValue3' }
    ]);
}
```

# Exec seeds files

_This commande will exec all seeds files inside **db/seeds** ._

```
make seed
```

```js
export async function seed(knex: Knex): Promise<void> {
    // Deletes ALL existing entries
    await knex('user').del();

    // Inserts seed entries
    await knex('user').insert([
        {
            firstname: 'madi',
            lastname: 'abdillah',
            email: 'abdillah@epitech.eu'
        }
    ]);
}
```

# Create backup file

_This commande will retrieve all data inside the current db and will create a SQL file inside **db/backup** ._

```
make api-backup
```

```sql
INSERT INTO public."user" VALUES ('e6cf3c12-ffc8-4914-8bee-0f522c015a87', 'madi', 'abdillah', 'abdillah@epitech.eu', NULL);
```
