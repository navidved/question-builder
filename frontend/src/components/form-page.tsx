import {
  Stack,
  Typography,
  Button,
  Box,
  TextField,
  Checkbox,
  FormGroup,
  FormControlLabel,
  RadioGroup,
  Radio,
} from "@mui/material";
import { useParams } from "react-router-dom";

import {
  useCheckVisitorAuth,
  useCreateVisitorAnswer,
  useGetForm,
  useUpdateVisitorAnswer,
} from "../api/hooks";
import { useFormStore } from "../store/formStore";
import AuthCheck from "./auth-check";
import { useAuthCheckStore } from "../store/authStore";
import { useVisitorAnswerState } from "../store/visitorAnswerStore";

export default function FormPage() {
  let params = useParams();

  let { formId } = params;

  if (formId == undefined) return null;

  const formItem = useFormStore((state) => state.formItem);
  const nextFormItem = useFormStore((state) => state.nextFormItem);
  const previousFormItem = useFormStore((state) => state.previousFormItem);
  const startForm = useFormStore((state) => state.startForm);

  const formAuthValue = useAuthCheckStore((state) => state.formAuthValue);
  const setAuthError = useAuthCheckStore((state) => state.setAuthError);

  const visitorAnswer = useVisitorAnswerState((state) => state.visitorAnswer);
  const resetVisitorAnswer = useVisitorAnswerState(
    (state) => state.resetVisitorAnswer
  );
  const addVisitorAnswer = useVisitorAnswerState(
    (state) => state.AddVisitorAnswer
  );

  const { data: formData, isFetching } = useGetForm(formId);
  const { mutate: checkVisitor, data: visitorAuthResponse } =
    useCheckVisitorAuth();
  const { mutate: createAnswer } = useCreateVisitorAnswer();
  const { mutate: updateAnswer } = useUpdateVisitorAnswer();

  function handleStart() {
    const visitorCheckData = {
      form_id: formData?.id,
      auth_type: formData?.auth_method,
      auth_value: formAuthValue,
    };
    checkVisitor(visitorCheckData, {
      onSuccess: () => {
        startForm();

        // navigate(`${formItem}`);
      },
      onError: () => {
        setAuthError(true);
      },
    });
  }

  function handleNext() {
    const visitorAnswerData = {
      visitor_id: visitorAuthResponse ? visitorAuthResponse?.visitor_id : null,
      form_id: visitorAuthResponse
        ? visitorAuthResponse?.form_id
        : formData?.id,
      form_item_id: formData?.form_items
        ? formData?.form_items[formItem]?.id
        : null,
      answer_type: formData?.form_items
        ? formData?.form_items[formItem]?.answer_type
        : null,
      answer: visitorAnswer,
    };
    const newVisitorAnswerData = {
      answer_type: formData?.form_items
        ? formData?.form_items[formItem]?.answer_type
        : null,
      answer: visitorAnswer,
    };
    const answerExists = visitorAuthResponse?.visitor_answers.find(
      (item) => item.form_item_id == form_items[formItem]?.id
    );
    answerExists == undefined
      ? createAnswer(visitorAnswerData, {
          onSuccess: () => {
            nextFormItem(formItem);
            resetVisitorAnswer();
          },
          onError: () => {
            console.log("There is an error");
          },
        })
      : updateAnswer(
          { newAnswerData: newVisitorAnswerData, answerId: answerExists?.id },
          {
            onSuccess: () => {
              nextFormItem(formItem);
              resetVisitorAnswer();
            },
            onError: () => {
              console.log("There is an error");
            },
          }
        );
  }
  function handlePrevious() {
    previousFormItem(formItem);
  }

  if (isFetching) return "Loading...";
  const { form_items, auth_method, title } = formData;

  return (
    <Stack justifyContent="space-between" height="50vh">
      {formItem >= form_items.length ? (
        <Typography variant="h2" textAlign="center" mt={20}>
          آفرین 😁
        </Typography>
      ) : (
        <>
          <Stack justifyContent="start" spacing={8} direction="column">
            <Typography variant="h4">{title}</Typography>
            {formItem == -1 ? (
              <AuthCheck auth_method={auth_method} />
            ) : (
              <Box
                sx={{
                  display: "flex",
                  flexDirection: "column",
                  justifyContent: "center",
                  alignItems: "start",
                  gap: "10px",
                  marginTop: "40px",
                }}
              >
                <Typography variant="h5">
                  {form_items[formItem].title}
                </Typography>
                {form_items[formItem].answer_type == "text" && (
                  <>
                    <Typography>{form_items[formItem].description}</Typography>
                    <TextField
                      onChange={(e) =>
                        addVisitorAnswer("text", e.target.value, visitorAnswer)
                      }
                      fullWidth
                      placeholder={form_items[formItem].options["text"]}
                      multiline
                      rows={4}
                    />
                  </>
                )}
                {form_items[formItem].answer_type == "multi-choice" && (
                  <>
                    <Typography>{form_items[formItem].description}</Typography>
                    <FormGroup>
                      {form_items[formItem].options["multi-choice"].map(
                        (item: string) => (
                          <FormControlLabel
                            control={
                              <Checkbox
                                name={item}
                                onChange={(e) =>
                                  addVisitorAnswer(
                                    "multi-choice",
                                    e.target.value,
                                    visitorAnswer
                                  )
                                }
                              />
                            }
                            label={item}
                            value={item}
                          />
                        )
                      )}
                    </FormGroup>
                  </>
                )}
                {form_items[formItem].answer_type == "single-choice" && (
                  <>
                    <Typography>{form_items[formItem].description}</Typography>
                    <FormGroup>
                      <RadioGroup
                        onChange={(e) =>
                          addVisitorAnswer(
                            "single-choice",
                            e.target.value,
                            visitorAnswer
                          )
                        }
                      >
                        {form_items[formItem].options["single-choice"].map(
                          (item: string) => (
                            <FormControlLabel
                              control={<Radio />}
                              label={item}
                              value={item}
                              key={item}
                            />
                          )
                        )}
                      </RadioGroup>
                    </FormGroup>
                  </>
                )}
              </Box>
            )}
          </Stack>
          <Box
            sx={{
              display: "flex",
              justifyContent: "center",
              alignItems: "center",
              gap: "10px",
              marginTop: "40px",
            }}
          >
            {formItem == -1 ? (
              <Button
                onClick={() => handleStart()}
                variant="contained"
                sx={{ width: "25%", borderRadius: "12px", fontSize: "20px" }}
              >
                شروع
              </Button>
            ) : (
              <Box
                sx={{
                  display: "flex",
                  justifyContent: "center",
                  alignItems: "center",
                  gap: "10px",
                  marginTop: "40px",
                }}
              >
                <Button
                  variant="contained"
                  sx={{
                    width: "content-fit",
                    borderRadius: "12px",
                    fontSize: "20px",
                  }}
                  onClick={() => handleNext()}
                  disabled={formItem == form_items.length - 1}
                >
                  مرحله بعد
                </Button>
                <Button
                  variant="contained"
                  sx={{
                    width: "content-fit",
                    borderRadius: "12px",
                    fontSize: "20px",
                  }}
                  onClick={() => handlePrevious()}
                  disabled={formItem == 0}
                >
                  مرحله قبل
                </Button>
                <Button
                  variant="contained"
                  sx={{
                    width: "content-fit",
                    borderRadius: "12px",
                    fontSize: "20px",
                  }}
                  onClick={() => handleNext()}
                >
                  ذخیره سازی و ارسال
                </Button>
              </Box>
            )}
          </Box>
        </>
      )}
    </Stack>
  );
}
