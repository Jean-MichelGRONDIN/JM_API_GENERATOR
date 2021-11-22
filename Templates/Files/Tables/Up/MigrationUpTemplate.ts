    .createTable('$MIGRATION_TABLE_NAME$', table => {
        table.uuid('id').primary().notNullable().defaultTo(knex.raw("gen_random_uuid()"));

        table.timestamp('created_at').notNullable().defaultTo(knex.fn.now());
        table.timestamp('updated_at').notNullable().defaultTo(knex.fn.now());
        table.timestamp('deleted_at').defaultTo(null);
    })