export interface $DTO_STRUC_NAME$ {
    creator_id: string,
    workspace_id: string,
}

export const $DTO_FUNC_NAME$ = (req: Request): $DTO_STRUC_NAME$ => {
    var obj = {
        workspace_id: req.params.workspace_id,
        creator_id: User.getInstance()?.getUserID(),
        // @todo check que workspace exist && qu'il soit correcte
    };
    // @todo check if user has access to workspace

    return (obj as $DTO_STRUC_NAME$);
};