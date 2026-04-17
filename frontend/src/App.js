const formData = new FormData();
formData.append("file", file);

const uploadRes = await uploadResume(formData);

// ✅ NOW it's safe to use uploadRes
console.log("EMAIL SENT:", email);
console.log("PAYLOAD:", {
  file_path: uploadRes.data.file_path,
  job_description: job,
  email: email
});