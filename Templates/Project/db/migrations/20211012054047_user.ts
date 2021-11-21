import { Knex } from "knex";

export async function up(knex: Knex): Promise<void> {
    return knex.schema.createTable('user', table => {
        table.uuid('id').primary().notNullable().defaultTo(knex.raw("gen_random_uuid()"));
        table.string('firstname');
        table.string('lastname');
        table.string('email');
        table.string('password');
    })
}

export async function down(knex: Knex): Promise<void> {
    return knex.schema.dropTable('user')
}

