export interface $DTO_STRUC_NAME$ {
$DTO_STRUC_FIELDS$
}

export const $DTO_FUNC_NAME$ = (req: Request): $DTO_STRUC_NAME$ => {
    var obj: LooseObject = {}
$DTO_FUNC_RETRIEVES$

    return (obj as $DTO_STRUC_NAME$);
};

$DTO_PLACEHOLDER$