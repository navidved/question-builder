// import {
//   Stack,
//   Typography,
//   Box,
//   TextField,
//   Checkbox,
//   FormGroup,
//   FormControlLabel,
//   RadioGroup,
//   Radio,
// } from "@mui/material";
// import { useParams } from "react-router-dom";

// const formItem = useFormStore((state) => state.formItem);
// const nextFormItem = useFormStore((state) => state.nextFormItem);
// const previousFormItem = useFormStore((state) => state.previousFormItem);
// const startForm = useFormStore((state) => state.startForm);

// export default function FormItemPage() {
//   let params = useParams();
//   let { formItem } = params;

//   if (formItem == undefined) return null;

//   return (
//     <Stack justifyContent="start" spacing={8} direction="column">
//       <Box
//         sx={{
//           display: "flex",
//           flexDirection: "column",
//           justifyContent: "center",
//           alignItems: "start",
//           gap: "10px",
//           marginTop: "40px",
//         }}
//       >
//         <Typography variant="h5">{form_items[formItem].title}</Typography>
//         {form_items[formItem].answer_type == "text" && (
//           <>
//             <Typography>{form_items[formItem].description}</Typography>
//             <TextField
//               onChange={(e) => handleAddAnswer("text", e.target.value)}
//               fullWidth
//               placeholder={
//                 visitorAuthResponse?.answer
//                   ? visitorAuthResponse?.answer[form_items[formItem].id]
//                   : form_items[formItem].options["text"]
//               }
//               multiline
//               rows={4}
//             />
//           </>
//         )}
//         {form_items[formItem].answer_type == "multi-choice" && (
//           <>
//             <Typography>{form_items[formItem].description}</Typography>
//             <FormGroup>
//               {form_items[formItem].options["multi-choice"].map(
//                 (item: string) => (
//                   <FormControlLabel
//                     control={
//                       <Checkbox
//                         name={item}
//                         onChange={(e) =>
//                           handleAddAnswer("multi-choice", e.target.value)
//                         }
//                       />
//                     }
//                     label={item}
//                     value={item}
//                   />
//                 )
//               )}
//             </FormGroup>
//           </>
//         )}
//         {form_items[formItem].answer_type == "single-choice" && (
//           <>
//             <Typography>{form_items[formItem].description}</Typography>
//             <FormGroup>
//               <RadioGroup
//                 onChange={(e) =>
//                   handleAddAnswer("single-choice", e.target.value)
//                 }
//               >
//                 {form_items[formItem].options["single-choice"].map(
//                   (item: string) => (
//                     <FormControlLabel
//                       control={<Radio />}
//                       label={item}
//                       value={item}
//                       key={item}
//                     />
//                   )
//                 )}
//               </RadioGroup>
//             </FormGroup>
//           </>
//         )}
//       </Box>
//     </Stack>
//   );
// }
