from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
import json
import os
from django.views import View
from .models import TranscriptInteract,WikiSearch,GPTSearch
from transcript.wiki_nlp import *
from transcript.gpt import *

def index(request):
    return render(request, 'index.html')

@api_view(["POST","GET"])
def get_data_from_post(request):
    if request.method == 'POST':
        ## extract the text data from the request
        transcript_text = json.loads(request.body)["transcript"]
        print(transcript_text)
        ## check it has saved into the database or not
        if WikiSearch.objects.filter(text=transcript_text).exists():
            print("This transcript already exists in the Wiki database.")
            search_result = WikiSearch.objects.get(text=transcript_text)
            print(search_result)

            if GPTSearch.objects.filter(text=transcript_text).exists():
                print("This transcript already exists in the Wiki database.")
                gpt_result = GPTSearch.objects.get(text=transcript_text)
            content =[search_result.result,gpt_result.answer]

            return JsonResponse({"response":content})
        else:
            ### call the wikipedia search function
            wiki_result = wiki_search(transcript_text)
            search_result =WikiSearch(text=transcript_text,result = wiki_result)
            search_result.save()
            print("successfully saved to Wiki database")
            print(type(search_result.result))
            final_result = search_result.result
            ### call the GPT function
            gpt_answer = GPT_answers(transcript_text)
            gpt_result =GPTSearch(text=transcript_text, answer = gpt_answer)
            gpt_result.save()
            print("successfully saved to GPT database")
            final_result =[search_result.result, gpt_result.answer]
            return JsonResponse({"response":final_result})
    #return JsonResponse({"response":"successs"})
    



@api_view(["POST","GET"])
def process_transcript(request):
    if request.method == 'POST':
        ## extract the text data from the request
        transcript_text = json.loads(request.body)["transcript"]
        print(transcript_text)
        ## check it has saved into the database or not
        if TranscriptInteract.objects.filter(text=transcript_text).exists():
            print("This transcript already exists in the Wiki database.")
            interact_result = TranscriptInteract.objects.get(text=transcript_text)
            #print(search_result)
            # get search result (summary) from Wikipedia
            wiki_answer = interact_result.wiki_result
            print(wiki_answer)
            #get answer from GPT
            gpt_result = interact_result.gpt_answer
            print(gpt_result)
            #content =[wiki_result,gpt_result]

            return JsonResponse({"Wiki results":wiki_answer,
                                 "GPT answers":gpt_result})
        else:
            ### call the wikipedia search function
            wiki_answer = wiki_search(transcript_text)
            ### call the GPT function
            gpt_answer = GPT_answers(transcript_text)
            ### call the Google search function
            google_result = ''
            ### save the transcript interaction result
            interact_result =TranscriptInteract(text = transcript_text,
                                                wiki_result = wiki_answer,
                                                gpt_answer = gpt_answer,
                                                google_result=google_result)
            interact_result.save()

            print("Successfully Saved To the Transcript Database!")
            print(interact_result.wiki_result)
            print("\n\n")
            print(interact_result.gpt_answer)
            #content = [interact_result.wiki_result,interact_result.gpt_answer]
            
            return JsonResponse({"Wiki results":interact_result.wiki_result,
                                 "GPT answers":interact_result.gpt_answer})



@api_view(["POST","GET"])
def Process_Wiki_Request(request):
    if request.method == 'POST':
        ## extract the text data from the request
        transcript_text = json.loads(request.body)["transcript"]
        print(transcript_text)
        ## check it has saved into the database or not
        if WikiSearch.objects.filter(text__exact=transcript_text).exists():
        #any(obj.text == transcript_text for obj in WikiSearch.objects):
            print("This transcript already exists in the Wiki database.")
            wiki_result = WikiSearch.objects.get(text=transcript_text)
            #print(search_result)
            # get search result (summary) from Wikipedia
            wiki_answer = wiki_result.result
            print(wiki_answer)
     
            #content =[wiki_result,gpt_result]

            return JsonResponse({"Wiki results":wiki_answer})
        else:
            ### call the wikipedia search function
            wiki_answer = wiki_search(transcript_text)

            ### save the transcript interaction result
            wiki_result =WikiSearch(text = transcript_text,
                                    result = wiki_answer,
                                               )
            wiki_result.save()

            print("Successfully Saved To the Wikipedia Interaction Database!")
            print(wiki_result.result)

            #content = [interact_result.wiki_result,interact_result.gpt_answer]
            
            return JsonResponse({"Wiki results":wiki_result.result})

@api_view(["POST","GET"])
def Process_GPT_Request(request):
    if request.method == 'POST':
        ## extract the text data from the request
        transcript_text = json.loads(request.body)["transcript"]
        print(transcript_text)
        ## check it has saved into the database or not
        if GPTSearch.objects.filter(text__exact=transcript_text).exists():
            print("This transcript already exists in the GPT database.")
            gpt_result = GPTSearch.objects.get(text=transcript_text)
            #print(search_result)
            # get search result (summary) from Wikipedia
            gpt_answer = gpt_result.answer
            print(gpt_answer)

            return JsonResponse({"GPT answers":gpt_answer})
        else:
            ### call the GPT search function
            gpt_answer = GPT_answers(transcript_text)

            ### save the transcript interaction result
            gpt_result =GPTSearch(text = transcript_text,
                                   answer = gpt_answer,
                                               )
            gpt_result.save()

            print("Successfully Saved To the GPT Interaction Database!")
            print(gpt_result.answer)

            #content = [interact_result.wiki_result,interact_result.gpt_answer]
            
            return JsonResponse({"GPT answers":gpt_result.answer})

