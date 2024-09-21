from django.forms import ModelForm, Textarea

from .models import AnswerSet


CHOICE1 = (
    ('A', 'Location of healthcare providers.'),
    ('B', 'A broader geographic area such as a state, province, county or city.'),
    ('C', 'The country where the health data originates or is relevant.'),
    ('D', 'Postal or ZIP code information.'),
    ('E', 'Geographic area covered by a healthcare provider.'),
    ('F', 'Location where a patient lives.'),
    ('G', 'Geographic regions defined for tracking and monitoring disease outbreaks.'),
    ('H', 'Geographic attributes related to environmental factors, such as air quality, water sources, and pollution levels.'),
    ('I', 'Information about a person''s recent travel, including destinations visited.'),
    ('J', 'Locations of pharmacies and drugstores.'),
    ('K', 'Data on the distribution of healthcare resources.'),
    ('L', 'Geographic information related to emergency response services.'),
    ('M', 'Additional geospatial layers, such as land use, transportation networks, and socioeconomic data.'),
    ('N', 'Any other geographic location.'),
)
CHOICE2 = (
    ('A', 'Date of Birth (DOB): The birthdate of a patient.'),
    ('B', 'Date of Admission (DOA): The date a patient is admitted.'),
    ('C', 'Date of Discharge (DOD): The date a patient is discharged.'),
    ('D', 'Date of Encounter (DOE): The date of a healthcare encounter, which can include appointments, consultations, or visits.'),
    ('E', 'Date of Diagnosis (DOD): The date when a medical condition or disease was diagnosed.'),
    ('F', 'Date of Procedure (DOP): The date when a medical procedure or surgery was performed.'),
    ('G', 'Date of Prescription (DOR): The date when a medication or treatment plan was prescribed.'),
    ('H', 'Date of Test/Examination (DOT): The date when medical tests, screenings, or examinations were conducted.'),
    ('I', 'Date of Immunization (DOI): The date when a vaccination or immunization was administered.'),
    ('J', 'Onset Date: The date when symptoms of a medical condition first appeared.'),
    ('K', 'Follow-Up Date: The date scheduled for a follow-up appointment or consultation.'),
    ('L', 'Any other time related.'),
)

CHOICE3 = (
    ('A', 'Transaction History: A record of past transactions, including dates, amounts, and descriptions.'),
    ('B', 'Transaction Status: The status of a transaction at different points in time &#40;e.g., pending, completed, canceled&#41;.'),
    ('C', 'Payment Frequency: Information about the frequency of recurring payments, such as weekly, bi-weekly, or semi-annually.'),
    ('D', 'Any other financial transactions, insurance information, billing records, etc.'),
)

CHOICE4 = (
    ('A', 'Age: The calculated age of an individual based on their date of birth.'),
    ('B', 'Generation: Categorizations based on birth years, such as Baby Boomers, Generation X, Millennials, and Generation Z.'),
    ('C', 'Age Group: Grouping individuals into predefined age ranges.'),
    ('D', 'Marital Status: Current marital status, such as single, married, divorced, or widowed.'),
    ('E', 'Any Employment History.'),
    ('F', 'Immigration Date: The date when an individual immigrated to a new country.'),
    ('G', 'Event Dates: Dates associated with significant life events, such as moving to a new location, starting or ending relationships, or major life transitions.'),
    ('H', 'Historical Demographic Data: Temporal data related to demographic changes over time, such as population growth, birth rates, and death rates.'),
    ('I', 'Fertility Timing: Dates related to childbirth, including the birthdate of children and the timing of pregnancies.'),
    ('J', 'Any other demographic information in data typically includes attributes related to the characteristics of individuals.'),
)

class AnswerSetForm(ModelForm):
    class Meta:
        model = AnswerSet
        fields = ["title", "description"]
        widgets = {
            "description": Textarea(attrs={"cols": 80, "rows": 3}),
        }

