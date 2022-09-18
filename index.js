const name = 'Gilang Dwi Rahadian';

function myName(strings, ...values){
    return strings.reduce((result, str, i) => `${result}${str}${values[0]}`);
}

const str = myName`halo, namaku adalah ${name}`;
console.log(str);
alert(str);