import axios from "axios";
import {
  UpdatedVisitorAnswerType,
  VisitorAnswerType,
  VisitorAuthCheckType,
} from "./types";

export async function getFormById(formId: string): Promise<any> {
  const { data } = await axios.get(
    `http://127.0.0.1:8000/api/visitor/form/${formId}`
  );
  return data;
}

export async function checkVisitorAuth(
  visitorData: VisitorAuthCheckType
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

export async function updateVisitorAnswer({
  newAnswerData,
  answerId,
}: {
  newAnswerData: UpdatedVisitorAnswerType;
  answerId: string;
}): Promise<any> {
  const { data } = await axios.patch(
    `http://127.0.0.1:8000/api/visitor/answer/update/${answerId}/`,
    newAnswerData
  );
  return data;
}
