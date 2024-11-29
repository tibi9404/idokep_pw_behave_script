Feature: Geeting informations from idokep.hu

    Scenario: Open site and write what to wear today into a txt file
       Given I navigate to the site
       And I accept the open dialog
       Then Query what to wear today
       And Write the value to a txt

   Scenario: Open site and query if rain is expected in the next four days
       Given I navigate to the site
       And I accept the open dialog
       Then Query if rain is expected in the next four days
       And Write the value to a csv

    Scenario: Open site then save rain and temperature maps
        Given I navigate to the site
        And I accept the open dialog
        When I navigate to temp map
        Then the temp map can be saved
        When I navigate to the past rain map
        Then the past rain map can be saved