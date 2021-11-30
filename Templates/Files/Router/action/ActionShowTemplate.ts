export const $ACTION_ACTION_NAME$ = (data: $ACTION_DTO_TYPE$): Promise<$ACTION_ACTION_RETURN_TYPE$> => {
    return new Promise(async (resolve, reject) => {
        let res: $ACTION_MODEL_NAME$|undefined = await knex('actions').where({
            'id': data.action_id,
            'deleted_at': null
        }).first();
        if (res == undefined){
            reject(newErrorDB("Action id not found"));
        } else {
            resolve(res);
        }
    });
}

$ACTION_PLACEHOLDER$