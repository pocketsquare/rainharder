// import { Resend } from 'resend';

// // Enum for choosing email providers (future-proof)
// export const EmailProvider = {
//   RESEND: 'resend',
//   // POSTMARK: 'postmark',  // For future flexibility
//   // SENDGRID: 'sendgrid',
// };

// // Initialize Resend client clearly from env variables
// const resend = new Resend(process.env.RESEND_API_KEY);

// // Single clear function to send transactional emails
// export async function sendTransactionalEmail({ provider, to, subject, html }) {
//   switch (provider) {
//     case EmailProvider.RESEND:
//       return resend.emails.send({
//         from: process.env.RESEND_FROM_EMAIL,
//         to,
//         subject,
//         html,
//       });
//     default:
//       throw new Error(`Unsupported email provider: ${provider}`);
//   }
// }
