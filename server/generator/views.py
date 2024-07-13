import base64
from django.http import JsonResponse
from openai import OpenAI
from server.settings import OPENAI_API_KEY


client = OpenAI(api_key=OPENAI_API_KEY)


def get_image(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('image')
        if not uploaded_file:
            return JsonResponse({"error": "No file uploaded"}, status=400)
        try:
            file_content = uploaded_file.read()
            image_base64 = base64.b64encode(file_content).decode('utf-8')
            response = client.chat.completions.create(
                model="gpt-3.5-turbo-instruct",
                messages=[
                    {
                    "role": "user",
                    "content": [
                        {
                        "type": "image_url",
                        "image_url": {
                            "url": "data:image/jpeg;base64,{image_base64}"
                        }
                        },
                        {
                            "type": "text",
                            "text": "이 사진과 관련된 블로그 포스팅 형식의 글을 써줘"
                        }
                    ]
                    }
                ],
                temperature=1,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            return JsonResponse(response['choices'][0]['text'].strip(), safe=False)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)



