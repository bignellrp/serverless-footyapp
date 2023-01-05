from flask import render_template, request, Blueprint, session, redirect, url_for
from services.get_date import next_wednesday
#import services.post_spread as post
from services.get_spread import results

result_blueprint = Blueprint('result', 
                             __name__, 
                             template_folder='templates', 
                             static_folder='static')

@result_blueprint.route('/result', methods=['GET', 'POST'])

def result():
    '''A function for building the results page.
    Takes in teama and teamb from flask 
    session so result carries between pages
    and returns the body to the google sheet 
    in row format'''
    
    if request.method == 'POST':
        if request.form['submit_button'] == 'Store':

            ##Get Colour from form
            teama_colour = request.form.get('ImageA')
            teamb_colour = request.form.get('ImageB')
            ##Pull data from flask session
            ##Taken from reddit 
            ##https://www.reddit.com/r/flask/comments/nsghsf/hidden_list/
            teama_passback = session['team_a']
            teamb_passback = session['team_b']
            scorea_passback = session['team_a_total']
            scoreb_passback = session['team_b_total']

            ##Build google_output list of values in a row
            google_output = []
            google_output.append((next_wednesday))
            google_output.append(str("-"))
            google_output.append(str("-"))
            google_output.append((scorea_passback))
            google_output.append((scoreb_passback))
            google_output.extend((teama_passback))
            google_output.extend((teamb_passback))
            google_output.append((teama_colour))
            google_output.append((teamb_colour))

            ##Now vars are safely in the google output remove 
            ##them from the session so they are not carried 
            ##from page to page unnecessarily.
            session.pop('team_a', None)
            session.pop('team_b', None)
            session.pop('team_a_total', None)
            session.pop('team_b_total', None)

            ##Gets Result data for validation
            result = results()
            scorea = result.scorea()
            date = result.date()
            
            ##Run Update Functions, either update or append
            if date == next_wednesday and scorea == "-":
                '''If the last row has next wednesdays date 
                then replace the results.
                Else append results on a new line'''
                #result = post.update_result(google_output)
                print("Running update function")
            else:
                #result = post.append_result(google_output)
                print("Running append function")

            ##Return Team A and Team B to the results template
            return render_template('post.html')
        if request.form['submit_button'] == 'Rerun':
            print("Rerun button pressed!")
            return redirect(url_for('index.index'))
    elif request.method == 'GET':
        ##If request method is not POST then it must be GET
        return render_template('result.html')