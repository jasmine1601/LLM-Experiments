import os
import genai

def get_env_variable(var_name, default_value=None):
  """
  Gets the value of an environment variable with a default value.
  """
  return os.environ.get(var_name, default_value)

env_file_path = '../.env'

if not os.path.exists(env_file_path):
  project_root = os.path.dirname(os.path.abspath(__file__))
  env_file_path = os.path.join(project_root, '.env')

if os.path.exists(env_file_path):
  with open(env_file_path, 'r') as f:
    for line in f:
      key, value = line.strip().split('=')
      os.environ[key] = value
else:
  print(".env file not found!")

GEMINI_API_KEY = get_env_variable('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("Give me terms, abbreviations and descriptions related to Healthcare Industry. Give me the response in the form of a JSON array containing JSON objects whose keys are term, abrreviation, description. For terms where abbreviation is 'null' give an empty string '' instead of the text 'null'")

print(response.text)

# OUTPUT:
# ```
# [
#   {
#     "term": "Ambulatory Surgery Center",
#     "abbreviation": "ASC",
#     "description": "A healthcare facility that provides surgical procedures on an outpatient basis, meaning patients are not admitted overnight."
#   },
#   {
#     "term": "Certified Medical Assistant",
#     "abbreviation": "CMA",
#     "description": "A healthcare professional who provides administrative, clinical, and laboratory support to physicians and other healthcare providers."
#   },
#   {
#     "term": "Clinical Laboratory Improvement Amendments",
#     "abbreviation": "CLIA",
#     "description": "Federal regulations that establish quality standards for clinical laboratories."
#   },
#   {
#     "term": "Emergency Medical Service",
#     "abbreviation": "EMS",
#     "description": "A system that provides emergency medical care to individuals who are acutely ill or injured."
#   },
#   {
#     "term": "Health Maintenance Organization",
#     "abbreviation": "HMO",
#     "description": "A type of health insurance plan that provides comprehensive medical services to members for a fixed monthly premium."
#   },
#   {
#     "term": "Home Health Agency",
#     "abbreviation": "HHA",
#     "description": "A healthcare provider that provides skilled nursing care, physical therapy, occupational therapy, and other medical services to patients in their homes."
#   },
#   {
#     "term": "International Classification of Diseases",
#     "abbreviation": "ICD",
#     "description": "A system of classifying diseases and other health problems used by healthcare providers and public health agencies."
#   },
#   {
#     "term": "Magnetic Resonance Imaging",
#     "abbreviation": "MRI",
#     "description": "A medical imaging technique that uses magnetic fields and radio waves to produce detailed images of the inside of the body."
#   },
#   {
#     "term": "National Health Service Corps",
#     "abbreviation": "NHSC",
#     "description": "A federal program that provides scholarships and loan repayment assistance to healthcare professionals who commit to working in underserved communities."
#   },
#   {
#     "term": "Occupational Safety and Health Administration",
#     "abbreviation": "OSHA",
#     "description": "A federal agency that sets and enforces workplace safety and health standards."
#   },
#   {
#     "term": "Patient Protection and Affordable Care Act",
#     "abbreviation": "ACA",
#     "description": "A federal law that expanded health insurance coverage to millions of Americans."
#   },
#   {
#     "term": "Pharmacy Benefit Manager",
#     "abbreviation": "PBM",
#     "description": "A company that negotiates drug prices with pharmaceutical manufacturers and provides other services to health plans and employers."
#   },
#   {
#     "term": "Quality Improvement Organization",
#     "abbreviation": "QIO",
#     "description": "A non-profit organization that works to improve the quality of healthcare services in a specific geographic area."
#   },
#   {
#     "term": "Registered Nurse",
#     "abbreviation": "RN",
#     "description": "A healthcare professional who provides direct patient care and is responsible for managing patient care plans."
#   },
#   {
#     "term": "Rural Health Clinic",
#     "abbreviation": "RHC",
#     "description": "A healthcare facility that provides primary care services to residents of rural areas."
#   },
#   {
#     "term": "Skilled Nursing Facility",
#     "abbreviation": "SNF",
#     "description": "A healthcare facility that provides long-term care and rehabilitation services to patients who need skilled nursing care."
#   },
#   {
#     "term": "Urgent Care Center",
#     "abbreviation": "UCC",
#     "description": "A healthcare facility that provides walk-in medical care for minor injuries and illnesses."
#   }
# ]
# ```