from django.db import models

# Create your models here.


class SpendingCategory(models.Model):
    """
    Captures Various Sectors in which transaction will be recorded
    """
    name = models.CharField(max_length=30, help_text="Where did you spend your money?", null=False)

    def __str__(self):
        return self.name


class SpendingSubCategory(models.Model):
    """
    SubCategory information like Shopping->Shoe, Clothing etc.
    """
    name = models.CharField(max_length=30, help_text="Where did you spend your money?")
    category_name = models.ForeignKey('SpendingCategory', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.name + "( " + self.category_name.name + ")"


class Transaction(models.Model):
    """
    Individual Transaction, provides transaction related info like where, when etc.
    """
    name_of_spending_category = models.ForeignKey('SpendingCategory', on_delete=models.CASCADE,
                                                    help_text="Provide a Spending Category", null=False, default="")
    name_of_spending_sub_category = models.ForeignKey('SpendingSubCategory', on_delete=models.CASCADE,
                                                      help_text="Provide a spending sub category", default="", null=False)
    amount_spent = models.FloatField(help_text="How Much Money did you spent?", null=False)
    date = models.DateField(help_text="When this transaction happened?", null=False)
    description = models.CharField(max_length=200, help_text="Care to elaborate?", null=True, blank=True, default="")

    def __str__(self):
        return "spent: " + str(self.amount_spent) + "\n" + "category: " + self.name_of_spending_category.name \
             + "\n" + "sub category: " + self.name_of_spending_category.name + "\n" \
             + "time: " + str(self.date.strftime("%Y-%m-%d") + "\n" + "description: " + self.description

