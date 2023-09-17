export type QuestionAnswerType = {
  "multi-choice": string[];
  "single-choice": string;
  text: string;
};

export type VisitorAnswerType = {
  visitor: number;
  form: number;
  form_item: number;
  answer: QuestionAnswerType;
};

export type visitorAuthCheckType = {
  form_id: number;
  auth_type: string;
  auth_value: string;
};
