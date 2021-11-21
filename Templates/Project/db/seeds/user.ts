import { Knex } from "knex";

export async function seed(knex: Knex): Promise<void> {
    // Deletes ALL existing entries
    await knex("user").del();

    // Inserts seed entries
    await knex("user").insert([
        { firstname: "madi", lastname: "abdillah", email: "abdillah@epitech.eu" },
    ]);
};
