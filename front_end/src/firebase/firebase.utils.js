
import firebase from 'firebase/compat/app';
import 'firebase/compat/firestore';
import 'firebase/compat/auth';

const config = {
    apiKey: "AIzaSyDp2TGQNAfQt8oK-tC2ajp3AqpheGxtZjc",
    authDomain: "crwn-db-18fce.firebaseapp.com",
    projectId: "crwn-db-18fce",
    storageBucket: "crwn-db-18fce.appspot.com",
    messagingSenderId: "448029270290",
    appId: "1:448029270290:web:c281f5a4b93e304c1193cb",
    measurementId: "G-1R3FVQY648"
  };

 export const createUserProfileDocument = async (userAuth, displayName,  ...additionalData) => {
    if (!userAuth) return;
    // createUserProfileDocument(user, 'merry', 34, 'asdfasd') // additionalData = [34, 'asdfasd']
    const userRef = firestore.doc(`users/${userAuth.uid}`)
    const snapShot = await userRef.get();
 
    if(!snapShot.exists) {
       const { email} = userAuth;
       const createdAt = new Date();

       try {
           await userRef.set({
             displayName: displayName,
             email,
             createdAt,
             ...additionalData
           })
       }catch (error) {
          console.log('error at creating user', error.message)
       }
    }
    return userRef;
  };


firebase.initializeApp(config);

export const auth = firebase.auth();
export const firestore = firebase.firestore();

const provider = new firebase.auth.GoogleAuthProvider();
provider.setCustomParameters({ prompt: 'select_account'});
export const signInWithGoogle = () => auth.signInWithPopup(provider);

export default firebase;