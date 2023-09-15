import { useQuery } from "@tanstack/react-query";
import axios from "axios";

const getFormById = async (formId: string): Promise<any> => {
  const { data } = await axios.get(
    `http://127.0.0.1:8000/api/visitor/${formId}`
  );
  return data;
};

export default function useGetForm(formId: string) {
  return useQuery({
    queryKey: ["form", formId],
    queryFn: () => getFormById(formId),
    enabled: !!formId,
  });
}
