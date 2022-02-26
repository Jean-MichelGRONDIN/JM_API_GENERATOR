export const $ACTION_ACTION_NAME$ = ($ACTION_DTO_CALL_BLOCK_PLACE$): Promise<$ACTION_ACTION_RETURN_TYPE$> => {
    return new Promise(async (resolve, reject) => {
        try {
            await knex('$ACTION_TABLE_NAME$').where({
$ACTION_WHERE_FIELDS$
                'deleted_at': null
            })
            .update({
                deleted_at: knex.fn.now()
            });
            resolve(null);
        } catch (error: any) {
            resolve(new ErrorDB(error));
        }
    });
}

$ACTION_PLACEHOLDER$