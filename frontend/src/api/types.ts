export type QuestionAnswerType = {
  "multi-choice": string[];
  "radio-button": string;
  text: string;
};

export type VisitorAnswerType = {
  visitor: number;
  form: number;
  form_item: number;
  answer: QuestionAnswerType;
};

export type visitorAuthCheckType = {
  form: number;
  auth_type: string;
  auth_value: string;
};
