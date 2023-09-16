import axios from "axios";
import { VisitorAnswerType, visitorAuthCheckType } from "./types";

export async function getFormById(formId: string): Promise<any> {
  const { data } = await axios.get(
    `http://127.0.0.1:8000/api/visitor/form/${formId}`
  );
  return data;
}

export async function checkVisitorAuth(
  visitorData: visitorAuthCheckType
): Promise<any> {
  const { data } = await axios.post(
    "http://127.0.0.1:8000/api/visitor/auth/",
    visitorData
  );
  return data;
}

export async function createVisitorAnswer(
  answerData: VisitorAnswerType
): Promise<any> {
  const { data } = await axios.post(
    "http://127.0.0.1:8000/api/visitor/answer/create/",
    answerData
  );
  return data;
}
