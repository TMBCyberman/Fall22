try {
    1 / 0; write-host 'hello, will i run after an error?'
}
catch {
    throw
}