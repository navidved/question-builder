export type QuestionAnswerType = {
  "multi-choice": string[];
  "single-choice": string;
  text: string;
};
export type AnswerKey = "multi-choice" | "single-choice" | "text";

export type VisitorAnswerType = {
  visitor_id: number | null;
  form_id: number | null;
  form_item_id: number | null;
  answer_type: AnswerKey;
  answer: QuestionAnswerType;
};

export type VisitorAuthCheckType = {
  form_id: number;
  auth_type: string;
  auth_value: string;
};

export type UpdatedVisitorAnswerType = {
  answer_type: AnswerKey;
  answer: QuestionAnswerType;
};
