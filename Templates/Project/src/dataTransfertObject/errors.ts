export class ErrorDataFromRequest {
    public constructor(err: Error) {
        this.error = err
        this.message = err.message
    }
    error: Error
    public message: string
}

export let newErrorDataFromRequest = (msg: string): ErrorDataFromRequest => {
    return new ErrorDataFromRequest(new Error(msg))
}