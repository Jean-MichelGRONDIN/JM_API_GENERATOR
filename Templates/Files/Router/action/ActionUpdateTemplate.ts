export const $ACTION_ACTION_NAME$ = (data: $ACTION_DTO_TYPE$): Promise<$ACTION_ACTION_RETURN_TYPE$> => {
    return new Promise(async (resolve, reject) => {
        await knex('actions').where({
            'id': data.action_id,
            'creator_id': data.creator_id,//@todo remove that one here
            'deleted_at': null
        })
        .update({
            title: data.title
        })
        .catch(function(error: Error) {
            reject(new ErrorDB(error));
        });
        resolve(null);
    });
}

$ACTION_PLACEHOLDER$