from django.shortcuts import render, redirect
from base.models import Report, Photo, Photo2, EmailGroup, Employee
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
import datetime
import os
from django.conf import settings
from django.contrib.staticfiles import finders 
from django.core.mail import EmailMessage, EmailMultiAlternatives


def link_callback(uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path


def report_pdf(request, pk):
    template_path = 'pdf_reports/report_pdf.html'
    request.session['rep_key'] = pk

    now = datetime.datetime.now()
    date_string = now.strftime('%B %d, %Y')

    destination = "/Users/marco/pythonProjects/LF_htmx/base/report.pdf"

    all_employees = Employee.objects.all()
    report = Report.objects.get(id=pk)
    photo1 = Photo.objects.filter(reports_id=pk)
    photo2 = Photo2.objects.filter(reports2_id=pk)
    rep_desc = report.rep_desc
    rep_user_name = report.rep_user_name
    desc = report.rep_desc
    rep_notes = report.rep_notes
    rep_date = report.rep_date
    pr_desc = report.project.pr_desc
    supervisors = report.supervisors



    member_name = request.GET.getlist('rep_fk_emp_key_sup')
    group_selected = request.GET.getlist('groups_field')
    show_group = []
    show_emails = []

    if group_selected:
        for group_name in group_selected:
            group = EmailGroup.objects.filter(name=group_name).first()
            if group:
                show_group.append(group)
                members = group.members.all()
                for member in members:
                    show_emails.append(member.email)

    show_single_name = ""
    if member_name is not None:
        show_single_name = member_name



    show_group_names = ""
    if show_group:
        for group in show_group:
            show_group_names = group.name
    else:
        print("No group found")


    the_form_member = request.GET.get('rep_fk_emp_key_sup')
    the_form_group = request.GET.get('groups_field')


    pages = len(photo1) + 3  
    context = {
        'report': report,
        'emails':all_employees,
        'mydate': date_string,
        'rep_desc': rep_desc,
        'rep_user_name': rep_user_name,
        'desc': desc,
        'rep_notes': rep_notes,
        'rep_date': rep_date,
        'pr_desc': pr_desc,
        'supervisors': supervisors,
        'photo1': photo1,
        'photo2': photo2,
        'rep_key': request.session['rep_key'],
        'totalpages': "test",
        'observation': "Observation",
        'totalpages': pages,
        'groups': EmailGroup.objects.all(),
        'show_group_names': show_group_names,
        'show_names': show_emails,
        'group_selected': group_selected,
        'show_single_name': show_single_name,
        'the_form_member': the_form_member,
		'the_form_group': the_form_group,
 
    }

    file = open(f"{report.project.pr_desc}-{date_string}.pdf", "w+b")
    #context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    email_groups = EmailGroup.objects.all() 
        
        # if error then show some funny view

    if report.employee.email is None:
        html_content = f'''
        <p>Project: <bold>{report.project.pr_desc}</bold></p>
        <p>From: L.F. Jennings Safety Department</p>
        <p><a href="https://google.com">Click here to open {report.project.pr_desc}</a></p>
        <br>
        Please find attached the safety report for {report.project.pr_desc}
        <br>
        <br>
        <br>
        {report.employee.name}, <br><br>  
        from Project Safety <br>
        <img src="https://mybucketholly.s3.amazonaws.com/jennings2.png" alt="LF Jennings Logo" width="75" height="75"><br>
        <bold>L.F. Jennings, INC</bold><br>
        407 N. Washington Street <br>
        Falls Church, VA 22046
        
        '''
    else:
        html_content = f'''
        <p>Project: <bold>{report.project.pr_desc}</bold></p>
        <p>From: L.F. Jennings Safety Department</p>
        <p><a href="https://google.com">Click here to open {report.project.pr_desc}</a></p>
        <br>
        Please find attached the safety report for {report.project.pr_desc}
        <br>
        <br>
        <br>
        {report.employee.name}, <br><br>  
        reply to {report.employee.name} here: <a href="mailto:{report.employee.email}">Send Email</a><br><br>
        from Project Safety <br>
        <img src="https://mybucketholly.s3.amazonaws.com/jennings2.png" alt="LF Jennings Logo" width="75" height="75"><br>
        <bold>L.F. Jennings, INC</bold><br>
        407 N. Washington Street <br>
        Falls Church, VA 22046
        
        '''		


        
    # create a pdf
    pisa_status = pisa.CreatePDF(
    html, 
    dest=file, 
    link_callback=link_callback)
    #time.sleep(1)


    if request.method == 'POST':
        print(f"New Report submitted by {report.employee.name} on {date_string}")
        #bcc_email = ['wesnetwork@keybyme.com', 'rbeery@lfjennings.com']  # Replace with the desired BCC email addresses
        bcc_email = ['marcowolff619@proton.me']  # Replace with the desired BCC email addresses

        if group_selected and show_single_name:
            for group in email_groups:
                if group.name in group_selected:
                    members = group.members.all()
                    recipient_list = [member.emp_email for member in members]

                    mail = EmailMultiAlternatives(
                        'Safety Report Email',
                        '',
                        settings.EMAIL_HOST_USER,
                        recipient_list + show_single_name,
                        bcc=bcc_email  # Remove the brackets around bcc_email
                    )
                    mail.attach_alternative(html_content, "text/html")
                    mail.attach_file(f"{report.project.pr_desc}-{date_string}.pdf")
                    mail.send()
        elif group_selected:
            for group in email_groups:
                if group.name in group_selected:
                    members = group.members.all()
                    recipient_list = [member.emp_email for member in members]
                    print("Recipient List:", recipient_list)
                    mail = EmailMultiAlternatives(
                        'Safety Report Email',
                        '',
                        settings.EMAIL_HOST_USER,
                        recipient_list,
                        bcc=bcc_email  # Remove the brackets around bcc_email
                    )
                    mail.attach_alternative(html_content, "text/html")
                    mail.attach_file(f"{report.project.pr_desc}-{date_string}.pdf")
                    mail.send()
        elif show_single_name:
            mail = EmailMultiAlternatives(
                'Safety Report Email',
                '',
                settings.EMAIL_HOST_USER,
                show_single_name,
                bcc=bcc_email  # Remove the brackets around bcc_email
            )
            mail.attach_alternative(html_content, "text/html")
            mail.attach_file(f"{report.project.pr_desc}-{date_string}.pdf")
            mail.send()


        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        #messages.success(request, 'Email sent')
        return redirect('reports')
    return render(request, 'pdf_reports/reporte_udp_standalone.html', context)
 
	