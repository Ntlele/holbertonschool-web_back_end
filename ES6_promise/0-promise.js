export default function getResponseFromAPI() {
  return new Promise(function (resolve, reject) {
    resolve('success')
    reject('failed')
  })
}
