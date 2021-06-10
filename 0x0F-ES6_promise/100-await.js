import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let responsePhoto;
  let responseUser;
  try {
    responsePhoto = await uploadPhoto();
    responseUser = await createUser();
  } catch (e) {
    responsePhoto = null;
    responseUser = null;
  }
  return { photo: responsePhoto, user: responseUser };
}
