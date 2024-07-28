import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const myPromise = Promise.all([uploadPhoto(), createUser()]).then(
    ([result1, result2]) => {
      const myBody = result1.body;
      const myName = result2.firstName;
      const myLast = result2.lastName;

      console.log(`${myBody} ${myName} ${myLast}`);
    },
  ).catch(() => {
    console.log('Signup system offline');
  });

  return myPromise;
}
