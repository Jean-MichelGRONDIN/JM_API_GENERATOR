import { Knex } from "knex";

export async function up(knex: Knex): Promise<void> {
    return knex.schema
$MIGRATION_UP$;
}

export async function down(knex: Knex): Promise<void> {
    return knex.schema
$MIGRATION_DOWN$;
}

