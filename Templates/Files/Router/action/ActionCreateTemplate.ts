export interface $ACTION_CUSTOM_RET_TYPE$ {
    id: string
}

export const $ACTION_ACTION_NAME$ = ($ACTION_DTO_CALL_BLOCK_PLACE$): Promise<$ACTION_ACTION_RETURN_TYPE$> => {
    return new Promise(async (resolve, reject) => {
        try {
            let newlyCreatedId: (string|undefined) = await knex('$ACTION_TABLE_NAME$').insert({
$ACTION_DB_ACTION_FIELDS$
            })
            .returning('id');
            resolve({ id: newlyCreatedId } as $ACTION_CUSTOM_RET_TYPE$);
        } catch (error: any) {
            resolve(new ErrorDB(error));
        }
    });
}

$ACTION_PLACEHOLDER$