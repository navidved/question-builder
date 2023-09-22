import { create } from "zustand";
import { AnswerKey, QuestionAnswerType } from "../api/types";

type AnswerState = {
  visitorAnswer: QuestionAnswerType;
};

type AnswerAction = {
  resetVisitorAnswer: () => void;
  AddVisitorAnswer: (
    key: AnswerKey,
    value: string,
    visitorAnswer: AnswerState["visitorAnswer"]
  ) => void;
};

export const useVisitorAnswerState = create<AnswerState & AnswerAction>(
  (set) => ({
    visitorAnswer: { "multi-choice": [], "single-choice": "", text: "" },
    resetVisitorAnswer: () =>
      set(() => ({
        visitorAnswer: { "multi-choice": [], "single-choice": "", text: "" },
      })),
    AddVisitorAnswer: (key, value, visitorAnswer) =>
      set(() => ({
        visitorAnswer:
          key == "multi-choice"
            ? {
                ...visitorAnswer,
                "multi-choice": visitorAnswer["multi-choice"].includes(value)
                  ? [...visitorAnswer["multi-choice"].filter((v) => v != value)]
                  : [
                      ...visitorAnswer["multi-choice"].filter(
                        (v) => v != value
                      ),
                      value,
                    ],
              }
            : { ...visitorAnswer, [key]: value },
      })),
  })
);
