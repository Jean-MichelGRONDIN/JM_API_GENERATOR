export interface $ACTION_CUSTOM_RET_TYPE$ {
    action_list: $ACTION_MODEL_NAME$[],
    count: number,
}

export const $ACTION_ACTION_NAME$ = ($ACTION_DTO_CALL_BLOCK_PLACE$): Promise<$ACTION_ACTION_RETURN_TYPE$> => {
    return new Promise(async (resolve, reject) => {
        try {
            let res = await knex.select("*").from("$ACTION_TABLE_NAME$").where({
$ACTION_WHERE_FIELDS$
                'deleted_at': null
            });
            const tab: $ACTION_MODEL_NAME$[] = Array.from(res, (value, _) => value as $ACTION_MODEL_NAME$);
            resolve({action_list: tab, count: tab.length} as $ACTION_CUSTOM_RET_TYPE$);
        } catch (error: any) {
            resolve(new ErrorDB(error));
        }
    });
}

$ACTION_PLACEHOLDER$