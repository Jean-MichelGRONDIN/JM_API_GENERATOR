export interface $ACTION_CUSTOM_RET_TYPE$ {
    action_list: $ACTION_MODEL_NAME$[],
    count: number,
}

export const $ACTION_ACTION_NAME$ = (data: $ACTION_DTO_TYPE$): Promise<$ACTION_ACTION_RETURN_TYPE$> => {
    return new Promise((resolve, reject) => {
        knex.select("*").from("$ACTION_TABLE_NAME$").where({
$ACTION_WHERE_FIELDS$
            'deleted_at': null
        })
        .then((res) => {
            const tab: $ACTION_MODEL_NAME$[] = Array.from(res, (value, _) => value as $ACTION_MODEL_NAME$);
            resolve({action_list: tab, count: tab.length} as $ACTION_CUSTOM_RET_TYPE$);
        }).catch(function(error: Error) {
            reject(new ErrorDB(error));
        });
    });
}

$ACTION_PLACEHOLDER$