from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from processes.models import AnswerSet, Answer
from processes.views import render_with_htmx


def convert_multiple_choice_question_to_array(answer):
    """
    Converts an answers multiple choice question to an array

    param: answer to convert multiple_answer to array
    return: array from csv
    """
    if answer and answer.multiple_answer:
        attributes = answer.multiple_answer.split(', ')
    else:
        attributes = []

    return attributes


def get_data_inventory_context(answer_set):
    """
    Gets the information for the question group 1 report

    param answer_set: the answer_set from which to use the answers from
    return: question group 1 results
    """
    check_unique_identifiers = Answer.objects.filter(answer_set=answer_set, question_id=101)[0].boolean_answer
    geographic_attributes = convert_multiple_choice_question_to_array(
        Answer.objects.filter(answer_set=answer_set, question_id=102).first())
    time_attributes = convert_multiple_choice_question_to_array(
        Answer.objects.filter(answer_set=answer_set, question_id=103).first())
    financial_attributes = convert_multiple_choice_question_to_array(
        Answer.objects.filter(answer_set=answer_set, question_id=104).first())
    demographic_attributes = convert_multiple_choice_question_to_array(
        Answer.objects.filter(answer_set=answer_set, question_id=104).first())

    free_text = Answer.objects.filter(answer_set=answer_set, question_id=106)[0].boolean_answer
    other_present = demographic_attributes or financial_attributes or time_attributes or geographic_attributes
    geo_present = False
    time_present = False
    fin_present = False
    demo_present = False
    geo_risk = {}
    demo_risk = {}
    time_risk = {}
    fin_risk = {}
    # analyse_data_inventory
    # if (check_unique_identifiers):
    if geographic_attributes:
        geo_present = True
        for values in geographic_attributes:
            if values == 'A':
                geo_risk[
                    values] = "Revealing the location of healthcare providers in patient records can potentially expose the identities of patients. Patients may want to keep their choice of healthcare provider private."
            if values == 'B':
                geo_risk[
                    values] = "Broad geographic areas can indirectly reveal patient locations. While not pinpointing individual addresses, it can still compromise the privacy of patients, especially in less densely populated regions."
            if values == 'C':
                geo_risk[
                    values] = "Knowing the country where health data originates or is relevant may disclose patients' nationalities or their health-related international activities, potentially affecting privacy and security."
            if values == 'D':
                geo_risk[
                    values] = "ZIP code information can be quite specific, and when combined with other data points, it can potentially lead to the re-identification of patients or expose more about their location."
            if values == 'E':
                geo_risk[
                    values] = "The geographic area served by a healthcare provider could provide clues about patient locations. For instance, a healthcare provider serving a rural area might indirectly identify patients from that region."
            if values == 'F':
                geo_risk[
                    values] = "Knowing the location where a patient lives is a direct invasion of their privacy and security. This information can be sensitive and must be handled carefully."
            if values == 'G':
                geo_risk[
                    values] = "While vital for public health, this information can indirectly reveal patient locations and may affect their privacy. Balancing the need for public health with individual privacy is essential."
            if values == 'H':
                geo_risk[
                    values] = "Revealing environmental data may indirectly expose patient locations and potentially their health-related vulnerabilities. This can be a privacy and security concern."
            if values == 'I':
                geo_risk[
                    values] = "Travel history can reveal a lot about an individual's whereabouts and may expose sensitive information about their activities and potential health risks."
            if values == 'J':
                geo_risk[
                    values] = "Knowing the locations of pharmacies and drugstores can indirectly reveal information about patients' access to medication and healthcare, potentially impacting their privacy."
            if values == 'K':
                geo_risk[
                    values] = "Data on the distribution of healthcare resources may indirectly disclose the geographic areas where patients reside and their access to healthcare services, affecting privacy and security."
            if values == 'L':
                geo_risk[
                    values] = "This data may expose information about emergency situations and the locations of patients in distress, potentially compromising their privacy and safety."
            if values == 'M':
                geo_risk[
                    values] = "Additional geospatial layers provide more context but can also be used to indirectly reveal patient locations and other sensitive information related to their environment and circumstances."
            if values == 'N':
                geo_risk[
                    values] = "Any unclassified geographic information can still be used to indirectly deduce patient locations, potentially impacting their privacy and security."

    if time_attributes:
        time_present = True
        for values in time_attributes:
            if values == 'A':
                time_risk[values] = [
                    "Re-identification of patients, especially when combined with other information.",
                    "Replace with age or age range"
                ]
            if values == 'B':
                time_risk[values] = [
                    "Potential re-identification of patients, especially if they have unique admission patterns.",
                    "Replace with the admission order (e.g., first, second, etc.) or admission year."
                ]
            if values == 'C':
                time_risk[values] = [
                    "Potential re-identification, as it could be linked to specific medical conditions or procedures.",
                    "Replace with discharge order or discharge year."
                ]
            if values == 'D':
                time_risk[values] = [
                    "Re-identification risk when combined with other data, especially if it involves unique healthcare providers.",
                    "Replace with encounter order or encounter year."
                ]
            if values == 'E':
                time_risk[values] = [
                    "Re-identification risk, as it could reveal specific medical conditions.",
                    "Replace with diagnosis order or diagnosis year."
                ]
            if values == 'F':
                time_risk[values] = [
                    "Re-identification risk, as it could reveal specific medical procedures.",
                    "Replace with procedure order or procedure year."
                ]
            if values == 'G':
                time_risk[values] = [
                    "Re-identification risk, especially if specific medications are linked to the prescription date.",
                    "Replace with prescription order or prescription year."
                ]
            if values == 'H':
                time_risk[values] = [
                    "Re-identification risk, as it could reveal specific medical tests or conditions.",
                    "Replace with test/examination order or test/examination year."
                ]
            if values == 'I':
                time_risk[values] = [
                    "Re-identification risk, especially if it reveals specific vaccines or medical history.",
                    "Replace with immunization order or immunization year."
                ]
            if values == 'J':
                time_risk[values] = [
                    "Re-identification risk, as it indicates the start of a medical condition.",
                    "Replace with onset order or onset year."
                ]
            if values == 'K':
                time_risk[values] = [
                    "Re-identification risk, as it relates to a scheduled appointment.",
                    "Replace with follow-up order or follow-up year."
                ]
            if values == 'L':
                time_risk[values] = [
                    "The risk depends on the specific nature of the data. Re-identification risk may apply in some cases.",
                    "Replace with a generalized description of the time-related event (e.g., Event date) or use an order or year designation."
                ]

    if financial_attributes:
        fin_present = True
        for values in financial_attributes:
            if values == 'A':
                fin_risk[values] = [
                    "Detailed transaction histories may expose sensitive financial information, including amounts, descriptions, and dates.",
                    "Aggregate transaction data into categories or use date ranges (e.g., Monthly transaction summary or Quarterly transaction report)."
                ]
            if values == 'B':
                fin_risk[values] = [
                    "The status of a transaction at different points in time may reveal sensitive information about the progress or outcome of financial transactions.",
                    "Replace with generalized status categories (e.g., Processing status)."
                ]
            if values == 'C':
                fin_risk[values] = [
                    "Information about recurring payment frequencies can be linked to specific financial obligations or arrangements.",
                    "Use generalized terms like Recurring payment information without specifying the exact frequency."
                ]
            if values == 'D':
                fin_risk[values] = [
                    "The risk depends on the specific nature of the data. Re-identification risk may apply to various financial data.",
                    "Replace with broader categories or descriptions (e.g., Financial records or Billing information)."
                ]

    if demographic_attributes:
        demo_present = True
        for values in demographic_attributes:
            if values == 'A':
                demo_risk[values] = [
                    " Re-identification risk, as age can be used to identify individuals when combined with other data.",
                    "Replace with age group or age range (e.g., Age 25-34)."
                ]
            if values == 'B':
                demo_risk[values] = [
                    "Generation categorizations can reveal the approximate birth years of individuals.",
                    "Use generalized generational categories without specifying birth years."
                ]
            if values == 'C':
                demo_risk[values] = [
                    "Age group data can still provide insights into the age distribution of a population.",
                    "Replace with broader age categories (e.g., Young adults, Middle-aged)."
                ]
            if values == 'D':
                demo_risk[values] = [
                    "Marital status information can be sensitive and potentially re-identify individuals.",
                    "Replace with generalized categories (e.g., Marital status: Single/Married)."
                ]
            if values == 'E':
                demo_risk[values] = [
                    "Detailed employment history can expose personal and professional information.",
                    "Aggregate employment data into categories (e.g., General employment history)."
                ]
            if values == 'F':
                demo_risk[values] = [
                    "Revealing immigration dates may lead to re-identification and privacy concerns.",
                    "Replace with immigration period or immigration status."
                ]
            if values == 'G':
                demo_risk[values] = [
                    "Specific life events can reveal personal details about an individual's history.",
                    "Aggregate events into broader categories (e.g., Life event history)."
                ]
            if values == 'H':
                demo_risk[values] = [
                    "Historical demographic data may include sensitive information about population changes.",
                    "Use aggregated demographic statistics without individual-level details."
                ]
            if values == 'I':
                demo_risk[values] = [
                    "Fertility timing data may expose information about childbirth and family planning.",
                    "Replace with generalized fertility data or family planning data."
                ]
            if values == 'J':
                demo_risk[values] = [
                    "The risk depends on the specific nature of the data, but re-identification may be possible.",
                    "Replace with broader demographic categories or descriptions."
                ]

    return {
        "unique_identifier": check_unique_identifiers,
        "geo_risk": geo_risk,
        "time_risk": time_risk,
        "fin_risk": fin_risk,
        "demo_risk": demo_risk,
        "other_present": other_present,
        "geo_present": geo_present,
        "time_present": time_present,
        "fin_present": fin_present,
        "demo_present": demo_present,
        "geo_risks": geo_risk,
        "free_text": free_text
    }


def get_persecutor_context(answer_set):
    """
    gets the results from question 2 persecutor risk

    param answer_set: The answer set from which to get the results
    returns the results of question 2 in json keyword argument format
    """
    whole_population = Answer.objects.filter(answer_set=answer_set, question_id=201)[0].boolean_answer
    generally_known = Answer.objects.filter(answer_set=answer_set, question_id=202)[0].boolean_answer
    self_reveal = Answer.objects.filter(answer_set=answer_set, question_id=203)[0].boolean_answer
    persecutor_risk = whole_population or generally_known or self_reveal

    return {
        "present": persecutor_risk,
        "whole_population": whole_population,
        "generally_known": generally_known,
        "self_reveal": self_reveal,
    }


def get_k_anonymity_context(answer_set):
    """
    gets the k anonymity context

    param answer_set: the answer set to get the k anonymity context from
    return: k anonymity context in keyword argument form
    """
    whole_population = Answer.objects.filter(answer_set=answer_set, question_id=201)[0].boolean_answer
    generally_known = Answer.objects.filter(answer_set=answer_set, question_id=202)[0].boolean_answer
    self_reveal = Answer.objects.filter(answer_set=answer_set, question_id=203)[0].boolean_answer
    persecutor_risk = whole_population or generally_known or self_reveal

    is_subset = Answer.objects.filter(answer_set=answer_set, question_id=301)[0].boolean_answer

    if (not persecutor_risk) and is_subset:
        current_k = Answer.objects.filter(answer_set=answer_set, question_id=303)[0].int_answer
    else:
        current_k = Answer.objects.filter(answer_set=answer_set, question_id=302)[0].int_answer

    if current_k == None:
        raise Exception("K-Anonymity value is missing")

    sufficient_k = current_k >= 5

    return {
        "is_subset": is_subset,
        "sufficient_k": sufficient_k,
        "current_k": current_k
    }


def get_context(answer_set, pdf_format):
    """
    Compiles all the contexts for the answer set into a big one that can be sent to the template

    param answer_set: the answer set used to get the answers
    param pdf_format: whether this document is for printing to pdf or web view
    return: the context for the report
    """
    return {
        "unique_identification": get_data_inventory_context(answer_set),
        "persecutor_risk": get_persecutor_context(answer_set),
        "k_anonymity": get_k_anonymity_context(answer_set),
        "process_name": answer_set.title,
        "process_description": answer_set.description,
        "pdf_format": pdf_format
    }


def report(request, answer_set_id):
    """
    Generates a report form the answer_set answers

    param request: WSGIRequest
    param answer_set_id: The id of the answer set to generate a report for
    return: a report from the answer_set answers
    """
    answer_set = get_object_or_404(AnswerSet, id=answer_set_id)
    try:
        context = get_context(answer_set, False)
    except:
        return redirect(reverse('question', args=([answer_set.pk, 3])))

    return render_with_htmx(request, "report.html", context=context)


def report_pdf(request, answer_set_id):
    """
    Generates a report in a formate suitable for printing

    param request: WSGIRequest
    param answer_set_id: The id of the answer set to generate a report for
    return: a report from the answer_set answers but this time without any css styling or other bloat
    """
    answer_set = get_object_or_404(AnswerSet, answer_set_id)
    context = get_context(answer_set, True)

    return render(request, "processes/partials/_report.html", context=context)
