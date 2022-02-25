export const $ACTION_ACTION_NAME$ = ($ACTION_DTO_CALL_BLOCK_PLACE$): Promise<$ACTION_ACTION_RETURN_TYPE$> => {
    return new Promise(async (resolve, reject) => {
        let res: $ACTION_MODEL_NAME$|undefined = await knex('$ACTION_TABLE_NAME$').where({
$ACTION_WHERE_FIELDS$
            'deleted_at': null
        }).first();
        if (res == undefined){
            resolve(newErrorDB("Action id not found"));
        } else {
            resolve(res);
        }
    });
}

$ACTION_PLACEHOLDER$