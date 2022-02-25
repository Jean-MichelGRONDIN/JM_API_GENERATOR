export const $ACTION_ACTION_NAME$ = (data: $ACTION_DTO_TYPE$): Promise<$ACTION_ACTION_RETURN_TYPE$> => {
    return new Promise(async (resolve, reject) => {
        await knex('$ACTION_TABLE_NAME$').where({
$ACTION_WHERE_FIELDS$
            'deleted_at': null
        })
        .update({
            deleted_at: knex.fn.now()
        })
        .catch(function(error: Error) {
            resolve(new ErrorDB(error));
        });
        resolve(null);
    });
}

$ACTION_PLACEHOLDER$