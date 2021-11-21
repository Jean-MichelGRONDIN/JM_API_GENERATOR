export class ErrorDB {
    public constructor(err: Error) {
        this.error = err
        this.message = err.message
    }
    error: Error
    public message: string
}

export let newErrorDB = (msg: string): ErrorDB => {
    return new ErrorDB(new Error(msg))
}