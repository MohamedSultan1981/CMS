from django import template
import re
register = template.Library() 

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
@register.filter(name='Vidsize') 
def Vidsize(EmbedText, HValue):
	PatternW=r'width="\d*"'
	WValue=int(HValue)*1.5
	replaceW=f'width="{int(WValue)}"'
	EmbedText=re.sub(PatternW,replaceW,EmbedText)
	PatternH=r'height="\d*"'
	replaceH=f'height="{HValue}"'
	EmbedText=re.sub(PatternH,replaceH,EmbedText)
	
	return EmbedText	
