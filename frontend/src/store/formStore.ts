import { create } from "zustand";
type FormState = {
  formItem: number;
};

type FormAction = {
  nextFormItem: (formItem: FormState["formItem"]) => void;
  previousFormItem: (formItem: FormState["formItem"]) => void;
  startForm: () => void;
};

export const useFormStore = create<FormState & FormAction>((set) => ({
  formItem: -1,
  nextFormItem: (formItem) => set(() => ({ formItem: formItem + 1 })),
  previousFormItem: (formItem) => set(() => ({ formItem: formItem - 1 })),
  startForm: () => set(() => ({ formItem: 0 })),
}));
