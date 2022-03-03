var AWS = require('aws-sdk'),
    region = "ap-south-1",
    secretName = "arn:aws:secretsmanager:ap-south-1:872436821098:secret:webd/secret_url-Y9oQwV",
    secret,
    decodedBinarySecret;

var client = new AWS.SecretsManager({
    region: region
});

client.getSecretValue({SecretId: secretName}, function(err, data) {
    if (err) {
        if (err.code === 'DecryptionFailureException')
            throw err;
        else if (err.code === 'InternalServiceErrorException')
            throw err;
        else if (err.code === 'InvalidParameterException')
            throw err;
        else if (err.code === 'InvalidRequestException')
            throw err;
        else if (err.code === 'ResourceNotFoundException')
            throw err;
    }
    else {
        if ('SecretString' in data) {
            const secret = data.SecretString;
            var parsedSecret = JSON.parse(secret);
        } else {
            let buff = new Buffer(data.SecretBinary, 'base64');
            decodedBinarySecret = buff.toString('ascii');
            var parsedSecret = JSON.parse(decodedBinarySecret);
        }
    }
    console.log(parsedSecret["MONGO_URL"]);
    console.log(parsedSecret);
});