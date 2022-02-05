import * as nodeFs from 'node:fs'
import * as nodeStream from 'node:stream'
import * as nodeUtil from 'node:util'
import fetch from 'node-fetch'
import { Request } from 'node-fetch'
import fs from 'fs'

const url = 'http://0.0.0.0:61111'
// let testRequest = new Request(url + '/sts_post/', {
//     method: 'post',
//     headers: {
//         'Content-Type': 'application/json;charset=utf-8;'
//     },
//     body: JSON.stringify({aa: 1})
// })
// fetch(testRequest).then(response => {
//     let result = response.text()
//     result.then(res => {
//         console.log(res)
//     })
// })

//// Here’s a code snippet translating a string in UTF8 encoding to base64:
/// const encoded = Buffer.from('username:password', 'utf8').toString('base64')  
////

//// Here’s a code snippet translating a base64-encoded string to UTF8:
/// const plain = Buffer.from('dXNlcm5hbWU6cGFzc3dvcmQ=', 'base64').toString('utf8')
///

/// encoder
/// let buff = fs.readFileSync('stack-abuse-logo.png');
/// let base64data = buff.toString('base64');
///
/// return "data:image/gif;base64,"+fs.readFileSync(file, 'base64');
///

////  decoder
/// let buff = new Buffer(data, 'base64');
/// fs.writeFileSync('stack-abuse-logo-out.png', buff);
///
//storage/lol/test/nodejs/octocat.png

const body = {
	field1: '1',
	aaa: '1',
	bbb: 8 ,
	imgg: "data:image/gif;base64,"+fs.readFileSync("/storage/lol/test/nodejs/octocat.png", 'base64')
};
const response = await fetch(url + '/ttt/', {
	method: 'post',
	body: JSON.stringify(body),
	headers: {'Content-Type': 'application/json'}
});

const data = await response.json()

// data.imgg=data.imgg.replace("data:image/gif;base64,","");
// let buff = new Buffer.from(data.imgg, 'base64')
// fs.writeFileSync('1.png', buff)


console.log(data);

// const streamPipeline = nodeUtil.promisify(nodeStream.pipeline);

// const response = await fetch('https://github.githubassets.com/images/modules/logos_page/Octocat.png');

// if (!response.ok) throw new Error(`unexpected response ${response.statusText}`);

// await streamPipeline(response.body, nodeFs.createWriteStream('./octocat.png'));