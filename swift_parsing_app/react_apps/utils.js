export function truncate(str, max) {
    return str.length > max ? str.substr(0, max - 1) + '…' : str;
}

export const requestConfig = {
    headers: {
        // 'x-auth-token': token,
        'Content-Type': 'application/json',
    },
    timeout: 5000,
};