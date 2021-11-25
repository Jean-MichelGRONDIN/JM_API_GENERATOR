export interface $DTO_STRUC_NAME$ {
$DTO_STRUC_FIELDS$
}

export const $DTO_FUNC_NAME$ = (req: Request): Promise<$DTO_STRUC_NAME$|ErrorDataFromRequest> => {
    return new Promise($DTO_ASYNC_PLACEHOLDER$(resolve, reject) => {
        var obj: LooseObject = {}
$DTO_FUNC_RETRIEVES$

        resolve(obj as $DTO_STRUC_NAME$);
    });
};

$DTO_PLACEHOLDER$