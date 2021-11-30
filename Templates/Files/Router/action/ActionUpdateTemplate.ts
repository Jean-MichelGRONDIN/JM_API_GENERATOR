export const $ACTION_ACTION_NAME$ = (data: $ACTION_DTO_TYPE$): Promise<$ACTION_ACTION_RETURN_TYPE$> => {
    return new Promise(async (resolve, reject) => {
        await knex('$ACTION_TABLE_NAME$').where({
$ACTION_WHERE_FIELDS$
            'deleted_at': null
        })
        .update({
$ACTION_DB_ACTION_FIELDS$
        })
        .catch(function(error: Error) {
            reject(new ErrorDB(error));
        });
        resolve(null);
    });
}

$ACTION_PLACEHOLDER$