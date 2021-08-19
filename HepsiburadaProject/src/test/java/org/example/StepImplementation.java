package org.example;

import com.thoughtworks.gauge.Step;
import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;


import java.util.List;
import java.util.Random;

public class StepImplementation extends Base {

    @Step("<second> saniye kadar bekle!")
    public void waitImplementation(int second) throws InterruptedException {
        Thread.sleep(second* 1000L);
    }

    @Step("<css> css li elemente tıkla")
    public void click(String css) {
        driver.findElement(By.cssSelector(css)).click();
    }

    @Step("<css> css'li yere <text> yazısını yaz")
    public void sendKeys(String css, String text) {
        driver.findElement(By.cssSelector(css)).sendKeys(text);
    }

    @Step("<css> css'li elementler arasından Kitap kategorisi için sekizinci butona tıkla")
            public void eighthButtonForBookCategory(String css) {
        List<WebElement> elements = driver.findElements(By.cssSelector(css));
        elements.get(8).click();
    }

    @Step("<css> css'li elementler arasından random tıkla")
    public void drone(String css){
        Random random = new Random();
        int r = random.nextInt(24);
        List<WebElement> elements = driver.findElements(By.cssSelector(css));
        elements.get(r).click();
    }

    @Step("<css> css'li elementler arasından ilk butona tıkla")
    public void firstButton(String css) {
        List<WebElement> elements = driver.findElements(By.cssSelector(css));
        elements.get(0).click();
    }

    @Step("<css> css'li elementler arasından ikinci butona tıkla")
    public void secondButton(String css) {
        List<WebElement> elements = driver.findElements(By.cssSelector(css));
        elements.get(1).click();
    }

}

