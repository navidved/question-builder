import { useMutation, useQuery } from "@tanstack/react-query";
import {
  checkVisitorAuth,
  createVisitorAnswer,
  getFormById,
  updateVisitorAnswer,
} from "./utils";

export function useGetForm(formId: string) {
  return useQuery({
    queryKey: ["form", formId],
    queryFn: () => getFormById(formId),
    enabled: !!formId,
  });
}

export function useCheckVisitorAuth() {
  return useMutation(checkVisitorAuth);
}

export function useCreateVisitorAnswer() {
  return useMutation(createVisitorAnswer);
}

export function useUpdateVisitorAnswer() {
  return useMutation(updateVisitorAnswer);
}
