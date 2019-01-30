from behave import given, when, then
import unittest, time, os
from appium import webdriver
from time import sleep

@given(u'que eu abra o app na pagina principal')
def abrir_app(context):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.0'
    desired_caps['deviceName'] = 'Galaxy S7'
    # Since the app is already installed launching it using package and activity name
    desired_caps['appPackage'] = 'br.com.seniorsolution.crefisa'
    desired_caps['appActivity'] = 'br.com.seniorsolution.crefisa.MainActivity'
    # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
    desired_caps['automationName'] = 'UiAutomator2'
    context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    context.driver.implicitly_wait(30)
        
    el1 = context.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.view.View[7]/android.view.View/android.widget.Button[3]")
    el1.click()

@when(u'eu coloco {valor} e {prazo}')
def inserir_valores(context, valor, prazo):
    el2 = context.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText")
    el2.click()
    el2.send_keys(valor)
    
    el3 = context.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText")
    el3.click()
    el3.send_keys(prazo)

@when(u'clico em "contratar agora"')
def clicar_botao(context):
    el4 = context.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.widget.Button")
    el4.click()


@then(u'devo ver a seguinte tela {resposta}')
def ver_resposta(context,resposta):
   if (resposta == 'contratar'):
        el1 = context.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.view.View[1]/android.view.View/android.view.View/android.view.View[2]/android.view.View[2]/android.view.View[2]/android.widget.Button[2]")
        el1.click()
   else:
        el5 = context.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View/android.app.Dialog/android.view.View/android.view.View[2]")
        el5.click()    