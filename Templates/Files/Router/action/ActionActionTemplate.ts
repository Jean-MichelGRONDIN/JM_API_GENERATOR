export const createActionAction = (data: actionCreateData): Promise<null|ErrorDB> => {
    return new Promise(async (resolve, reject) => {
        await knex('actions')
            .insert({
                creator_id: data.creator_id,
                workspace_id: data.workspace_id,
                title: data.title,
            })
            .catch(function(error: Error) {
                reject(new ErrorDB(error));
            });
        resolve(null);
    });
}

$ACTION_PLACEHOLDER$